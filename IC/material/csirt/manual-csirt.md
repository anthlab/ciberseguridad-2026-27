# Manual del CSIRT — SOC de xest

Base del entregable `IC-E12`. Define quién hace qué en un incidente, cómo se escala y
con qué procedimientos. El equipo lo completa con sus datos y lo ensaya en la UT7.

---

## 1. Misión

Reducir el tiempo entre que un incidente ocurre y la organización lo contiene, minimizando el impacto y cumpliendo las obligaciones de notificación.

## 2. Roles

| Rol | Responsabilidad | Titular | Suplente |
|---|---|---|---|
| **Coordinador de incidente** | Dirige la respuesta, decide el escalado, único punto de decisión | | |
| **Analista L1** | Triaje de alertas, primera clasificación | | |
| **Analista L2** | Investigación, contención, análisis | | |
| **Analista L3** | Casos complejos, forense, ingeniería inversa | | |
| **Portavoz** | Comunicación externa (único autorizado) | | |
| **Enlace jurídico** | Notificación regulatoria, valoración legal | | |

## 3. Matriz de escalado

| Severidad | Criterio | Quién decide | A quién se informa | Plazo interno |
|---|---|---|---|---|
| **Crítica** | Servicio esencial caído / dato personal masivo / ransomware activo | Coordinador + Dirección | Dirección, jurídico, CERT | Inmediato |
| **Alta** | Compromiso confirmado de un sistema | Coordinador | Dirección | < 1 h |
| **Media** | Actividad sospechosa por confirmar | Analista L2 | Coordinador | < 4 h |
| **Baja** | Evento aislado, sin impacto | Analista L1 | — | Registro |

## 4. Matriz RACI (por fase NIST)

| Fase | Coordinador | L1 | L2 | L3 | Portavoz | Jurídico |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| Detección y triaje | I | R | C | | | |
| Contención | A | | R | C | | I |
| Erradicación / recuperación | A | | R | R | | I |
| Notificación | A | | | | R | R |
| Lecciones aprendidas | R | C | C | C | I | I |

*(R responsable · A aprobador · C consultado · I informado)*

## 5. Contactos

### Internos
- Dirección: ____________________
- Jurídico / DPD: ____________________
- Comunicación: ____________________

### Externos
- **INCIBE-CERT**: incidencias@incibe-cert.es · 017
- **CCN-CERT** (sector público): ____________________
- **AEPD** (sede electrónica, notificación de brechas): sedeagpd.gob.es
- **Grupo de Delitos Telemáticos (Guardia Civil)** / **BCIT (Policía Nacional)**
- Proveedor de nube / MSSP: ____________________

## 6. Herramientas preinstaladas (jump kit)

- Triage forense: Velociraptor, KAPE, CyLR.
- Memoria: Volatility 3.
- Red: Wireshark, Zeek, Arkime.
- Caso: TheHive + Cortex.
- Inteligencia: MISP.
- Jump host aislado para el análisis.

## 7. Procedimientos ensayados

- Ejercicios de mesa (tabletop) semestrales.
- Simulacro técnico anual (contención + recuperación).
- Revisión del manual tras cada incidente real.
