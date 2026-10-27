#!/usr/bin/env bash
# ============================================================================
#  IC · UT3 — Generador de actividad de laboratorio para validar detecciones
# ============================================================================
#  Reproduce, de forma CONTROLADA y en LOOPBACK, las técnicas ATT&CK que las
#  reglas Sigma del SOC de xest deben detectar. Sirve para "disparar" las
#  alertas y comprobar que la telemetría llega y que las reglas funcionan.
#
#  Una regla que no se ha disparado con un evento real está SIN validar.
#  Este script produce ese evento real.
#
#  ┌───────────────────────────────────────────────────────────────────────┐
#  │  SOLO en la VLAN de laboratorio aislada de xest, sobre una máquina de   │
#  │  prácticas con agente Wazuh instalado. NUNCA contra la red del centro   │
#  │  ni contra Internet. Todo el tráfico de este script es a 127.0.0.1.     │
#  └───────────────────────────────────────────────────────────────────────┘
#
#  Uso:
#     sudo bash generar-actividad.sh            # ejecuta las 4 técnicas
#     sudo bash generar-actividad.sh reverse    # solo una: reverse|cron|download|txt
#     sudo bash generar-actividad.sh --limpiar  # borra los artefactos que deja
#
#  Requisitos en la máquina objetivo (Linux con agente Wazuh):
#     - auditd + reglas de execve activas, o Sysmon-for-Linux, para que Wazuh
#       reciba process_creation. Ver ficha-E4-arquitectura.md, paso 4.
#     - nc (netcat), curl y python3 disponibles (vienen de serie en la VM).
# ============================================================================
set -uo pipefail

MARK="[gen-actividad]"
ART_DIR="/tmp/ut3-lab"
CRON_FILE="/etc/cron.d/xest-lab-persist"
mkdir -p "$ART_DIR"

log() { printf '%s %s\n' "$MARK" "$*"; }

# --- Guardarraíl: negarse a correr si parece que NO es la VLAN de laboratorio ---
guardarrail() {
  local ip
  ip="$(hostname -I 2>/dev/null | tr ' ' '\n' | grep -E '^10\.10\.10\.' || true)"
  if [[ -z "$ip" ]]; then
    log "AVISO: no veo una IP 10.10.10.0/24 (la VLAN de laboratorio)."
    log "Si NO estás en el laboratorio aislado de xest, aborta con Ctrl-C ahora."
    log "Continuando en 5 s por si el direccionamiento del aula es otro..."
    sleep 5 2>/dev/null || true
  fi
}

# --- T1: Reverse shell candidata (T1059.004) ------------------------------------
# Levanta un listener LOCAL en 127.0.0.1:9999 y le habla con el patrón /dev/tcp.
# No hay salida a ningún host externo: es una conexión a uno mismo.
tecnica_reverse() {
  log "T1059.004 · reverse shell candidata (bash /dev/tcp a 127.0.0.1)"
  ( timeout 4 nc -lvnp 9999 >/dev/null 2>&1 & ) 2>/dev/null
  sleep 1
  # La línea de comando contiene /dev/tcp/ -> dispara linux_suspicious_reverse_shell.yml
  timeout 3 bash -c 'exec 3<>/dev/tcp/127.0.0.1/9999; echo id >&3' 2>/dev/null || true
  # Variante nc -e (patrón nc_shell)
  timeout 3 bash -c 'nc 127.0.0.1 9999 -e /bin/sh' 2>/dev/null || true
  log "  hecho."
}

# --- T2: Persistencia por cron (T1053.003) --------------------------------------
# Escribe una tarea cron en /etc/cron.d apuntando a un script en /tmp.
tecnica_cron() {
  log "T1053.003 · persistencia vía /etc/cron.d con binario en /tmp"
  echo '#!/bin/sh'                        > "$ART_DIR/.u.sh"
  echo 'echo lab >/dev/null'             >> "$ART_DIR/.u.sh"
  chmod +x "$ART_DIR/.u.sh"
  # TargetFilename en /etc/cron.d + hint /tmp -> dispara linux_persistence_cron_and_systemd.yml
  printf '* * * * * root %s/.u.sh\n' "$ART_DIR" > "$CRON_FILE"
  log "  creado $CRON_FILE"
}

# --- T3: Descarga y ejecución en una línea (T1105 / T1059.004) ------------------
# curl a un servidor HTTP LOCAL (127.0.0.1:8000) tuberizado a bash.
tecnica_download() {
  log "T1105 · descarga+ejecución (curl 127.0.0.1 | bash)"
  echo 'echo "payload de laboratorio (inocuo)"' > "$ART_DIR/payload.sh"
  ( cd "$ART_DIR" && timeout 5 python3 -m http.server 8000 >/dev/null 2>&1 & ) 2>/dev/null
  sleep 1
  # La línea 'curl ... | bash' dispara la regla propia linux_download_and_exec.yml (IC-E5)
  timeout 4 bash -c 'curl -fsSL http://127.0.0.1:8000/payload.sh | bash' 2>/dev/null || true
  log "  hecho."
}

# --- T4: Volumen anómalo de queries TXT (T1071.004) -----------------------------
# 60 consultas TXT contra un mismo dominio inexistente. Suricata (NIDS) las ve
# en eve.json -> dispara net_dns_tunneling_high_txt_volume.yml.
tecnica_txt() {
  log "T1071.004 · 60 queries DNS TXT (candidato a DNS tunneling)"
  if ! command -v dig >/dev/null 2>&1; then
    log "  'dig' no está; usando 'host'. (apt install dnsutils para dig)"
  fi
  local i
  for i in $(seq 1 60); do
    if command -v dig >/dev/null 2>&1; then
      dig +short TXT "seg${i}.exfil.xest-lab.local" @127.0.0.1 >/dev/null 2>&1 || true
    else
      host -t TXT "seg${i}.exfil.xest-lab.local" 127.0.0.1 >/dev/null 2>&1 || true
    fi
  done
  log "  60 queries TXT emitidas."
}

limpiar() {
  log "limpiando artefactos..."
  rm -f "$CRON_FILE"
  rm -rf "$ART_DIR"
  pkill -f 'python3 -m http.server 8000' 2>/dev/null || true
  pkill -f 'nc -lvnp 9999' 2>/dev/null || true
  log "listo. Entorno restaurado."
}

main() {
  local sel="${1:-all}"
  case "$sel" in
    --limpiar|-c|clean) limpiar; exit 0 ;;
  esac
  guardarrail
  log "inicio $(date '+%F %T') — marca de correlación: $MARK"
  case "$sel" in
    reverse)  tecnica_reverse ;;
    cron)     tecnica_cron ;;
    download) tecnica_download ;;
    txt)      tecnica_txt ;;
    all)      tecnica_reverse; tecnica_cron; tecnica_download; tecnica_txt ;;
    *) echo "opción no reconocida: $sel (usa reverse|cron|download|txt|all|--limpiar)"; exit 2 ;;
  esac
  log "fin. Ahora comprueba las alertas en el panel de Wazuh (Threat Hunting)."
  log "Recuerda limpiar después:  sudo bash $0 --limpiar"
}

main "$@"
