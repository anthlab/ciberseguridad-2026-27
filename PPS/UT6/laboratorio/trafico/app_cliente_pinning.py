#!/usr/bin/env python3
"""
Simulador de la app NotasXest CON FIJACIÓN DE CERTIFICADO (pinning) — PPS · UT6.

Demuestra la parte defensiva de RA4.d: una app que fija (pinnea) el certificado de su
servidor NO se puede interceptar aunque el usuario instale el CA de mitmproxy. El cliente
calcula el hash SHA-256 del certificado presentado y lo compara con el pin esperado; si no
coincide (porque mitmproxy ha suplantado el certificado), ABORTA la conexión.

Flujo de la práctica:
  1) Levanta el backend en TLS:   python3 backend_inseguro.py --tls
  2) Calcula el pin del cert real: python3 app_cliente_pinning.py --calcular-pin
     -> copia el valor a PIN_ESPERADO (o pásalo con --pin).
  3) Conexión DIRECTA (sin mitmproxy):  pin coincide -> OK.
  4) Conexión a través de mitmproxy:    pin distinto -> BLOQUEADO (lo que queremos ver).

Requiere solo librería estándar (ssl, hashlib).
"""
import argparse
import hashlib
import socket
import ssl

HOST_DEFECTO = "127.0.0.1"
PUERTO_DEFECTO = 8443

# Rellénalo con la salida de --calcular-pin (hash del certificado legítimo del backend).
PIN_ESPERADO = ""


def obtener_cert_der(host, port, proxy=None):
    """Abre TLS (opcionalmente vía proxy CONNECT) y devuelve el certificado DER presentado."""
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    # No verificamos la cadena a propósito: aquí el control es el PIN, no la CA.
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    raw = socket.create_connection((proxy[0], proxy[1]) if proxy else (host, port), timeout=10)
    if proxy:
        raw.sendall(f"CONNECT {host}:{port} HTTP/1.1\r\nHost: {host}:{port}\r\n\r\n".encode())
        resp = raw.recv(4096)
        if b"200" not in resp.split(b"\r\n", 1)[0]:
            raise RuntimeError(f"proxy CONNECT falló: {resp!r}")

    ss = ctx.wrap_socket(raw, server_hostname=host)
    der = ss.getpeercert(binary_form=True)
    ss.close()
    return der


def pin_de(der):
    return hashlib.sha256(der).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default=HOST_DEFECTO)
    ap.add_argument("--port", type=int, default=PUERTO_DEFECTO)
    ap.add_argument("--proxy", default=None, help="host:port de mitmproxy, p.ej. 127.0.0.1:8080")
    ap.add_argument("--pin", default=PIN_ESPERADO, help="pin SHA-256 esperado del certificado")
    ap.add_argument("--calcular-pin", action="store_true", help="solo imprime el pin del cert y sale")
    args = ap.parse_args()

    proxy = None
    if args.proxy:
        h, p = args.proxy.split(":")
        proxy = (h, int(p))

    der = obtener_cert_der(args.host, args.port, proxy)
    pin = pin_de(der)

    if args.calcular_pin:
        print("PIN del certificado presentado (SHA-256):")
        print(pin)
        return

    print(f"[pinning] pin presentado : {pin}")
    print(f"[pinning] pin esperado   : {args.pin or '(no configurado)'}")
    if not args.pin:
        print("[pinning] ERROR: configura --pin o PIN_ESPERADO con --calcular-pin primero.")
        return
    if pin == args.pin:
        print("[pinning] OK: el certificado coincide con el pin. Conexión de confianza.")
    else:
        print("[pinning] BLOQUEADO: certificado distinto del pin -> posible interceptación (mitmproxy).")
        print("[pinning] La app aborta la conexión. Esto es lo que impide el MITM.")


if __name__ == "__main__":
    main()
