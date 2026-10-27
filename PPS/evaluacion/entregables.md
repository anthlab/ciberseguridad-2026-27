# PPS 5023 — Cuaderno de entregables (enunciados para el alumnado)

Reglas: entrega por número de lista `NN-PPS-EX-<nombre>`. Criterio que atraviesa el módulo:
**una vulnerabilidad no está cerrada hasta que existe una prueba de regresión** que fallaría
si alguien la reintroduce. Trabajo sobre el repositorio del proyecto (ramas, PR, revisión).

---

## PPS-E1 · Lectura comparada (UT1 · I2/R2)
Para tres implementaciones equivalentes de un validador (Python/Java/C): localiza **punto de
entrada, sink y validación** en cada una y señala **dónde puede fallar** cada modelo de
ejecución. **Entrega**: `NN-PPS-E1-lectura.md` (tabla + razonamiento).

## PPS-E2 · Suite de pruebas y cobertura (UT1 · I1/R1)
Suite `pytest` con **cobertura medida** y al menos un **test de regresión** de un fallo dado.
Demuestra que la cobertura alta con aserciones triviales no prueba nada.
**Entrega**: `tests/` + informe de cobertura + `NN-PPS-E2-notas.md`.

## PPS-E3 · Dictamen de lenguaje + aislamiento (UT2 · I2/R2)
Dictamen de elección entre Go/Python/C para un servicio que procesa ficheros subidos,
justificado con criterios de seguridad. Más la **evidencia de seccomp**: perfil aplicado
(`UT2/laboratorio/perfil-restrictivo.json`) y captura de la syscall `mount` **rechazada**.
**Entrega**: `NN-PPS-E3-dictamen.md` + captura.

## PPS-E4 · Nivel ASVS (UT3 · I2/R2)
Asigna nivel ASVS a tres aplicaciones y **justifícalo**; para el portal SOC (nivel 2),
extrae la **lista de requisitos aplicables** y trázala a las pruebas que los verificarán
(`PPS/material/plantillas/checklist_asvs.md`). **Entrega**: `NN-PPS-E4-asvs.md`.

## PPS-E5 · Modelo STRIDE (UT3 · I2/R2)
Diagrama de flujo de datos del portal SOC + amenazas STRIDE por elemento con su **control
mitigador** + matriz de riesgo (impacto × probabilidad).
**Entrega**: `NN-PPS-E5-stride.md` + diagrama.

## PPS-E6 · Explotación web documentada (UT4 · I1/R1)
Reproduce con petición y captura **cuatro familias distintas** sobre Juice Shop/DVWA: una
inyección, un XSS, un fallo de sesión y un IDOR. **Entrega**: `NN-PPS-E6-explotacion.md`.

## PPS-E7 · Corrección + regresión (UT4 · I3/R3)
Corrige en el **código del portal** las cuatro familias de forma estructural (parametrizar,
codificar salida, endurecer sesión, control de acceso por rol) y añade por cada una un
**test de regresión** que fallaría si el bug vuelve. **Entrega**: PR en el repo + `tests/`.

## PPS-E8 · Migración a Argon2id (UT5 · I1/R1)
Sustituye el almacén de contraseñas por **Argon2id** con parámetros justificados y migración
transparente (re-hash al validar con el esquema antiguo). **Entrega**: PR + `NN-PPS-E8.md`.

## PPS-E9 · Bastionado con auditoría antes/después (UT5 · I2/R2)
Aplica el baseline nginx (`PPS/material/baseline/nginx-hardening.conf`) y demuestra la mejora
con `testssl.sh` y `lynis` **antes y después** (diff). **Entrega**: `antes-*.txt`,
`despues-*.txt`, `NN-PPS-E9-bastionado.md`.

## PPS-E10 · Análisis estático móvil (UT6 · I1/R1)
Informe MobSF del APK de laboratorio confirmado a mano con jadx: **permisos excesivos,
secretos incrustados, almacenamiento inseguro**. **Entrega**: `NN-PPS-E10-movil.md`.

## PPS-E11 · Tráfico móvil y compras (UT6 · I2/R2)
Interceptación con mitmproxy (HTTP en claro, TLS, fijación) + argumentación de por qué la
**validación de compras va en el servidor**. **Entrega**: `NN-PPS-E11-trafico.md`.

## PPS-E12 · Rama protegida y flujo (UT7 · I1/R1)
Configura la protección de la rama principal (revisión obligatoria, CI requerido, sin push
directo) y documenta el flujo rama→PR→revisión→CI→fusión. **Entrega**: captura de la config
+ `NN-PPS-E12-flujo.md`.

## PPS-E13 · CI que bloquea (UT7 · I3/R3)
Canalización de seguridad (SAST/SCA/secretos/IaC) adaptada de
`PPS/material/pipeline/ci-seguridad.yml`, que **rompe el build** ante un hallazgo. Probada
con un **caso que debe fallar** (p. ej. un secreto de prueba). **Entrega**: PR + captura del
build en rojo.

## PPS-E14 · Canario con reversión (UT8 · I3/R3)
Despliegue canario con sonda de disponibilidad y **reversión automática** demostrada ante
degradación. **Entrega**: `NN-PPS-E14-despliegue.md` + logs.

## PPS-E15 · DR ensayado (UT8 · I2/R2)
Procedimiento de recuperación ante desastres **ejecutado**: restauración real de una copia
con **RTO/RPO medidos en el ensayo** (no estimados). **Entrega**: `NN-PPS-E15-dr.md`.
