# PPS · UT2 — Seguridad del lenguaje y del entorno de ejecución

**5 horas** · RA1 (e) · Servicio SOC: Prevención — configuración segura · Evidencia `PPS-E3`

## Qué vamos a conseguir

Elegir un lenguaje y demostrar cómo limita el entorno una operación.

## Antes de empezar

Herramientas: C, Go y Python; Docker y strace en Linux.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Compara los programas de memoria-segura y registra qué protección aporta cada lenguaje y qué riesgo queda en sus dependencias.

2. Resuelve cadena-suministro/FICHA-alumno.md como análisis documental. No instales los nombres sospechosos del fichero de ejemplo.

3. Completa el dictamen: amenaza, criterio, alternativa, decisión y coste operativo. No justifiques una elección solo por popularidad.

4. Abre seccomp/FICHA-seccomp.md. Usa exclusivamente los contenedores indicados y conserva el comando de referencia sin perfil.

5. Repite la misma operación con el perfil aplicado. Compara usuario, capacidades e imagen: deben mantenerse iguales para atribuir el cambio a seccomp.

6. Anota syscall, error y efecto. Cierra PPS-E3 con una prueba de bloqueo y una explicación de los límites del contenedor.

## Cómo comprobar que está hecho

Misma operación y privilegios en ambos ensayos; bloqueo atribuible al perfil; dictamen trazable.

> Ejecutar mount sin argumentos solo lista montajes; no demuestra el bloqueo de mount(2).

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT2-seguridad-lenguaje-entorno-ejecucion.md).
- [FICHA-alumno](laboratorio/cadena-suministro/FICHA-alumno.md)
- [PLANTILLA-dictamen](laboratorio/dictamen/PLANTILLA-dictamen.md)
- [README](laboratorio/memoria-segura/README.md)
- [FICHA-seccomp](laboratorio/seccomp/FICHA-seccomp.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
