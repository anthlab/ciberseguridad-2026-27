# Laboratorio UT5 — Credenciales, bastionado y contramedidas

Dos bloques, uno por sesión de 4 h.

## `almacen-credenciales/` — PPS-E8 (sesión 1)

| Fichero | Qué es |
|---|---|
| `store.py` | Almacén de partida: SHA-256 sin sal. Es lo que tienes que migrar. |
| `usuarios.json` | Datos de prueba: 10 usuarios con hash SHA-256. |
| `crack_demo.py` | Demo del coste de romper SHA-256 frente a Argon2id. |
| `ficha-E8.md` | Enunciado. |

## `bastionado/` — PPS-E9 (sesión 2)

| Fichero | Qué es |
|---|---|
| `auditar.sh` | Auditoría antes/después (testssl + lynis) y comparación. |
| `docker-compose.waf.yml` | WAF ModSecurity + OWASP CRS delante del portal. |
| `modsec/tuning.conf` | Ejemplo de ajuste acotado de un falso positivo. |
| `ficha-E9.md` | Enunciado. |

La configuración floja de partida del portal está en `comun/entornos/objetivos/portal-soc/nginx.conf`.

> Todo el bloque de bastionado se ejecuta en la red aislada del laboratorio (`xest`). Nunca contra Internet ni contra la red del centro.
