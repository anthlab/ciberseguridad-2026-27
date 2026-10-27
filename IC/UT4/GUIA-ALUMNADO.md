# IC · UT4 — Detección de incidentes de seguridad física e inteligencia de fuentes abiertas

**8 horas** · RA2 (c, d) · Servicio SOC: Detección — vigilancia y alerta temprana · Evidencias `IC-E6`, `IC-E7`

## Qué vamos a conseguir

Incorporar fuentes físicas y abiertas al proceso de detección.

## Antes de empezar

Herramientas: Logs sintéticos, Python/jq y Wazuh; capturas OSINT locales.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Lee L1-deteccion-fisica.md e inventaría sensores, activos y situaciones relevantes.

2. Reproduce el mensaje de laboratorio y comprueba campos extraídos antes de escribir la regla.

3. Valida una alarma y una situación legítima para reducir ruido.

4. Lee L2-osint-dominio.md y analiza las capturas proporcionadas con fecha y procedencia.

5. Contrasta cada supuesto indicador; distingue activo de la organización, homónimo y dato antiguo.

6. Completa las plantillas IC-E6 e IC-E7 indicando acción, responsable y criterio de cierre.

## Cómo comprobar que está hecho

Campos bien interpretados; alertas contrastadas; indicadores con contexto.

> Una mención de marca o coincidencia de dominio no es por sí sola evidencia de compromiso.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT4-deteccion-fisica-osint.md).
- [L1-deteccion-fisica](laboratorio/L1-deteccion-fisica.md)
- [L2-osint-dominio](laboratorio/L2-osint-dominio.md)
- [IC-E6-ruta-de-alerta](laboratorio/plantillas/IC-E6-ruta-de-alerta.md)
- [IC-E7-registro-osint](laboratorio/plantillas/IC-E7-registro-osint.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
