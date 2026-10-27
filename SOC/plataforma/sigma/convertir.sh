#!/usr/bin/env bash
# SOC de xest — conversión Sigma → regla Wazuh
#
# Uso:
#   ./convertir.sh <fichero.yml> > /tmp/rule.xml
#
# Requisitos:
#   pip install sigma-cli pysigma-backend-elasticsearch
#
# Estrategia:
#   1) Pasar el YAML Sigma por `sigma convert -t lucene` para obtener
#      la expresión de búsqueda en formato Lucene.
#   2) Envolver esa expresión en un <rule> Wazuh que hace matching sobre
#      full_log/data.* con field regex.
#   3) Extraer tags MITRE ATT&CK y ponerlos como <group>.
#
# La regla resultante se copia a /var/ossec/etc/rules/local_rules.xml
# del manager y se recarga la config.

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "uso: $0 <fichero.yml>" >&2
  exit 2
fi

SIGMA_FILE="$1"
if [[ ! -f "$SIGMA_FILE" ]]; then
  echo "No existe: $SIGMA_FILE" >&2
  exit 3
fi

if ! command -v sigma >/dev/null 2>&1; then
  echo "sigma-cli no encontrado. Instala con: pip install sigma-cli pysigma-backend-elasticsearch" >&2
  exit 4
fi

LUCENE="$(sigma convert -t lucene "$SIGMA_FILE" 2>/dev/null | head -1)"
if [[ -z "$LUCENE" ]]; then
  echo "sigma convert no produjo salida. Revisar la regla o el pipeline." >&2
  exit 5
fi

TITLE="$(awk -F': *' '/^title:/{sub(/^title: */,""); print; exit}' "$SIGMA_FILE")"
LEVEL_SIGMA="$(awk -F': *' '/^level:/{print $2; exit}' "$SIGMA_FILE")"
TAGS="$(awk '/^tags:/{f=1;next} f && /^  -/{gsub(/^  - */,"");print} f && !/^  -/ && !/^$/{f=0}' "$SIGMA_FILE" | tr '\n' ',' | sed 's/,$//')"

case "$LEVEL_SIGMA" in
  critical) LEVEL_WAZUH=13 ;;
  high)     LEVEL_WAZUH=12 ;;
  medium)   LEVEL_WAZUH=9  ;;
  low)      LEVEL_WAZUH=6  ;;
  *)        LEVEL_WAZUH=8  ;;
esac

RULE_ID=$(( 100000 + RANDOM % 900 ))

# Escape XML mínimo del campo regex
LUCENE_XML="$(printf '%s' "$LUCENE" | sed -e 's/&/\&amp;/g' -e 's/</\&lt;/g' -e 's/>/\&gt;/g' -e 's/"/\&quot;/g')"

cat <<EOF
<group name="sigma,$TAGS,">
  <rule id="$RULE_ID" level="$LEVEL_WAZUH">
    <match>$LUCENE_XML</match>
    <description>Sigma — $TITLE</description>
    <mitre>
$(printf '%s' "$TAGS" | tr ',' '\n' | grep -E '^attack\.t[0-9]' | sed 's|^attack\.|      <id>|; s|$|</id>|')
    </mitre>
  </rule>
</group>
EOF
