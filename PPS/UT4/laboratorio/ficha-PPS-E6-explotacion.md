# Ficha PPS-E6 — Explotación web documentada (UT4 · RA3 a-d · I1/R1)

**Entrega:** `NN-PPS-E6-explotacion.md` (una ficha por familia). Instrumento I1, rúbrica **R1**.
**Entorno:** tu Kali, con los objetivos publicados solo en `127.0.0.1`. Objetivos: Juice Shop
(`http://juice.xest.local:3000`) y DVWA (`http://dvwa.xest.local:8081`, nivel `low`). Levántalos con
`docker compose -f comun/entornos/objetivos/docker-compose.yml up -d` y resuelve los nombres con
`comun/entornos/objetivos/hosts-puesto` (ver guía de instalación, apartado 8).

> Salida cero (R1): cualquier acción sobre un sistema fuera del alcance autorizado
> califica la práctica con 0. Solo Juice Shop / DVWA de la VLAN de aula.

## Qué tienes que hacer

Reproduce y **documenta con petición y captura** cuatro familias **distintas**. Cada ficha
debe permitir a un compañero repetir el ataque desde cero.

### 1. Inyección SQL — login (Juice Shop)
- Objetivo: entrar como el primer usuario sin conocer la contraseña.
- Carga a probar en el campo de correo: `' OR 1=1 --`
- Evidencia: la petición `POST /rest/user/login` y la respuesta con el token de sesión.

### 2. XSS — campo reflejado o almacenado (Juice Shop / DVWA)
- Objetivo: que el navegador **ejecute** tu marca en la página.
- Carga a probar: `<script>alert(document.domain)</script>` (o `<img src=x onerror=alert(1)>`).
- Evidencia: la URL/campo usado y la captura del `alert` disparado.

### 3. Fallo de gestión de sesión (DVWA / Juice Shop)
- Objetivo: demostrar **una** de estas: cookie de sesión sin `HttpOnly`/`Secure`, o
  identificador de sesión que **no cambia** tras iniciar sesión (fijación).
- Evidencia: captura del inspector de cookies (atributos) o de las cabeceras `Set-Cookie`
  antes y después del login mostrando el **mismo** identificador.

### 4. Control de acceso roto — IDOR (Juice Shop: cesta/pedidos)
- Objetivo: leer un recurso de **otro** usuario cambiando un identificador en la petición.
- Ejemplo: acceder a `api/Baskets/<otro_id>` o a un pedido ajeno alterando el `id` de la URL.
- Evidencia: petición con el `id` ajeno y la respuesta con datos que no son tuyos.

## Formato de cada ficha (usa la plantilla del repo)

Plantilla: `~/xest-lab/2026-2027/PPS/material/plantillas/informe-vulnerabilidad.md`.
Por familia: **descripción · evidencia de explotación (petición + captura) · impacto**.
La corrección y la prueba de regresión van en E7 (esta ficha solo explota y documenta).

## Se evalúa (R1, resumen)
- **Ejecución técnica**: las cuatro familias reproducidas de verdad, no descritas.
- **Evidencia y reproducibilidad**: petición + captura que permiten repetir desde cero.
- **Higiene operativa**: todo dentro de la VLAN; nada contra Internet ni la red del centro.
