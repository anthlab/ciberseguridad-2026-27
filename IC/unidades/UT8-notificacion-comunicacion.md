# IC · UT8 — Notificación y comunicación del incidente

**10 horas** · RA5 (a, b, c, d, e) · Servicio SOC: Respuesta — notificación regulatoria · Evidencias `IC-E15`, `IC-E16`, `IC-E17`

---

## 1. Objetivo de la unidad

Detectar y responder no basta: hay que **notificar en plazo** a quien corresponda. Esta unidad cubre las obligaciones regulatorias, sus relojes y la comunicación interna, a autoridades, a afectados y a medios. Un analista que no sabe notificar en plazo expone a su organización a sanción; por eso RA5, aunque pese poco, es eliminatorio.

## 2. Contenido

### 2.1 Procedimiento de notificación y relojes (RA5.a)

| Marco | Plazo | Destinatario | Umbral |
|---|---|---|---|
| **RGPD art. 33** | 72 h desde constatación | AEPD | Riesgo para derechos y libertades |
| **RGPD art. 34** | Sin demora indebida | Afectados | Riesgo alto |
| **NIS2 (UE 2022/2555)** | Alerta 24 h · notificación 72 h · informe final 1 mes | CSIRT nacional (INCIBE-CERT / CCN-CERT) | Incidente significativo |
| **ENS (RD 311/2022)** | Según categoría | CCN-CERT | Sistemas del sector público |
| **DORA (UE 2022/2554)** | 4 h · 72 h · 1 mes | Autoridad sectorial | Incidente TIC significativo |

### 2.2 Notificación interna (RA5.b)

Dirección, jurídico, RRHH, comunicación. Quién decide y quién ejecuta cada paso.

### 2.3 Notificación a autoridades (RA5.c)

AEPD, INCIBE-CERT, CCN-CERT, Fuerzas y Cuerpos de Seguridad (Grupo de Delitos Telemáticos de la Guardia Civil, BCIT de la Policía Nacional).

### 2.4 Comunicación a afectados y terceros (RA5.d)

Afectados, clientes, proveedores. Mensaje claro, sin agravar el impacto ni ocultar lo relevante.

### 2.5 Comunicación a medios (RA5.e)

Portavoz único, mensaje base, gestión de preguntas hostiles. Cuándo procede y cuándo no.

## 3. Laboratorio guiado

### Parte A — Árbol de decisión (RA5.a)

1. Construye el **árbol de decisión** de notificación: dado un incidente, qué marcos aplican, con qué plazo y a quién. Usa la plantilla de [`IC/material/notificacion/`](../material/notificacion/).

### Parte B — Redactar notificaciones (RA5.b, RA5.c, RA5.d)

2. Redacta el **borrador de notificación a la AEPD en 72 h** (plantilla `rgpd-72h.md`) y la **alerta temprana NIS2 en 24 h** (plantilla `nis2-24h.md`) para el incidente del ejercicio.

### Parte C — Rueda de prensa simulada (RA5.e)

3. Simulación de comunicación pública: portavoz, mensaje base y respuesta a preguntas hostiles preparadas por el propio grupo.

## 4. Entregables

- **`IC-E15`** (informe, rúbrica R2): procedimiento de notificación con árbol de decisión y plantillas cumplimentadas.
- **`IC-E16`** (defensa oral, rúbrica R4): simulación de comunicación pública y a autoridades.
- **`IC-E17`** (prueba objetiva, plantilla): plazos, sujetos obligados y umbrales de notificación. Prueba escrita sin material de apoyo; la entrega el profesor en el aula.

## 5. Criterios de superación

- El árbol de decisión aplica el marco y el plazo correctos a cada supuesto.
- Los borradores de notificación cumplen contenido y plazo.
- La prueba objetiva demuestra que los plazos y umbrales están memorizados, no consultados.

## 6. Por qué RA5 es eliminatorio

Notificar fuera de plazo o a quien no corresponde tiene consecuencias legales para la
organización. La competencia técnica no compensa el incumplimiento regulatorio: por eso
este RA no se compensa con los demás.

## 7. Referencias

- **RGPD** arts. 33 y 34 · **Directiva NIS2** (UE) 2022/2555 · **ENS** RD 311/2022 art. 33 · **DORA** (UE) 2022/2554.
- AEPD — guía de notificación de brechas. INCIBE-CERT y CCN-CERT — procedimientos.
- Plantillas: [`IC/material/notificacion/`](../material/notificacion/).
