#!/usr/bin/env python3
"""verifica_asvs.py — sonda de requisitos ASVS 4.0.3 (nivel 2) verificables desde fuera.

Uso didáctico PPS · UT3. Sondea el portal SOC de xest (entorno de laboratorio, la
imagen nginx de partida deliberadamente floja) y reporta qué requisitos ASVS de nivel 2
cumple o incumple SIN necesidad de acceso al código, solo mirando la respuesta HTTP.

Es la pieza que convierte la lista de requisitos ASVS en PRUEBAS ejecutables: cada fila
de la salida traza un requisito del estándar a una comprobación automática. Un requisito
"cumplido" sin una prueba que lo demuestre no cuenta como verificado (criterio del módulo).

Solo biblioteca estándar (sin dependencias). Uso exclusivo en la VLAN de aula aislada.

    python3 verifica_asvs.py [host] [puerto]
    # por defecto: localhost 8080  (portal-soc del docker-compose de objetivos)

Código de salida: 0 si se cumplen TODOS los requisitos verificables; 1 si falta alguno;
2 si no se puede contactar con el objetivo.
"""
import sys
import socket
import http.client

HOST = sys.argv[1] if len(sys.argv) > 1 else "localhost"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8080


def sondear(host, port):
    """Devuelve (status, headers_dict) de un GET / o lanza OSError."""
    conn = http.client.HTTPConnection(host, port, timeout=5)
    try:
        conn.request("GET", "/")
        resp = conn.getresponse()
        headers = {k.lower(): v for k, v in resp.getheaders()}
        return resp.status, headers
    finally:
        conn.close()


def main():
    print(f"[*] Sondeando el portal SOC de xest en http://{HOST}:{PORT}/ ...")
    try:
        status, headers = sondear(HOST, PORT)
    except (ConnectionRefusedError, socket.timeout, OSError) as e:
        print(f"[ERROR] No se puede contactar con http://{HOST}:{PORT}/  ({e})")
        print("        Arranca el objetivo:  docker compose up -d portal-soc")
        return 2

    server = headers.get("server", "(ausente)")

    # Cada comprobación: (req ASVS, descripción, ¿cumple?, detalle observado)
    resultados = [
        ("9.1.1", "Se fuerza TLS (sin HTTP en claro)",
         status != 200,
         f"responde por HTTP con {status}, sin redirección a HTTPS"),
        ("14.4.1", "X-Content-Type-Options: nosniff",
         headers.get("x-content-type-options", "").lower() == "nosniff",
         headers.get("x-content-type-options", "(ausente)")),
        ("14.4.3", "Content-Security-Policy definida",
         "content-security-policy" in headers,
         headers.get("content-security-policy", "(ausente)")),
        ("14.4.1", "Strict-Transport-Security (HSTS)",
         "strict-transport-security" in headers,
         headers.get("strict-transport-security", "(ausente)")),
        ("14.4.1", "X-Frame-Options / anti-clickjacking",
         "x-frame-options" in headers,
         headers.get("x-frame-options", "(ausente)")),
        ("14.4.1", "Referrer-Policy definida",
         "referrer-policy" in headers,
         headers.get("referrer-policy", "(ausente)")),
        ("14.3.2", "El servidor no revela su versión",
         "/" not in server,
         f"Server: {server}"),
    ]

    print()
    print(f"{'ASVS':<7} {'Requisito':<42} {'Estado':<8} Detalle")
    print("-" * 96)
    cumplidos = 0
    for req, desc, ok, detalle in resultados:
        marca = "OK" if ok else "FALLA"
        simbolo = "✅" if ok else "❌"
        cumplidos += 1 if ok else 0
        print(f"{req:<7} {desc:<42} {simbolo} {marca:<5} {detalle}")

    total = len(resultados)
    print("-" * 96)
    print(f"[=] {cumplidos}/{total} requisitos ASVS L2 verificables desde fuera CUMPLIDOS.")
    if cumplidos < total:
        print("[!] Cada FALLA es una tarea de bastionado para UT4/UT5. La lista de arriba")
        print("    ES la agenda de trabajo (traza requisito -> prueba -> corrección).")
        return 1
    print("[OK] Superficie externa conforme a los requisitos comprobados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
