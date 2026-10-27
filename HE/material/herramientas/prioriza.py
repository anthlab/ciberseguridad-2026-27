#!/usr/bin/env python3
"""Priorización de vulnerabilidades por explotabilidad real (HE · UT2).

Toma una lista de CVE y las ordena combinando tres señales, en este orden:

    1. KEV (CISA) — ¿se explota de forma activa? Prioridad máxima.
    2. EPSS       — probabilidad de explotación en 30 días.
    3. CVSS       — gravedad, como desempate.

El objetivo didáctico es que el alumno vea por qué el orden por CVSS descendente es
un error: una vulnerabilidad en KEV con CVSS medio va por delante de una teórica con
CVSS 9.8.

Fuentes de datos (APIs públicas, sin clave):
    - EPSS: https://api.first.org/data/v1/epss?cve=CVE-XXXX-YYYY
    - KEV : https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
    - CVSS: se lee del fichero de entrada (columna cvss) o de la NVD si se amplía.

Uso:
    python3 prioriza.py --cve-list lote_cves.txt --salida priorizado.csv
    python3 prioriza.py --demo        # sin red: usa un lote de ejemplo incrustado

Formato de --cve-list: una línea por CVE, opcionalmente con su CVSS separado por coma:
    CVE-2021-44228,10.0
    CVE-2023-1234
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.request
from typing import Iterable

KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
EPSS_URL = "https://api.first.org/data/v1/epss?cve={}"

DEMO = [
    ("CVE-2021-44228", 10.0),  # Log4Shell — en KEV, EPSS altísimo
    ("CVE-2019-0708", 9.8),    # BlueKeep — en KEV
    ("CVE-2023-99999", 9.9),   # teórica alta, sin explotación conocida
    ("CVE-2020-1472", 10.0),   # Zerologon — en KEV
    ("CVE-2022-12345", 6.5),   # media, supongamos en KEV
]


def leer_lote(path: str) -> list[tuple[str, float | None]]:
    filas: list[tuple[str, float | None]] = []
    with open(path, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            partes = [p.strip() for p in linea.split(",")]
            cve = partes[0].upper()
            cvss = float(partes[1]) if len(partes) > 1 and partes[1] else None
            filas.append((cve, cvss))
    return filas


def cargar_kev() -> set[str]:
    try:
        with urllib.request.urlopen(KEV_URL, timeout=30) as resp:
            data = json.load(resp)
        return {v["cveID"].upper() for v in data.get("vulnerabilities", [])}
    except Exception as exc:  # noqa: BLE001 — sin red, se avisa y se sigue
        print(f"aviso: no se pudo descargar KEV ({exc}); se asume KEV vacío", file=sys.stderr)
        return set()


def epss_de(cve: str) -> float:
    try:
        with urllib.request.urlopen(EPSS_URL.format(cve), timeout=30) as resp:
            data = json.load(resp)
        registros = data.get("data", [])
        if registros:
            return float(registros[0].get("epss", 0.0))
    except Exception as exc:  # noqa: BLE001
        print(f"aviso: EPSS no disponible para {cve} ({exc})", file=sys.stderr)
    return 0.0


def prioriza(lote: Iterable[tuple[str, float | None]], kev: set[str]) -> list[dict]:
    filas = []
    for cve, cvss in lote:
        en_kev = cve in kev
        epss = epss_de(cve)
        filas.append(
            {
                "cve": cve,
                "kev": "SÍ" if en_kev else "no",
                "epss": round(epss, 4),
                "cvss": cvss if cvss is not None else "",
                # Clave de orden: KEV manda, luego EPSS, luego CVSS
                "_orden": (1 if en_kev else 0, epss, cvss or 0.0),
            }
        )
    filas.sort(key=lambda f: f["_orden"], reverse=True)
    for i, fila in enumerate(filas, 1):
        fila["prioridad"] = i
        del fila["_orden"]
    return filas


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cve-list", help="fichero con un CVE por línea (opcional: ,cvss)")
    parser.add_argument("--salida", help="CSV de salida (por defecto, stdout)")
    parser.add_argument("--demo", action="store_true", help="usa un lote de ejemplo sin leer fichero")
    args = parser.parse_args()

    if args.demo:
        lote = DEMO
    elif args.cve_list:
        lote = leer_lote(args.cve_list)
    else:
        parser.error("indica --cve-list o --demo")

    kev = cargar_kev()
    filas = prioriza(lote, kev)

    campos = ["prioridad", "cve", "kev", "epss", "cvss"]
    destino = open(args.salida, "w", newline="", encoding="utf-8") if args.salida else sys.stdout
    escritor = csv.DictWriter(destino, fieldnames=campos, lineterminator="\n")
    escritor.writeheader()
    escritor.writerows(filas)
    if args.salida:
        destino.close()
        print(f"escrito {args.salida} con {len(filas)} vulnerabilidades priorizadas")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
