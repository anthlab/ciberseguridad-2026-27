#!/usr/bin/env python3
"""Muestra alertas de Wazuh (formato alerts.json, una por línea) ordenadas por hora.

Uso:
    python3 ver_alertas.py FICHERO [--min-nivel N] [--agente NOMBRE] [--regla ID] [--ip IP]

Ejemplos:
    python3 ver_alertas.py alertas-SINTETICAS-2026-11-02.jsonl
    python3 ver_alertas.py alertas-SINTETICAS-2026-11-02.jsonl --min-nivel 10
    python3 ver_alertas.py mis-alertas.jsonl --agente pc-alumno
"""
import argparse
import json
import sys


def main() -> int:
    ap = argparse.ArgumentParser(description="Ver alertas de Wazuh ordenadas por hora")
    ap.add_argument("fichero")
    ap.add_argument("--min-nivel", type=int, default=0)
    ap.add_argument("--agente")
    ap.add_argument("--regla")
    ap.add_argument("--ip", help="IP de origen (data.srcip)")
    a = ap.parse_args()

    alertas, malas = [], 0
    with open(a.fichero, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            try:
                alertas.append(json.loads(linea))
            except json.JSONDecodeError:
                malas += 1
    if malas:
        print(f"Aviso: {malas} líneas no son JSON válido y se han ignorado.", file=sys.stderr)

    filas = []
    for al in sorted(alertas, key=lambda x: x.get("timestamp", "")):
        regla, agente = al.get("rule", {}), al.get("agent", {})
        ip = al.get("data", {}).get("srcip", "")
        try:
            nivel = int(regla.get("level", 0))
        except (TypeError, ValueError):
            nivel = 0
        if nivel < a.min_nivel:
            continue
        if a.agente and agente.get("name") != a.agente:
            continue
        if a.regla and str(regla.get("id")) != a.regla:
            continue
        if a.ip and ip != a.ip:
            continue
        filas.append((al.get("timestamp", "")[:19].replace("T", " "), agente.get("name", "?"),
                      str(regla.get("id", "?")), str(regla.get("level", "?")), ip,
                      regla.get("description", "")))

    print(f"{'Hora':19}  {'Agente':14} {'Regla':>6} {'Niv':>3}  {'IP origen':15} Descripción")
    for f in filas:
        print(f"{f[0]:19}  {f[1]:14} {f[2]:>6} {f[3]:>3}  {f[4]:15} {f[5]}")
    print(f"\n{len(filas)} alertas mostradas de {len(alertas)} leídas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
