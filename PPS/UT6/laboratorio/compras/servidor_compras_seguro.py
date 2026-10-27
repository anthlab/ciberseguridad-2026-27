#!/usr/bin/env python3
"""
Servidor de activación de "NotasXest Premium" — VERSIÓN SEGURA (PPS · UT6).

Corrección RA4.c: la validación ocurre EN EL SERVIDOR. El cliente no envía un flag de
"soy premium"; envía el RECIBO que la tienda le entregó al pagar. El recibo es un token
firmado por la tienda (aquí, HMAC-SHA256 con un secreto que solo conoce el backend, en
producción sería la verificación contra Google Play / App Store). El servidor:

  1) Verifica la firma del recibo (no lo puede fabricar el cliente).
  2) Comprueba que no se haya consumido ya (anti-reutilización).
  3) Solo entonces concede premium.

Un cliente manipulado o un proxy que inyecte {"purchase_valid": true} NO consigue nada:
no tiene forma de firmar un recibo válido sin el secreto del servidor.

Expone:  POST /activar-premium   con cuerpo {"usuario": "...", "recibo": "<pedido>.<firma>"}
Uso:     python3 servidor_compras_seguro.py            # 127.0.0.1:8092

El módulo `emitir_recibo` simula lo que hace la TIENDA al cobrar (lado servidor de confianza),
y se usa en el test para generar recibos legítimos.
"""
import hashlib
import hmac
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# Secreto del servidor. En producción no es un HMAC casero: es la verificación del recibo
# contra la API de la tienda. Aquí sirve para demostrar el principio "el cliente no puede
# fabricar la prueba de compra".
SECRETO_TIENDA = b"secreto-servidor-solo-backend-UT6"

RECIBOS_CONSUMIDOS = set()   # anti-reutilización (estado en memoria)
PREMIUM_CONCEDIDO = set()


def emitir_recibo(id_pedido: str) -> str:
    """Lo hace la TIENDA tras cobrar. Devuelve '<id_pedido>.<firma_hex>'."""
    firma = hmac.new(SECRETO_TIENDA, id_pedido.encode(), hashlib.sha256).hexdigest()
    return f"{id_pedido}.{firma}"


def _firma_valida(recibo: str) -> bool:
    if "." not in recibo:
        return False
    id_pedido, firma = recibo.rsplit(".", 1)
    esperada = hmac.new(SECRETO_TIENDA, id_pedido.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(esperada, firma)


def procesar_compra(payload: dict) -> dict:
    """LÓGICA SEGURA: verifica el recibo firmado en el servidor. Ignora cualquier flag."""
    usuario = payload.get("usuario", "")
    recibo = payload.get("recibo", "")
    if not recibo or not _firma_valida(recibo):
        return {"premium": False, "motivo": "recibo ausente o firma no válida"}
    id_pedido = recibo.rsplit(".", 1)[0]
    if id_pedido in RECIBOS_CONSUMIDOS:
        return {"premium": False, "motivo": "recibo ya utilizado"}
    RECIBOS_CONSUMIDOS.add(id_pedido)
    PREMIUM_CONCEDIDO.add(usuario)
    return {"premium": True, "motivo": "recibo verificado en servidor"}


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
    print("[compras-seguro] escuchando en http://127.0.0.1:8092/activar-premium")
    print("[compras-seguro] recibo de ejemplo:", emitir_recibo("pedido-0001"))
    ThreadingHTTPServer(("127.0.0.1", 8092), Handler).serve_forever()
