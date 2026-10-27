# Ficha de laboratorio · UT2 — Escaneo por plantillas con nuclei (refuerzo)

**Módulo**: HE 5025 · **UT2** · **RA1 g, i** · práctica de manos (no es evidencia calificable;
alimenta el criterio de HE-E3 y enlaza con UT8).
**Entorno**: **VLAN aislada de xest**. Objetivos del `docker-compose.yml` de
`comun/entornos/objetivos/`. **Nada fuera de la VLAN.**

---

## Por qué esta práctica

En la primera sesión priorizaste vulnerabilidades **en papel** (un lote de CVE). Ahora ves
de dónde salen esos hallazgos: un **escáner por plantillas**. `nuclei` no "adivina": lanza
firmas (YAML) contra un objetivo y reporta coincidencias. Es la herramienta de escaneo que
aparece en el arsenal de casi todos los perfiles — por eso la tocas hoy.

## Preparación (una vez, en la estación atacante)

```bash
# Kali suele traerlo; si no, o para tenerlo al día (recomendado):
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
export PATH="$PATH:$HOME/go/bin"
nuclei -version
nuclei -update-templates      # baja el repo de plantillas mantenido por la comunidad
```

Comprueba que los objetivos están arriba (los levanta el profesor):

```bash
docker compose -f ~/.../comun/entornos/objetivos/docker-compose.yml ps
curl -sI http://portal-soc.xest.local:8080/ | head -1   # espera: HTTP/1.1 200 OK
```

## Paso 1 — Detección de tecnología y cabeceras (sin ruido)

```bash
nuclei -u http://portal-soc.xest.local:8080 \
    -tags tech,misconfig -severity info,low,medium
```

**Qué esperas ver**: detección del **servidor (nginx)** y hallazgos de **cabeceras de
seguridad ausentes** (falta `Content-Security-Policy`, `X-Frame-Options`, `Strict-Transport-Security`).
El `portal-soc` arranca deliberadamente flojo: PPS lo endurece a lo largo del curso.

## Paso 2 — Escaneo sobre la app vulnerable moderna

```bash
nuclei -u http://juice.xest.local:3000 \
    -tags exposure,misconfig,tech -severity info,low,medium,high
```

**Qué esperas ver**: cabeceras faltantes, posibles rutas/archivos expuestos y fingerprint de
la aplicación (OWASP Juice Shop). No profundices hoy: Juice Shop es el objetivo grande de UT8.

## Paso 3 — Verificar a mano (esto es lo que separa un escáner de un auditor)

Coge **un** hallazgo del Paso 1 (p. ej. "falta X-Frame-Options") y **compruébalo tú**:

```bash
curl -sI http://portal-soc.xest.local:8080/ | grep -iE 'x-frame|content-security|strict-transport'
```

Si el `grep` no devuelve la cabecera, el hallazgo es **cierto**. Si nuclei dijera algo que el
`curl` desmiente, sería un **falso positivo**: en un informe, un hallazgo automático que no
verificas a mano **no existe**.

## Cierre (2 líneas en tu cuaderno)

- ¿Qué severidad reportó nuclei para las cabeceras faltantes y estás de acuerdo? ¿Subirías
  o bajarías el riesgo según **el activo** (un portal público vs. una API interna)?
- Enlaza con HE-E3: para una pyme, ¿nuclei libre es suficiente, o para banca pedirías un
  escáner con soporte? Justifícalo en una frase.

> Regla de aula: todo esto ocurre contra `*.xest.local` en la VLAN de laboratorio. Escanear
> cualquier otra cosa = **0 y protocolo de convivencia** (UT1).
