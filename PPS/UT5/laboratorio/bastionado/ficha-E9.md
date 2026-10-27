# Ficha de laboratorio · PPS-E9 — Bastionado del servidor con auditoría antes/después

**UT5 · RA3.f, RA3.g · Rúbrica R2 (informe técnico) · Instrumento I2**

> Entorno: **VLAN aislada de xest**. Objetivos levantados
> (`~/xest-lab/2026-2027/comun/entornos/objetivos → docker compose up -d`).
> Herramientas: `testssl.sh`, `lynis`, Docker. Regla de oro: nada fuera del
> laboratorio, nunca contra Internet ni la red del centro.

## Contexto

El portal SOC arranca con una configuración de nginx **deliberadamente floja**
(`objetivos/portal-soc/nginx.conf`): sin cabeceras de seguridad, revela la versión,
admite `TRACE`, lista directorios y no limita la tasa. Tu trabajo es bastionarlo y
**demostrar** la mejora midiéndola antes y después, no afirmándola.

## Material que se te entrega / reutilizas

| Recurso | Dónde |
|---|---|
| Config de partida (floja) | `comun/entornos/objetivos/portal-soc/nginx.conf` |
| Baseline endurecido de referencia | `proyectos/proyectofinal/PPS/material/baseline/nginx-hardening.conf` |
| Script de auditoría antes/después | `auditar.sh` (esta carpeta) |
| WAF ModSecurity + CRS | `docker-compose.waf.yml` + `modsec/tuning.conf` |

## Tareas

### Parte A — Auditar el "antes"

```bash
./auditar.sh antes https://portal-soc.xest.local
```
Guarda `evidencia/antes-tls.txt` y `evidencia/antes-lynis.txt`. Anota el
**Hardening index** de Lynis y las carencias TLS/cabeceras que detecta testssl.

### Parte B — Aplicar el baseline y auditar el "después"

1. Sustituye la config floja por el baseline endurecido (adaptando dominio,
   rutas y certificados). Repasa qué añade cada bloque: HSTS, CSP,
   `X-Content-Type-Options`, `Referrer-Policy`, TLS 1.2/1.3, `server_tokens off`,
   bloqueo de `TRACE`, `limit_req`.
2. Valida y recarga:
   ```bash
   sudo nginx -t && sudo systemctl reload nginx
   ```
3. Audita el "después" y genera el diff:
   ```bash
   ./auditar.sh despues https://portal-soc.xest.local
   ```
   `evidencia/diff-tls.txt` es tu prueba objetiva de la mejora.

### Parte C — WAF con OWASP CRS y ajuste de un falso positivo (RA3.g)

1. Levanta el WAF por delante del portal:
   ```bash
   docker compose -f docker-compose.waf.yml up -d
   docker logs -f portal-waf     # log de auditoría de ModSecurity
   ```
   Empieza en `DetectionOnly` (solo registra).
2. Genera tráfico legítimo que dispare un **falso positivo** (por ejemplo, un
   texto de formulario legítimo que contenga comillas o palabras como `select`) y localízalo en el log (regla que lo marca, parámetro, ruta).
3. **Ajusta la regla** de forma acotada (`modsec/tuning.conf`), no desactives el
   WAF. Documenta la exclusión y su justificación.
4. Pasa a bloqueo (`MODSEC_RULE_ENGINE=On`) y demuestra dos cosas: el tráfico
   legítimo ya pasa, y un ataque real (p. ej. `?q=1' OR '1'='1`) **sigue bloqueado**.

## Qué entregar (`NN-PPS-E9-bastionado.md`)

- `antes-tls.txt`, `despues-tls.txt`, `antes-lynis.txt`, `despues-lynis.txt` y
  `diff-tls.txt`.
- Informe R2: resumen ejecutivo + detalle técnico + trazabilidad
  carencia → cambio de config → evidencia de que se cerró.
- El ajuste del falso positivo del WAF con su justificación y la prueba de que el
  control sigue activo para ataques reales.
- Cita de la norma aplicable (**CCN-STIC 652**, CIS Benchmark nginx) explicando
  por qué aplica.

## Criterio de superación

La mejora del bastionado se **demuestra con el diff antes/después**, no se afirma.
El falso positivo del WAF se resuelve **afinando la regla**, nunca apagando el
control. Sin el "antes" guardado, el trabajo no es defendible.
