#!/usr/bin/env bash
# PPS UT8 · Ensayo de recuperación ante desastres con RTO y RPO MEDIDOS (no estimados).
#
# Secuencia realista:
#   1) copia verificada de partida
#   2) actividad posterior (datos aún NO respaldados) -> esto es lo que se perderá
#   3) DESASTRE: se borra la BD en caliente
#   4) RESTAURACIÓN desde la última copia + cronómetro hasta /health=200
#   5) RTO medido (cronómetro) y RPO medido (recuento de datos perdidos y ventana)
#
# Requiere el portal estable en marcha (docker compose -f docker-compose.canario.yml up -d estable).
# Genera la evidencia de PPS-E15.
set -euo pipefail
cd "$(dirname "$0")/.."

DB="datos/soc.db"
URL="http://localhost:8091/health"
sano() { curl -s -o /dev/null -w '%{http_code}' --max-time 2 "$URL" 2>/dev/null || echo 000; }

echo "== 1) Copia de seguridad verificada de partida =="
dr/backup.sh
ULT=$(ls -t backups/soc-*.db | head -1)
T_BACKUP=$(stat -c %Y "$ULT")
N_BACKUP=$(sqlite3 "$ULT" "SELECT COUNT(*) FROM alertas;")
echo "Copia de referencia: $ULT ($N_BACKUP alertas)"
echo

echo "== 2) Actividad POSTERIOR a la copia (datos todavía sin respaldar) =="
sleep 2   # abre una ventana temporal medible entre copia y desastre
python3 - "$DB" <<'PY'
import sqlite3, sys, datetime
c = sqlite3.connect(sys.argv[1])
m = c.execute("SELECT COALESCE(MAX(id),0) FROM alertas").fetchone()[0]
for k in range(1, 26):   # 25 alertas nuevas tras la copia
    c.execute("INSERT INTO alertas(id,ts,severidad,regla,origen,host) VALUES(?,?,?,?,?,?)",
              (m + k, datetime.datetime.now().isoformat(), "alta", "c2-beacon",
               "192.0.2.66", "portal-soc.xest.local"))
c.commit()
print("Insertadas 25 alertas nuevas. Total ahora:",
      c.execute("SELECT COUNT(*) FROM alertas").fetchone()[0])
PY
N_ANTES=$(sqlite3 "$DB" "SELECT COUNT(*) FROM alertas;")
echo

echo "== 3) DESASTRE: se pierde la BD en caliente =="
t0=$(date +%s.%N)
T_DESASTRE=$(date +%s)
rm -f "$DB"
docker kill portal-estable >/dev/null 2>&1 || true
echo "BD borrada a las $(date -d @"$T_DESASTRE" +%T). Servicio ahora: HTTP $(sano)"
echo

echo "== 4) RESTAURACIÓN desde la última copia buena =="
sqlite3 "$ULT" ".backup '$DB'"                                   # restaura el fichero
docker start portal-estable >/dev/null 2>&1 \
    || docker compose -f docker-compose.canario.yml up -d estable >/dev/null
deadline=$((SECONDS + 120))
until [ "$(sano)" = "200" ]; do
  [ "$SECONDS" -lt "$deadline" ] || { echo "FALLO: servicio no recuperado en 120 s" >&2; exit 1; }
  sleep 0.2
done
t1=$(date +%s.%N)

RTO=$(awk "BEGIN{printf \"%.1f\", $t1 - $t0}")
N_TRAS=$(sqlite3 "$DB" "SELECT COUNT(*) FROM alertas;")
PERDIDAS=$(( N_ANTES - N_TRAS ))
RPO_S=$(( T_DESASTRE - T_BACKUP ))
echo

echo "================ RESULTADO DEL ENSAYO (MEDIDO) ================"
printf ' Tiempo de recuperación observado: %s s   (hasta /health=200 tras el desastre)\n' "$RTO"
printf ' Ventana sin copia: %s s   (aproximación por fecha del fichero de copia)\n' "$RPO_S"
printf ' Datos perdidos: %s alertas (las insertadas tras la copia)\n' "$PERDIDAS"
printf ' Copia usada   : %s\n' "$ULT"
echo "=============================================================="
echo "Estos números salen del cronómetro y del recuento, no de una estimación."

echo "Distingue estas medidas del ensayo de los objetivos RTO/RPO acordados. Para la pérdida temporal efectiva, contrasta las marcas de los últimos datos recuperados."
