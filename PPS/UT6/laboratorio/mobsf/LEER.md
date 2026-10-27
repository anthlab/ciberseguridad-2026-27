# MobSF en el laboratorio de UT6

## Con APK y contenedor (camino normal)

```bash
docker run --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf
# navegador -> http://localhost:8000 -> arrastrar el APK de NotasXest
```

Lee, en este orden, las secciones del informe:
1. **Security Score** y grado.
2. **Permissions**: filtra por `dangerous`.
3. **Manifest Analysis**: `debuggable`, `clear text traffic`, `allowBackup`, actividad
   exportada, `network_security_config`.
4. **Secrets** / **Code Analysis**: clave de API, contraseña incrustada, almacenamiento
   inseguro (`SharedPreferences`).

Cada hallazgo se **confirma a mano** con jadx/grep (ver ficha PPS-E10).

## Sin APK ni emulador (alternativa documentada en la unidad)

Usa `informe-mobsf-ejemplo.json` (este directorio): es un recorte coherente con
`app-laboratorio/`, con los mismos permisos, secretos y hallazgos. Sirve para que el
alumnado practique la **lectura e interpretación** del informe y la redacción de PPS-E10
aunque no haya dispositivo. La confirmación manual se hace igualmente sobre `salida_jadx/`.

```bash
python3 -m json.tool informe-mobsf-ejemplo.json | less
```
