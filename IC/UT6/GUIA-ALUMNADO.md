# IC · UT6 — Investigación del incidente: evidencias, análisis e intercambio de información

**12 horas** · RA3 (a, b, c, d) · Servicio SOC: Respuesta — análisis · Protección — inteligencia operacional · Evidencias `IC-E10`, `IC-E11`

## Qué vamos a conseguir

Investigar sin perder trazabilidad y compartir indicadores con contexto.

## Antes de empezar

Herramientas: Hashes, evidencias locales, Velociraptor/Volatility cuando existan adquisiciones; STIX/MISP.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Lee ficha-IC-E10-adquisicion.md e inventaría los archivos proporcionados. Distingue imagen de memoria, logs y salidas previamente generadas.

2. Calcula hashes, conserva originales y analiza copias. Rellena cadena de custodia con cada transferencia.

3. Relaciona procesos, red, persistencia y registros en una línea de tiempo normalizada a UTC.

4. Formula una hipótesis de entrada y busca evidencia que pueda refutarla, además de la que la apoya.

5. Resuelve ficha-IC-E11-investigacion.md y contrasta con el informe HE-E12 recibido.

6. Exporta indicadores con contexto, vigencia y restricciones. Validar JSON no valida STIX ni demuestra importación en MISP; comprueba cada nivel por separado.

## Cómo comprobar que está hecho

Originales preservados; cronología fundamentada; formato e importación distinguidos.

> Sin imagen de memoria no se acredita adquisición ni ejecución real de Volatility; las salidas de ejemplo son análisis documental.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT6-investigacion-evidencias-intercambio.md).
- [HE-E12-informe-intrusion](laboratorio/evidencias/HE-E12-informe-intrusion.md)
- [ficha-IC-E10-adquisicion](laboratorio/ficha-IC-E10-adquisicion.md)
- [ficha-IC-E11-investigacion](laboratorio/ficha-IC-E11-investigacion.md)
- [plantilla-cadena-custodia](laboratorio/plantilla-cadena-custodia.md)
- [plantilla-informe-forense](laboratorio/plantilla-informe-forense.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
