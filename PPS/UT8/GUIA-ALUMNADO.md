# PPS · UT8 — Despliegue automatizado, resiliencia y recuperación ante desastres

**5 horas** · RA5 (d, e, f) · Servicio SOC: Prevención — continuidad del despliegue · Evidencias `PPS-E14`, `PPS-E15`

## Qué vamos a conseguir

Desplegar, revertir y recuperar con medidas reales.

## Antes de empezar

Herramientas: Docker, nginx, Python y SQLite; scripts del laboratorio.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Lee README.md y genera el dataset sintético con el comando indicado. Guarda una copia inicial.

2. Arranca solo el servicio estable y comprueba /health y una operación funcional.

3. Sigue ejercicio-E14-canario.md: ejecuta el canario degradado y conserva la decisión de reversión.

4. Repite con canario sano. Distingue respuesta del proxy y respuesta directa de cada versión.

5. Sigue ejercicio-E15-dr.md en datos de laboratorio: realiza copia, verifica integridad, simula pérdida y restaura.

6. Mide inicio de interrupción, retorno funcional y antigüedad del último dato recuperado. Calcula RTO/RPO con esas marcas y prueba que los datos restaurados son utilizables.

## Cómo comprobar que está hecho

Reversión observada; restauración real; tiempos y pérdida de datos medidos.

> docker compose down detiene y elimina contenedores/redes, pero no equivale a restaurar los datos.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT8-despliegue-resiliencia-recuperacion.md).
- [README](laboratorio/README.md)
- [procedimiento-dr-plantilla](laboratorio/dr/procedimiento-dr-plantilla.md)
- [ejercicio-E14-canario](laboratorio/ejercicio-E14-canario.md)
- [ejercicio-E15-dr](laboratorio/ejercicio-E15-dr.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
