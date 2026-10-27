# IC-E7 · Vigilancia OSINT del dominio — plantilla del entregable

> Rellena esta plantilla. Es el núcleo de `NN-IC-E7-osint.md`. Rúbrica **R1**
> (`~/xest-lab/2026-2027/docs/planificacion/rubricas.md`). Objeto de la vigilancia:
> la **organización** xest y su exposición, **no personas** (política de aula:
> `../../comun/legal/osint-aula-politica.md`). Reglas de oro del entregable:
>
> - Cada hallazgo lleva **fuente + fecha**.
> - Cada hallazgo se **contrasta con una segunda fuente** antes de elevarse a alerta.
> - Todo hallazgo termina en un **veredicto**: `ALERTA` o `DESCARTADO`, y el descartado
>   lleva **justificación**. Un cierre en blanco cuenta como error (igual que una alerta falsa).

## Registro de hallazgos

| # | Superficie | Hallazgo | Fuente 1 (fecha) | Segunda fuente / verificación (fecha) | Veredicto | Justificación / prioridad |
|---|---|---|---|---|---|---|
| 1 | Subdominios/certificados | | | | ALERTA / DESCARTADO | |
| 2 | Credenciales expuestas | | | | | |
| 3 | Typosquatting | | | | | |
| 4 | Menciones (foros/pastes) | | | | | |
| … | | | | | | |

**Superficies a cubrir** (todas): certificados y subdominios (`crt.sh`), credenciales
expuestas (HIBP / combolist), dominios similares (`dnstwist`), menciones en foros y pastes.

## Resumen ejecutivo (3-5 líneas)

Para dirección: cuántos hallazgos, cuántos elevados a alerta, el más grave y la acción
recomendada. Sin jerga.

## Anexo de descartes

Lista de lo descartado con la razón concreta (subdominio que ya no resuelve, homónimo sin
relación, mención de otra marca). Este anexo es lo que separa un informe profesional de un
volcado de herramienta.
