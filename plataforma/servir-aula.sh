#!/usr/bin/env bash
# Sirve la web del curso en la red del aula (sin Internet).
#   ./plataforma/servir-aula.sh [puerto]      (por defecto 8000)
# Si no existe _build/site, la genera primero (necesita uv y, la primera vez, Internet).
set -euo pipefail
cd "$(dirname "$0")/.."
PUERTO="${1:-8000}"
if [ ! -f _build/site/index.html ]; then
  uv run --with-requirements plataforma/requirements.txt python3 plataforma/build.py
fi
IP=$(hostname -I 2>/dev/null | awk '{print $1}' || true)
[ -n "${IP:-}" ] || IP=$(ipconfig getifaddr en0 2>/dev/null || echo "IP-del-equipo")
echo "Alumnado: http://$IP:$PUERTO/   (Ctrl+C para parar)"
exec python3 -m http.server "$PUERTO" --bind 0.0.0.0 --directory _build/site
