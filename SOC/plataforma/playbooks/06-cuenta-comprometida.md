# Playbook 06 — Cuenta comprometida (identidad)

| Categoría | Severidad | Criticidad | SLA respuesta |
|---|---|---|---|
| Intrusions — Compromised account / Unauthorized access | Alta | P2 (P1 si es cuenta privilegiada) | 30 min |

## Precondiciones
- Wazuh ingiere logs de Entra ID / Google Workspace / AD on-prem (Azure Sign-In, MFA, Conditional Access).
- Regla de correlación de *impossible travel* activa.
- Inventario de cuentas privilegiadas (`Global Admin`, `Domain Admin`, `Root` cloud) documentado.
- Procedimiento de revocación de tokens definido y probado.

## Fase 1 — Detección y análisis
Indicadores:
- Wazuh: `rule.groups: [authentication_failures, brute_force]` con éxito posterior desde IP no habitual.
- Alertas de proveedor: sign-in desde geolocalización nueva, MFA saltado por token, uso de `Enterprise App` no autorizada.
- Reporte del usuario: *"me han saltado sesiones sin motivo"*, *"no reconozco esta actividad"*.
- Fuga de credenciales en dumps (HIBP, DeHashed) coincidente con dominio corporativo.

Análisis:
1. Historia de sign-in de la cuenta (últimos 7 días): IPs, dispositivos, User-Agents, geo.
2. Actividad posterior al primer login sospechoso: cambios de config, reglas de reenvío, MFA methods, OAuth grants, mailbox rules.
3. Alcance de permisos de la cuenta (privilegios, grupos, SPN, delegaciones).
4. Otros artefactos: token replay, Golden SAML si es Entra federado.

## Fase 2 — Contención
**Inmediata (< 15 min):**
1. Bloquear la cuenta (`Disable-ADAccount`, Entra `Block sign-in`, Google `Suspend`).
2. Revocar todas las sesiones activas (`Revoke-AzureADUserAllRefreshToken`, Google `Reset sign-in cookies`).
3. Revocar tokens OAuth emitidos.
4. Bloquear IPs y ASN del atacante en Conditional Access / Firewall.

**Corta (1 h):**
5. Revisar y eliminar mailbox rules maliciosas (reenvío externo, borrado automático de correos con palabra clave).
6. Revisar `Enterprise Apps` con consent otorgado por el usuario en los últimos 30 días.
7. Buscar exfil colateral (uso del token para leer OneDrive/SharePoint/Drive, Graph API).

## Fase 3 — Erradicación
1. Rotar contraseña con complejidad alta y **caducidad forzada tras el reset**.
2. Forzar MFA + registro de nuevo authenticator device desde entorno confiable.
3. Revisar y purgar cualquier persistencia: reglas de reenvío, MFA methods duplicados, App passwords, SSH keys, PATs.
4. Si la cuenta es privilegiada: **desprivilegiar temporalmente** y reincorporar con just-in-time cuando se confirme limpieza.

## Fase 4 — Recuperación
1. Comunicación al usuario: qué pasó, qué se ha hecho, qué debe hacer él (verificar dispositivos, cambiar contraseñas de otros servicios donde reutilizaba).
2. Reintegrar sesiones desde dispositivos confiables solo tras validar la limpieza.
3. Vigilancia extra 30 días con reglas específicas para esa identidad.

## Fase 5 — Actividad post-incidente
1. Informe con línea de tiempo, alcance, vector de entrada (credential stuffing, phishing, MFA fatigue, adversary-in-the-middle).
2. Si vector = phishing → activar Playbook 02 sobre la campaña.
3. Si vector = fuga de dump → forzar cambio de contraseña en toda la nómina que reutilice y añadir vigilancia HIBP recurrente.
4. Registro de la brecha si hubo acceso a datos personales (RGPD).
5. Mejoras: MFA obligatorio a toda la nómina, Conditional Access más estricto, monitorización de OAuth grants.

## Notificaciones regulatorias
Depende del acceso a datos:
- Sin evidencia de acceso a datos personales → registro interno.
- Con evidencia → RGPD 33/34 en 72 h (AEPD + afectados si riesgo alto).
- Entidad NIS2 esencial con incidente significativo → 24 h / 72 h / 1 mes.

## Herramientas SOC involucradas
- **Wazuh** — logs de sign-in y correlación (impossible travel, brute force).
- **Suricata** — detección de exfil colateral vía sesión abusada.
- **TheHive** — caso con task por acción de contención.
- **Cortex** — analyzers IP reputation, ASN, HIBP.
- **MISP** — publicación IoCs.
- **Proveedor cloud** (Entra ID, Google Workspace) — el 80 % de la contención se hace desde ahí.

## Criterios de cierre
- Cuenta bloqueada + reset + MFA nuevo + sesiones revocadas + tokens revocados.
- 0 mailbox rules, 0 OAuth grants sospechosas, 0 App passwords sobrantes.
- 72 h sin nueva actividad anómala sobre la cuenta.
- Vector de entrada mitigado (o abierto un ticket asociado si excede el scope del playbook).

## Métricas específicas
| Métrica | Objetivo |
|---|---|
| Tiempo hasta bloqueo de la cuenta | ≤ 15 min |
| Tiempo hasta revocación de tokens | ≤ 20 min |
| Nº de sesiones revocadas | Documentado |
| Nº de mailbox rules maliciosas encontradas | Documentado |
| Vector cerrado antes de próxima cuenta afectada | Sí |
