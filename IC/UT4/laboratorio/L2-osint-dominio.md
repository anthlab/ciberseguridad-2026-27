# Laboratorio L2 · Vigilancia OSINT del dominio (IC · UT4, Sesión 2)

> Ficha del alumnado. Objeto de la vigilancia: la **organización** xest y su exposición,
> **no personas** (política de aula: `../../comun/legal/osint-aula-politica.md`). Al terminar
> habrás producido el borrador de **IC-E7**. Un dato sin contrastar es un rumor, no una alerta.

## Objetivo

Vigilar cuatro superficies de exposición de `xest.local`, **contrastar cada hallazgo con una
segunda fuente** y cerrar cada uno con un veredicto: `ALERTA` o `DESCARTADO` (justificado).

## Materiales (capturas sintéticas, laboratorio offline)

- `datos/crt.sh-xest.local.json` — export tipo crt.sh (certificados/subdominios).
- `datos/dnstwist-xest.local.json` — export tipo dnstwist (dominios parecidos).
- `datos/filtracion-credenciales-xest.csv` — combolist/breach con credenciales.
- `datos/menciones-foros.txt` — menciones en foros, pastes y canales.
- Plantilla del entregable: `plantillas/IC-E7-registro-osint.md`.

> Nota: `crt.sh`, HIBP y `dnstwist` son servicios de Internet. La VLAN del aula está
> aislada, así que trabajamos sobre **estas capturas sintéticas**. Si la política del aula
> autoriza salida puntual, el profesor mostrará las herramientas reales contra un dominio
> propio; el ejercicio evaluable usa los ficheros de `datos/`.

## Parte A · Certificados y subdominios (20 min)

```bash
# subdominios únicos publicados en Certificate Transparency
jq -r '.[].name_value' datos/crt.sh-xest.local.json | sort -u
# ¿cuáles están cubiertos por un certificado VIGENTE a día de hoy?
jq -r --arg hoy "2026-11-09" '.[] | select(.not_after >= $hoy) | .common_name' \
  datos/crt.sh-xest.local.json | sort -u
```
**Preguntas**: ¿qué subdominios NO deberían estar expuestos? ¿alguno es un resto antiguo?

## Parte B · Typosquatting (15 min)

```bash
# dominios parecidos que están REGISTRADOS (tienen registro A), excluyendo el original
jq -r '.[] | select(.dns_a != null and .fuzzer != "original") | .domain' \
  datos/dnstwist-xest.local.json
```
Un dominio parecido registrado **no es phishing** hasta confirmar que aloja una copia del
portal. Ese es el paso de la Parte D.

## Parte C · Credenciales y menciones (20 min)

```bash
# credenciales del dominio corporativo (¡ojo con el ruido de otros dominios!)
grep -i '@xest.local' datos/filtracion-credenciales-xest.csv
# menciones: primero ingenuo (substring), luego con límite de palabra
grep -ic 'xest' datos/menciones-foros.txt
grep -iwE 'xest' datos/menciones-foros.txt | grep -v '^#'
```
**Pregunta clave**: ¿por qué el primer `grep` da más resultados? ¿cuáles son falsos positivos?

## Parte D · Contrastar y cerrar cada hallazgo (25 min)

Por cada hallazgo, aplica **segunda fuente** antes de elevar:

- Un subdominio: ¿resuelve todavía? `dig +short old-portal.xest.local @<DNS-lab>`
  (o `getent hosts`). Si no resuelve → candidato a descarte.
- Un typo: ¿aloja el clon del portal? Comprueba el contenido, no solo el 200:
  ```bash
  curl -s http://xest-soc.local/ | grep -i 'portal soc'   # HTTP 200 != existe el clon
  ```
- Una credencial: ¿el email corresponde a un empleado **actual**? Contrasta con el
  inventario/directorio. Una cuenta dada de baja se trata distinto (deshabilitar, no rotar).
- Una mención: ¿habla de xest o de otra marca homónima?

Rellena `plantillas/IC-E7-registro-osint.md`: una fila por hallazgo con fuente+fecha,
segunda fuente, **veredicto** y justificación. El anexo de descartes es obligatorio.

## Entrega

Borrador de `NN-IC-E7-osint.md`. Se pule como IC-E7 (rúbrica R1). Recuerda: un cierre en
blanco (hallazgo sin veredicto) cuenta como error, igual que una alerta falsa.
