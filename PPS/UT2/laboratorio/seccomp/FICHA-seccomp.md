# Reto · Construir tu propio perfil seccomp (PPS · UT2)

> Solo en la VLAN aislada de xest. Aquí pasas de *usar* un perfil a *escribir* uno, y de la
> lógica "bloqueo lo peligroso" (deny-list) a la lógica de producción "solo permito lo necesario"
> (allowlist, deny-by-default). Esto es la segunda mitad de la evidencia PPS-E3.

## Dos filosofías de perfil

| | `perfil-restrictivo.json` (deny-list) | `perfil-minimo.json` (allowlist) |
|---|---|---|
| `defaultAction` | `SCMP_ACT_ALLOW` (permite por defecto) | `SCMP_ACT_ERRNO` (deniega por defecto) |
| Qué declaras | Las syscalls **peligrosas** que bloqueas | Las syscalls **necesarias** que permites |
| Riesgo | Se te olvida bloquear alguna | El binario no arranca si falta una |
| Uso | Didáctico / rápido | **Producción** (así es el perfil por defecto de Docker) |

## Tarea

1. Parte de una allowlist **deliberadamente incompleta** (por ejemplo, solo `execve`, `write`,
   `exit_group`). Aplícala a `id` y observa el fallo:

   ```bash
   docker run --rm --security-opt seccomp=./mi-perfil.json alpine id
   ```

2. **Lee el error.** El kernel mata el proceso al llegar a la primera syscall no permitida.
   Con `SCMP_ACT_ERRNO` el binario recibe `EPERM` y suele abortar con un mensaje. Para ver
   exactamente **qué** syscall falta, ejecútalo bajo `strace` con el perfil `unconfined`:

   ```bash
   docker run --rm --security-opt seccomp=unconfined alpine \
     sh -c 'apk add -q strace; strace -f id 2>&1 | tail -30'
   ```

   Esa traza es la lista de syscalls reales que `id` necesita.

3. **Itera**: añade a tu allowlist las syscalls que la traza muestra hasta que `id` corra sin
   error. Ese ciclo —arrancar, leer la syscall que falta, añadirla— es exactamente cómo se
   endurece un contenedor en producción.

4. **Verifica que sigue conteniendo**: comprueba que, con tu perfil ya funcional para `id`, una
   syscall peligrosa que NO añadiste (p. ej. `mount`) sigue rechazada.

## Qué entregar (parte B de PPS-E3)

- Tu `mi-perfil.json` (allowlist, deny-by-default) con el que `id` corre.
- La **captura** de la syscall bloqueada (el `Operation not permitted` de `mount` o `ptrace`).
- Una frase sobre la **diferencia de superficie** entre el contenedor por defecto y el tuyo.

> No basta con que `id` funcione: eso solo prueba que la allowlist es **suficiente**. Hay que
> demostrar también que es **restrictiva** — que algo prohibido se rechaza de verdad. Afirmar
> el aislamiento sin verlo bloquear no acredita el criterio (rúbrica R2).
