# PPS · UT7 — DevSecOps: control de versiones, construcción e integración continua

**10 horas** · RA5 (a, b, c, g) · Servicio SOC: Prevención — canalización segura · Evidencias `PPS-E12`, `PPS-E13`

## Qué vamos a conseguir

Impedir que un cambio inseguro llegue a la rama de entrega.

## Antes de empezar

Herramientas: Git, pytest, Semgrep, Trivy, Gitleaks y Checkov; forja/runner del aula.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Crea rama de trabajo en el proyecto local y realiza un cambio pequeño con mensaje descriptivo.

2. Configura la protección en la forja indicada por el profesor: revisión y comprobaciones requeridas. Git local por sí solo no impone revisiones.

3. Ejecuta los controles uno a uno y registra herramienta, versión, reglas y bases utilizadas.

4. Añade un defecto sintético conocido a una rama de prueba. Verifica que el control pertinente devuelve fallo.

5. Integra los controles en la canalización sin ocultar errores; verifica que la fusión queda bloqueada.

6. Corrige, repite la canalización y documenta la revisión. Sin forja disponible, practica controles locales y deja PPS-E12 pendiente de demostración real.

## Cómo comprobar que está hecho

Caso inseguro bloqueado; caso corregido aceptado; protección demostrada en servidor.

> Sin Internet, las bases de vulnerabilidades, reglas, acciones y contenedores deben estar precargados.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT7-devsecops-ci.md).
- [ficha-PPS-E12-rama-protegida](laboratorio/ficha-PPS-E12-rama-protegida.md)
- [ficha-PPS-E13-ci-bloquea](laboratorio/ficha-PPS-E13-ci-bloquea.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
