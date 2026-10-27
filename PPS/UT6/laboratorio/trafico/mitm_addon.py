"""
Addon de mitmproxy para la práctica de tráfico móvil (PPS · UT6) — solo VLAN de aula.

Resalta en la consola de mitmproxy los hallazgos que buscamos en clase: peticiones en
HTTP en claro, claves de API en cabeceras y contraseñas en el cuerpo. Sirve para que, al
lanzar el simulador de la app, el alumnado VEA marcado el problema sin tener que leer todo
el volcado.

Uso:
    mitmproxy   -s mitm_addon.py --mode regular --listen-port 8080     # interactivo
    mitmdump -q -s mitm_addon.py --mode regular --listen-port 8080     # no interactivo
"""
import re
from mitmproxy import http, ctx

PATRONES = [
    ("API-KEY", re.compile(r"xk_live_[0-9a-f]{16,}", re.I)),
    ("PASSWORD", re.compile(r'"password"\s*:\s*"[^"]+"', re.I)),
    ("BEARER", re.compile(r"Bearer\s+[A-Za-z0-9._-]+", re.I)),
    ("AWS-KEY", re.compile(r"AKIA[0-9A-Z]{8,}", re.I)),
]


def _revisar(texto, origen):
    for etiqueta, patron in PATRONES:
        for m in patron.finditer(texto or ""):
            ctx.log.warn(f"[UT6] {etiqueta} en {origen}: {m.group(0)}")


def request(flow: http.HTTPFlow):
    if flow.request.scheme == "http":
        ctx.log.warn(f"[UT6] HTTP EN CLARO -> {flow.request.pretty_url}")
    # Cabeceras (X-Api-Key, Authorization) y cuerpo (contraseña)
    cabeceras = "\n".join(f"{k}: {v}" for k, v in flow.request.headers.items())
    _revisar(cabeceras, "cabecera")
    _revisar(flow.request.get_text(strict=False), "cuerpo")
