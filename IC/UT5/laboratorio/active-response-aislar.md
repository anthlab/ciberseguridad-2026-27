# Respuesta activa de Wazuh — aislar endpoint y bloquear C2

Configuración de referencia para disparar la contención **desde el SOC**. Se despliega en el
manager de Wazuh de `~/xest-lab/2026-2027/SOC/plataforma/`. Uso didáctico, VLAN aislada.

## 1. `firewall-drop` sobre la IP del C2 (incluido en Wazuh)

En `ossec.conf` del manager, asocia la respuesta activa `firewall-drop` a la regla que dispara
la baliza C2 (la de la alerta A07). Bloquea el indicador en el agente durante un tiempo:

```xml
<active-response>
  <command>firewall-drop</command>
  <location>local</location>
  <rules_id>100207</rules_id>   <!-- regla local del beacon a 185.220.101.47 -->
  <timeout>0</timeout>          <!-- 0 = permanente hasta revisión manual -->
</active-response>
```

## 2. Script de aislamiento (deja solo el canal con el SOC)

Crea `/var/ossec/active-response/bin/aislar-host.sh` en el agente (o despliégalo con la config
del manager). Aísla el endpoint salvo la comunicación con el manager Wazuh:

```bash
#!/bin/sh
# aislar-host.sh — respuesta activa: aísla el endpoint sin apagarlo.
# Wazuh pasa "add"/"delete" en $1 para aplicar o revertir.
SOC="10.10.10.20"
ACTION="$1"
if [ "$ACTION" = "add" ]; then
    iptables -P INPUT DROP
    iptables -P OUTPUT DROP
    iptables -A OUTPUT -d "$SOC" -p tcp --dport 1514 -j ACCEPT
    iptables -A INPUT  -s "$SOC" -j ACCEPT
    logger "IR: host AISLADO (solo SOC $SOC) por respuesta activa Wazuh"
elif [ "$ACTION" = "delete" ]; then
    iptables -F; iptables -P INPUT ACCEPT; iptables -P OUTPUT ACCEPT
    logger "IR: aislamiento REVERTIDO"
fi
exit 0
```

Registro en `ossec.conf`:

```xml
<command>
  <name>aislar-host</name>
  <executable>aislar-host.sh</executable>
  <expect></expect>
</command>
<active-response>
  <command>aislar-host</command>
  <location>local</location>
  <rules_id>100205</rules_id>   <!-- regla local del webshell/compromiso confirmado -->
  <timeout>0</timeout>
</active-response>
```

## 3. Verificación de que la respuesta se ejecutó (no basta con que exista)

```bash
# En el manager: la respuesta activa debe aparecer en el log
tail -n 20 /var/ossec/logs/active-responses.log
# En el endpoint: aislado pero reportando
systemctl is-active wazuh-agent       # active
ping -c1 -W2 8.8.8.8; echo "rc=$?"    # rc=1 (sin salida general)
```

> Gate instalado ≠ gate activo: comprueba **siempre** con un caso que debe fallar (el `ping`
> que ya no sale). Una respuesta activa "configurada" que nunca se dispara es un aislamiento
> que no existe.
