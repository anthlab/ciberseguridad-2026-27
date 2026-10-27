# Ficha de laboratorio · HE-E4 — Priorización real de vulnerabilidades

**Módulo**: HE 5025 · **UT2** · **RA1 h, i** · Instrumento I1 · Rúbrica **R1**
**Entrega**: `NN-HE-E4-priorizado.csv` + `NN-HE-E4-justificacion.md`
**Entorno**: estación de aula (Kali). No requiere objetivos de red; solo la herramienta y el lote.

---

## Contexto

Te llega un lote de **30 vulnerabilidades** (CVE con su CVSS) de un inventario de xest. Tu
jefe de SOC te pide una cosa muy concreta: **el orden en que hay que parchear**, y que
justifiques por qué ese orden **no** es el del CVSS.

La regla de ordenación de este ejercicio es `KEV → EPSS → CVSS`; en un entorno real se añade contexto de activos, exposición y controles:

1. ¿Está en **KEV** (CISA)? → se explota **ya**. Prioridad máxima.
2. ¿**EPSS** alto? → probable que se explote en 30 días.
3. **CVSS** solo desempata la gravedad.

## Paso 1 — Enriquecer el lote

En el aula (VLAN aislada, sin Internet) usamos los snapshots locales de KEV y EPSS:

```bash
cd ~/xest-lab/2026-2027/HE/UT2/laboratorio     # o donde tengas el material
python3 prioriza.py --cve-list lote_cves.txt \
    --kev-file kev_snapshot.json --epss-file epss_snapshot.csv \
    --salida priorizado.csv
column -s, -t priorizado.csv | less -S
```

> Este script funciona exclusivamente con fuentes locales. No quites esos argumentos. Para una revisión actual, prepara nuevas fuentes, conserva su fecha y repite el análisis; los datos de este ejercicio son didácticos.

**Salida esperada** (primeras filas): la #1 es `CVE-2021-44228` (Log4Shell), y el bloque
de las que **están en KEV** ocupa los primeros puestos. Fíjate en dónde caen los CVSS 10.0
que **no** están en KEV.

## Paso 2 — Encontrar las discrepancias (esto es lo que se evalúa)

Compara mentalmente dos órdenes: el que da tu `priorizado.csv` y el que darías **solo por
CVSS descendente**. Localiza **3 CVE donde discrepan** y por cada uno escribe **una frase**
que explique por qué sube o baja. Pistas de lo que buscas:

- Una vulnerabilidad de **CVSS alto (7.x)** que queda **por delante** de otras de CVSS 9.8/10.0.
- Un **CVSS 10.0** que cae al final de la lista.
- Un CVE en KEV cuyo **contexto** (p. ej. requiere acceso local) matizarías con criterio propio.

Cada frase debe **nombrar la señal** que causa el movimiento (KEV presente, EPSS alto,
gravedad de desempate), no solo el número.

## Entregable

1. `NN-HE-E4-priorizado.csv` — la salida de la herramienta.
2. `NN-HE-E4-justificacion.md` — las **3 discrepancias** argumentadas (una frase cada una)
   + una conclusión de 2-3 líneas: *¿por qué CVSS solo no basta para priorizar?*

## Se te evalúa por (extracto R1)

- **Ejecución técnica**: obtienes la lista priorizada correcta y sabes explicar la clave de orden.
- **Verificación**: contrastas el orden real con el orden por CVSS y señalas dónde chocan.
- **Higiene**: nada ejecutado fuera de la VLAN; el CSV es reproducible desde cero.

Rúbrica completa: `~/xest-lab/2026-2027/docs/planificacion/rubricas.md` (R1).
