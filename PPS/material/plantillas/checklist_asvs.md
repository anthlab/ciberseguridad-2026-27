# Checklist de verificación ASVS — Nivel 2 (PPS · UT3)

Extracto operativo de OWASP ASVS 4.0.3 para una aplicación de **nivel 2** (con datos
sensibles y cuentas de usuario, como el portal del SOC de xest). No sustituye al
estándar completo: es la hoja de trabajo para trazar cada requisito a la prueba que
lo verifica. Marca el estado y enlaza la evidencia.

Estados: ✅ cumple · ⚠️ parcial · ❌ no cumple · N/A no aplica

## V2 · Autenticación

| Req. | Verificación | Estado | Evidencia |
|---|---|:--:|---|
| 2.1.1 | Las contraseñas tienen al menos 12 caracteres | | |
| 2.1.7 | Se comprueba la contraseña contra listas de comprometidas | | |
| 2.2.1 | Hay defensa contra fuerza bruta (límite de tasa, bloqueo) | | |
| 2.4.1 | Las contraseñas se almacenan con función de derivación de coste (Argon2id/bcrypt) | | |

## V3 · Gestión de sesión

| Req. | Verificación | Estado | Evidencia |
|---|---|:--:|---|
| 3.2.1 | El identificador de sesión se regenera tras autenticarse | | |
| 3.2.3 | Las cookies de sesión llevan `HttpOnly`, `Secure`, `SameSite` | | |
| 3.3.1 | La sesión expira por inactividad y de forma absoluta | | |
| 3.4.1 | Hay protección CSRF en las operaciones que cambian estado | | |

## V4 · Control de acceso

| Req. | Verificación | Estado | Evidencia |
|---|---|:--:|---|
| 4.1.1 | El control de acceso se aplica en el servidor, en cada petición | | |
| 4.1.3 | Denegación por defecto: sin permiso explícito, no hay acceso | | |
| 4.2.1 | No hay acceso a objetos de otros usuarios cambiando un identificador (IDOR) | | |

## V5 · Validación, sanitización y codificación

| Req. | Verificación | Estado | Evidencia |
|---|---|:--:|---|
| 5.1.3 | Toda entrada se valida (allowlist) tras canonicalizar | | |
| 5.2.5 | Se evita la inyección de plantilla (no se renderiza entrada como plantilla) | | |
| 5.3.3 | La salida se codifica según el contexto (HTML, atributo, JS, URL) | | |
| 5.3.4 | Las consultas usan parametrización, nunca concatenación | | |

## V7 · Manejo de errores y registro

| Req. | Verificación | Estado | Evidencia |
|---|---|:--:|---|
| 7.1.1 | No se registran secretos ni datos personales innecesarios | | |
| 7.4.1 | Los errores no revelan detalles internos al usuario | | |

## V9 · Comunicaciones

| Req. | Verificación | Estado | Evidencia |
|---|---|:--:|---|
| 9.1.1 | Solo se usa TLS (1.2/1.3); no hay HTTP en claro | | |
| 9.1.2 | Se usan suites de cifrado fuertes | | |

## V14 · Configuración

| Req. | Verificación | Estado | Evidencia |
|---|---|:--:|---|
| 14.4.1 | Se envían las cabeceras de seguridad (HSTS, CSP, nosniff...) | | |
| 14.4.3 | Hay una Content-Security-Policy efectiva | | |
| 14.5.2 | Se rechazan métodos HTTP innecesarios | | |

---

**Nota de uso:** cada fila con estado ✅ debe enlazar a una prueba automática o a una
captura de auditoría (`PPS-E4` a `PPS-E9`). Un requisito marcado como cumplido sin
evidencia no cuenta como verificado.
