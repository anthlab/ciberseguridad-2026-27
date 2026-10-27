# Informe de investigación forense — [Incidente xest] (plantilla · IC-E10 + IC-E11)

> Estructura mínima esperada (rúbricas R1/R2/R3). Rellena cada sección; no dejes huecos.
> Distingue siempre **lo verificado** (visto en la evidencia) de **lo inferido**.

## 0. Resumen ejecutivo (para dirección, ≤10 líneas)
Qué pasó, cuándo se detectó, alcance, causa raíz en una frase y estado actual. Sin jerga.

## 1. Ficha del caso
- Referencia SOC / analista / fechas.
- Sistemas afectados y ventana temporal del incidente.
- Origen del caso: **HE-E12** (ejercicio del equipo rojo). Coordinación con **AF** y **PPS**.

## 2. Adquisición y cadena de custodia (RA3.a)
- Orden de volatilidad seguido y **justificación**.
- Tabla de evidencias con hash (enlaza `plantilla-cadena-custodia.md`).
- Verificación de integridad (`sha256sum -c`).

## 3. Análisis (RA3.b)
- **Procesos**: proceso anómalo, PID, ruta, padre, por qué es sospechoso.
- **Red**: conexiones C2 (IP, puerto, proceso).
- **Memoria**: código inyectado (malfind), cadenas relevantes, download cradle descodificado.
- **Persistencia**: claves de registro y tareas creadas por el atacante.
- **Disco/registro**: artefactos de ejecución, ficheros creados.

## 4. Línea de tiempo (RA3.b) y mapeo ATT&CK (RA3.c)
| Hora (UTC) | Evento | Evidencia que lo soporta | Técnica ATT&CK |
|---|---|---|---|
| | | | |

## 5. Vector de entrada y causa raíz (RA3.c)
- **Vector**: cómo entró al entorno.
- **Causa raíz**: por qué fue posible (no el síntoma). Recomendación devuelta a PPS.
- **Contraste con HE-E12**: coincidencias, discrepancias y puntos ciegos de la investigación.

## 6. Indicadores de compromiso (IoC) e intercambio (RA3.d)
- Tabla de IoC (tipo, valor, confianza).
- **Evento MISP** (id/enlace), **TLP** asignado y **justificación**.
- **Export STIX 2.1** adjunto y validado.

## 7. Recomendaciones y traspaso
- Entrada a **UT7** (respuesta/erradicación) y **UT8** (notificación).
- Qué queda para **AF** (análisis del binario) y **PPS** (bastionado).
