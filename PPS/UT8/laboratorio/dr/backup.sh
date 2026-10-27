#!/usr/bin/env bash
# PPS UT8 · Copia VERIFICADA de la BD del SOC.
# "Una copia que no se restaura no es una copia." Aquí, además de copiar, se comprueba
# la integridad de la copia (PRAGMA integrity_check): si no pasa, el script falla.
set -euo pipefail
cd "$(dirname "$0")/.."

DB="datos/soc.db"
mkdir -p backups
STAMP=$(date +%Y%m%d-%H%M%S)
OUT="backups/soc-$STAMP.db"

[ -f "$DB" ] || { echo "No existe $DB (¿has ejecutado seed_alertas.py?)"; exit 1; }

sqlite3 "$DB" ".backup '$OUT'"          # copia en caliente, consistente
integridad=$(sqlite3 "$OUT" "PRAGMA integrity_check;")
n=$(sqlite3 "$OUT" "SELECT COUNT(*) FROM alertas;")

echo "$STAMP  copia=$OUT  integridad=$integridad  alertas=$n" | tee -a backups/backups.log

if [ "$integridad" != "ok" ]; then
    echo "COPIA CORRUPTA: integridad=$integridad" >&2
    exit 1
fi
echo "OK: copia verificada -> $OUT ($n alertas)"
