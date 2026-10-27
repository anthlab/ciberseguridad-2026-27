#!/usr/bin/env bash
# trigger-llmnr.sh — se ejecuta en la ESTACIÓN VÍCTIMA (no en la del atacante).
# Simula a un usuario cuyo equipo intenta llegar a un recurso de red cuyo nombre NO
# existe en DNS (un servidor de ficheros mal escrito, una unidad de red que ya no está).
# Al fallar el DNS, el equipo pregunta por LLMNR/NBT-NS en broadcast... y Responder,
# en la estación atacante, contesta suplantando ese recurso y captura el hash NetNTLMv2.
#
# SOLO en la VLAN de laboratorio. Correlato de un usuario real: nadie "ataca", solo
# teclea mal un nombre de servidor. Ese es justo el punto de la clase.
set -u

# Nombres inexistentes en el DNS del lab -> forzarán la consulta LLMNR/NBT-NS.
OBJETIVOS=("fileserv01" "backup-nas" "impresora-planta2")

echo "[victima] Simulando accesos a recursos de red inexistentes (genera tráfico LLMNR)..."
for h in "${OBJETIVOS[@]}"; do
  echo "  -> intentando \\\\$h\\datos"
  # smbclient dispara la resolución del nombre; al no estar en DNS, sale la consulta LLMNR.
  # Las credenciales son de la cuenta de laboratorio de esta estación víctima.
  smbclient -L "//$h" -U 'XEST\\jdoe%Verano2026!' -t 3 >/dev/null 2>&1
  sleep 2
done
echo "[victima] Hecho. Si Responder estaba a la escucha, ya tiene el NetNTLMv2 de jdoe."

# Windows (equivalente para una víctima Windows del lab): abrir en Explorer
#   \\fileserv01\datos   o ejecutar en cmd:   net view \\fileserv01
