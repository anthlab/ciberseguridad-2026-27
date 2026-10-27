#!/usr/bin/env python3
"""analiza_rf.py - decide si un dispositivo de radio usa CODIGO FIJO
(vulnerable a repeticion/replay) o CODIGO EVOLUTIVO (rolling code).

Uso:
    python3 analiza_rf.py capturas-rf.csv

Agrupa las capturas por dispositivo y compara las tramas (payload_hex). Si el
dispositivo emite SIEMPRE la misma trama, un simple 'replay' abre. Si cada
pulsacion cambia, el replay simple no sirve (rolling code tipo KeeLoq).

Curso HE 5025 - CIPFP Cheste. Capturas de laboratorio (mandos propios).
"""
import csv
import sys
from collections import defaultdict


def main():
    if len(sys.argv) != 2:
        sys.exit("uso: python3 analiza_rf.py <capturas.csv>")
    porta = defaultdict(list)
    with open(sys.argv[1], newline="") as f:
        for row in csv.DictReader(f):
            porta[row["dispositivo"]].append(row)

    print("=" * 68)
    print(" ANALISIS RF - codigo fijo vs rolling code")
    print("=" * 68)
    vulnerables = []
    for disp, caps in porta.items():
        payloads = [c["payload_hex"] for c in caps]
        unicos = set(payloads)
        freq = caps[0]["frecuencia_mhz"]
        mod = caps[0]["modulacion"]
        ratio = len(unicos) / len(payloads)
        if len(unicos) == 1:
            veredicto = "CODIGO FIJO  -> REPLAY VIABLE"
            vulnerables.append(disp)
        elif ratio >= 0.9:
            veredicto = "ROLLING CODE -> replay simple NO viable"
        else:
            veredicto = "MIXTO/PREFIJO comun -> revisar a mano"
        print(f"\n[{disp}]  {freq} MHz / {mod}")
        print(f"  capturas={len(payloads)}  tramas_unicas={len(unicos)}  "
              f"diversidad={ratio:.0%}")
        print(f"  veredicto: {veredicto}")
        if len(unicos) > 1:
            # prefijo comun (posible numero de serie del emisor)
            pref = payloads[0]
            for p in payloads[1:]:
                i = 0
                while i < len(pref) and i < len(p) and pref[i] == p[i]:
                    i += 1
                pref = pref[:i]
            if len(pref) >= 2:
                print(f"  prefijo comun (serie del emisor): {pref}... "
                      f"(la parte que cambia es el contador cifrado)")

    print("\n" + "=" * 68)
    if vulnerables:
        print(" Dispositivos que un atacante abre con captura+replay:")
        for d in vulnerables:
            print(f"   - {d}")
    print(" Contramedida: rolling code / mensaje autenticado con nonce.")
    print("=" * 68)


if __name__ == "__main__":
    main()
