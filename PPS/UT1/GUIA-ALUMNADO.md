# PPS · UT1 — Código, modelos de ejecución y pruebas de software

**9 horas** · RA1 (a, b, c, d) · Servicio SOC: Prevención — calidad del software · Evidencias `PPS-E1`, `PPS-E2`

## Qué vamos a conseguir

Leer código y demostrar con pruebas qué comportamiento garantiza.

## Antes de empezar

Herramientas: Python, pytest y coverage; C y Java para lectura comparada.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Abre los tres validadores de laboratorio y marca entrada, transformación y operación sensible. Copia la línea exacta que fundamenta cada observación.

2. Predice el resultado con una entrada normal, una vacía y una fuera del rango. Distingue error de sintaxis, de ejecución y de lógica.

3. Trabaja en miniproyecto y ejecuta la suite inicial. Conserva la salida antes de modificar código.

4. Añade una aserción que compruebe el valor y otra que compruebe el rechazo de una entrada inválida. Una aserción siempre verdadera no verifica el programa.

5. Introduce un cambio controlado que reproduzca el fallo en una copia; comprueba que el test lo detecta, deshaz ese cambio y repite la suite.

6. Mide la cobertura y explica qué comportamiento importante sigue sin probarse. Entrega la tabla de lectura y las pruebas con su salida.

## Cómo comprobar que está hecho

Suite inicial reproducible; test que falla con el defecto y pasa con la corrección; interpretación de cobertura.

> Que todos los tests pasen solo demuestra las propiedades que realmente comprueban. No equivale a ausencia de vulnerabilidades.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT1-codigo-modelos-ejecucion-pruebas.md).

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
