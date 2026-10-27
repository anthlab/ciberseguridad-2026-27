#!/usr/bin/env bash
# PPS UT8 · Ingeniería del caos a pequeña escala.
# Mata el proceso del portal estable (SIGKILL) y mide el tiempo REAL de recuperación
# gracias a la política restart: unless-stopped. El número sale del cronómetro, no del deseo.
set -euo pipefail
cd "$(dirname "$0")"

SVC="portal-estable"
URL="http://localhost:8091/health"
sano() { curl -s -o /dev/null -w '%{http_code}' --max-time 2 "$URL" 2>/dev/null || echo 000; }

echo "Estado previo: HTTP $(sano)"
echo "$(date +%T.%3N)  MATANDO $SVC (SIGKILL) — simula la caída del proceso"
docker kill "$SVC" >/dev/null
t0=$(date +%s.%N)

# Docker reinicia el contenedor por la política restart. Esperamos hasta /health=200.
deadline=$((SECONDS + 120))
until [ "$(sano)" = "200" ]; do
  [ "$SECONDS" -lt "$deadline" ] || { echo "FALLO: servicio no recuperado en 120 s" >&2; exit 1; }
  sleep 0.2
done
t1=$(date +%s.%N)

echo "$(date +%T.%3N)  RECUPERADO — HTTP 200"
mttr=$(awk "BEGIN{printf \"%.2f\", $t1 - $t0}")
echo "Tiempo REAL de recuperación (MTTR): ${mttr} s"
echo "Este número es medido, no estimado."
