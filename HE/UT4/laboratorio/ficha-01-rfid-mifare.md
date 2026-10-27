# HE · UT4 · Ficha 01 — Clonado y análisis de una tarjeta RFID (MIFARE Classic)

> **Entorno**: VLAN aislada de laboratorio (xest-lab). Material **propio del centro**.
> Analizar RF/RFID de terceros es delito (arts. 197 bis/ter CP). Regla del aula: sin ROE
> firmado (HE-E1), nada de práctica activa.
> **Vinculación**: RA2.e · alimenta el informe **HE-E7** y la defensa oral **HE-E8**.

## Contexto

La empresa ficticia **xest** abre sus puertas con tarjetas **MIFARE Classic 1K**. Vais a
demostrar, sobre una tarjeta **de laboratorio**, por qué esa tecnología no debe usarse hoy
para control de acceso, y qué contramedida lo resolvería.

## Parte A — Demostración con Proxmark3 (la hace el profesor; vosotros observáis)

Sobre una tarjeta etiquetada **LAB**:

```
[usb] pm3 --> hf search              # identifica el tipo de tarjeta
[usb] pm3 --> hf mf autopwn          # recupera las claves de una Classic
[usb] pm3 --> hf mf dump             # vuelca los 16 sectores a fichero
```

Anota: ¿qué tipo detecta `hf search`? ¿Cuántas claves recupera `autopwn` y en cuánto tiempo?

## Parte B — Análisis del volcado (la hacéis TODOS)

No hace falta hardware: trabajáis sobre el volcado ya obtenido `datos/tarjeta-lab-01.dump`
(64 bloques, 16 bytes cada uno, un bloque por línea en hexadecimal).

1. Ejecuta el analizador incluido:

   ```bash
   cd datos
   python3 parse_mifare.py tarjeta-lab-01.dump
   ```

2. Responde en tu entregable (`NN-HE-UT4-ficha01.md`):

   - **P1.** ¿Qué **UID** tiene la tarjeta y qué modelo es (según SAK/ATQA)?
   - **P2.** ¿Cuántos sectores usan **clave por defecto** y cuál es? ¿Qué implica para un
     atacante?
   - **P3.** Localiza el bloque que contiene la **credencial de la puerta** (dato ASCII
     legible). ¿Qué sector es? Transcribe lo que se lee.
   - **P4.** El analizador marca un **bloque de valor** (monedero). ¿Qué saldo tiene y en qué
     sector? ¿Por qué es trivial falsificarlo en esta tarjeta?
   - **P5.** Explica en 3 líneas **por qué es posible** clonar esta tarjeta (pista: cifrado
     Crypto-1, claves por defecto) y **qué contramedida** lo evitaría.

3. **[RETO]** Modifica a mano una copia del volcado para **subir el saldo** del monedero a
   50,00 unidades manteniendo la coherencia del bloque de valor (valor + complemento + copia).
   Vuelve a ejecutar `parse_mifare.py` sobre tu copia y demuestra el nuevo saldo. Explica qué
   control del lector real detectaría (o no) esta manipulación.

## Evidencia a guardar

- Salida de `parse_mifare.py` (captura o pegado).
- Tus respuestas P1-P5 y el reto.
- **Este análisis es el hallazgo H-01 (RFID) de tu informe HE-E7.**

## Errores frecuentes

| Síntoma | Causa / salida |
|---|---|
| `bloque de N bytes (esperados 16)` | Línea partida o con espacios: cada línea son 32 caracteres hex. |
| `autopwn` no saca claves (Proxmark) | La tarjeta no es Classic o no tiene claves por defecto: usa la tarjeta **LAB** provista. |
| No encuentro el dato de la puerta | Está en un **bloque de datos**, no en el trailer; míralo en la sección ASCII del analizador. |
