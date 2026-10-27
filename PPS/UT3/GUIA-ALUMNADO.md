# PPS · UT3 — Nivel de verificación de seguridad: OWASP ASVS y superficie de riesgo

**8 horas** · RA2 (a, b, c, d) · Servicio SOC: Prevención — gestión de la exposición · Evidencias `PPS-E4`, `PPS-E5`

## Qué vamos a conseguir

Convertir riesgos en requisitos verificables y modelar amenazas.

## Antes de empezar

Herramientas: Navegador, Python, portal local; ASVS y STRIDE.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Lee apps-escenario.md y asigna nivel de verificación según datos, exposición y consecuencias.

2. Registra la versión de ASVS que utiliza tu lista. No mezcles identificadores entre ediciones.

3. Arranca el portal y ejecuta verifica_asvs.py. Lee su código para explicar qué comprueba cada sonda.

4. Clasifica los resultados: verificado, incumplido o no cubierto. Una sonda de cabeceras no verifica todo ASVS.

5. Dibuja procesos, almacenes, flujos y límites de confianza con dfd-portal-soc.md.

6. Completa stride-plantilla.md: amenaza, condición necesaria, impacto, control y prueba de que el control funciona.

## Cómo comprobar que está hecho

Versión ASVS indicada; límites de confianza explícitos; cada control tiene una prueba.

> ASVS define requisitos; STRIDE ayuda a plantear amenazas. Un escaneo no sustituye a ninguno.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT3-asvs-superficie-riesgo.md).
- [apps-escenario](laboratorio/apps-escenario.md)
- [dfd-portal-soc](laboratorio/dfd-portal-soc.md)
- [stride-plantilla](laboratorio/stride-plantilla.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
