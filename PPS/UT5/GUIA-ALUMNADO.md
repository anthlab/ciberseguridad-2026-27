# PPS · UT5 — Vulnerabilidades web II: credenciales, bastionado del servidor y contramedidas

**8 horas** · RA3 (e, f, g) · Servicio SOC: Prevención — configuración segura · Evidencias `PPS-E8`, `PPS-E9`

## Qué vamos a conseguir

Proteger credenciales y contrastar el bastionado del servicio.

## Antes de empezar

Herramientas: Python/Argon2id, nginx, curl; testssl.sh, Lynis y WAF en el entorno preparado.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Lee almacen-credenciales/ficha-E8.md y trabaja sobre una copia de usuarios.json.

2. Registra esquema antiguo y nuevo. Verifica que el alta nueva usa el esquema nuevo y que un acceso correcto migra el registro antiguo.

3. Comprueba acceso incorrecto, hash malformado y repetición de acceso. Justifica coste de Argon2id con una medición en tu equipo.

4. Lee bastionado/ficha-E9.md y guarda respuestas HTTP y auditoría inicial.

5. Valida sintaxis de nginx antes de aplicar el cambio. Configura TLS con certificados del laboratorio y conserva acceso al servicio.

6. Repite la misma batería de pruebas; si trabajas con WAF, incluye una petición legítima y otra de ataque para comprobar falsos positivos y eficacia.

## Cómo comprobar que está hecho

Migración verificable; nginx acepta la configuración; diferencia antes/después interpretada.

> Lynis revisa el sistema donde se ejecuta; no sustituye una auditoría remota de un sitio web.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT5-vulnerabilidades-web-ii-bastionado.md).
- [README](laboratorio/README.md)
- [ficha-E8](laboratorio/almacen-credenciales/ficha-E8.md)
- [ficha-E9](laboratorio/bastionado/ficha-E9.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
