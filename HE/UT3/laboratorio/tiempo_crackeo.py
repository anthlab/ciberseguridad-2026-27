#!/usr/bin/env python3
"""Estima el tiempo de crackeo por FUERZA BRUTA de una clave WPA2.

Uso didáctico HE · UT3. Convierte la velocidad medida en el aula (hashcat -m 22000,
en H/s) en el tiempo que tardaría una clave que NO esté en ningún diccionario. Sin
dependencias externas.

Ejemplos:
    # tabla longitud x alfabeto con la velocidad medida
    python3 tiempo_crackeo.py --rate 412000 --tabla

    # un caso concreto
    python3 tiempo_crackeo.py --rate 412000 --longitud 8 --charset loweralphanum

    # comparar dos GPUs / dos alumnos
    python3 tiempo_crackeo.py --rate 4200000000 --longitud 12 --charset mixed
"""
from __future__ import annotations

import argparse

# Tamaño del alfabeto por familia de caracteres.
CHARSETS: dict[str, int] = {
    "digits": 10,            # 0-9
    "lower": 26,             # a-z
    "loweralphanum": 36,     # a-z 0-9
    "mixed": 62,             # a-z A-Z 0-9
    "full": 95,              # imprimibles ASCII (incluye símbolos)
}

SEGUNDOS_POR_ANIO = 365.25 * 24 * 3600  # 31.557.600
TOPE_ANIOS = 100  # por encima de esto lo damos por inviable en clase


def formato_tiempo(segundos: float) -> str:
    """Devuelve el tiempo en la unidad legible más adecuada."""
    if segundos > TOPE_ANIOS * SEGUNDOS_POR_ANIO:
        return f">{TOPE_ANIOS} años"
    if segundos < 1e-3:
        return f"{segundos * 1e6:.1f} us"
    if segundos < 1:
        return f"{segundos * 1e3:.1f} ms"
    unidades = [
        ("años", SEGUNDOS_POR_ANIO),
        ("días", 86400),
        ("h", 3600),
        ("min", 60),
        ("s", 1),
    ]
    for nombre, factor in unidades:
        if segundos >= factor:
            return f"{segundos / factor:.2f} {nombre}"
    return f"{segundos:.2f} s"


def tiempo_medio(rate: float, alfabeto: int, longitud: int) -> tuple[float, int]:
    """Tiempo medio (mitad del espacio de búsqueda) y espacio total."""
    espacio = alfabeto ** longitud
    segundos = (espacio / 2) / rate
    return segundos, espacio


def entropia_bits(alfabeto: int, longitud: int) -> float:
    from math import log2
    return longitud * log2(alfabeto)


def imprime_tabla(rate: float, longitudes: list[int]) -> None:
    familias = list(CHARSETS.items())
    print(f"\nVelocidad: {rate:,.0f} H/s (WPA2, hashcat modo 22000)\n")
    cabecera = "Long".ljust(6) + "".join(
        f"{nombre}({tam})".ljust(18) for nombre, tam in familias
    )
    print(cabecera)
    print("-" * len(cabecera))
    for longitud in longitudes:
        fila = str(longitud).ljust(6)
        for _, tam in familias:
            seg, _ = tiempo_medio(rate, tam, longitud)
            fila += formato_tiempo(seg).ljust(18)
        print(fila)
    print(
        "\nNota: 'tiempo medio' = (alfabeto^longitud / 2) / velocidad. "
        f"Umbral de inviabilidad usado: {TOPE_ANIOS} años.\n"
    )


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--rate", type=float, required=True,
                   help="Velocidad medida en H/s (ver bench-wifi.sh)")
    p.add_argument("--tabla", action="store_true",
                   help="Imprime la tabla longitud x alfabeto")
    p.add_argument("--longitud", type=int, help="Longitud de la clave (caso concreto)")
    p.add_argument("--charset", choices=CHARSETS, default="loweralphanum",
                   help="Alfabeto (caso concreto)")
    args = p.parse_args()

    if args.tabla:
        imprime_tabla(args.rate, [8, 10, 12, 14, 16])
        return

    if args.longitud is None:
        p.error("indica --tabla o --longitud")

    alfabeto = CHARSETS[args.charset]
    seg, espacio = tiempo_medio(args.rate, alfabeto, args.longitud)
    bits = entropia_bits(alfabeto, args.longitud)
    print(f"\nClave: longitud {args.longitud}, alfabeto {args.charset} ({alfabeto} símbolos)")
    print(f"Espacio de búsqueda : {espacio:,} candidatas ({bits:.1f} bits de entropía)")
    print(f"Velocidad           : {args.rate:,.0f} H/s")
    print(f"Tiempo medio (bruta): {formato_tiempo(seg)}\n")


if __name__ == "__main__":
    main()
