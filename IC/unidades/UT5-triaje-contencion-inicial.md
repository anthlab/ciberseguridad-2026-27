# IC · UT5 — Triaje: clasificación, valoración, seguimiento y contención inicial

**8 horas** · RA2 (e) · RA3 (e) · Servicio SOC: Detección — gestión de alertas · Respuesta — contención · Evidencias `IC-E8`, `IC-E9`

---

## 1. Objetivo de la unidad

El SOC recibe más alertas de las que puede investigar a fondo. El triaje decide qué merece atención, en qué orden y con qué primera respuesta. Esta unidad practica el triaje sobre una cola real, con gestión de caso en TheHive y contención inicial. **Requiere la arquitectura de detección de la UT3 emitiendo alertas.**

## 2. Contenido

### 2.1 Cola de alertas y niveles (RA2.e)

- Flujo L1 → L2 → L3: L1 clasifica y descarta ruido; L2 investiga; L3 casos complejos.
- Criterios de priorización: criticidad del activo, alcance, confianza en la detección.

### 2.2 Valoración (RA2.e)

Por cada alerta: ¿es falso positivo? ¿qué activo afecta? ¿qué alcance? ¿qué confianza tiene la detección? De ahí sale la prioridad.

### 2.3 Gestión del caso (RA2.e)

En **TheHive**: observables, tareas, TLP (semáforo de difusión) y trazabilidad temporal. **Cortex** enriquece los observables (reputación de IP, hash, dominio).

### 2.4 Contención inicial (RA3.e)

Primeras medidas para limitar el daño **sin destruir evidencia**: aislamiento de host, bloqueo de indicador (IP/dominio C2), revocación de sesión o credencial.

## 3. Laboratorio guiado

### Parte A — Triaje cronometrado (RA2.e)

1. Se presenta una **cola de 20 alertas** mezcladas con falsos positivos. Clasifícalas por prioridad **con reloj**. Justifica por escrito cada cierre por falso positivo (un cierre en blanco es error).

### Parte B — Gestión del caso en TheHive (RA2.e)

```bash
# TheHive + Cortex desplegados en SOC/plataforma
# Abrir caso, añadir observables, lanzar analizadores de Cortex, registrar tareas y timeline
```

2. Abre y documenta un caso completo en TheHive, con observables enriquecidos por Cortex y línea de tiempo.

### Parte C — Contención inicial (RA3.e)

3. Ejecuta una contención desde el SIEM/XDR (aísla un endpoint, bloquea un indicador) **preservando la evidencia** para el análisis posterior.

## 4. Entregables

- **`IC-E8`** (informe, rúbrica R2): procedimiento de triaje y matriz de priorización de xest.
- **`IC-E9`** (reto integrado, rúbrica R3): caso en TheHive completo con contención inicial documentada.

## 5. Criterios de superación

- El triaje prioriza con criterio (activo, alcance, confianza), no por orden de llegada.
- Cada falso positivo está justificado por escrito.
- La contención limita el daño sin contaminar la evidencia.

## 6. Errores frecuentes

- Cerrar alertas como falso positivo sin justificar: se pierde la trazabilidad y se repiten errores.
- Contener destruyendo la evidencia (apagar el equipo en vez de aislarlo) y dejar sin materia al forense.

## 7. Referencias

- NIST SP 800-61 rev. 2 — detección y análisis.
- TheHive + Cortex — documentación.
- Matriz de priorización: ver plantilla en [`IC/material/plantillas/matriz-triaje.md`](../material/plantillas/matriz-triaje.md).
