# IC · UT7 — Respuesta, ciberresiliencia y recuperación del servicio

**14 horas** · RA4 (a, b, c, d, e, f) · Servicio SOC: Respuesta — contención, erradicación, recuperación · Evidencias `IC-E12`, `IC-E13`, `IC-E14`

---

## 1. Objetivo de la unidad

Es la unidad de mayor peso del módulo: dar respuesta completa a un incidente con playbooks ensayados, mantener el servicio (ciberresiliencia), erradicar la amenaza y recuperar desde copia verificada, cerrando con lecciones aprendidas. Aquí el SOC demuestra para qué existe.

## 2. Contenido

### 2.1 Playbooks por categoría (RA4.a)

Seis playbooks operativos (en [`SOC/plataforma/playbooks/`](../../SOC/plataforma/playbooks/)):

1. Ransomware
2. Phishing / BEC
3. Malware en endpoint
4. Exfiltración de datos
5. DDoS
6. Cuenta comprometida (identidad)

Cada uno sigue la estructura NIST y decide por fase.

### 2.2 Ciberresiliencia (RA4.b)

- Continuidad del servicio durante el incidente: RTO/RPO, copias inmutables, degradación controlada.
- Fortalecer identificación, detección, prevención, contención, recuperación y cooperación con terceros.

### 2.3 Flujo de decisión y escalado (RA4.c)

- Matriz RACI del CSIRT: quién decide, quién ejecuta, quién es informado.
- Escalado interno (dirección, jurídico) y externo (CERT, proveedor).

### 2.4 Erradicación y recuperación (RA4.d)

- Eliminar el vector, el malware persistido y cualquier puerta trasera.
- Restaurar desde **copia verificada**, endurecer y **monitorizar reforzado** las semanas siguientes.

### 2.5 Lecciones aprendidas (RA4.e, RA4.f)

- Retrospectiva sin culpables: qué falló en el proceso, no quién.
- Acciones correctoras con responsable y fecha; seguimiento hasta el cierre.
- Retroalimentación a PPS (bastionado) y HE (nuevos escenarios).

## 3. Laboratorio guiado

### Parte A — Playbooks (RA4.a)

1. Redacta y ensaya los **seis playbooks** del SOC de xest, partiendo de los de `SOC/plataforma/playbooks/`.

### Parte B — Tabletop de ransomware (RA4.b, RA4.c)

2. Ejecuta el **ejercicio de mesa** de ransomware con roles repartidos y **reloj real**, usando el escenario de [`IC/material/plantillas/tabletop-ransomware.md`](../material/plantillas/tabletop-ransomware.md). Decide contención, verificación de copias, escalado y notificación.

### Parte C — Simulacro técnico (RA4.d)

3. Simulacro técnico: contén, erradica y **restaura desde copia verificada** un sistema de laboratorio. Mide el tiempo de vuelta a la normalidad.

### Parte D — Retrospectiva (RA4.e, RA4.f)

4. Retrospectiva con acciones correctoras asignadas (responsable + fecha de verificación).

## 4. Entregables

- **`IC-E12`** (informe, rúbrica R2): manual del CSIRT — roles, matriz de escalado y seis playbooks ensayados.
- **`IC-E13`** (reto integrado, rúbrica R3): informe del tabletop con autocrítica y plan de acciones correctoras.
- **`IC-E14`** (defensa oral, rúbrica R4): defensa del incidente ante tribunal simulado.

## 5. Criterios de superación

- Los seis playbooks están redactados y ensayados, no solo descritos.
- El tabletop se ejecuta con reloj real y produce autocrítica útil.
- La recuperación usa copia verificada y mide el tiempo real.

## 6. Referencias

- **NIST SP 800-61 rev. 2** — ciclo de respuesta.
- **ISO/IEC 27035** — gestión de incidentes.
- **CCN-STIC 817 / 403** — gestión de ciberincidentes.
- Manual CSIRT y playbooks: [`IC/material/csirt/`](../material/csirt/) y [`SOC/plataforma/playbooks/`](../../SOC/plataforma/playbooks/).
