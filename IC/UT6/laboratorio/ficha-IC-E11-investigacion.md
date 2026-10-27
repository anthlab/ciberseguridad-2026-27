# Ficha IC-E11 · Timeline, causa raíz e intercambio (para el alumnado)

**Evidencia**: IC-E11 · RA3 b,c,d · Instrumento I3 · Rúbrica **R3** (reto integrado).
**Caso**: el mismo de IC-E10. Ahora **reconstruyes** el incidente y **compartes** la
inteligencia. Bolsa de evidencias en `evidencias/`.

## Parte A — Línea de tiempo y ATT&CK (RA3.b, RA3.c)

1. Fusiona tus hallazgos (memoria, registro, EVTX, log del portal) en una **línea de tiempo**
   única, ordenada por hora. Tienes de apoyo `evidencias/timeline-supertimeline.csv`.
2. **Mapea cada paso a una técnica de MITRE ATT&CK** (identificador `Txxxx`).
3. Determina el **vector de entrada** y la **causa raíz**. Aviso: *"había malware"* NO es
   causa raíz. La causa raíz es **por qué fue posible entrar**.

## Parte B — Contraste con la verdad terreno (verificación, RA3.c)

4. El docente te entrega ahora `evidencias/HE-E12-informe-intrusion.md`. **Compara** tu
   reconstrucción con lo que el rojo declara: ¿coincide el vector, la cadena, la causa raíz?
   Anota lo que **no pudiste ver** solo con la memoria y por qué.

## Parte C — Intercambio de inteligencia (RA3.d)

5. Construye el **evento MISP** con los IoC del caso (IP/URL/hash/fichero/persistencia),
   etiquétalo con el **TLP** que corresponda y **publícalo**.
6. **Exporta a STIX 2.1** y valida el bundle.

```
MISP -> Add Event -> Attributes (IoC) -> Galaxy/Tags (ATT&CK + TLP) -> Publish -> Download as STIX 2.1
# Validación del bundle:
python -m stix2validator NN-IC-E11-stix-bundle.json   # tu export; o: stix2 parse
```

**Decisión TLP** (justifícala): ¿el caso puede compartirse con la comunidad (CCN-CERT /
INCIBE-CERT) o solo dentro de xest? Explica por qué eliges **TLP:AMBER** frente a GREEN/RED.

**Entrega**: `NN-IC-E11-investigacion.md` (timeline + ATT&CK + causa raíz + contraste HE-E12) +
export STIX 2.1 validado. Se corrige con R3: se valora la **integración** con HE/AF/PPS y la
**reproducibilidad**.
