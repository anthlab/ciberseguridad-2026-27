# Ficha PPS-E12 — Rama principal protegida + flujo de revisión

**UT7 · RA5.b · Instrumento I1 · Rúbrica R1 · Semana 15**
Entrega: captura de la configuración + `NN-PPS-E12-flujo.md`.

## Objetivo

Que en el repositorio del proyecto **nada entre a `main` sin revisión y sin la CI en verde**, y
documentar el flujo de trabajo que lo garantiza.

## Qué tienes que hacer

1. En el repositorio del proyecto (GitHub/GitLab de aula), configura la **protección de la rama
   principal** con, al menos:
   - Revisión obligatoria por par (mínimo 1 aprobación) antes de fusionar.
   - Comprobaciones de estado requeridas: el workflow de seguridad debe pasar en verde.
   - **Prohibido el empuje directo** a `main` (todo entra por Pull/Merge Request).
   - La protección **también aplica a administradores** (que el dueño no se la salte).
2. Crea una rama de trabajo, haz un cambio pequeño y llévalo hasta `main` **por el flujo
   correcto**: rama → PR → revisión → CI en verde → fusión.
3. **Comprueba que la barrera existe**: intenta un `git push` directo a `main` y captura el
   rechazo del servidor.

## Qué entregas

- Captura de la pantalla de configuración de protección de rama (con las opciones activas).
- Captura del **rechazo** del push directo a `main`.
- `NN-PPS-E12-flujo.md`: describe el flujo rama→PR→revisión→CI→fusión de **tu** repositorio, con
  el nombre real de las ramas, quién revisa y qué comprobación se exige.

## Se valora (R1, resumen)

- **Verificación del resultado**: no basta con activar la casilla; hay que **demostrar que
  bloquea** (el push rechazado). Marcar la opción sin probarla es "gate instalado, no activo".
- **Evidencia y reproducibilidad**: cualquiera debe poder repetir la configuración leyendo tu doc.

## Pista

El push directo debe devolver algo parecido a:

```
! [remote rejected] main -> main (protected branch hook declined)
error: failed to push some refs to '...'
```

Si tu push a `main` **funciona**, la protección no está activa: revísala.
