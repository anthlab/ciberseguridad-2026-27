# Playbooks — Respuesta a incidentes SOC de xest

Colección de playbooks operativos alineados con el ciclo de vida NIST SP 800-61 rev. 2. Cada uno responde a una categoría típica de incidente y sigue una estructura común:

1. Categoría, severidad y SLA de respuesta.
2. Precondiciones (qué debe estar en pie antes de que suene la alerta).
3. Fases NIST — Detección · Contención · Erradicación · Recuperación · Post-incidente.
4. Notificaciones regulatorias.
5. Herramientas del SOC involucradas.
6. Criterios de cierre y métricas.

Estos playbooks se materializan en **TheHive** como *Case templates* (Fase 3) — cada tarea de la lista es una `task` con su owner, deadline y checklist. La versión markdown de este directorio es la fuente de verdad; el import a TheHive se hace con `curl` a la API (`/api/v1/caseTemplate`).

## Catálogo

| # | Playbook | Categoría eCSIRT.net | SLA respuesta |
|---|---|---|---|
| 01 | [Ransomware](01-ransomware.md) | Malicious Code · Ransomware | 15 min |
| 02 | [Phishing / BEC](02-phishing.md) | Fraud · Phishing | 30 min |
| 03 | [Malware en endpoint](03-malware-endpoint.md) | Malicious Code · Infected System | 30 min |
| 04 | [Exfiltración de datos](04-exfiltracion.md) | Information Content Security · Data breach | 15 min |
| 05 | [Denegación de servicio (DDoS)](05-ddos.md) | Availability · DoS/DDoS | 15 min |
| 06 | [Cuenta comprometida](06-cuenta-comprometida.md) | Intrusions · Compromised account | 30 min |

## Módulo del ciclo
Estos playbooks son la materialización operativa del módulo `IC/` (referencia del material de origen; consulta la guía de la unidad). Lo que allí se enseña en teoría, aquí se ejecuta contra el SIEM + SOAR + TIP del laboratorio.

## Cómo se usan
1. **Alerta** — Wazuh dispara una alerta que cumple los criterios del playbook (regla dedicada o correlación).
2. **Case creation** — la integración `custom-w2thive` (ver `../integrations/` (referencia del material de origen; consulta la guía de la unidad)) crea automáticamente un caso en TheHive con el *Case template* correspondiente.
3. **Ejecución** — el analista sigue el checklist. Cada tarea marca su timestamp de finalización, lo que alimenta métricas MTTA (Mean Time To Acknowledge) y MTTR (Mean Time To Respond).
4. **Cierre** — al cerrar el caso, la sección "Actividad post-incidente" alimenta las lecciones aprendidas que refinan reglas, playbooks y baseline PPS.

## Métricas comunes
| Métrica | Fórmula | Objetivo laboratorio |
|---|---|---|
| MTTA | Tiempo desde `Alerta creada` hasta `Case asignado` | < 15 min |
| MTTR | Tiempo desde `Alerta creada` hasta `Case cerrado` | < 8 h (crít.) / < 24 h (alta) |
| Tasa contención | Casos contenidos < 4 h / Casos totales | > 80 % |
| Reincidencia | Casos por mismo vector en 30 d | ≤ 1 |
