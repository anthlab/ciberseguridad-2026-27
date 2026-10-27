# PPS · UT4 — Vulnerabilidades web I: entrada, inyección, sesión y control de acceso

**11 horas** · RA3 (a, b, c, d) · Servicio SOC: Prevención — gestión de vulnerabilidades · Evidencias `PPS-E6`, `PPS-E7`

---

## 1. Objetivo de la unidad

Es la unidad de mayor peso del módulo. Aquí se cierra el círculo del análisis: se **explota** cada familia de vulnerabilidad web en un laboratorio, se **corrige** en el código real del proyecto y se **prueba** que la corrección cierra el hueco y no reaparece. El criterio profesional que rige toda la unidad: una vulnerabilidad no está cerrada hasta que existe una prueba de regresión que fallaría si alguien la reintroduce.

## 2. Contenido

### 2.1 Validación de entrada (RA3.a)

- **Lista de permitidos** (allowlist) antes que lista de bloqueados: es más seguro definir lo válido que enumerar lo prohibido.
- **Canonicalización** antes de validar: normalizar codificación (URL, Unicode) para que `%2e%2e` y `..` se traten igual.
- **Codificación de salida** según el contexto (HTML, atributo, JavaScript, URL): la validación de entrada no sustituye a la codificación de salida.

### 2.2 Inyección (RA3.b)

| Tipo | Sink | Mitigación correcta |
|---|---|---|
| **SQLi** | Consulta a base de datos | Consultas parametrizadas (nunca concatenar) |
| **Inyección de comandos** | Shell del sistema | Evitar la shell; API con argumentos separados |
| **Inyección de plantilla (SSTI)** | Motor de plantillas | No renderizar entrada del usuario como plantilla |
| **XSS reflejado / almacenado / DOM** | Respuesta HTML / DOM | Codificación de salida + CSP |
| **LDAP / NoSQL** | Directorio / base documental | Parametrización específica del motor |

La inyección se produce cuando dato y código se mezclan en el mismo canal. La solución estructural es **separarlos** (parametrizar), no "limpiar" el dato.

### 2.3 Gestión de sesión (RA3.c)

- Cookies de sesión con `HttpOnly`, `Secure`, `SameSite`.
- Rotación del identificador de sesión tras autenticarse (evita fijación de sesión).
- Expiración por inactividad y absoluta.
- Protección **CSRF**: token sincronizador o `SameSite=Strict/Lax` + verificación de origen.

### 2.4 Control de acceso (RA3.d)

- Control **por rol** (RBAC) y verificación en **cada** petición, en el servidor.
- Fallo de autorización a nivel de objeto (IDOR): que el usuario A no pueda leer el recurso del usuario B cambiando un identificador en la URL.
- Denegar por defecto: sin permiso explícito, no hay acceso.

## 3. Laboratorio guiado

> Entorno: laboratorio deliberadamente vulnerable (OWASP Juice Shop o DVWA) para explotar, y el repositorio del proyecto para corregir. Semgrep para la revisión de código.

### Parte A — Explotar (RA3.a–d)

```bash
# Levantar OWASP Juice Shop en local
docker run --rm -p 3000:3000 bkimminich/juice-shop
# Navegar a http://localhost:3000
```

1. Reproduce y documenta, con captura y petición, al menos **cuatro familias distintas**: una inyección, un XSS, un fallo de sesión y un fallo de control de acceso (IDOR).

### Parte B — Revisar código (RA3.a, RA3.b)

```bash
python3 -m pip install semgrep
# Reglas de la comunidad orientadas a seguridad
semgrep --config p/owasp-top-ten --sarif -o semgrep.sarif .
semgrep --config p/security-audit .
```

2. Ejecuta Semgrep sobre el proyecto y **confirma manualmente** cada hallazgo: distingue el verdadero positivo del falso. Un hallazgo sin confirmar no es un hallazgo.

### Parte C — Corregir y probar (RA3.a–d)

3. Corrige cada vulnerabilidad confirmada en el código del proyecto:
   - SQLi → consulta parametrizada.
   - XSS → codificación de salida contextual.
   - Sesión → atributos de cookie y rotación.
   - IDOR → verificación de propiedad del objeto.
4. Escribe, por cada corrección, una **prueba de regresión** que falle contra el código vulnerable y pase contra el corregido.

```bash
python3 -m pytest tests/test_seguridad.py -v
```

## 4. Entregables

- **`PPS-E6`** (informe, rúbrica R2): informe vulnerabilidad→corrección→prueba para al menos cuatro familias, con evidencia de explotación y del cierre.
- **`PPS-E7`** (reto integrado, rúbrica R3): confirmaciones en el repositorio que cierran los hallazgos, cada una acompañada de su prueba de regresión, revisadas por un compañero.

## 5. Criterios de superación

- Cada familia se explota **y** se corrige sobre el código real, no solo se describe.
- Toda corrección lleva prueba de regresión que demuestra el ciclo completo.
- Los falsos positivos de Semgrep están identificados y descartados con justificación.

## 6. Errores frecuentes

- "Limpiar" la entrada en vez de parametrizar el sink: sigue habiendo inyección con la carga adecuada.
- Corregir el XSS validando la entrada y olvidar la codificación de salida.
- Dar por cerrado un IDOR ocultando el botón en la interfaz sin verificar la autorización en el servidor.
- Aceptar los hallazgos de Semgrep sin confirmarlos: se corrige lo que no es y se ignora lo que sí.

## 7. Referencias

- OWASP **WSTG 4.2** — secciones de validación de entrada, inyección, gestión de sesión y autorización.
- OWASP Cheat Sheets: Injection Prevention, XSS Prevention, Session Management, Access Control, CSRF Prevention.
- Semgrep — reglas `p/owasp-top-ten` y `p/security-audit`.
