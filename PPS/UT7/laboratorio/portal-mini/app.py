"""
portal-mini — servicio de PRÁCTICA con vulnerabilidades a propósito (PPS · UT7).

NO es código de producción. Existe para que las herramientas de la canalización
(Semgrep SAST, Trivy SCA, Checkov IaC) tengan algo que detectar y para demostrar
que la CI BLOQUEA. Solo se ejecuta en la VLAN aislada de laboratorio.

Vulnerabilidades sembradas (búscalas con Semgrep en el laboratorio):
  - Inyección SQL por concatenación de cadena (línea del `cur.execute`).
  - Inyección de comandos por concatenar entrada en `os.popen`.
  - `debug=True` en el arranque (fuga de información en producción).
"""

import os
import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/usuario")
def usuario():
    nombre = request.args.get("nombre", "")            # ENTRADA (no confiable)
    con = sqlite3.connect("portal.db")
    cur = con.cursor()
    # SINK SQL — concatenación => inyección SQL. Semgrep (regla sqli-concat) lo marca.
    cur.execute("SELECT id, rol FROM usuarios WHERE nombre = '" + nombre + "'")
    filas = cur.fetchall()
    con.close()
    return str(filas)


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")       # ENTRADA (no confiable)
    # SINK shell — concatenación => inyección de comandos.
    return os.popen("ping -c1 " + host).read()


if __name__ == "__main__":
    # debug=True en producción expone la consola de depuración: mala configuración.
    app.run(host="0.0.0.0", port=5000, debug=True)
