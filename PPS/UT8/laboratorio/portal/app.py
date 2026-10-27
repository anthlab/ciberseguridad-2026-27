#!/usr/bin/env python3
"""Portal SOC de xest — servicio mínimo con /health para PPS UT8.

Solo biblioteca estándar: corre en cualquier python3 sin `pip install`.
El endpoint /health comprueba DE VERDAD la dependencia (la BD de alertas):
si la base de datos no responde, /health devuelve 503. Ese es el antídoto
contra el "healthcheck que siempre dice healthy".

Variables de entorno:
  PORT       puerto de escucha            (def. 8080)
  DB_PATH    ruta de la BD sqlite         (def. /data/soc.db)
  VERSION    versión que se anuncia       (def. 1.0.0)
  FAIL_MODE  none | http5xx | db          (inyección de fallo del laboratorio)
             - http5xx: toda respuesta es 503 (canario roto -> dispara reversión)
             - db     : ignora la BD real y simula dependencia caída
"""
import json
import os
import sqlite3
import time
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", "8080"))
DB_PATH = os.environ.get("DB_PATH", "/data/soc.db")
VERSION = os.environ.get("VERSION", "1.0.0")
FAIL_MODE = os.environ.get("FAIL_MODE", "none")
START = time.time()


def contar_alertas():
    """Toca la dependencia real. Si la BD no está, lanza excepción y /health cae."""
    if FAIL_MODE == "db":
        raise RuntimeError("dependencia BD simulada como caída (FAIL_MODE=db)")
    con = sqlite3.connect(DB_PATH, timeout=2)
    try:
        return con.execute("SELECT COUNT(*) FROM alertas").fetchone()[0]
    finally:
        con.close()


class H(BaseHTTPRequestHandler):
    def _send(self, code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *_a):  # silencio: el registro lo lleva la sonda
        pass

    def do_GET(self):
        if FAIL_MODE == "http5xx":
            return self._send(503, {"status": "error",
                                    "motivo": "fallo inyectado (http5xx)",
                                    "version": VERSION})
        if self.path == "/health":
            try:
                n = contar_alertas()
            except Exception as e:
                return self._send(503, {"status": "error", "dependencia": "bd",
                                        "detalle": str(e), "version": VERSION})
            return self._send(200, {"status": "ok", "version": VERSION,
                                    "alertas": n,
                                    "uptime_s": round(time.time() - START, 1)})
        if self.path in ("/", "/alertas"):
            try:
                n = contar_alertas()
            except Exception as e:
                return self._send(503, {"status": "error", "detalle": str(e)})
            return self._send(200, {"servicio": "portal-soc",
                                    "version": VERSION, "alertas": n})
        self._send(404, {"status": "no encontrado", "ruta": self.path})


if __name__ == "__main__":
    print(f"portal-soc v{VERSION} escuchando en :{PORT} "
          f"(db={DB_PATH}, fail={FAIL_MODE})", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), H).serve_forever()
