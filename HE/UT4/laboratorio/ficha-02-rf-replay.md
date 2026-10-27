# HE · UT4 · Ficha 02 — Radiofrecuencia subgigahercio: ¿replay o rolling code?

> **Entorno**: VLAN aislada / banco de RF del centro. Mandos **propios de laboratorio**.
> Capturar y **reemitir** RF de terceros (garajes, coches, timbres ajenos) es delito.
> **Vinculación**: RA2.e · alimenta el hallazgo **H-02** de tu informe **HE-E7**.

## Contexto

Muchos dispositivos de 433/868 MHz (mandos de garaje, timbres, sensores) siguen usando
**código fijo**: envían siempre la misma trama. Eso los hace vulnerables a un ataque de
**repetición (replay)**: capturas una vez, retransmites y abre. Los diseños modernos usan
**rolling code** (contador cifrado que cambia en cada pulsación). Vais a distinguir unos de
otros a partir de capturas reales de laboratorio.

## Parte A — Demostración con URH (la hace el profesor)

Con **Universal Radio Hacker** (https://github.com/jopohl/urh) y un HackRF/RTL-SDR, sobre un
mando **LAB**: sintonizar 433.92 MHz, capturar la señal, ver la **modulación** (OOK/ASK),
demodular a bits y observar si la trama se **repite** entre pulsaciones. Concepto de
*rolling code* y por qué un mando moderno no se repite sin más.

## Parte B — Análisis de las capturas (la hacéis TODOS)

Trabajáis sobre `datos/capturas-rf/capturas-rf.csv` (17 capturas de 4 dispositivos ya
demoduladas a `payload_hex`).

1. Ejecuta el analizador:

   ```bash
   cd datos/capturas-rf
   python3 analiza_rf.py capturas-rf.csv
   ```

2. Responde (`NN-HE-UT4-ficha02.md`):

   - **P1.** Lista los dispositivos que son **código fijo** (replay viable) y los que son
     **rolling code**. Justifícalo con el número de **tramas únicas** por dispositivo.
   - **P2.** En `mando-garaje-B` el analizador detecta un **prefijo común**. ¿Qué representa
     esa parte fija y qué representa la parte que cambia?
   - **P3.** ¿Por qué el `sensor-puerta-868` es **fijo** y aun así **repetirlo no ayuda** a un
     atacante que quiere entrar? (pista: piensa qué hace ese mensaje).
   - **P4.** Escribe la **secuencia de comandos conceptual** de un replay con URH/HackRF
     contra `mando-garaje-A` (capturar → guardar → retransmitir). No hace falta ejecutarla;
     descríbela con precisión.
   - **P5.** Contramedida: ¿qué convierte un mando de código fijo en resistente al replay?
     Nombra el mecanismo y por qué el atacante ya no puede reutilizar una captura.

## Evidencia a guardar

- Salida de `analiza_rf.py`.
- Respuestas P1-P5.
- **Es el hallazgo H-02 (RF replay) de tu informe HE-E7.**

## Errores frecuentes

| Síntoma | Causa |
|---|---|
| URH no ve la señal (demo) | Frecuencia/ganancia mal; empezar por la frecuencia impresa en el mando LAB. |
| "Todos parecen iguales" | Estás mirando la portadora, no el payload demodulado; usa la columna `payload_hex`. |
