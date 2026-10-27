#!/usr/bin/env python3
"""detecta_clon_rfid.py - regla de deteccion que le FALTA al SOC de xest.

Analiza el log del lector de acceso y marca dos anomalias que un clon de
tarjeta produce y que el control de acceso, por si solo, NO detecta:

  1) Acceso fuera del horario autorizado (07:00-21:00).
  2) 'Viaje imposible': el mismo UID aparece en dos lectores distintos en una
     ventana demasiado corta para desplazarse (indicio de tarjeta duplicada).

Uso:
    python3 detecta_clon_rfid.py lector-rfid.log

Curso HE 5025 - CIPFP Cheste. Ejercicio de equipo morado (UT4).
"""
import sys
from datetime import datetime

HORA_INI, HORA_FIN = 7, 21          # horario laboral autorizado
VENTANA_VIAJE_S = 300               # < 5 min entre lectores = imposible


def cargar(path):
    reg = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            fecha, hora, lector, uid, res = line.split()
            ts = datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M:%S")
            reg.append({"ts": ts, "lector": lector, "uid": uid, "res": res})
    return reg


def main():
    if len(sys.argv) != 2:
        sys.exit("uso: python3 detecta_clon_rfid.py <lector.log>")
    reg = cargar(sys.argv[1])
    alertas = []

    # Regla 1: fuera de horario
    for r in reg:
        if r["res"] == "CONCEDIDO" and not (HORA_INI <= r["ts"].hour < HORA_FIN):
            alertas.append((r["ts"], "FUERA_DE_HORARIO",
                            f"{r['uid']} en {r['lector']} a las {r['ts'].time()}"))

    # Regla 2: viaje imposible (mismo UID, lectores distintos, ventana corta)
    por_uid = {}
    for r in sorted(reg, key=lambda x: x["ts"]):
        prev = por_uid.get(r["uid"])
        if prev and prev["lector"] != r["lector"]:
            dt = (r["ts"] - prev["ts"]).total_seconds()
            if 0 <= dt <= VENTANA_VIAJE_S:
                alertas.append((r["ts"], "VIAJE_IMPOSIBLE",
                                f"{r['uid']}: {prev['lector']} -> {r['lector']} "
                                f"en {int(dt)} s (posible tarjeta duplicada)"))
        por_uid[r["uid"]] = r

    print("=" * 66)
    print(" DETECCION DE CLON RFID - regla propuesta para el SOC")
    print("=" * 66)
    if not alertas:
        print(" Sin anomalias.")
    for ts, tipo, det in sorted(alertas):
        print(f" [{ts}] {tipo:16s} {det}")
    print("=" * 66)
    print(f" Total anomalias: {len(alertas)}  (el control de acceso original: 0)")
    print("=" * 66)


if __name__ == "__main__":
    main()
