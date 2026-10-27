# IC-E6 · Detección física integrada — plantilla del entregable

> Rellena esta plantilla. Es el núcleo de `NN-IC-E6-fisica.md`. Rúbrica **R2**
> (`~/xest-lab/2026-2027/docs/planificacion/rubricas.md`). El criterio clave: cada
> **evento físico** debe conectar con una **alerta lógica** en el SOC, con su regla y su
> prioridad. Un control físico que no llega al SOC es un punto ciego, no una defensa.

## 1. Alcance e inventario de controles

Parte del inventario `datos/inventario-controles-fisicos.csv`. Complétalo: hay controles
con la columna `integrado_soc = NO` y sin evento/alerta definidos. Tu trabajo es decidir
cuáles deben integrarse y con qué evento y alerta.

| Control | Zona | Tipo | Telemetría | Integrado SOC | Evento físico | Alerta lógica |
|---|---|---|---|---|---|---|
| _(copia y completa las 10 filas del CSV)_ | | | | | | |

## 2. Ruta de alerta (evento físico → alerta en el SOC)

Por cada evento relevante, la cadena completa:

| Evento físico | Control que lo capta | Telemetría / formato | Regla SOC (id) | Alerta lógica (nivel) | Prioridad (Crit×Alc×Conf) | Acción del analista |
|---|---|---|---|---|---|---|
| Apertura de rack fuera de horario | Sensor rackA | syslog key=value | 100201 | Apertura rack CPD fuera de horario (10) | | |
| _(añade una fila por evento)_ | | | | | | |

> Prioridad = Criticidad × Alcance × Confianza (1-3 cada factor), como la matriz de UT5
> (`~/xest-lab/2026-2027/IC/material/plantillas/matriz-triaje.md`).

## 3. Puntos ciegos declarados

Controles que **no** se integran (y por qué es aceptable) o que faltan por instalar.
Un punto ciego reconocido y justificado es rigor; uno oculto es un fallo.

## 4. Verificación

Demuestra que la cadena funciona: pega la salida de `wazuh-logtest` (o del laboratorio
sin Wazuh, el script `probar-reglas.sh`) para **al menos** el evento crítico de rack y el
de tailgating, mostrando la regla que dispara y su nivel.
