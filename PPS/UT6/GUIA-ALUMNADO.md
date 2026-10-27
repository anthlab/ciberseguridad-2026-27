# PPS · UT6 — Seguridad en aplicaciones para dispositivos móviles

**9 horas** · RA4 (a, b, c, d, e) · Servicio SOC: Prevención — superficie móvil · Evidencias `PPS-E10`, `PPS-E11`

## Qué vamos a conseguir

Relacionar código móvil, tráfico y decisiones del servidor.

## Antes de empezar

Herramientas: jadx/MobSF, Python y mitmproxy; APK o fuentes didácticas incluidas.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Lee README.md y registra si analizas un APK real del laboratorio o el árbol de fuentes proporcionado.

2. Resuelve fichas/E10-analisis-estatico.md: vincula cada hallazgo a permiso, fichero o llamada concreta.

3. Si usas MobSF, conserva versión, hash del APK e informe. Confirma a mano y descarta alertas sin evidencia.

4. Sigue la ficha de tráfico con los clientes y backend locales. Distingue HTTP, TLS con CA de laboratorio y fijación de certificado.

5. Compara el servidor de compras vulnerable y el seguro. Prueba importe, usuario, producto y repetición de la misma operación.

6. Entrega el informe diferenciando análisis de fuentes, simulación y ejecución Android: no presentes uno como prueba del otro.

## Cómo comprobar que está hecho

Cada hallazgo tiene ubicación; tráfico interpretado; compra validada en servidor.

> Un árbol de fuentes equivalente sirve para razonar, pero no acredita haber ejecutado un APK.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT6-seguridad-aplicaciones-moviles.md).
- [build-apk](laboratorio/app-laboratorio/build-apk.md)
- [E10-analisis-estatico](laboratorio/fichas/E10-analisis-estatico.md)
- [E11-trafico-compras](laboratorio/fichas/E11-trafico-compras.md)
- [LEER](laboratorio/mobsf/LEER.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
