#!/usr/bin/env python3
"""Detector de typosquats offline para el ejercicio de UT2 (PPS).

Compara cada dependencia de un requirements.txt con una lista de paquetes PyPI
legítimos y conocidos. Si un nombre NO está en la lista pero se parece mucho a
uno que sí (distancia de edición pequeña), lo marca como sospechoso. Es la
versión "a mano" de lo que hace un SCA en la CI (UT7). No necesita red.

Uso:
    python3 detectar_typosquat.py requirements-sospechoso.txt
"""
import difflib
import sys

# Lista blanca mínima de paquetes legítimos relevantes para el portal SOC.
# En un caso real se usaría el índice completo de PyPI / la lista de más
# descargados; aquí basta con los candidatos del ejercicio.
LEGITIMOS = {
    "flask", "requests", "urllib3", "pyyaml", "cryptography", "python-dateutil",
    "colorama", "numpy", "django", "beautifulsoup4", "gunicorn", "pyjwt",
    "pytest", "coverage", "sqlalchemy",
}


def nombre_paquete(linea: str) -> str:
    """Extrae el nombre del paquete de una línea de requirements (sin versión)."""
    linea = linea.strip()
    for sep in ("==", ">=", "<=", "~=", ">", "<", "!=", "[", ";"):
        if sep in linea:
            linea = linea.split(sep)[0]
    return linea.strip().lower()


def analizar(ruta: str) -> int:
    sospechosos = 0
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            if not linea.strip() or linea.lstrip().startswith("#"):
                continue
            nombre = nombre_paquete(linea)
            if nombre in LEGITIMOS:
                print(f"[ OK ]        {nombre}")
                continue
            # No está en la lista blanca: ¿se parece a alguno legítimo?
            parecidos = difflib.get_close_matches(nombre, LEGITIMOS, n=1, cutoff=0.7)
            if parecidos:
                print(f"[SOSPECHOSO]  {nombre:<18} -> ¿quiso decir '{parecidos[0]}'?")
                sospechosos += 1
            else:
                print(f"[REVISAR]     {nombre:<18} -> no está en la lista blanca y no se parece a nada conocido")
                sospechosos += 1
    print(f"\nResultado: {sospechosos} dependencia(s) a bloquear antes de instalar.")
    return 1 if sospechosos else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("uso: python3 detectar_typosquat.py <requirements.txt>", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(analizar(sys.argv[1]))
