# HE · UT8 — Auditoría de aplicaciones web

**8 horas** · RA5 (a, b, c, d, e, f) · Servicio SOC: Protección — validación de la aplicación en producción · Evidencias `HE-E15`, `HE-E16`

## Qué vamos a conseguir

Auditar una aplicación con pruebas manuales y un informe defendible.

## Antes de empezar

Herramientas: Navegador, Burp/ZAP, curl, WSTG; escáneres de apoyo.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Comprueba que el servicio de PPS UT4–UT5 está disponible y registra su versión y alcance.

2. Sigue ficha-01-recon-flujo-wstg.md: observa el flujo con dos cuentas ficticias y permisos distintos.

3. Formula una hipótesis por hallazgo y captura petición, respuesta y efecto; conserva también un caso legítimo de control.

4. Usa ficha-02-automatizacion-verificacion.md para contrastar resultados automáticos. Las plantillas no amplían el alcance autorizado.

5. Prioriza impacto y probabilidad con contexto; propone la corrección y una prueba de cierre por hallazgo.

6. Entrega HE-E15 y prepara la defensa HE-E16 reproduciendo un caso desde cero. Un JWT decodificado no implica firma verificada ni vulnerabilidad.

## Cómo comprobar que está hecho

Evidencia reproducible; permisos y lógica revisados; corrección verificable.

> No supongas que cambiar a nivel high en DVWA elimina todos los fallos; verifica el código y la versión.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT8-auditoria-web.md).
- [ficha-01-recon-flujo-wstg](laboratorio/ficha-01-recon-flujo-wstg.md)
- [ficha-02-automatizacion-verificacion](laboratorio/ficha-02-automatizacion-verificacion.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
