# PPS · UT5 — Vulnerabilidades web II: credenciales, bastionado del servidor y contramedidas

**8 horas** · RA3 (e, f, g) · Servicio SOC: Prevención — configuración segura · Evidencias `PPS-E8`, `PPS-E9`

---

## 1. Objetivo de la unidad

La aplicación puede ser correcta y aun así el servicio ser inseguro por cómo se almacenan las contraseñas, cómo está configurado el servidor web y qué defensas hay contra automatización. Esta unidad cierra RA3 con el bastionado del servidor y las contramedidas, y exige la evidencia de auditoría **antes y después** que hace defendible el trabajo.

## 2. Contenido

### 2.1 Almacenamiento de contraseñas (RA3.e)

- Nunca en claro, nunca con hash rápido (MD5, SHA-1, SHA-256 a secas).
- Funciones de derivación con coste ajustable: **Argon2id** (preferida), bcrypt, scrypt.
- Sal única por usuario (la incluyen estas funciones) y parámetros de coste justificados por el hardware.

```python
# Ejemplo con argon2-cffi
from argon2 import PasswordHasher
ph = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=4)
hash_ = ph.hash("contraseña-del-usuario")   # almacenar hash_
ph.verify(hash_, "contraseña-del-usuario")  # verificar
```

### 2.2 Bastionado del servidor web (RA3.f)

- Cabeceras de seguridad: `Strict-Transport-Security`, `Content-Security-Policy`, `X-Content-Type-Options`, `Referrer-Policy`.
- TLS moderno: solo 1.2/1.3, suites fuertes, sin renegociación insegura.
- Ocultar versión, deshabilitar métodos innecesarios (`TRACE`), permisos mínimos de fichero.
- Referencia: **CCN-STIC 652** (Nginx), **CIS Benchmark** Nginx/Apache.

### 2.3 Contramedidas anti-automatización (RA3.g)

- **HSTS** para forzar HTTPS; **CSP** para contener XSS.
- Limitación de tasa (rate limiting) contra fuerza bruta y registro masivo.
- CAPTCHA / bloqueo progresivo tras intentos fallidos.
- WAF (ModSecurity + OWASP Core Rule Set) en modo aprendizaje primero, luego bloqueo, ajustando falsos positivos.

## 3. Laboratorio guiado

### Parte A — Migrar el almacén de contraseñas (RA3.e)

1. Sustituye el almacenamiento actual del proyecto por **Argon2id** con parámetros justificados.
2. Implementa la migración transparente: al validar con el esquema antiguo, re-hashea con el nuevo.

### Parte B — Bastionar Nginx y auditar antes/después (RA3.f)

```bash
# Auditoría ANTES
testssl.sh --quiet --color 0 https://staging.local > antes-tls.txt
sudo lynis audit system > antes-lynis.txt

# Aplicar la configuración endurecida (ver PPS/material/baseline/nginx-hardening.conf)
sudo nginx -t && sudo systemctl reload nginx

# Auditoría DESPUÉS
testssl.sh --quiet --color 0 https://staging.local > despues-tls.txt
sudo lynis audit system > despues-lynis.txt
diff antes-tls.txt despues-tls.txt
```

3. Aplica la baseline y demuestra la mejora con el diff de las auditorías.

### Parte C — WAF con OWASP CRS (RA3.f, RA3.g)

```bash
# ModSecurity + CRS en modo detección primero
# SecRuleEngine DetectionOnly  -> revisar log -> SecRuleEngine On
tail -f /var/log/modsec_audit.log
```

4. Despliega ModSecurity con CRS, provoca un falso positivo real con tráfico legítimo del proyecto y **ajusta la regla** en vez de desactivar el WAF. Documenta el ajuste.

## 4. Entregables

- **`PPS-E8`** (laboratorio, rúbrica R1): servidor web bastionado con evidencia de auditoría antes y después (testssl.sh + Lynis) y el diff que prueba la mejora.
- **`PPS-E9`** (reto integrado, rúbrica R3): configuración de WAF y contramedidas anti-automatización con justificación de cada regla y del ajuste del falso positivo.

## 5. Criterios de superación

- Las contraseñas se almacenan con Argon2id y parámetros justificados; hay migración transparente.
- La mejora del bastionado se **demuestra** con auditoría antes/después, no se afirma.
- El falso positivo del WAF se resuelve afinando la regla, no apagando el control.

## 6. Errores frecuentes

- Subir la iteración de bcrypt "a ojo" sin medir el coste real en el hardware de producción.
- Añadir cabeceras de seguridad y romper la aplicación por una CSP demasiado estricta sin fase de solo-informe.
- Desactivar el WAF al primer falso positivo en vez de ajustar la regla: se pierde el control entero por un caso.

## 7. Referencias

- OWASP Password Storage Cheat Sheet · `argon2-cffi`.
- **CCN-STIC 652** (Nginx) · CIS Benchmarks Nginx/Apache.
- OWASP ModSecurity **Core Rule Set** · testssl.sh · Lynis.
