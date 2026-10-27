#!/usr/bin/env python3
"""
Servidor de activación de "NotasXest Premium" — VERSIÓN VULNERABLE (PPS · UT6).

Antipatrón RA4.c: la validación de la compra se hace en el CLIENTE y el servidor se limita
a creer lo que el cliente le manda. Si el cuerpo dice {"purchase_valid": true}, activa
premium. Cualquiera que manipule la app o el tráfico (mitmproxy) activa premium sin pagar.

Expone:  POST /activar-premium   con cuerpo JSON.
Uso:     python3 servidor_compras_vulnerable.py            # 127.0.0.1:8091
"""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PREMIUM_CONCEDIDO = set()  # usuarios a los que se activó premium (estado en memoria)


def procesar_compra(payload: dict) -> dict:
    """LÓGICA VULNERABLE: confía en el flag que envía el cliente."""
    usuario = payload.get("usuario", "")
    if payload.get("purchase_valid") is True:      # <-- el cliente decide
        PREMIUM_CONCEDIDO.add(usuario)
        return {"premium": True, "motivo": "cliente afirmó compra válida"}
    return {"premium": False, "motivo": "el cliente no afirmó compra"}


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/activar-premium":
            self.send_error(404)
            return
        n = int(self.headers.get("Content-Length", 0))
        try:
            payload = json.loads(self.rfile.read(n).decode("utf-8"))
        except Exception:
            payload = {}
        resp = json.dumps(procesar_compra(payload)).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(resp)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    print("[compras-vulnerable] escuchando en http://127.0.0.1:8091/activar-premium")
    ThreadingHTTPServer(("127.0.0.1", 8091), Handler).serve_forever()
