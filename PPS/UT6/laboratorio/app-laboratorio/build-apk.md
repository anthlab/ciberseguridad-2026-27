# Cómo obtener el APK de NotasXest (opcional)

La carpeta `app-laboratorio/` contiene las **fuentes** de la app vulnerable. Para analizarla
con MobSF hace falta un `.apk`. Hay dos caminos:

## Opción 1 (recomendada en aula) — no compilar

No necesitas el APK para dar la clase:

- **jadx/grep**: trabaja directamente sobre `../salida_jadx/`, que ya imita la salida de
  `jadx` (mismas fuentes + manifiesto). El `grep` de secretos funciona tal cual.
- **MobSF**: lee el informe pregrabado `../mobsf/informe-mobsf-ejemplo.json`, coherente con
  estas fuentes.

## Opción 2 — compilar el APK (si tienes Android SDK)

Estas fuentes están pensadas para dejarlas caer en un proyecto Android mínimo
(`minSdk 23`, `targetSdk 28`) y compilar en depuración:

```bash
# dentro de un proyecto Android que use estas fuentes y este AndroidManifest.xml
./gradlew assembleDebug
# el APK queda en app/build/outputs/apk/debug/app-debug.apk
```

Copia:
- `AndroidManifest.xml` → `app/src/main/AndroidManifest.xml`
- `java/com/xest/notaslab/*.java` → `app/src/main/java/com/xest/notaslab/`
- `res/xml/network_security_config.xml` → `app/src/main/res/xml/`

Sube el `app-debug.apk` resultante a MobSF. El APK firmado en depuración es suficiente para
el laboratorio (de hecho MobSF marcará la firma de depuración como hallazgo).

> El objetivo del ejercicio es **analizar**, no publicar. El APK de laboratorio no se
> distribuye fuera del aula.
