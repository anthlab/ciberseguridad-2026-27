# Ficha PPS-E10 · Análisis estático de una app móvil (MobSF + jadx)

**UT6 · RA4 a,b,e · Instrumento I1 · Rúbrica R1 · Semana 13**
Entorno: VLAN de laboratorio de xest. App de laboratorio `NotasXest` (`app-laboratorio/`).
Herramientas: MobSF (contenedor), jadx, `grep`.

> Regla de aula: todo el análisis ocurre sobre el APK/fuentes de laboratorio, en la VLAN
> aislada. No se analiza ninguna app ajena sin autorización por escrito.

## Objetivo

Producir un informe de análisis **estático** de `NotasXest` que documente, con evidencia,
tres clases de hallazgo del OWASP MASTG y proponga su remediación:

1. **Permisos excesivos** (mínimo privilegio roto).
2. **Secretos incrustados** en el binario (claves, contraseñas, URLs internas).
3. **Almacenamiento inseguro** de datos sensibles.

Cada hallazgo de MobSF debe **confirmarse a mano** con jadx/`grep`. Un hallazgo que no
confirmas, no lo pones.

## Pasos

1. **MobSF.** Arranca el contenedor y sube el APK (o, si no hay APK/emulador, lee el informe
   pregrabado `mobsf/informe-mobsf-ejemplo.json`).
   ```bash
   docker run --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf
   # navegador -> http://localhost:8000 -> subir el APK
   ```
   Extrae del informe: puntuación, permisos peligrosos, secretos, hallazgos de manifiesto
   y de almacenamiento.

2. **Confirmar con jadx/grep.** Sobre las fuentes decompiladas (`salida_jadx/sources`, ya
   provista; o genera la tuya con `jadx -d salida_jadx <apk>`):
   ```bash
   grep -rniE "api[_-]?key|secret|password|https?://" salida_jadx/sources | head
   ```
   Localiza el fichero y la línea exacta de cada secreto y del almacenamiento inseguro.

3. **Permisos.** Abre `salida_jadx/resources/AndroidManifest.xml` y lista los permisos
   `dangerous`. Para cada uno, argumenta si una app de notas lo necesita.

## Entregable

`NN-PPS-E10-movil.md` siguiendo la plantilla del repo
(`PPS/material/plantillas/informe-vulnerabilidad.md`, adaptada a móvil):

- **Resumen**: tabla de hallazgos (permisos / secretos / almacenamiento) con severidad.
- **Por hallazgo**: descripción, **evidencia** (fichero:línea del grep o captura de MobSF),
  impacto y **remediación concreta** (p. ej. "mover a Android Keystore", "quitar READ_SMS").
- **Trazabilidad**: cada hallazgo de MobSF apunta a su confirmación manual.

## Se evalúa (R1)

Ejecución técnica, **evidencia y reproducibilidad** (comandos y salidas para repetirlo),
verificación (confirmaste el hallazgo con una segunda herramienta), higiene operativa
(trabajo en la VLAN) y tiempo. La ofuscación **no** cuenta como control: si el secreto sale
con jadx, es un secreto público.
