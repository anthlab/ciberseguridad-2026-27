# HE-E7 · Esqueleto del informe de auditoría inalámbrica

> Plantilla de arranque del entregable **HE-E7** (rúbrica **R2**). El informe completo de
> pentest está en el repo `HE/material/plantillas/informe-pentest.md` (referencia para el
> nivel de detalle); aquí tienes la versión **inalámbrica** ya orientada a los 3 hallazgos de
> la UT4. Entrega: `NN-HE-E7-informe.pdf`. Sin ROE firmado (HE-E1) no se admite.

## 1. Resumen ejecutivo *(1 página, sin jerga, para dirección)*

- Alcance en una frase (auditoría inalámbrica de xest-lab: RFID, RF, Wi-Fi).
- Postura general (semáforo).
- Los 3 riesgos principales y su consecuencia de negocio.
- Recomendación principal.

## 2. Alcance y metodología

- Perímetro (referencia al **ROE HE-E1**): tarjetas/mandos/red **de laboratorio** xest-lab.
- Ventana de ejecución y regla de parada.
- Metodología: PTES / NIST SP 800-115. Marco legal (solo material propio de laboratorio).

## 3. Resumen de hallazgos

| Id | Hallazgo | Dimensión rota | Probabilidad | Impacto | Riesgo |
|---|---|---|---|---|---|
| H-01 | Clonado de credencial RFID (MIFARE Classic, claves por defecto) | Autenticidad | Alta | Alto | **Crítico** |
| H-02 | Apertura por repetición de RF (mando de código fijo) | Autenticidad | Media | Medio-Alto | **Alto** |
| H-03 | Punto de acceso no autorizado (rogue AP) sin detección | Confidencialidad | Media | Alto | **Alto** |

Matriz riesgo (probabilidad × impacto):

```
Impacto ▲
  Alto  │            H-03      H-01
  Medio │        H-02
  Bajo  │
        └───────────────────────────▶ Probabilidad
             Baja    Media    Alta
```

## 4. Hallazgos detallados *(uno por cada uno; rellena con TU evidencia)*

### H-01 — Clonado de credencial RFID
- **Activo**: control de acceso físico (puertas, CPD).
- **Evidencia**: salida de `parse_mifare.py` (16/16 sectores con clave por defecto; credencial
  en sector 1; monedero falsificable en sector 5).
- **Impacto de negocio**: acceso no autorizado a instalaciones; fraude del monedero.
- **Remediación**: MIFARE DESFire EV3 (AES, autenticación mutua), claves diversificadas,
  saldo/credencial validados en servidor. **Prioridad 1**.

### H-02 — Apertura por repetición de RF
- **Activo**: mando de acceso 433 MHz.
- **Evidencia**: `analiza_rf.py` — `mando-garaje-A` código fijo, 5 capturas idénticas.
- **Impacto**: acceso físico por captura + replay con SDR de bajo coste.
- **Remediación**: mandos con rolling code autenticado. **Prioridad 2**.

### H-03 — Rogue AP sin detección
- **Activo**: red inalámbrica xest-lab y sus clientes.
- **Evidencia**: contraste morado (Ficha 03) — deauth detectado, **evil twin no**.
- **Impacto**: captura de credenciales / MITM sobre clientes engañados.
- **Remediación**: WIDS con detección de SSID en BSSID no autorizado; 802.1X. **Prioridad 2**.

## 5. Recomendaciones de detección (a IC)

- Regla evil twin: SSID conocido en BSSID no autorizado.
- Regla correlación RFID: viaje imposible + acceso fuera de horario (ver `detecta_clon_rfid.py`).
- Fuente pendiente: sonda SDR sub-GHz para visibilidad de RF.

## 6. Conclusión

Traduce el riesgo técnico a decisión de negocio: qué se arregla ya, qué coste evita.

---
*Para la defensa oral **HE-E8** (rúbrica R4, ≤10 min): elige H-01, demuéstralo en vivo con
plan B (volcado ya obtenido) y traduce el impacto a consecuencia de negocio.*
