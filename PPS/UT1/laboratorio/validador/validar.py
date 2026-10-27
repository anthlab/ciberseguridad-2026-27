#!/usr/bin/env python3
"""PPS UT1 · Validador de nombre de usuario — versión Python (INTERPRETADO).

Ejercicio PPS-E1: localiza el PUNTO DE ENTRADA, el SINK y la VALIDACIÓN,
y señala DÓNDE PUEDE FALLAR este modelo de ejecución.

Pista: en un lenguaje interpretado, el código fuente viaja al servidor y hay
construcciones que ejecutan cadenas como si fueran código.
"""
import os
import sqlite3


def validar_nombre(nombre: str) -> bool:
    # VALIDACIÓN (débil): solo comprueba longitud, no el contenido.
    return 0 < len(nombre) <= 32


def buscar_usuario(nombre: str):
    # PUNTO DE ENTRADA: 'nombre' viene del exterior.
    if not validar_nombre(nombre):
        raise ValueError("nombre no válido")

    con = sqlite3.connect(":memory:")
    # SINK 1 (SQL): se concatena el dato en la consulta -> inyección SQL.
    consulta = "SELECT * FROM usuarios WHERE nombre = '" + nombre + "'"
    con.execute(consulta)

    # SINK 2 (shell): el dato acaba en una orden del sistema -> inyección de comandos.
    os.system("logger acceso de " + nombre)

    # SINK 3 (ejecución dinámica): construcción propia de lenguajes interpretados.
    regla = "len('" + nombre + "') > 0"
    return eval(regla)   # nunca evaluar cadenas construidas con datos del usuario


if __name__ == "__main__":
    import sys
    print(buscar_usuario(sys.argv[1] if len(sys.argv) > 1 else "ana"))
