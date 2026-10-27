# HE UT8 · Ficha 01 (alumnado) — Recon, proxy y control de acceso

**Módulo** 5025 Hacking Ético · **UT8** (sesión 1 de 2) · **RA5 CE a, b, c, d**.
**Evidencia que alimenta**: HE-E15 (informe de auditoría web, I2/R2).
**Prerrequisito bloqueante**: ROE del curso firmado (HE-E1) · PPS UT4 y UT5 cerradas.

> **Reglas de aula**: todo en la **VLAN aislada** de xest; nunca la red del centro ni
> Internet; cada hallazgo se documenta con **petición + respuesta + captura** y marca de
> tiempo; actuar fuera de alcance = 0 (rúbrica R1, salida cero).

Objetivos (levantados con `docker compose up -d` en `comun/entornos/objetivos/`):

| Objetivo | URL |
|---|---|
| portal-soc | `http://portal-soc.xest.local:8080` |
| Juice Shop | `http://juice.xest.local:3000` |
| DVWA | `http://dvwa.xest.local:8081` (nivel low) |
| bWAPP | `http://bwapp.xest.local:8083` |

---

## §1 — Inventario y *fingerprinting* del portal (RA5.b)

Completa la tabla **sin usar todavía el proxy**, solo con `curl`. No modifiques nada.

```bash
curl -sI http://portal-soc.xest.local:8080/
curl -sI http://portal-soc.xest.local:8080/ | grep -iE 'strict-transport|content-security|x-content-type|referrer-policy|x-frame'
curl -s -X OPTIONS -i http://portal-soc.xest.local:8080/ | grep -i '^Allow'
curl -s -o /dev/null -w '%{http_code}\n' http://portal-soc.xest.local:8080/static/
```

| Comprobación | Resultado observado | ¿Hallazgo? (sí/no) | Sección WSTG |
|---|---|---|---|
| Versión del servidor (banner) | | | WSTG-INFO-02 |
| Cabecera `Strict-Transport-Security` | | | WSTG-CONF-07 |
| Cabecera `Content-Security-Policy` | | | WSTG-CLNT-* |
| Cabecera `X-Content-Type-Options` | | | WSTG-CONF |
| Métodos HTTP admitidos (`Allow`) | | | WSTG-CONF-06 |
| Listado de directorios en `/static/` | | | WSTG-CONF-04 |

**Pista honesta**: alguna comprobación saldrá *NO vulnerable* (p. ej. TRACE en nginx da 405).
Anótala igual: distinguir *comprobado y seguro* de *comprobado y vulnerable* es parte del rigor.

---

## §2 — Interceptar el flujo con proxy (RA5.a, c)

1. Arranca el proxy: `zaproxy &` (escucha en `127.0.0.1:8080`).
2. Configura el navegador de la Kali: proxy manual `127.0.0.1:8080` y acepta el **CA de ZAP**.
3. Registra un usuario en **Juice Shop** (`Account → Login → Not yet a customer?`), inicia
   sesión y **añade un producto a la cesta**.
4. Observa el árbol de peticiones en ZAP: ese es el **mapa de la aplicación**.

**Identifica el mecanismo de sesión** (responde en tu informe):

```bash
# En la consola del navegador (F12) sobre Juice Shop, tras iniciar sesión:
#   window.localStorage.getItem('token')
# Decodifica el payload del JWT (sin verificar firma):
echo 'PEGA_AQUI_EL_JWT' | cut -d. -f2 | base64 -d 2>/dev/null | jq .
```

- ¿La sesión es cookie o token? ¿Dónde se guarda? __________
- ¿Qué campos lleva el token (`id`, `role`, `iat`)? __________
- ¿El `id` parece **secuencial**? (pista para el §3) __________

---

## §3 — Examen manual WSTG I: control de acceso / IDOR (RA5.d) · RETO en parejas

Encuentra y **evidencia al menos DOS** fallos de control de acceso **distintos**. Cada uno
con la petición propia, la ajena y la respuesta que lo demuestra.

**A) IDOR de objeto — la cesta de Juice Shop**
```bash
TOKEN='PEGA_AQUI_TU_JWT'
# Tu cesta (usa el id que viste en el flujo, p.ej. 6):
curl -s http://juice.xest.local:3000/rest/basket/6 -H "Authorization: Bearer $TOKEN" | jq '.data.Products[].name'
# Prueba un id vecino (5, 4, ...):
curl -s http://juice.xest.local:3000/rest/basket/5 -H "Authorization: Bearer $TOKEN" | jq '.data'
```
¿Puedes leer una cesta que no es tuya? Documenta las dos peticiones.

**B) Control de acceso a nivel de función**
- Navega directamente a `http://juice.xest.local:3000/#/administration` **sin ser admin**.
- ¿Se te niega o accedes? Captura el resultado.

**C) DVWA (nivel low)** — elige un módulo de autorización (p. ej. salto por parámetro) y
evidencia el acceso indebido.

Rellena por cada hallazgo:

| Id | Hallazgo | Objetivo | Categoría WSTG | Petición propia / ajena | Impacto (1 frase) |
|---|---|---|---|---|---|
| H-a | | | WSTG-ATHZ-04 (IDOR) | | |
| H-b | | | WSTG-ATHZ-02 (función) | | |

---

## §4 — Registrar en la plantilla de informe (base de HE-E15)

Abre `HE/material/plantillas/informe-pentest.md` y traslada tus **dos hallazgos** a la ficha
de hallazgo detallado (H-01, H-02) con: categoría/TTP ATT&CK, evidencia reproducible,
impacto de negocio, remediación (CWE) y prioridad provisional. Se completará en la sesión 2.

## Checklist de salida (sesión 1)

- [ ] Tabla de fingerprinting del §1 completa (con al menos un "comprobado y seguro").
- [ ] Mecanismo de sesión identificado y JWT decodificado.
- [ ] **Dos** hallazgos de control de acceso evidenciados (petición propia + ajena + captura).
- [ ] Ambos volcados a la plantilla del informe.
