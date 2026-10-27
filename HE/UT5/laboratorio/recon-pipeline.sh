#!/usr/bin/env bash
# HE UT5 · Práctica 02 — pipeline de enumeración activa (HE-E10)
# Orquesta el recon activo contra UN objetivo autorizado del laboratorio xest y deja
# TODAS las salidas en una carpeta de evidencia. NO explota nada: solo descubre y sondea.
#
# Uso:   ./recon-pipeline.sh objetivo.xest.local  [dominio_base]
#   ej.  ./recon-pipeline.sh objetivo.xest.local xest.local
#
# Reglas (rúbrica R1, salida cero): SOLO objetivos *.xest.local de la VLAN aislada.
# Un objetivo fuera de alcance = 0 en la práctica y protocolo de convivencia. El script
# aborta si el objetivo no termina en .xest.local, como barrera técnica de esa regla.
set -euo pipefail

OBJ="${1:-}"
DOM="${2:-xest.local}"
WORDLIST="${WORDLIST:-/usr/share/seclists/Discovery/Web-Content/common.txt}"

if [[ -z "$OBJ" ]]; then
  echo "uso: $0 <objetivo.xest.local> [dominio_base]" >&2; exit 2
fi

# --- Barrera de alcance: sin esto no se ejecuta nada (regla dura del módulo) ---
if [[ "$OBJ" != *.xest.local ]]; then
  echo ">> ABORTA: '$OBJ' no es un objetivo *.xest.local del laboratorio." >&2
  echo ">> Enumerar fuera de alcance = 0 en la práctica. Revisa el objetivo." >&2
  exit 3
fi

# Comprobar que resuelve antes de tocar nada (un cero sin verificar no vale)
if ! getent hosts "$OBJ" >/dev/null; then
  echo ">> ABORTA: '$OBJ' no resuelve. ¿Está levantado docker-compose y el DNS del lab?" >&2
  exit 4
fi

STAMP="$(date +%Y%m%d-%H%M%S)"
OUT="recon_${OBJ}_${STAMP}"
mkdir -p "$OUT"; cd "$OUT"
echo "== Evidencia en $(pwd) =="

log() { printf '\n### %s — %s\n' "$(date +%H:%M:%S)" "$*"; }

have() { command -v "$1" >/dev/null 2>&1; }

# --- Fase 0: pasivo institucional (no toca el objetivo) ---
log "Fase 0 · pasivo (crt.sh + subfinder) sobre $DOM"
curl -s "https://crt.sh/?q=%25.${DOM}&output=json" 2>/dev/null \
  | jq -r '.[].name_value' 2>/dev/null | sort -u > crtsh.txt || true
if have subfinder; then subfinder -d "$DOM" -silent > subs_pasivos.txt || true; fi
cat crtsh.txt subs_pasivos.txt 2>/dev/null | sort -u > hosts_candidatos.txt || true
echo "  hosts candidatos: $(wc -l < hosts_candidatos.txt 2>/dev/null || echo 0)"

# --- Fase 1: activo (a partir de aquí el SOC nos ve) ---
log "Fase 1 · resolución de hosts vivos (dnsx)"
if have dnsx; then
  subfinder -d "$DOM" -silent 2>/dev/null | dnsx -silent -a -resp > hosts.txt || true
fi
[[ -s hosts.txt ]] || echo "$OBJ" > hosts.txt

log "Fase 1 · nmap -sV -sC contra $OBJ"
nmap -sV -sC -oA nmap_objetivo "$OBJ" || echo "  (nmap devolvió error, revisar a mano)"

log "Fase 1 · httpx (título/tecnología/servidor)"
if have httpx; then
  httpx -l hosts.txt -title -tech-detect -status-code -server -o httpx.txt || true
fi

log "Fase 1 · ffuf (fuzzing de contenido)"
if have ffuf && [[ -r "$WORDLIST" ]]; then
  ffuf -u "http://${OBJ}/FUZZ" -w "$WORDLIST" -mc 200,301,302,401,403 \
       -of csv -o ffuf.csv -s || true
else
  echo "  (ffuf no disponible o wordlist no legible: $WORDLIST)"
fi

log "Fase 1 · nuclei (plantillas)"
if have nuclei; then
  nuclei -u "http://${OBJ}" -severity critical,high,medium -o nuclei.txt -silent || true
fi

# --- Fase 2: verificación manual mínima (confirma lo que nuclei sugiere) ---
log "Fase 2 · verificación a mano (cabeceras / directorio / TRACE)"
{
  echo "== curl -sI / =="
  curl -sI "http://${OBJ}/" || true
  echo; echo "== /static/ (autoindex?) =="
  curl -s "http://${OBJ}/static/" | head -5 || true
  echo; echo "== TRACE =="
  curl -s -X TRACE "http://${OBJ}/" -i | head -5 || true
} > verificacion_manual.txt 2>&1
echo "  -> verificacion_manual.txt"

log "LISTO. Evidencia completa en $(pwd)"
echo "Siguiente paso (a mano): rellenar plantilla-inventario-HE-E10.md con estas salidas,"
echo "verificando cada hallazgo automático antes de darlo por bueno."
