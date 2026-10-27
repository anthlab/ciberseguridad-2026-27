#!/usr/bin/env bash
# Comprueba conectividad HTTP. Uso: bash smoke-test.sh portal|web|historico
# No sustituye login, operación funcional ni aceptación de la práctica.
set -euo pipefail
scope="${1:-web}"
ok=0; ko=0
check() {
  local label="$1" url="$2"
  if curl -fLsS --connect-timeout 3 --max-time 15 "$url" >/dev/null; then
    printf '[OK] %s\n' "$label"; ok=$((ok+1))
  else
    printf '[FALLO] %s — %s\n' "$label" "$url"; ko=$((ko+1))
  fi
}
command -v curl >/dev/null || { echo '[FALLO] Falta curl'; exit 1; }
case "$scope" in
 portal) check 'Portal' http://127.0.0.1:8080/ ;;
 web)
  check 'Portal' http://127.0.0.1:8080/
  check 'Juice Shop' http://127.0.0.1:3000/
  check 'DVWA login' http://127.0.0.1:8081/login.php ;;
 historico)
  check 'vuln-web' http://127.0.0.1:8082/
  check 'bWAPP' http://127.0.0.1:8083/ ;;
 *) echo 'Uso: bash smoke-test.sh portal|web|historico'; exit 2 ;;
esac
printf '%s respuestas correctas; %s fallos.\n' "$ok" "$ko"
[ "$ko" -eq 0 ] || exit 1
echo 'Conectividad HTTP comprobada. Completa la prueba funcional de la ficha.'
