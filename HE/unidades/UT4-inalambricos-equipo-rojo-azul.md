# HE · UT4 — Otros sistemas inalámbricos y ejercicios de equipo rojo y azul

**6 horas** · RA2 (e, f, g) · Servicio SOC: Protección — equipo morado · Evidencias `HE-E7`, `HE-E8`

---

## 1. Objetivo de la unidad

Ampliar la auditoría inalámbrica más allá del Wi-Fi (Bluetooth/BLE, RFID/NFC, radiofrecuencia subgigahercio) y practicar la metodología de **equipo morado**: rojo y azul trabajando coordinados, donde cada técnica ofensiva se coteja en tiempo real con la capacidad de detección.

## 2. Contenido

### 2.1 Otros sistemas inalámbricos (RA2.e)

| Tecnología | Riesgo típico | Herramienta de laboratorio |
|---|---|---|
| **Bluetooth / BLE** | Emparejamiento inseguro, rastreo | bettercap, nRF |
| **RFID / NFC** | Clonado de credencial de acceso | Proxmark3, Flipper Zero |
| **Subgigahercio (433/868 MHz)** | Repetición de mandos (garajes, timbres) | HackRF, Flipper Zero |

Límite legal y ético: solo sobre dispositivos y tarjetas **propios de laboratorio**. El análisis de RF de terceros y la reemisión pueden ser delito.

### 2.2 Equipo rojo, azul y morado (RA2.f)

- **Rojo**: ejecuta las técnicas.
- **Azul**: detecta y responde.
- **Morado**: ambos coordinados, en la misma sesión, para maximizar el aprendizaje de detección. Cada técnica ATT&CK ejecutada se coteja con la regla de detección del SOC.

### 2.3 Informe de auditoría inalámbrica (RA2.g)

Estructura: alcance, hallazgos con evidencia, riesgo (probabilidad × impacto), remediación. Presentación oral de resultados.

## 3. Laboratorio guiado

> Entorno: equipos de RF del centro bajo registro de uso; tarjetas RFID de laboratorio.

### Parte A — Clonado RFID de laboratorio (RA2.e)

```bash
# Con Proxmark3 sobre una tarjeta PROPIA de laboratorio
pm3 --> hf search
pm3 --> hf mf autopwn        # recuperar claves de una MIFARE Classic de laboratorio
pm3 --> hf mf dump           # volcar contenido
```

1. Clona una credencial RFID **de laboratorio**, analiza por qué es posible y qué contramedida lo evitaría (tarjetas con cifrado moderno, lectores con autenticación mutua).

### Parte B — Ejercicio morado (RA2.f)

2. El equipo rojo ejecuta una técnica (p. ej. rogue AP de la UT3 o repetición de RF) y el azul documenta, **en la misma sesión**, qué detectó y con qué regla. Se registra qué quedó sin detectar.

### Parte C — Informe y defensa (RA2.g)

3. Redacta el informe de la auditoría inalámbrica y **preséntalo oralmente** ante el grupo, con recomendación de remediación priorizada.

## 4. Entregables

- **`HE-E7`** (informe, rúbrica R2): informe de auditoría inalámbrica con hallazgos, riesgo y remediación.
- **`HE-E8`** (defensa oral, rúbrica R4): presentación y defensa de los resultados ante el grupo.

## 5. Criterios de superación

- El clonado se realiza sobre material propio de laboratorio y se explica la contramedida.
- El ejercicio morado produce el catálogo de qué se detectó y qué no.
- La defensa oral traduce el hallazgo técnico a riesgo comprensible.

## 6. Referencias

- Proxmark3, Flipper Zero, HackRF — documentación y marco legal de uso.
- MITRE ATT&CK — técnicas de acceso por hardware/RF.
