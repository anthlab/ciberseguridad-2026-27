# Sigma → Wazuh — reglas de correlación

[Sigma](https://sigmahq.io) es el formato estándar para expresar reglas de detección independientes del SIEM. En el SOC de xest usamos Sigma como fuente y convertimos a formato Wazuh (XML) para que las evalúe el manager.

## Reglas incluidas

| Fichero | ATT&CK | Fuente |
|---|---|---|
| [`linux_suspicious_reverse_shell.yml`](linux_suspicious_reverse_shell.yml) | T1059.004 (Unix Shell) | Propia (patrones bash/nc/socat reversos) |
| [`linux_persistence_cron_and_systemd.yml`](linux_persistence_cron_and_systemd.yml) | T1053.003 · T1543.002 | Propia |
| [`windows_powershell_encoded_command.yml`](windows_powershell_encoded_command.yml) | T1059.001 · T1027.004 | Propia (mirror pattern SigmaHQ) |
| [`net_dns_tunneling_high_txt_volume.yml`](net_dns_tunneling_high_txt_volume.yml) | T1071.004 · T1041 | Propia (Suricata eve.json) |
| [`auth_impossible_travel.yml`](auth_impossible_travel.yml) | T1078.004 | Propia (Entra ID / Google) |

Estas 5 son ejemplos base. El catálogo completo de la comunidad está en https://github.com/SigmaHQ/sigma — miles de reglas para Windows, Linux, macOS, cloud, network. Recomendamos partir de las taggeadas como `attack.execution`, `attack.persistence`, `attack.credential_access` y `attack.exfiltration`.

## Conversión a Wazuh

Instalar `sigma-cli` (herramienta oficial):

```bash
pip install sigma-cli
pip install pysigma-backend-splunk pysigma-backend-elasticsearch pysigma-pipeline-sysmon
# No hay backend oficial de Wazuh, así que convertimos primero a Elasticsearch
# Lucene y luego lo envolvemos en <rule> de Wazuh (script convertir.sh).
```

Ejecutar:
```bash
./convertir.sh linux_suspicious_reverse_shell.yml > /tmp/rule.xml
```

El script:
1. Convierte Sigma → Lucene query con `sigma convert -t lucene`.
2. Envuelve la query en un `<rule>` de Wazuh con `level 12`, `groups` derivados de `tags` Sigma, y `field` de matching sobre `full_log` o el campo eve/json correspondiente.
3. La regla resultante se copia a `/var/ossec/etc/rules/local_rules.xml` del manager.

## Ejemplo de regla Wazuh generada

Sigma `windows_powershell_encoded_command.yml` (fragmento) → Wazuh:

```xml
<group name="sigma,attack.execution,attack.t1059.001,">
  <rule id="100050" level="12">
    <if_group>windows,powershell</if_group>
    <field name="win.eventdata.commandLine">-e(nc|nco|ncod|ncode|ncodedc|ncodedco|ncodedcom|ncodedcomm|ncodedcomma|ncodedcomman|ncodedcommand)?</field>
    <description>Sigma — PowerShell EncodedCommand suspicious flag (T1059.001)</description>
  </rule>
</group>
```

## Recarga en caliente

```bash
docker compose exec wazuh.manager /var/ossec/bin/wazuh-control reload
# o si el reload no aplica en tu versión:
docker compose restart wazuh.manager
```

## Referencias
- SigmaHQ — https://github.com/SigmaHQ/sigma
- Sigma spec — https://github.com/SigmaHQ/sigma-specification
- Wazuh custom rules — https://documentation.wazuh.com/current/user-manual/ruleset/custom.html
- MITRE ATT&CK — https://attack.mitre.org
