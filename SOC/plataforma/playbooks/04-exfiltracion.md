# Playbook 04 — Exfiltración de datos

| Categoría | Severidad | Criticidad | SLA respuesta |
|---|---|---|---|
| Information Content Security — Data breach | Crítica | P1 | 15 min |

## Precondiciones
- Suricata escuchando en interfaz con visibilidad de tráfico saliente.
- Wazuh integrado con logs de proxy, DNS, DLP y cloud (Entra, Google, AWS CloudTrail).
- Inventario de datos clasificado (nivel de sensibilidad ENS o similar) documentado y accesible al SOC.

## Fase 1 — Detección y análisis
Indicadores:
- Suricata: volumen anómalo de DNS TXT (posible DNS tunneling), HTTPS a dominio no visto antes con SNI raro, `ET INFO Data Exfiltration ...`.
- Wazuh: descarga masiva de fichero desde SharePoint / Confluence / repositorio Git.
- DLP: match de patrón sensible (DNI, IBAN, historia clínica).
- Proveedor cloud: alerta de exfiltración vía OAuth token o SAS URL.
- Actor externo: publicación en foro / leak site con muestra.

Análisis:
1. Identificar el **qué** (tabla, bucket, unidad) y el **cuánto** (volumen bytes + número de registros).
2. Identificar el **cómo**: exfil desde host interno vía proxy, vía cloud API, vía token, vía correo saliente, vía USB.
3. Identificar el **quién**: cuenta origen, host origen, IP destino.
4. Evaluar **impacto RGPD**: naturaleza del dato, número de afectados, gravedad, probabilidad de mal uso.

## Fase 2 — Contención
**Inmediata:**
1. Bloquear el canal de exfil identificado (IP, dominio, cuenta, token, SAS URL).
2. Aislar el host origen desde Wazuh si es interno.
3. Revocar el token / OAuth grant / SAS URL en cloud.
4. Deshabilitar la cuenta origen.

**Corta (1 h):**
5. Cortar el vector si aún hay flujo activo.
6. Congelar logs de al menos 30 días atrás (retención forense extendida).
7. Preservar evidencia técnica en el host origen (coordinación con `AF`).

## Fase 3 — Erradicación
1. Rotar credenciales de la cuenta comprometida y todas las cuentas relacionadas.
2. Auditar concesiones OAuth y tokens API — revocar y regenerar.
3. Reimagen del host origen si compromiso confirmado.
4. Aplicar parche del CVE de entrada si se ha identificado.

## Fase 4 — Recuperación
1. Coordinar con jurídico y comunicación la respuesta pública.
2. Notificar a los afectados (obligación RGPD art. 34 si riesgo alto).
3. Ofrecer medidas de mitigación al afectado (bloqueo de tarjetas, cambio de contraseñas, monitorización de identidad).
4. Vigilancia extra 90 días sobre el mismo canal + sobre exfil recurrentes.

## Fase 5 — Actividad post-incidente
1. Informe a dirección con cronograma, causa raíz, coste (directo + indirecto: multa RGPD, litigios, reputación).
2. Registro AEPD: art. 33 en 72 h con toda la información conocida; complementar si aparecen más datos.
3. Lecciones aprendidas: DLP rules nuevas, controles de acceso mínimo privilegio, MFA + condicional access.
4. Publicar evento MISP interno para federados con TLP restrictivo.

## Notificaciones regulatorias — este es el playbook con más obligaciones

| Marco | Plazo | Destinatario | Umbral |
|---|---|---|---|
| **RGPD art. 33** | 72 h desde constatación | AEPD | Si hay riesgo para derechos y libertades |
| **RGPD art. 34** | Sin demora indebida | Afectados | Si riesgo es alto |
| **NIS2** | 24 h / 72 h / 1 mes | INCIBE-CERT o CCN-CERT | Incidente significativo |
| **ENS RD 311/2022** | Según categoría | CCN-CERT | Sistema público |
| **DORA** | 4 h / 72 h / 1 mes | Autoridad sectorial | Incidente TIC significativo |
| **LO 3/2018 art. 39** | Sin demora | Delegado de Protección de Datos interno | Siempre que haya brecha |
| **Código Penal** | Denuncia | GDT / BCIT | Si delito perseguible |

## Herramientas SOC involucradas
- **Suricata** — detección de canal de exfil (DNS tunneling, HTTPS anómalo).
- **Wazuh** — logs proxy, DLP, cloud, endpoint.
- **TheHive** — caso con checklist de notificación regulatoria.
- **Cortex** — analyzers de reputación (Onyphe, DomainTools, PassiveTotal).
- **MISP** — publicación TLP:AMBER a comunidad de confianza.
- **AF** — cadena de custodia para procedimiento penal.

## Criterios de cierre
- Canal de exfil cerrado y confirmado no operativo 72 h.
- Todas las cuentas y tokens implicados rotados / revocados.
- Notificaciones regulatorias enviadas y acuse recibido.
- Registro interno actualizado (art. 30 RGPD).
- Comunicación a afectados completada.

## Métricas específicas
| Métrica | Objetivo |
|---|---|
| Tiempo hasta corte del canal | ≤ 15 min |
| Volumen exfiltrado | Documentado en informe |
| Número de afectados | Documentado |
| Cumplimiento plazo AEPD 72 h | 100 % |
| Cumplimiento plazo NIS2 24 h alerta | 100 % |
