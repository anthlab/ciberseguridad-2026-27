# Playbook 02 — Phishing / BEC

| Categoría | Severidad | Criticidad | SLA respuesta |
|---|---|---|---|
| Fraud — Phishing / Business Email Compromise | Alta | P2 | 30 min desde reporte usuario o alerta |

## Precondiciones
- Buzón de reporte del usuario: `phishing@<dominio>` o botón *Report Phishing* del cliente de correo.
- Suricata detecta URL maliciosas en tráfico HTTP/HTTPS con SNI y DNS.
- Wazuh recibe logs de la pasarela de correo (Exchange, Postfix, M365 Message Trace).
- MISP con feeds abuse.ch URLhaus + PhishTank activos y cacheados.

## Fase 1 — Detección y análisis
Fuentes:
- Reporte de usuario (email adjunto en `.eml`).
- Alerta Wazuh sobre logs de pasarela (`spam`, `dmarc_fail`, `sender_reputation_low`).
- Suricata detecta acceso a dominio en URLhaus.
- Analyzer Cortex `EmlParser` sobre el `.eml`.

Extraer del `.eml`:
- Cabeceras completas (Received, DKIM/SPF/DMARC, X-Originating-IP).
- Sender real (`Return-Path` vs `From`).
- Enlaces (desofuscar `href`, seguir 3 saltos).
- Adjuntos (hash SHA-256, verificar en VirusTotal + MalwareBazaar).
- Idioma, tipografía, urgencia (indicador de campaña masiva).

Clasificar:
| Subtipo | Indicador |
|---|---|
| **Phishing genérico** | Enlace a página que suplanta login corporativo |
| **BEC** (CEO fraud) | Suplantación de directivo, petición de transferencia o cambio de nómina |
| **Spear phishing** | Personalizado con datos internos, adjunto tipo Excel con macros |
| **Whaling** | Dirigido a directivos o consejo |

## Fase 2 — Contención
1. Consultar buzones — cuántos usuarios recibieron el mismo mensaje. `Search-Mailbox` (Exchange) o `Get-MessageTrace` (M365).
2. **Purgar** el mensaje de todos los buzones (`Search-Mailbox -DeleteContent` o *Content Search + Purge*).
3. Bloquear dominio remitente y URL destino en:
   - Pasarela de correo (deny list).
   - Proxy web + DNS interno.
   - Firewall perimetral.
   - EDR (URL block).
4. Si algún usuario ya hizo clic: aislar el endpoint desde Wazuh, iniciar Playbook 06 (cuenta comprometida) y/o 03 (malware endpoint).
5. Añadir IoCs a MISP como evento propio (compartir con la comunidad).

## Fase 3 — Erradicación
1. Rotar credenciales de usuarios que introdujeron credenciales en la página falsa.
2. Revocar sesiones activas de esos usuarios (Entra ID / Google Workspace).
3. Revisar reglas de reenvío recientes en los buzones afectados (persistencia típica de BEC).
4. Revisar concesiones OAuth recientes (BEC moderno usa apps maliciosas de terceros).

## Fase 4 — Recuperación
1. Comunicación breve a los afectados: qué pasó, qué se ha hecho, qué deben hacer ellos (cambio de contraseña, revisar reglas, MFA obligatorio).
2. Formación puntual — recordatorio de 3 puntos, no un curso.
3. Vigilancia extra sobre buzones afectados durante 30 días.

## Fase 5 — Actividad post-incidente
1. Informe: quién, cuántos afectados, alcance del daño, coste.
2. Refinar reglas de detección (DMARC estricto p=quarantine → p=reject).
3. Actualizar campañas de simulación de phishing internas para incorporar el vector real observado.
4. Lecciones aprendidas: ¿el bloqueo de correo pudo haber pasado antes? ¿MFA obligatorio en toda la nómina?

## Notificaciones regulatorias

| Escenario | Marco | Plazo | Destinatario |
|---|---|---|---|
| Credenciales o datos personales comprometidos | RGPD art. 33/34 | 72 h / sin demora | AEPD + afectados |
| Entidad esencial NIS2 con incidente significativo | NIS2 art. 23 | 24 h / 72 h / 1 mes | INCIBE-CERT o CCN-CERT |
| Sector financiero DORA | DORA | 4 h / 72 h / 1 mes | Autoridad sectorial |
| Fraude consumado (transferencia efectuada) | Código Penal | Denuncia | GDT / BCIT + banco (retención SWIFT) |

## Herramientas SOC involucradas
- **Wazuh** — logs de pasarela + endpoint + búsqueda global.
- **Suricata** — detección de acceso a phishing sites en tráfico.
- **TheHive** — caso con task por afectado.
- **Cortex** — analyzers EmlParser, URLhaus, VirusTotal, Google Safe Browsing.
- **MISP** — IoC lookup + publish evento propio.
- **PPS** — endurecimiento pasarela (DMARC/DKIM/SPF, ARC, Advanced Anti-Phishing).

## Criterios de cierre
- Ningún buzón conserva el mensaje.
- Todos los usuarios que hicieron clic tienen credenciales rotadas y sesiones revocadas.
- IoCs bloqueados en las 4 capas (correo, proxy, firewall, EDR).
- Evento MISP publicado con TLP:AMBER o TLP:CLEAR según decisión.

## Métricas específicas
| Métrica | Objetivo |
|---|---|
| Tiempo desde reporte hasta purga | ≤ 30 min |
| % usuarios que clicaron | ≤ 5 % |
| % usuarios que introdujeron credenciales | ≤ 1 % |
| Vector reutilizado en 30 días | Bloqueado en primera instancia |
