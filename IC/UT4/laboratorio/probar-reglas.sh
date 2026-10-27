#!/usr/bin/env bash
# Simulador offline de las reglas físicas de xest (IC · UT4).
# Reproduce la lógica de wazuh/local_rules-fisica.xml SIN necesitar un Wazuh levantado,
# para poder verificar la cadena evento->alerta en cualquier estación del aula.
# Uso:   bash probar-reglas.sh datos/eventos-fisicos.log
# La fuente de verdad es el XML; esto es solo un banco de pruebas didáctico.
set -euo pipefail

LOG="${1:-datos/eventos-fisicos.log}"
[[ -f "$LOG" ]] || { echo "No encuentro el log: $LOG" >&2; exit 1; }

# Estado para la regla de frecuencia (100205): 3 badge_denied en el mismo asset / 30 s.
declare -A last_ts   # asset -> epoch de la 1ª denegación de la ventana
declare -A count     # asset -> nº de denegaciones en la ventana

epoch() { date -d "2026 $1 $2 $3" +%s 2>/dev/null || echo 0; }

fire() { printf '  \033[1;31m[ALERTA]\033[0m regla %s (nivel %s): %s\n' "$1" "$2" "$3"; }

while IFS= read -r line; do
  [[ "$line" =~ xestpacs: ]] || continue
  mon=$(awk '{print $1}' <<<"$line"); day=$(awk '{print $2}' <<<"$line"); tim=$(awk '{print $3}' <<<"$line")
  kv=${line#*xestpacs: }
  event=$(grep -oP 'event=\K\S+' <<<"$kv" || true)
  zone=$(grep -oP 'zone=\K\S+' <<<"$kv" || true)
  asset=$(grep -oP 'asset=\K\S+' <<<"$kv" || true)
  actor=$(grep -oP 'actor=\K\S+' <<<"$kv" || true)
  result=$(grep -oP 'result=\K\S+' <<<"$kv" || true)
  ooh=$(grep -oP 'out_of_hours=\K\S+' <<<"$kv" || true)
  ts=$(epoch "$mon" "$day" "$tim")

  echo "· $mon $day $tim  event=$event asset=$asset actor=$actor ooh=$ooh"

  if [[ "$event" == "rack_open" && "$ooh" == "yes" ]]; then
    fire 100201 10 "Apertura de rack en CPD fuera de horario en $asset por $actor"
  elif [[ "$event" == "door_open" && "$actor" == "UNKNOWN" && "$ooh" == "yes" ]]; then
    fire 100202 10 "Acceso físico no identificado al $zone fuera de horario en $asset"
  elif [[ "$event" == "usb_insert" && "$result" == "deny" ]]; then
    fire 100203 8 "USB no autorizado bloqueado en $asset ($zone) [T1200]"
  elif [[ "$event" == "cctv_signal_lost" ]]; then
    fire 100204 9 "Pérdida de señal de CCTV en $asset: posible manipulación"
  elif [[ "$event" == "tailgating" ]]; then
    fire 100207 10 "Tailgating detectado en $asset ($zone)"
  elif [[ "$event" == "badge_denied" ]]; then
    # ventana de 30 s por asset
    if [[ -n "${last_ts[$asset]:-}" ]] && (( ts - last_ts[$asset] <= 30 )); then
      count[$asset]=$(( ${count[$asset]:-1} + 1 ))
    else
      last_ts[$asset]=$ts; count[$asset]=1
    fi
    if (( ${count[$asset]} >= 3 )); then
      fire 100205 10 "Múltiples tarjetas denegadas en $asset (${count[$asset]} en <=30s): tarjeta clonada / fuerza bruta física"
      count[$asset]=0   # evita re-disparar en cada evento posterior de la misma ráfaga
    fi
  fi
done < "$LOG"
