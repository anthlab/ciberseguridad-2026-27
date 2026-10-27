#!/usr/bin/env python3
"""
Backend de laboratorio de NotasXest (PPS · UT6) — solo VLAN de aula.

Simula el servidor "api.xest.local" al que llama la app móvil. Sirve el login y la
sincronización de notas. Por defecto habla HTTP EN CLARO (para la práctica de
interceptación con mitmproxy). Con --tls sirve HTTPS con el certificado indicado, para
la parte de fijación de certificado (pinning).

Uso:
    python3 backend_inseguro.py                 # HTTP claro en 0.0.0.0:8090
    python3 backend_inseguro.py --tls           # HTTPS en 0.0.0.0:8443 (requiere cert.pem/key.pem)

Solo librería estándar: no necesita pip.
"""
import argparse
import json
import ssl
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# La misma clave que aparece incrustada en el APK. El servidor la "acepta" sin más:
# es un secreto compartido y estático, otro antipatrón que se ve en el tráfico.
API_KEY = "xk_live_9f2c7b41ad554e0e8d3b6a1029f4c7de"

# Recibos de compra legítimos que la tienda habría emitido (para el servidor SEGURO de
# compras; aquí solo se listan como referencia del lote de datos del laboratorio).
NOTAS_DEMO = [
    {"id": 1, "titulo": "Reunión SOC", "cuerpo": "Rotar credencial VPN el viernes"},
    {"id": 2, "titulo": "Lista compra", "cuerpo": "Café, adaptadores USB-C"},
]


class Handler(BaseHTTPRequestHandler):
    server_version = "NotasXest/1.2"

    def _json(self, code, obj):
        cuerpo = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def _leer_cuerpo(self):
        n = int(self.headers.get("Content-Length", 0))
        if n == 0:
            return {}
        try:
            return json.loads(self.rfile.read(n).decode("utf-8"))
        except Exception:
            return {}

    def do_POST(self):
        if self.path == "/login":
            datos = self._leer_cuerpo()
            usuario = datos.get("usuario", "")
            # No comprueba realmente la contraseña: es un backend de laboratorio.
            token = "eyJhbGciOiJub25lIn0.demo-token-" + usuario
            return self._json(200, {"ok": True, "token": token, "usuario": usuario})
        return self._json(404, {"error": "ruta no encontrada"})

    def do_GET(self):
        if self.path == "/sync":
            if self.headers.get("X-Api-Key") != API_KEY:
                return self._json(401, {"error": "api key invalida"})
            return self._json(200, {"notas": NOTAS_DEMO})
        if self.path == "/health":
            return self._json(200, {"estado": "vivo"})
        return self._json(404, {"error": "ruta no encontrada"})

    def log_message(self, fmt, *args):
        print("[backend]", self.address_string(), "-", fmt % args)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="0.0.0.0")
    ap.add_argument("--port", type=int, default=None)
    ap.add_argument("--tls", action="store_true", help="servir HTTPS (requiere cert.pem/key.pem)")
    ap.add_argument("--cert", default="cert.pem")
    ap.add_argument("--key", default="key.pem")
    args = ap.parse_args()

    port = args.port or (8443 if args.tls else 8090)
    httpd = ThreadingHTTPServer((args.host, port), Handler)

    esquema = "http"
    if args.tls:
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ctx.load_cert_chain(certfile=args.cert, keyfile=args.key)
        httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
        esquema = "https"

    print(f"[backend] NotasXest escuchando en {esquema}://{args.host}:{port}  (Ctrl-C para parar)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[backend] parado")


if __name__ == "__main__":
    main()
