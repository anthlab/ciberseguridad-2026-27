# Hoja de decisiones — Tabletop de ransomware (IC-E13, RA4.b/c)

> Escenario: `IC/material/plantillas/tabletop-ransomware.md`. El facilitador suelta inyectos con
> su reloj; vosotros decidís **con la información del momento** y **anotáis cada decisión con su
> hora de reloj de mesa**. Al final se evalúa la calidad de la decisión y la **autocrítica**, no
> que el incidente saliera bien.

## Roles del equipo (del manual CSIRT)

- Coordinador de incidente: ____________________
- Analista L1: ____________________   · Analista L2: ____________________
- Portavoz: ____________________      · Enlace jurídico: ____________________

## Registro de decisiones (reloj real)

| T+ (inyecto) | Hora de mesa | Decisión tomada | Quién la tomó | Justificación breve |
|---|---|---|---|---|
| 00:00 cifrado masivo | | | | |
| 00:10 propagación SMB | | | | |
| 00:20 cae facturación | | | | |
| 00:30 doble extorsión + datos | | | | |
| 00:40 exigen pago 48 h | | | | |
| 00:50 llama un medio | | | | |
| 01:00 paciente cero (phishing) | | | | |
| 01:10 copias sin verificar | | | | |

## Relojes regulatorios

- Hora en que se detectó el dato personal comprometido: __________ → **RGPD 72 h vence**: __________
- Hora en que se identificó el vector (NIS2): __________ → **NIS2 24 h (alerta) vence**: __________

## Autocrítica (preguntas de cierre)

1. ¿Cuándo se activó formalmente el CSIRT? ¿Se tardó de más? ¿Qué lo causó?
   `__________________________________________________________________`
2. ¿La contención preservó la evidencia o la destruyó?
   `__________________________________________________________________`
3. ¿Se cumplieron los relojes (RGPD 72 h, NIS2 24 h)?
   `__________________________________________________________________`
4. ¿La decisión sobre el pago estaba fundamentada o fue improvisada?
   `__________________________________________________________________`
5. ¿Qué regla de detección habría dado más margen? (→ UT3 / HE)
   `__________________________________________________________________`
6. ¿Qué medida de bastionado (PPS) habría evitado la propagación?
   `__________________________________________________________________`

> Estas respuestas son la materia prima del informe IC-E13 (tabletop) y de las acciones
> correctoras de IC-E14. Sé honesto: un fallo reconocido con lucidez puntúa más que un
> "salió todo perfecto".
