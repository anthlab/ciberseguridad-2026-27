#!/usr/bin/env bash
# Auditoría ANTES/DESPUÉS del portal SOC de xest — PPS-E9.
#
# La mitad del entregable es el "antes": si no lo guardas antes de bastionar, no
# puedes demostrar la mejora, solo afirmarla. Este script deja las evidencias en
# ./evidencia y, en la fase "despues", genera el diff que prueba el endurecimiento.
#
# Uso:
#   ./auditar.sh antes    [https://portal-soc.xest.local]   # con la config floja
#   # ... aplicar el baseline y  sudo nginx -t && sudo systemctl reload nginx ...
#   ./auditar.sh despues  [https://portal-soc.xest.local]   # con la config endurecida
#
# Requiere: testssl.sh y lynis en el PATH. Solo VLAN aislada de xest.
set -u

FASE="${1:-antes}"
OBJETIVO="${2:-https://portal-soc.xest.local}"
OUT="$(cd "$(dirname "$0")" && pwd)/evidencia"
mkdir -p "$OUT"

case "$FASE" in
  antes|despues) ;;
  *) echo "fase inválida: usa 'antes' o 'despues'"; exit 2 ;;
esac

echo "== [$FASE] Auditoría TLS de $OBJETIVO con testssl.sh =="
if command -v testssl.sh >/dev/null 2>&1; then
  testssl.sh --quiet --color 0 "$OBJETIVO" > "$OUT/${FASE}-tls.txt" 2>&1 \
    && echo "   -> $OUT/${FASE}-tls.txt"
else
  echo "   [AVISO] testssl.sh no está en el PATH; instálalo o clónalo del repo oficial."
fi

echo "== [$FASE] Auditoría del sistema con Lynis =="
if command -v lynis >/dev/null 2>&1; then
  sudo lynis audit system --quiet > "$OUT/${FASE}-lynis.txt" 2>&1 \
    && echo "   -> $OUT/${FASE}-lynis.txt"
  # El índice de endurecimiento de Lynis: número que sube al bastionar.
  grep -i "Hardening index" "$OUT/${FASE}-lynis.txt" || true
else
  echo "   [AVISO] lynis no está en el PATH."
fi

if [ "$FASE" = "despues" ] && [ -f "$OUT/antes-tls.txt" ] && [ -f "$OUT/despues-tls.txt" ]; then
  echo "== Diferencia TLS antes/después (la mejora, medida) =="
  diff "$OUT/antes-tls.txt" "$OUT/despues-tls.txt" | tee "$OUT/diff-tls.txt"
  echo "   -> $OUT/diff-tls.txt"
fi

echo "Hecho. Evidencias en: $OUT"
