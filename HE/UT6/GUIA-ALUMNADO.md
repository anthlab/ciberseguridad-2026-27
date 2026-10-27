# HE · UT6 — Interceptación, ataque de intermediario y explotación de sistemas

**9 horas** · RA3 (c, d, e) · Servicio SOC: Protección — validación empírica de controles · Evidencias `HE-E11`, `HE-E12`

## Qué vamos a conseguir

Demostrar un fallo de infraestructura y comprobar su contramedida.

## Antes de empezar

Herramientas: Docker/VMs del laboratorio, proxy de red, Metasploit y herramientas indicadas en las fichas.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Lee README-entorno-UT6.md. Identifica atacante, víctima, servicio, segmento y punto de captura.

2. Anota la comunicación de referencia antes de introducir el cambio experimental.

3. Sigue las fichas 01, 02 y 03 únicamente en el segmento de prácticas y con cuentas ficticias.

4. Relaciona cada efecto con una evidencia: petición, autenticación o sesión de laboratorio; no confundas un mensaje de éxito con control efectivo.

5. Aplica la contramedida de la ficha y repite la misma prueba para comparar.

6. Rellena plantilla-HE-E12-compromiso.md y entrega a IC el jueves un paquete con alcance, tiempos UTC, archivos y hashes para el miércoles siguiente.

## Cómo comprobar que está hecho

Efecto demostrado; control contrastado; transferencia reproducible a IC.

> Las prácticas MITM necesitan conectividad y topología específicas; publicar una web en localhost no reproduce ese segmento.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT6-interceptacion-mitm-explotacion.md).
- [ficha-01-mitm](laboratorio/ficha-01-mitm.md)
- [ficha-02-responder](laboratorio/ficha-02-responder.md)
- [ficha-03-explotacion](laboratorio/ficha-03-explotacion.md)
- [plantilla-HE-E12-compromiso](laboratorio/plantilla-HE-E12-compromiso.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
