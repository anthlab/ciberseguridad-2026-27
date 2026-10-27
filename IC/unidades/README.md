# IC — Unidades de trabajo

Desarrollo de las 8 unidades del módulo **Incidentes de ciberseguridad (5021)**. Cada
unidad incluye contenido, guion de laboratorio con comandos reales y entregables con su
rúbrica. Marco y evaluación en `PROGRAMACION.md` (referencia del material de origen; consulta la guía de la unidad).

> El módulo opera sobre la plataforma del SOC desplegada en [`SOC/plataforma/`](../../SOC/plataforma/)
> (Wazuh, Suricata, TheHive, Cortex, MISP). Las UT6 y UT7 se coordinan con el equipo rojo
> de Hacking ético: el incidente que se investiga es el que se ha producido en el curso.

| UT | Título | Horas | RA | Unidad |
|---|---|---:|---|---|
| UT1 | Gobierno de la ciberseguridad y normativa del puesto de trabajo | 8 | RA1 | [abrir](UT1-gobierno-normativa-puesto.md) |
| UT2 | Cultura de seguridad: concienciación, materiales y auditoría | 8 | RA1 | [abrir](UT2-concienciacion-auditoria.md) |
| UT3 | Taxonomía de incidentes y arquitectura de detección | 12 | RA2 | [abrir](UT3-taxonomia-arquitectura-deteccion.md) |
| UT4 | Detección de incidentes de seguridad física e inteligencia de fuentes abiertas | 8 | RA2 | [abrir](UT4-deteccion-fisica-osint.md) |
| UT5 | Triaje: clasificación, valoración, seguimiento y contención inicial | 8 | RA2/RA3 | [abrir](UT5-triaje-contencion-inicial.md) |
| UT6 | Investigación del incidente: evidencias, análisis e intercambio | 12 | RA3 | [abrir](UT6-investigacion-evidencias-intercambio.md) |
| UT7 | Respuesta, ciberresiliencia y recuperación del servicio | 14 | RA4 | [abrir](UT7-respuesta-resiliencia-recuperacion.md) |
| UT8 | Notificación y comunicación del incidente | 10 | RA5 | [abrir](UT8-notificacion-comunicacion.md) |

## Material de apoyo

- [`material/csirt/manual-csirt.md`](../material/csirt/manual-csirt.md) — roles, matriz de escalado y RACI del CSIRT (UT7, `IC-E12`).
- [`material/plantillas/matriz-triaje.md`](../material/plantillas/matriz-triaje.md) — priorización reproducible de alertas (UT5, `IC-E8`).
- [`material/plantillas/tabletop-ransomware.md`](../material/plantillas/tabletop-ransomware.md) — escenario de ejercicio de mesa (UT7, `IC-E13`).
- [`material/notificacion/rgpd-72h.md`](../material/notificacion/rgpd-72h.md) — borrador de notificación a la AEPD (UT8, `IC-E15`).
- [`material/notificacion/nis2-24h.md`](../material/notificacion/nis2-24h.md) — alerta temprana NIS2 (UT8, `IC-E15`).
- `IC-E17` — prueba objetiva de plazos, sujetos y umbrales de notificación (UT8). La entrega el profesor en el aula.

## Coordinación con otros módulos

- `coordinacion/IC-AF-cadena-custodia.md` (referencia del material de origen; consulta la guía de la unidad) — traspaso de evidencia a Análisis forense (UT5/UT6).
- `coordinacion/IC-NC-obligaciones-playbooks.md` (referencia del material de origen; consulta la guía de la unidad) — obligación normativa → notificación → playbook (UT8).
