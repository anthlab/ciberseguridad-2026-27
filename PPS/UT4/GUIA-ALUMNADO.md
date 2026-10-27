# PPS · UT4 — Vulnerabilidades web I: entrada, inyección, sesión y control de acceso

**11 horas** · RA3 (a, b, c, d) · Servicio SOC: Prevención — gestión de vulnerabilidades · Evidencias `PPS-E6`, `PPS-E7`

## Qué vamos a conseguir

Reproducir fallos web y corregir su causa con regresiones.

## Antes de empezar

Herramientas: Docker, navegador/proxy, Python, pytest; Semgrep como apoyo.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Prepara el laboratorio local y dos cuentas ficticias con permisos distintos. Anota aplicación y versión.

2. Sigue ficha-PPS-E6-explotacion.md. Para cada familia guarda petición, respuesta y efecto observado en el objetivo autorizado.

3. Abre portal/README-alumnado.md y localiza en el código el dato que llega a la operación sensible.

4. Escribe primero un test que falle ante el defecto. Corrige con consultas parametrizadas, escape contextual, gestión de sesión o autorización por objeto según corresponda.

5. Ejecuta tests positivos y negativos: un usuario autorizado debe poder trabajar y otro no debe acceder al mismo objeto.

6. Entrega PPS-E7 con el cambio, regresiones y comparación antes/después; separa la demostración sobre Juice Shop del código del portal que has corregido.

## Cómo comprobar que está hecho

Cuatro familias con evidencia; corrección estructural; permisos legítimos conservados.

> Que desaparezca una alerta del escáner no prueba que la vulnerabilidad esté corregida.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT4-vulnerabilidades-web-i.md).
- [ficha-PPS-E6-explotacion](laboratorio/ficha-PPS-E6-explotacion.md)
- [ficha-PPS-E7-correccion](laboratorio/ficha-PPS-E7-correccion.md)
- [README-alumnado](laboratorio/portal/README-alumnado.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
