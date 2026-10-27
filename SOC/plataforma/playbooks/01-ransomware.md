# Playbook 01 — Ransomware

| Categoría | Severidad | Criticidad | SLA respuesta |
|---|---|---|---|
| Malicious Code — Ransomware | Crítica | P1 | 15 min desde la primera alerta |

## Precondiciones
- Wazuh manager operativo con agentes desplegados en endpoints y servidores.
- Suricata escuchando la interfaz que ve el tráfico interno / a Internet.
- Backups offline verificados en los últimos 7 días.
- Contacto con CCN-CERT (organismos ENS) o INCIBE-CERT (resto) por canal seguro definido.
- Punto de contacto con dirección, jurídico, comunicación y RRHH ya designado.

## Fase 1 — Detección y análisis
Indicadores típicos:
- Alertas Wazuh con `rule.groups: [ransomware, ossec]` disparadas por `syscheck` (ficheros modificados masivamente en corto tiempo).
- Detección Suricata de familias conocidas (`ET TROJAN Ransomware ...`, ClamAV signature match).
- Nota de rescate en el escritorio o en `readme.txt` de directorios afectados.
- Extensiones `.locked`, `.encrypted`, `.<random>` en ficheros de usuario.
- Comunicación saliente a `.onion` o dominios sospechosos vía DNS.

Confirmación:
1. Extraer un fichero cifrado y su versión original (backup). Verificar cifrado real (entropía > 7.5, cabecera anómala).
2. Consultar hash de la nota o binario en MISP y VirusTotal (analyzer Cortex).
3. Identificar familia con [ID Ransomware](https://id-ransomware.malwarehunterteam.com/) o [NoMoreRansom](https://www.nomoreransom.org/).

## Fase 2 — Contención
**Inmediata (primeros 15 min):**
1. Aislar el host afectado desde Wazuh: `active-response firewall-drop` sobre el agente o desde EDR de red.
2. Bloquear el rango del atacante en el firewall perimetral.
3. Deshabilitar cuentas de servicio comprometidas en el AD.
4. Cortar rutas de propagación conocidas: SMB entre segmentos, RDP inbound, WMI remoto.

**Corta (primera hora):**
5. Congelar copias de seguridad — evitar que se sobrescriban backups sanos.
6. Verificar si el ransomware se ha propagado por movimiento lateral (BloodHound + logs Wazuh de otros agentes en la misma VLAN).
7. Preservar evidencia — cadena de custodia sobre el host afectado (coordinación con módulo `AF`).

## Fase 3 — Erradicación
1. Reimagen del host afectado desde imagen dorada limpia. **No** intentar limpiar in-situ salvo laboratorio.
2. Rotar credenciales de todas las cuentas usadas en el host afectado (locales, dominio, aplicaciones, tokens, keys en `~/.ssh`, PATs de git).
3. Bloquear IoCs en firewall, proxy y EDR: hashes, dominios C2, IPs.
4. Aplicar parches del CVE de entrada si se ha identificado (ver KEV de CISA + EPSS).

## Fase 4 — Recuperación
1. Restaurar datos desde el backup más reciente **verificado sano** (comprobar hash conocido de al menos 3 ficheros no afectados).
2. Reintegrar el host al dominio con nueva cuenta de máquina.
3. Vigilancia reforzada 30 días: reglas Sigma específicas + hunting semanal.
4. Comunicación interna a usuarios afectados (RRHH + comunicación).

## Fase 5 — Actividad post-incidente
1. Informe final: timeline, causa raíz, coste (horas + productividad + rescate no pagado).
2. Lecciones aprendidas: nuevas reglas Wazuh/Sigma, mejoras baseline PPS, purga de vectores no utilizados.
3. Reporte a partes interesadas y reguladores.
4. Actualización de este playbook si aparecieron pasos no cubiertos.

## Decisión sobre el pago del rescate
**Política del SOC de xest: no pagar por defecto.** Pagar solo si se cumple todo:
1. La organización se paraliza y no hay backup viable.
2. Dirección + jurídico dan aprobación por escrito.
3. Se ha consultado a la Guardia Civil / Policía Nacional (GDT / BCIT).
4. El actor no aparece en listas OFAC / sanciones UE (transferir a un sancionado es delito).

El pago **no garantiza** desencriptación completa ni ausencia de doble extorsión (leak site).

## Notificaciones regulatorias

| Marco | Plazo | Destinatario |
|---|---|---|
| RGPD art. 33 | 72 h | AEPD (si compromete datos personales) |
| RGPD art. 34 | Sin demora | Afectados (si riesgo alto) |
| NIS2 | 24 h alerta / 72 h notificación / 1 mes informe | INCIBE-CERT o CCN-CERT |
| ENS RD 311/2022 | Según categoría | CCN-CERT |
| DORA | 4 h alerta / 72 h intermedio / 1 mes final | Autoridad sectorial (BdE/CNMV) |
| Código Penal | Denuncia | GDT (Guardia Civil) o BCIT (Policía) |

## Herramientas SOC involucradas
- **Wazuh** — detección, aislamiento, active-response, forensic snapshot.
- **Suricata** — detección de C2 y propagación lateral (SMB scan).
- **TheHive** — orquestación del caso.
- **Cortex** — analyzers VirusTotal, MISP, HybridAnalysis, ID_Ransomware.
- **MISP** — enriquecimiento con IoCs conocidos de la familia.
- **AF (Análisis Forense)** — preservación de evidencia y análisis post-mortem.

## Criterios de cierre
- Ningún host aislado presenta nueva actividad maliciosa en 72 h.
- Vector de entrada mitigado permanentemente.
- Copia de seguridad post-incidente creada y verificada.
- Comunicaciones regulatorias entregadas y acuse recibido.
- Lecciones aprendidas documentadas y publicadas al equipo.

## Métricas específicas
| Métrica | Objetivo |
|---|---|
| Tiempo hasta aislamiento del primer host | ≤ 15 min |
| % hosts afectados / hosts totales | ≤ 5 % |
| Tiempo hasta restauración de servicio esencial | ≤ 24 h |
| Volumen de datos cifrado | Documentado |
| Pagado / no pagado | No (por defecto) |
