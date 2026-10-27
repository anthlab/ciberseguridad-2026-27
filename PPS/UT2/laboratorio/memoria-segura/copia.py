#!/usr/bin/env python3
"""PPS · UT2 · El mismo programa en Python — SOLO LABORATORIO.

Python tiene seguridad de memoria: los objetos gestionan su propia memoria y no
existe la copia sin límites de C. El desbordamiento de pila no ocurre. El riesgo
en Python NO es la memoria: es la *cadena de suministro* (paquetes maliciosos) y
construcciones como eval()/pickle sobre datos de entrada. Eso se ve en el resto
de la unidad.

Ejecutar:
    python3 copia.py ana
    python3 copia.py $(python3 -c 'print("A"*64)')   # imprime las 64 A, sin corromper nada
"""
import sys


def guardar_nombre(entrada: str) -> None:
    # str gestiona su tamaño; no hay buffer fijo que desbordar.
    print(f"Nombre guardado: {entrada}")


def main() -> int:
    if len(sys.argv) < 2:
        print(f"uso: {sys.argv[0]} <nombre>", file=sys.stderr)
        return 1
    guardar_nombre(sys.argv[1])
    print("Fin del programa.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
