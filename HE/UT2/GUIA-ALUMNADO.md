# HE · UT2 — Vulnerabilidades, tipos de ataque y arsenal de auditoría

**8 horas** · RA1 (f, g, h, i) · Servicio SOC: Prevención — gestión de vulnerabilidades · Evidencias `HE-E3`, `HE-E4`

## Qué vamos a conseguir

Priorizar vulnerabilidades y elegir herramientas con criterio.

## Antes de empezar

Herramientas: Lote CVE, priorizador, Nmap/Nuclei en laboratorio.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Abre ficha-priorizacion.md y registra la fecha del lote y de las fuentes de enriquecimiento.

2. Distingue identificador CVE, tipo CWE, gravedad CVSS, probabilidad EPSS y explotación conocida KEV.

3. Prioriza con exposición, criticidad y controles del activo. Justifica dos cambios respecto al orden por gravedad.

4. Completa ficha-arsenal-perfil.md: objetivo, entrada, salida, permisos y limitaciones de cada herramienta elegida.

5. Ejecuta ficha-escaneo-nuclei.md solo sobre el objetivo local autorizado y con plantillas preparadas.

6. Confirma manualmente un resultado y documenta un falso positivo o una limitación. Si no hay red, usa el lote fechado sin fingir una consulta actual.

## Cómo comprobar que está hecho

Fuentes fechadas; prioridad razonada; salida automática contrastada.

> Una puntuación alta no demuestra explotación, y una coincidencia de versión tampoco.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT2-vulnerabilidades-arsenal.md).
- [ficha-arsenal-perfil](laboratorio/ficha-arsenal-perfil.md)
- [ficha-escaneo-nuclei](laboratorio/ficha-escaneo-nuclei.md)
- [ficha-priorizacion](laboratorio/ficha-priorizacion.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
