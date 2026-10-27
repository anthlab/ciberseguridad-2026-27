"""Almacén de credenciales del portal SOC de xest — VERSIÓN DE PARTIDA (insegura).

Guarda las contraseñas como SHA-256 en hexadecimal y SIN sal. Es el punto de
partida que el alumnado debe migrar a Argon2id en el entregable PPS-E8.

Puntos débiles sembrados a propósito (que hay que cerrar):
  - SHA-256 es un hash de propósito general, RÁPIDO: una GPU calcula miles de
    millones por segundo -> fuerza bruta y diccionarios triviales.
  - Sin sal: dos usuarios con la misma clave tienen el mismo hash, y sirven las
    tablas rainbow precalculadas.
  - Sin coste ajustable: no se puede encarecer el cálculo con el hardware nuevo.

NO usar en producción. Solo laboratorio de la VLAN aislada de xest.
"""
import hashlib
import json
import sys
from pathlib import Path

BD = Path(__file__).with_name("usuarios.json")


def _cargar() -> dict:
    return json.loads(BD.read_text(encoding="utf-8"))


def _guardar(datos: dict) -> None:
    BD.write_text(json.dumps(datos, indent=2, ensure_ascii=False), encoding="utf-8")


def hash_legacy(clave: str) -> str:
    """Esquema DÉBIL: SHA-256 sin sal. Rápido de calcular = rápido de crackear."""
    return hashlib.sha256(clave.encode("utf-8")).hexdigest()


def crear_usuario(usuario: str, clave: str) -> None:
    datos = _cargar()
    datos[usuario] = {"hash": hash_legacy(clave), "esquema": "sha256"}
    _guardar(datos)


def verificar(usuario: str, clave: str) -> bool:
    datos = _cargar()
    reg = datos.get(usuario)
    if reg is None:
        return False
    return reg["hash"] == hash_legacy(clave)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("uso: python3 store.py <usuario> <clave>")
        raise SystemExit(2)
    usuario, clave = sys.argv[1], sys.argv[2]
    print("OK" if verificar(usuario, clave) else "DENEGADO")
