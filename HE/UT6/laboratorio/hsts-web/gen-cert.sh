#!/usr/bin/env bash
# Genera el certificado autofirmado de hsts-web (una sola vez).
# Uso:  ./hsts-web/gen-cert.sh
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)/certs"
mkdir -p "$DIR"

if [[ -f "$DIR/hsts.crt" && -f "$DIR/hsts.key" ]]; then
  echo "[=] Certificado ya presente en $DIR — nada que hacer."
  exit 0
fi

openssl req -x509 -newkey rsa:2048 -nodes \
  -keyout "$DIR/hsts.key" -out "$DIR/hsts.crt" \
  -days 825 -subj "/CN=hsts.xest.local" \
  -addext "subjectAltName=DNS:hsts.xest.local,DNS:objetivo.xest.local"

chmod 600 "$DIR/hsts.key"
echo "[+] Certificado generado en $DIR"
echo "    (autofirmado: en las estaciones de aula se acepta la excepción una vez para el lab)"
