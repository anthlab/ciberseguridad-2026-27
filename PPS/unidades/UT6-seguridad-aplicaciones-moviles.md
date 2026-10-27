# PPS · UT6 — Seguridad en aplicaciones para dispositivos móviles

**9 horas** · RA4 (a, b, c, d, e) · Servicio SOC: Prevención — superficie móvil · Evidencias `PPS-E10`, `PPS-E11`

---

## 1. Objetivo de la unidad

La aplicación móvil corre en un dispositivo que no controlamos y puede ser desensamblada por su dueño. Esta unidad enseña a analizar sus riesgos propios —permisos, almacenamiento, firma, tráfico, secretos en el binario— con la metodología OWASP MASTG.

## 2. Contenido

### 2.1 Modelos de permisos (RA4.a)

- **Android**: permisos declarados en el manifiesto, concedidos en tiempo de ejecución; llamadas al sistema protegidas.
- **iOS**: permisos por capacidad, consentimiento explícito del usuario.
- Principio de mínimo privilegio: una app que pide más permisos de los que necesita es un riesgo y una señal.

### 2.2 Almacenamiento seguro (RA4.b)

- Datos sensibles en el almacén protegido del sistema: **Android Keystore**, **iOS Keychain**.
- Cifrado de bases de datos locales (SQLCipher) y no dejar secretos en `SharedPreferences`/`plist` en claro.

### 2.3 Firma y validación de compras (RA4.c)

- Firma de la aplicación: garantiza origen e integridad; verificarla en la distribución.
- **Validación de compras integradas en el servidor**, nunca solo en el cliente: el cliente es manipulable.

### 2.4 Tráfico y protocolos inseguros (RA4.d)

- Detección de HTTP en claro, TLS mal configurado, ausencia de fijación de certificado.
- Interceptación con proxy para ver qué envía realmente la app.

### 2.5 Fugas en el binario (RA4.e)

- Claves de API, URLs internas, credenciales incrustadas en el APK/IPA.
- Inspección estática del binario para encontrarlas.

## 3. Laboratorio guiado

> Entorno: APK de laboratorio (o app propia), MobSF, jadx y mitmproxy. Emulador o dispositivo de laboratorio; alternativa virtualizada documentada para quien no disponga de hardware.

### Parte A — Análisis estático con MobSF y jadx (RA4.a, RA4.b, RA4.e)

```bash
# MobSF en contenedor
docker run --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf
# Subir el APK por la interfaz web y revisar: permisos, secretos, almacenamiento

# Decompilar para inspección manual
jadx -d salida_jadx app-laboratorio.apk
grep -rniE "api[_-]?key|secret|password|https?://" salida_jadx/sources | head
```

1. Extrae del informe MobSF: permisos excesivos, secretos incrustados y almacenamiento inseguro. Confirma manualmente con jadx.

### Parte B — Interceptar el tráfico (RA4.d)

```bash
# Proxy de interceptación
mitmproxy --mode regular --listen-port 8080
# Configurar el proxy en el dispositivo/emulador e instalar el CA de mitmproxy
```

2. Captura el tráfico de la app y demuestra un protocolo inseguro (HTTP en claro o ausencia de fijación de certificado). Si la app fija el certificado, documenta el intento y el bloqueo.

### Parte C — Diseño de validación de compras (RA4.c)

3. Diseña el flujo de validación de una compra integrada **contra servidor**, con firma verificable, y explica por qué la validación solo en cliente es insuficiente.

## 4. Entregables

- **`PPS-E10`** (informe, rúbrica R2): informe MASTG de la aplicación con hallazgos (permisos, secretos, almacenamiento) y remediación propuesta.
- **`PPS-E11`** (laboratorio, rúbrica R1): captura y análisis del tráfico con demostración del protocolo inseguro o del intento de interceptación bloqueado.

## 5. Criterios de superación

- Los hallazgos de MobSF se confirman manualmente con jadx.
- La interceptación se demuestra sobre tráfico real de la app.
- El diseño de validación de compras sitúa la comprobación en el servidor.

## 6. Errores frecuentes

- Confiar en la ofuscación del APK como si fuera cifrado.
- Validar la compra solo en el cliente.
- Guardar el token o la clave en almacenamiento no protegido del dispositivo.

## 7. Referencias

- OWASP **MASTG** y **MASVS**.
- OWASP Mobile Top Ten.
- MobSF, jadx, mitmproxy — documentación oficial.
