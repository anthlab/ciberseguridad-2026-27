# Ficha PPS-E7 — Corrección estructural + regresión (UT4 · RA3 a-d · I3/R3)

**Entrega:** PR en el repo del proyecto que cierra las cuatro familias en `portal/app.py`
+ `tests/test_seguridad.py` con una prueba de regresión por familia + revisión de un
compañero. Instrumento I3, rúbrica **R3** (reto integrado).

> Regla del módulo: una vulnerabilidad **no está cerrada** hasta que existe una prueba de
> regresión que **falla** contra el código vulnerable y **pasa** contra el corregido.
> Si el test no falla contra el `app.py` de partida, no prueba nada: reescríbelo.

## Punto de partida

El fichero `portal/app.py` trae las cuatro familias. Antes de corregir, **confirma** cada
sink con Semgrep y con lectura manual entrada→sink (la de UT1):

```bash
python3 -m pip install semgrep
semgrep --config p/owasp-top-ten --config p/security-audit portal/app.py
```

Aviso importante: **Semgrep no encuentra las cuatro**. Marca el XSS reflejado y la cookie
insegura, pero **la SQLi del login y el IDOR de `/recurso` los tienes que encontrar tú**
leyendo el flujo entrada→sink. Un hallazgo sin confirmar no es un hallazgo, y una familia
que la herramienta no marca **sigue estando ahí**.

## Corrección — hazla ESTRUCTURAL, no cosmética

| Familia | Corrección correcta | Corrección FALSA (no vale) |
|---|---|---|
| **SQLi** | Consulta **parametrizada** (marcadores `?`) | «Limpiar» comillas de la entrada |
| **XSS** | **Codificar la salida** por contexto + CSP | Validar solo la entrada |
| **Sesión** | `HttpOnly`+`Secure`+`SameSite`+expiración y **rotar** el `sid` tras login | Cambiar el nombre de la cookie |
| **IDOR** | Verificar el **dueño** del objeto en cada petición; denegar por defecto | Ocultar el enlace en la interfaz |

## Pruebas de regresión (`tests/test_seguridad.py`)

Una por familia. Cada una debe **fallar** contra el `app.py` de partida y **pasar** tras tu
corrección. Guía de qué comprobar:

- **SQLi**: `POST /login` con `usuario=' OR '1'='1' -- ` debe devolver **401**, no autenticar.
- **XSS**: `GET /buscar?q=<script>...` — el cuerpo **no** contiene `<script>` crudo; sí `&lt;script&gt;`.
- **Sesión**: tras `POST /login`, la cabecera `Set-Cookie` contiene `HttpOnly` y `SameSite`,
  y el `sid` emitido **no** es el que traía el cliente (rotación).
- **IDOR**: con la sesión de Ana, `GET /recurso/102` (recurso de Bruno) devuelve **403**.

```bash
cd portal
python3 -m pytest tests/ -v      # objetivo: 4 passed contra tu código corregido
```

Comprobación del ciclo completo (hazla y déjala escrita en el PR): revierte **una** de tus
correcciones, corre la suite y enseña que su prueba **se pone en rojo**. Eso demuestra que
la prueba blinda de verdad.

## Se evalúa (R3, resumen)
- **Solución técnica**: corrección estructural, no parche cosmético; eliges y justificas.
- **Automatización y repetibilidad**: `pytest tests/` reproduce el cierre desde cero.
- **Trabajo en el repositorio**: confirmaciones atómicas (una por familia), revisadas por un par.
- **Integración**: este portal corregido es el objetivo que **HE UT8** auditará.
