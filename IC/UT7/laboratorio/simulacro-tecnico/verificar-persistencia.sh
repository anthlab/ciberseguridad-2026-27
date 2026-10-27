#!/bin/bash
# verificar-persistencia.sh — CHECKPOINT objetivo de IC-E13 (RA4.d).
# Comprueba, sobre el contenedor comprometido, que las cuatro puertas traseras están
# cerradas Y que el servicio sigue en pie. Cualquier puerta abierta se marca [FALLO]
# con la etiqueta de cuál es. 6/6 en verde = erradicación completa y servicio restaurado.
#
# Uso:  bash verificar-persistencia.sh
set -uo pipefail

CONT=portal-comprometido
URL=http://localhost:8090
verde=0
total=6

check() {           # check "<etiqueta>" <0-si-limpio>
  local etiqueta="$1" rc="$2"
  if [ "$rc" -eq 0 ]; then
    echo "[OK]   $etiqueta"
    verde=$((verde+1))
  else
    echo "[FALLO] $etiqueta"
  fi
}

# 1 · webshell: ningún .php con eval/base64 en el webroot
docker exec "$CONT" bash -c \
  'grep -RIlq --include="*.php" -e "eval(" -e "base64_decode" /var/www/html' 2>/dev/null
[ $? -ne 0 ] && rc=0 || rc=1
check "webshell: no se encuentra ningún .php con eval/base64 en el webroot" "$rc"

# 2 · usuario backdoor svc-backup no existe
docker exec "$CONT" id svc-backup >/dev/null 2>&1 && rc=1 || rc=0
check "usuario backdoor: svc-backup no existe" "$rc"

# 3 · sin cron hacia la IP del atacante
docker exec "$CONT" bash -c \
  'grep -RIlq -e "10.10.66.66" -e "bash -i" /etc/cron.d /etc/cron.* 2>/dev/null' 2>/dev/null
[ $? -ne 0 ] && rc=0 || rc=1
check "cron malicioso: sin tareas hacia 10.10.66.66" "$rc"

# 4 · sin SUID sospechoso fuera de rutas de sistema
n=$(docker exec "$CONT" bash -c \
  'find / -perm -4000 -type f 2>/dev/null | grep -vE "^/usr/(bin|lib)" | wc -l' 2>/dev/null)
[ "${n:-1}" -eq 0 ] && rc=0 || rc=1
check "binario SUID: sin SUID sospechoso fuera de rutas de sistema" "$rc"

# 5 · el servicio responde 200
code=$(curl -s -o /dev/null -w '%{http_code}' "$URL/" 2>/dev/null)
[ "$code" = "200" ] && rc=0 || rc=1
check "servicio: HTTP 200 en $URL/" "$rc"

# 6 · la webshell ya no responde (404)
code=$(curl -s -o /dev/null -w '%{http_code}' "$URL/assets/.cache.php" 2>/dev/null)
[ "$code" = "404" ] && rc=0 || rc=1
check "webshell viva: /assets/.cache.php ya no responde (404)" "$rc"

echo "======================================================"
if [ "$verde" -eq "$total" ]; then
  echo "RESULTADO: LIMPIO — $verde/$total comprobaciones en verde"
  exit 0
else
  echo "RESULTADO: PENDIENTE — $verde/$total en verde (revisa los [FALLO])"
  exit 1
fi
