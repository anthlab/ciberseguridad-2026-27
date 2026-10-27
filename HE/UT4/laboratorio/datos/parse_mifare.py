#!/usr/bin/env python3
"""parse_mifare.py - analizador didactico de un volcado MIFARE Classic 1K.

Uso:
    python3 parse_mifare.py tarjeta-lab-01.dump

Lee un volcado de 64 bloques (16 bytes/bloque, un bloque por linea en hex) y
muestra: bloque de fabricante (UID/BCC/SAK/ATQA), claves A/B de cada sector,
si son claves POR DEFECTO, datos ASCII imprimibles y bloques de valor.

Curso HE 5025 - CIPFP Cheste. Solo para tarjetas de laboratorio (xest-lab).
"""
import sys

DEFAULT_KEYS = {
    "FFFFFFFFFFFF": "clave de fabrica",
    "A0A1A2A3A4A5": "clave de transporte NXP",
    "D3F7D3F7D3F7": "clave publica NDEF",
    "000000000000": "clave nula",
}


def load(path):
    blocks = []
    with open(path) as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            b = bytes.fromhex(line)
            if len(b) != 16:
                sys.exit(f"[!] bloque de {len(b)} bytes (esperados 16): {line}")
            blocks.append(b)
    if len(blocks) not in (64, 256):
        sys.exit(f"[!] {len(blocks)} bloques; una Classic 1K tiene 64")
    return blocks


def printable(b):
    return "".join(chr(c) if 32 <= c < 127 else "." for c in b)


def main():
    if len(sys.argv) != 2:
        sys.exit("uso: python3 parse_mifare.py <fichero.dump>")
    blocks = load(sys.argv[1])
    n_sectores = len(blocks) // 4

    print("=" * 64)
    print(" ANALISIS MIFARE Classic 1K  -  parse_mifare.py")
    print("=" * 64)

    # Bloque 0 - fabricante
    b0 = blocks[0]
    uid = b0[0:4]
    bcc = b0[4]
    bcc_calc = uid[0] ^ uid[1] ^ uid[2] ^ uid[3]
    sak = b0[5]
    atqa = b0[6:8]
    print("\n[ Bloque 0 - fabricante ]")
    print(f"  UID  : {uid.hex().upper()}  ({len(uid)} bytes)")
    print(f"  BCC  : {bcc:02X}  ({'OK' if bcc == bcc_calc else 'INCORRECTO'})")
    print(f"  SAK  : {sak:02X}   ATQA: {atqa.hex().upper()}   -> "
          f"{'MIFARE Classic 1K' if sak == 0x08 else 'otro tipo'}")

    # Sectores y claves
    print("\n[ Claves por sector (trailer) ]")
    debiles = 0
    for s in range(n_sectores):
        trailer = blocks[s * 4 + 3]
        keyA = trailer[0:6].hex().upper()
        acc = trailer[6:10].hex().upper()
        keyB = trailer[10:16].hex().upper()
        etq_a = DEFAULT_KEYS.get(keyA)
        etq_b = DEFAULT_KEYS.get(keyB)
        flag = ""
        if etq_a or etq_b:
            debiles += 1
            flag = "  <-- CLAVE POR DEFECTO"
        print(f"  S{s:02d}  A={keyA} B={keyB}  acc={acc}{flag}")
    print(f"\n  Sectores con clave por defecto: {debiles}/{n_sectores}")

    # Datos ASCII imprimibles (>=4 chars alfanumericos seguidos)
    print("\n[ Datos ASCII imprimibles en bloques de datos ]")
    hallados = 0
    for i, b in enumerate(blocks):
        if i == 0 or i % 4 == 3:
            continue  # saltar fabricante y trailers
        texto = printable(b)
        alfa = sum(c.isalnum() for c in texto)
        if alfa >= 4:
            hallados += 1
            print(f"  bloque {i:2d} (sector {i//4}): '{texto}'")
    if not hallados:
        print("  (ninguno)")

    # Bloques de valor (formato MIFARE value block)
    print("\n[ Posibles bloques de valor (monedero) ]")
    valores = 0
    for i, b in enumerate(blocks):
        if i % 4 == 3:
            continue
        v = int.from_bytes(b[0:4], "little")
        inv = int.from_bytes(b[4:8], "little")
        v2 = int.from_bytes(b[8:12], "little")
        if v == v2 and (v ^ 0xFFFFFFFF) == inv and v != 0:
            valores += 1
            print(f"  bloque {i:2d} (sector {i//4}): saldo = {v} "
                  f"({v/100:.2f} unidades)")
    if not valores:
        print("  (ninguno)")

    print("\n" + "=" * 64)
    print(f" Veredicto: tarjeta {'CLONABLE con claves conocidas' if debiles else 'protegida'}"
          f"  ({debiles}/{n_sectores} sectores debiles)")
    print("=" * 64)


if __name__ == "__main__":
    main()
