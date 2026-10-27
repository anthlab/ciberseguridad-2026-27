# IC · UT2 — Cultura de seguridad: plan de concienciación, materiales y auditoría de cumplimiento

**8 horas** · RA1 (c, d, e) · Servicio SOC: Gestión — cultura de seguridad · Evidencias `IC-E2`, `IC-E3`

---

## 1. Objetivo de la unidad

El eslabón más atacado es la persona. Esta unidad diseña un plan de concienciación con materiales propios, lo ejecuta con un simulacro medible y audita su cumplimiento. La concienciación no se declara: se mide.

## 2. Contenido

### 2.1 Plan de formación y concienciación (RA1.c)

- Público objetivo segmentado (dirección, técnicos, administración).
- Canales y calendario: no una charla anual, sino refuerzo continuo.
- Indicadores desde el diseño: tasa de clic en phishing, tasa de reporte, tiempo medio hasta el reporte.

### 2.2 Materiales (RA1.d)

Píldoras breves, cartelería, microlearning, simulacros de phishing. Mensaje claro, accionable, sin culpabilizar.

### 2.3 Métricas de eficacia (RA1.c)

| Métrica | Qué mide | Meta |
|---|---|---|
| Tasa de clic | % que pica en el phishing simulado | Bajar con el tiempo |
| Tasa de reporte | % que reporta el correo sospechoso | Subir con el tiempo |
| Tiempo medio de reporte | Cuánto tarda el primero en avisar | Bajar |

La tasa de reporte importa más que la de clic: una organización donde alguien avisa rápido contiene antes.

### 2.4 Auditoría de cumplimiento (RA1.e)

Lista de verificación del plan de prevención, hallazgos priorizados, acciones correctoras.

## 3. Laboratorio guiado

### Parte A — Campaña de concienciación (RA1.c, RA1.d)

1. Diseña una campaña de 4 semanas para el personal ficticio de xest: temas, canales, calendario, materiales.

### Parte B — Simulacro de phishing (RA1.d)

```bash
# GoPhish en laboratorio, sobre buzones de prueba y con consentimiento documentado
# Configurar: plantilla de correo, página de aterrizaje, grupo de destinatarios de laboratorio
# Lanzar la campaña y recoger métricas: enviados, abiertos, clics, reportes
```

2. Ejecuta un simulacro **sobre buzones de laboratorio** con consentimiento documentado. Recoge y **lee críticamente** las métricas.

### Parte C — Auditoría (RA1.e)

3. Audita el cumplimiento del plan de prevención con una lista de verificación y prioriza los hallazgos.

## 4. Entregables

- **`IC-E2`** (informe, rúbrica R2): plan de concienciación + kit de materiales + informe de auditoría de cumplimiento.
- **`IC-E3`** (laboratorio, rúbrica R1): ejecución del simulacro y lectura crítica de las métricas.

## 5. Criterios de superación

- El plan define métricas desde el diseño, no las improvisa al final.
- El simulacro se ejecuta con consentimiento y sus métricas se interpretan (no solo se listan).
- La auditoría produce acciones correctoras priorizadas.

## 6. Ética

El simulacro de phishing se realiza sobre buzones de laboratorio o del propio grupo,
con consentimiento documentado. No se simula sobre personas no informadas ajenas al
ejercicio.

## 7. Referencias

- ENISA — Awareness Raising.
- GoPhish — documentación.
- CCN-STIC 896 — cultura de seguridad.
