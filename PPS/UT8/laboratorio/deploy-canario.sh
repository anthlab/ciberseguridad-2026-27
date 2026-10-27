#!/usr/bin/env bash
# PPS UT8 · Despliegue canario con sonda de disponibilidad y REVERSIÓN AUTOMÁTICA.
#
#   ./deploy-canario.sh                      # canario sano -> se promueve
#   CANARY_FAIL=http5xx ./deploy-canario.sh  # canario degradado -> reversión automática
#
# Deja un log con marca temporal por sonda: esa es la evidencia de PPS-E14.
set -euo pipefail
cd "$(dirname "$0")"

COMPOSE="docker compose -f docker-compose.canario.yml"
UMBRAL=20            # % de errores que dispara la reversión
MUESTRAS=20          # nº de sondas
INTERVALO=1          # s entre sondas
CANARY_URL="http://localhost:8092/health"
LOG="deploy-$(date +%Y%m%d-%H%M%S).log"

log() { echo "$(date +%H:%M:%S) $*" | tee -a "$LOG"; }

log "== Estado de partida: solo ESTABLE (v1.0.0) sirviendo en :8091 =="
$COMPOSE up -d estable
sleep 3

log "== Desplegando CANARIO (v2.0.0, FAIL_MODE=${CANARY_FAIL:-none}) en :8092 =="
CANARY_FAIL="${CANARY_FAIL:-none}" $COMPOSE --profile canario up -d canario
sleep 4   # respeta el start_period del healthcheck

log "== Sonda de disponibilidad sobre el canario: $MUESTRAS muestras =="
err=0
for i in $(seq 1 "$MUESTRAS"); do
    code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 2 "$CANARY_URL" || echo 000)
    if [ "$code" = "200" ]; then
        log "  sonda $i/$MUESTRAS -> $code OK"
    else
        err=$((err + 1)); log "  sonda $i/$MUESTRAS -> $code FALLO"
    fi
    sleep "$INTERVALO"
done

tasa=$(( err * 100 / MUESTRAS ))
log "== Tasa de error del canario: ${tasa}% (umbral ${UMBRAL}%) =="

if [ "$tasa" -gt "$UMBRAL" ]; then
    log "!! DEGRADACIÓN DETECTADA -> REVERSIÓN AUTOMÁTICA"
    $COMPOSE --profile canario stop canario >/dev/null
    $COMPOSE --profile canario rm -f canario >/dev/null
    log ">> Reversión completada: el canario se retira, ESTABLE (:8091) sigue intacto."
    log ">> Evidencia PPS-E14 en: $LOG"
else
    log "OK: canario sano -> PROMOCIÓN."
    log "   En producción aquí se subiría su peso en nginx-canario.conf y se recargaría el proxy."
    log ">> Evidencia PPS-E14 en: $LOG"
fi
