# Ficha del alumnado — Simulacro técnico: erradicar y recuperar (IC-E13, RA4.d)

> **Entorno**: VLAN aislada de xest. El contenedor `portal-comprometido` es un objetivo
> de laboratorio. No ejecutes nada de esto contra la red del centro ni contra Internet.
> **Evidencia a producir**: la parte técnica de IC-E13 (respuesta ejecutada) con RTO real
> medido y la salida `6/6 LIMPIO` del checker.

## Objetivo

Un sistema de xest ha sido comprometido. Tienes los IoC de HE (`ioc-he-e14.md`). Tu misión:
1. **Contener** y hacer triaje: cazar **todas** las puertas traseras.
2. **Erradicar** cada una.
3. **Recuperar** el servicio desde una **copia verificada** y **medir el RTO real**.
4. **Demostrar** que no queda persistencia (checker en 6/6).

## Paso 0 · El reloj arranca

Anota la **hora de inicio** en cuanto empieces a responder. El RTO se mide desde aquí hasta
que el servicio vuelve a estar operativo y limpio.

`Hora de inicio: __________`

## Paso 1 · Confirmar el compromiso

```bash
docker compose ps
curl -s "http://localhost:8090/assets/.cache.php?c=id"
```
¿Qué devuelve el segundo comando y por qué es un problema?

`__________________________________________________________________`

## Paso 2 · Triaje: cazar la persistencia (usa ioc-he-e14.md)

```bash
docker exec -it portal-comprometido bash
```
Localiza y anota cada puerta (comando que la delata + evidencia encontrada):

| # | Puerta | Comando que la delata | Evidencia (salida) |
|---|---|---|---|
| 1 | Webshell | | |
| 2 | Usuario backdoor + clave | | |
| 3 | Cron reverse shell | | |
| 4 | Binario SUID | | |

## Paso 3 · Erradicar cada puerta

Anota el comando de erradicación de cada una. **Antes de dar por erradicado, no restaures nada.**

`1) ______________________  2) ______________________`
`3) ______________________  4) ______________________`

## Paso 4 · Recuperar desde copia verificada

Primero **verifica** la copia por hash; solo si sale `OK`, restaura:
```bash
cd copia-verificada && sha256sum -c SHA256SUMS
```
Resultado: `__________`  (si sale `FAILED`, **para**: restaurar sería reinfectarse)

Restaura el webroot limpio, reinicia el servicio y comprueba que responde `200`.
Anota la **hora de fin** y calcula el **RTO real**:

`Hora de fin: __________   RTO real = fin - inicio = __________`
`RTO objetivo del servicio: 4 h.   ¿Se ha cumplido? __________`

## Paso 5 · Demostrar ausencia de persistencia

```bash
bash verificar-persistencia.sh
```
Pega aquí el resultado. **No has terminado hasta ver `6/6 LIMPIO`.** Si sale algún
`[FALLO]`, vuelve al paso 3 sobre esa puerta concreta.

`RESULTADO: __________`

## Paso 6 · Monitorización reforzada

Propón **una regla de detección por cada puerta** que cerraste (qué evento debería alertar):

- Webshell: `______________________________________________`
- Usuario nuevo: `______________________________________________`
- Cron a IP externa: `______________________________________________`
- SUID nuevo: `______________________________________________`

## Para IC-E13 (parte técnica)

Vuelca en tu informe: vector y persistencia (con el IoC que delató cada puerta),
erradicación (comando por puerta), recuperación (hash `OK` + RTO real medido),
la salida `6/6 LIMPIO` y las reglas de monitorización reforzada.
