#!/usr/bin/env bash
# bench-wifi.sh — mide la velocidad REAL de crackeo WPA2 (hashcat modo 22000)
# en el equipo del aula y muestra cómo alimentar tiempo_crackeo.py con ese dato.
#
# HE · UT3. Uso:  bash bench-wifi.sh
#
# No ataca nada: solo corre el benchmark interno de hashcat.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! command -v hashcat >/dev/null 2>&1; then
  echo "[!] hashcat no está instalado. En Kali:  sudo apt install -y hashcat" >&2
  exit 1
fi

echo "[*] Benchmark WPA2 (modo 22000). Puede tardar ~1 min..."
echo "[*] Fíjate en la línea 'Speed.#*' del resultado (H/s, kH/s o MH/s)."
echo "----------------------------------------------------------------------"

# -b: benchmark ; -m 22000: WPA-PBKDF2-PMKID+EAPOL. Mostramos la salida íntegra:
# el alumno lee la velocidad agregada 'Speed.#*.........: N unidad'.
hashcat -b -m 22000 || {
  echo "[!] hashcat -b falló. Sin GPU prueba CPU:  hashcat -b -m 22000 -D 1" >&2
  exit 1
}

cat <<'EOF'
----------------------------------------------------------------------
Ahora convierte esa velocidad a H/s y pásasela a tiempo_crackeo.py:

  - 412.3 kH/s   -> 412300
  - 1.85 MH/s    -> 1850000
  - 12.4 GH/s    -> 12400000000   (poco realista en WPA2: revisa la unidad)

  python3 tiempo_crackeo.py --rate <TU_H/s> --tabla

Recuerda: WPA2 es LENTO (PBKDF2, 4096 iteraciones). Velocidades típicas van de
kH/s (CPU) a unos pocos MH/s (GPU de gama alta). Si ves GH/s, has confundido la
unidad al convertir.
EOF
