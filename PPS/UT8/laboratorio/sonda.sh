#!/usr/bin/env bash
# PPS UT8 · Sonda de disponibilidad reutilizable.
# Uso:  ./sonda.sh URL [muestras] [intervalo_s]
#       ./sonda.sh http://localhost:8091/health 10 1
# Imprime cada muestra y la tasa de error final (código de salida 1 si hay algún fallo).
set -euo pipefail
URL="${1:?uso: ./sonda.sh URL [muestras] [intervalo]}"
N="${2:-10}"
INT="${3:-1}"
err=0
for i in $(seq 1 "$N"); do
    code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 2 "$URL" || echo 000)
    [ "$code" = "200" ] && estado=OK || { estado=FALLO; err=$((err + 1)); }
    printf '%s  %2d/%d  %s  %s\n' "$(date +%T)" "$i" "$N" "$code" "$estado"
    sleep "$INT"
done
tasa=$(( err * 100 / N ))
echo "Tasa de error: ${tasa}% (${err}/${N})"
[ "$err" -eq 0 ]
