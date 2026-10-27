# HE · UT7 — Post-explotación: credenciales, pivotaje y persistencia

**8 horas** · RA4 (a, b, c, d) · Servicio SOC: Protección — emulación de adversarios · Evidencias `HE-E13`, `HE-E14`

## Qué vamos a conseguir

Analizar credenciales y caminos de acceso, y cerrar el ejercicio sin residuos.

## Antes de empezar

Herramientas: Laboratorio de pivote, datos BloodHound y herramientas de credenciales previstas.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Parte solo del acceso de laboratorio que haya validado el profesor y registra permisos iniciales.

2. Completa ficha-E13-credenciales.md con datos sintéticos. Distingue contraseña, hash, respuesta de autenticación y token.

3. Lee bloodhound-demo/README.md; contrasta los caminos del grafo con permisos y servicios del entorno.

4. Sigue pivote-lab/README.md y ficha-E14-cadena.md, documentando cada cambio de contexto y límite del alcance.

5. Registra observables para IC y comprueba el efecto de la contramedida correspondiente.

6. Cierra sesiones y elimina únicamente los artefactos creados por el ejercicio siguiendo su inventario. Verifica que el acceso añadido ya no funciona.

## Cómo comprobar que está hecho

Contexto de acceso identificado; cada salto tiene evidencia; limpieza comprobada.

> Un camino dibujado por una herramienta es una hipótesis hasta comprobar sus condiciones.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT7-post-explotacion-persistencia.md).
- [README](laboratorio/bloodhound-demo/README.md)
- [ficha-E13-credenciales](laboratorio/ficha-E13-credenciales.md)
- [ficha-E14-cadena](laboratorio/ficha-E14-cadena.md)
- [README](laboratorio/pivote-lab/README.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
