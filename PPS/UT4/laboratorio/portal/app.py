"""Portal SOC de xest — versión VULNERABLE de partida (PPS · UT4).

Este es el código sobre el que trabaja el alumnado en la UT4. Contiene, DE FORMA
DELIBERADA, las cuatro familias de vulnerabilidad de RA3:

  1. SQLi en el login  ..............  concatenación de la entrada en la consulta.
  2. XSS reflejado (/buscar) y almacenado (/comentarios) .. salida sin codificar.
  3. Gestión de sesión débil ........  cookie sin HttpOnly/Secure/SameSite y sin
                                       rotación del identificador tras autenticar
                                       (permite fijación de sesión).
  4. IDOR en /recurso/<id> ..........  no comprueba que el recurso sea del usuario.

El alumnado debe: (E6) explotar cada una en laboratorio y (E7) corregirlas de forma
ESTRUCTURAL en este mismo fichero y escribir una prueba de regresión por cada una.

Ejecutar SOLO en la VLAN de aula aislada:
    pip install flask
    flask --app app run           # http://127.0.0.1:5000
"""
from __future__ import annotations
import secrets
import sqlite3

from flask import Flask, make_response, redirect, request

# Semilla de datos del laboratorio (sintética, sin datos personales reales).
USUARIOS = [
    # (id, usuario, password, rol)
    (1, "ana", "ana123", "analista"),
    (2, "bruno", "bruno123", "analista"),
    (3, "admin", "admin123", "admin"),
]

# recurso_id -> (dueño_id, contenido)
RECURSOS = {
    101: (1, "Informe de incidente de Ana: phishing dirigido a RRHH."),
    102: (2, "Informe de incidente de Bruno: escaneo de puertos externo."),
    103: (3, "Cuadro de mando del SOC (solo administración)."),
}


def _abrir_db() -> sqlite3.Connection:
    """Base de datos en memoria, sembrada en cada petición (reproducible en clase)."""
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE usuarios (id INT, usuario TEXT, password TEXT, rol TEXT)")
    db.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", USUARIOS)
    return db


def create_app() -> Flask:
    app = Flask(__name__)

    # Almacén de sesiones en memoria del proceso: sid -> datos del usuario.
    sesiones: dict[str, dict] = {}
    # Muro de comentarios (para el XSS almacenado).
    comentarios: list[str] = []

    def usuario_actual() -> dict | None:
        return sesiones.get(request.cookies.get("sid", ""))

    @app.get("/")
    def indice():
        return (
            "<h1>Portal SOC · xest — acceso</h1>"
            '<form method="post" action="/login">'
            'Usuario: <input name="usuario">'
            'Contraseña: <input name="password" type="password">'
            '<button type="submit">Entrar</button></form>'
            '<p><a href="/buscar?q=incidente">Buscar</a> · '
            '<a href="/comentarios">Comentarios</a></p>'
        )

    @app.post("/login")
    def login():
        u = request.form.get("usuario", "")
        p = request.form.get("password", "")
        db = _abrir_db()
        # VULNERABLE (SQLi): dato y código en el mismo canal.
        consulta = (
            "SELECT id, usuario, rol FROM usuarios "
            f"WHERE usuario = '{u}' AND password = '{p}'"
        )
        fila = db.execute(consulta).fetchone()
        db.close()
        if not fila:
            return "Credenciales no válidas.", 401
        # VULNERABLE (sesión): reutiliza el sid que traiga el cliente -> fijación.
        sid = request.cookies.get("sid") or secrets.token_hex(16)
        sesiones[sid] = {"id": fila[0], "usuario": fila[1], "rol": fila[2]}
        resp = make_response(redirect("/panel"))
        # VULNERABLE (sesión): cookie sin HttpOnly, sin Secure, sin SameSite.
        resp.set_cookie("sid", sid)
        return resp

    @app.get("/panel")
    def panel():
        u = usuario_actual()
        if not u:
            return redirect("/")
        return f"<h1>Panel de {u['usuario']} ({u['rol']})</h1>"

    @app.get("/buscar")
    def buscar():
        q = request.args.get("q", "")
        # VULNERABLE (XSS reflejado): refleja la entrada sin codificar.
        return f"<h1>Resultados para: {q}</h1><p>Sin coincidencias.</p>"

    @app.route("/comentarios", methods=["GET", "POST"])
    def ver_comentarios():
        if request.method == "POST":
            comentarios.append(request.form.get("texto", ""))
            return redirect("/comentarios")
        # VULNERABLE (XSS almacenado): vuelca los comentarios sin codificar.
        items = "".join(f"<li>{c}</li>" for c in comentarios)
        return (
            "<h1>Comentarios del turno</h1>"
            f"<ul>{items}</ul>"
            '<form method="post"><input name="texto">'
            '<button type="submit">Publicar</button></form>'
        )

    @app.get("/recurso/<int:rid>")
    def recurso(rid: int):
        u = usuario_actual()
        if not u:
            return redirect("/")
        registro = RECURSOS.get(rid)
        if registro is None:
            return "No existe.", 404
        _duenno, contenido = registro
        # VULNERABLE (IDOR): no comprueba que el recurso sea del usuario actual.
        return f"<pre>{contenido}</pre>"

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=False)
