#!/bin/bash
# crear-copia-verificada.sh — PREP DEL PROFESOR (ejecutar UNA vez antes de clase).
# Genera la copia de seguridad limpia del portal y su manifiesto de hashes.
# La copia sale del MISMO webroot legítimo con el que se construye la imagen, así que
# representa el "estado bueno conocido" anterior al compromiso.
set -euo pipefail
cd "$(dirname "$0")"

SRC="../seed/webroot"
OUT="portal-clean.tar.gz"

if [ ! -d "$SRC" ]; then
  echo "ERROR: no encuentro el webroot limpio en $SRC" >&2
  exit 1
fi

tar czf "$OUT" -C "$SRC" .
sha256sum "$OUT" > SHA256SUMS

echo "Copia verificada creada. Anota este hash y guárdalo aparte:"
cat SHA256SUMS
echo
echo "En clase, el alumnado la verificará con:  sha256sum -c SHA256SUMS  ->  $OUT: OK"
