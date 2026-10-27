# IC · UT6 — Investigación del incidente: evidencias, análisis e intercambio de información

**12 horas** · RA3 (a, b, c, d) · Servicio SOC: Respuesta — análisis · Protección — inteligencia operacional · Evidencias `IC-E10`, `IC-E11`

---

## 1. Objetivo de la unidad

Investigar a fondo un incidente: adquirir y custodiar evidencias, analizarlas, reconstruir la cadena de ataque, determinar la causa raíz e intercambiar la inteligencia resultante. El caso a investigar es la intrusión que el módulo HE ha producido en el ejercicio; ambos se coordinan en la misma semana.

## 2. Contenido

### 2.1 Adquisición y custodia de evidencias (RA3.a)

- **Orden de volatilidad**: memoria antes que disco, disco antes que copias.
- Hash de cada evidencia (integridad), sellado, cadena de custodia.
- Coordinación con el módulo **AF (Análisis forense)**: IC define el uso legal de la evidencia; AF la analiza en profundidad.

### 2.2 Análisis (RA3.b)

- Línea de tiempo del incidente: qué pasó y cuándo.
- Artefactos de sistema, memoria, red y registros.
- Correlación de eventos hasta reconstruir la secuencia.

### 2.3 Investigación y causa raíz (RA3.c)

- Cómo entró el atacante (vector), qué hizo, hasta dónde llegó.
- Determinación de la causa raíz (no el síntoma).

### 2.4 Intercambio de información (RA3.d)

- **MISP** para compartir IoCs; **STIX 2.1** como formato estándar.
- **TLP** (Traffic Light Protocol) para controlar la difusión.
- Relación con CCN-CERT / INCIBE-CERT y con proveedores.

## 3. Laboratorio guiado

### Parte A — Triaje forense (RA3.a, RA3.b)

```bash
# Velociraptor sobre la máquina comprometida de laboratorio
# Recolección dirigida: procesos, conexiones, persistencia, artefactos de ejecución
velociraptor --config server.config.yaml frontend
# Análisis de memoria con Volatility 3
vol -f memoria.raw windows.pslist
vol -f memoria.raw windows.malfind
```

1. Adquiere y analiza la evidencia de la máquina comprometida por HE, respetando el orden de volatilidad y hasheando cada pieza.

### Parte B — Línea de tiempo y ATT&CK (RA3.b, RA3.c)

2. Construye la **línea de tiempo** del incidente y **mapea las TTPs a ATT&CK**. Determina el vector de entrada y la causa raíz.

### Parte C — Intercambio (RA3.d)

```bash
# Publicar el evento con sus IoCs en MISP y exportar STIX 2.1
# Asignar TLP adecuado
```

3. Publica el evento en MISP con sus IoCs y expórtalo en STIX 2.1, con el TLP adecuado.

## 4. Entregables

- **`IC-E10`** (informe, rúbrica R2): informe de investigación con línea de tiempo, causa raíz e IoCs.
- **`IC-E11`** (reto integrado, rúbrica R3): evento MISP publicado y exportación STIX validada.

## 5. Criterios de superación

- La evidencia se adquiere con criterio forense (volatilidad, hash, custodia).
- La línea de tiempo reconstruye la intrusión y la causa raíz es la causa, no el síntoma.
- El evento MISP/STIX es válido y con TLP correcto.

## 6. Coordinación

Este caso proviene de **HE UT6/UT7** (la intrusión del ejercicio) y se coordina con **AF**
para la cadena de custodia. La causa raíz vuelve a **PPS** como requisito de bastionado.

## 7. Referencias

- NIST SP 800-61 rev. 2 y NIST SP 800-86.
- Velociraptor, Volatility 3, KAPE.
- MISP, STIX 2.1, TLP v2.0 (FIRST).
- MITRE ATT&CK.
