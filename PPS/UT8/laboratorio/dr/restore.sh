#!/usr/bin/env bash
# PPS UT8 · Restaura la última copia buena de la BD del SOC sobre datos/soc.db.
set -euo pipefail
cd "$(dirname "$0")/.."

ULT=$(ls -t backups/soc-*.db 2>/dev/null | head -1 || true)
[ -n "$ULT" ] || { echo "No hay copias en backups/ (ejecuta dr/backup.sh primero)"; exit 1; }

sqlite3 "$ULT" ".backup 'datos/soc.db'"
n=$(sqlite3 datos/soc.db "SELECT COUNT(*) FROM alertas;")
echo "Restaurada: $ULT -> datos/soc.db ($n alertas)"
