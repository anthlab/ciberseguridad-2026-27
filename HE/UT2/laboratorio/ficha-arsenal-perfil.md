# Ficha de laboratorio · HE-E3 — Arsenal por perfil de organización

**Módulo**: HE 5025 · **UT2** · **RA1 g, i** · Instrumento I2 · Rúbrica **R2**
**Entrega**: `NN-HE-E3-arsenal.md`

---

## Contexto

No existe "el mejor arsenal": existe el arsenal **adecuado a la organización**. Lo que sirve
a una pyme de 12 personas no sirve a una entidad financiera, y a la administración pública le
condiciona la elección una norma que a la pyme no le aplica (el **ENS**).

Vas a construir un **cuadro comparativo** de herramientas de **monitorización** y de
**auditoría** para tres perfiles, y —esto es lo importante— **justificar cada elección**.
No vale una lista genérica de "nmap + nuclei para todos".

## Los tres perfiles

| Perfil | Rasgos que condicionan la elección |
|---|---|
| **Pyme** | Presupuesto bajo, sin equipo de seguridad dedicado, prioriza coste y sencillez. |
| **Administración pública (ENS)** | Obligada por el **Esquema Nacional de Seguridad**: trazabilidad, categorización, herramientas con soporte/certificación, cumplimiento CCN-STIC. |
| **Entidad financiera** | Criticidad máxima, 24/7, exigencias regulatorias (DORA/PCI-DSS), tolerancia a fallo mínima, presupuesto alto. |

## Tarea

Rellena, para cada perfil, al menos **una herramienta por fase** (recon, escaneo,
explotación/auditoría, monitorización/detección) y **una frase de criterio** por elección.
Apóyate en `../../recursos/arsenal-github.md` y en la tabla de arsenal por fase de la unidad.

Plantilla mínima (amplíala):

```markdown
## Pyme
| Fase | Herramienta | Criterio (por qué ESTA para ESTE perfil) |
|---|---|---|
| Escaneo de vulnerabilidades | ... | ... |
| Monitorización | ... | ... |
| ...
```

Repite el bloque para **Administración ENS** y **Entidad financiera**.

## Criterio de elección — dimensiones que DEBES tocar

- **Coste / licencia** (libre vs comercial): ¿lo puede pagar y mantener este perfil?
- **Cumplimiento**: ¿la administración necesita algo certificado / con soporte? ¿la
  financiera exige registro y retención de logs por normativa?
- **Criticidad y disponibilidad**: ¿el objetivo tolera un escaneo agresivo o hay que
  medir el ruido y programar ventanas?
- **Capacidad del equipo**: ¿hay analistas para operar una herramienta compleja o hace
  falta algo automatizado con GUI?

## Entregable

`NN-HE-E3-arsenal.md`: los tres cuadros + un párrafo de cierre que responda:
*"Si tuviera un único euro más, ¿en qué perfil y en qué herramienta lo gastaría, y por qué?"*

## Se te evalúa por (extracto R2)

- **Corrección técnica**: las herramientas existen, hacen lo que dices y encajan en la fase.
- **Fundamento normativo**: citas ENS/DORA/PCI cuando condiciona la elección, no de adorno.
- **Priorización del riesgo**: la elección responde al **perfil**, no es la misma lista tres veces.

Rúbrica completa: `~/xest-lab/2026-2027/docs/planificacion/rubricas.md` (R2).
