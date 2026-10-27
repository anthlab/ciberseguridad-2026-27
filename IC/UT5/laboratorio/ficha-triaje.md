# Ficha del alumnado — Triaje cronometrado de la cola (IC-E8)

**Objetivo**: convertir 20 alertas en una cola priorizada con criterio reproducible y arrancar
el **procedimiento de triaje** del SOC de xest. Entrega asociada: **IC-E8** (rúbrica R2).

**Dataset**: `cola-alertas-lab.csv` (20 alertas, con falsos positivos mezclados).
**Matriz de referencia**: `IC/material/plantillas/matriz-triaje.md` del repo
(`Prioridad = Criticidad × Alcance × Confianza`, cada factor de 1 a 3).

---

## Parte A — Triaje con reloj (35 min)

Tienes **35 minutos** para clasificar las 20 alertas. Rellena una fila por alerta:

| ID | Criticidad (1-3) | Alcance (1-3) | Confianza (1-3) | Prioridad (P1-P4) | ¿Falso positivo? | Justificación (obligatoria si es FP) |
|----|:---:|:---:|:---:|:---:|:---:|---|
| A01 | | | | | | |
| … | | | | | | |
| A20 | | | | | | |

**Reglas duras**:
1. Cada cierre por **falso positivo** exige una frase de descarte por escrito. Un cierre en
   blanco cuenta como error de triaje (en un SOC real, así se pierde el rastro de un incidente).
2. No todo es "prioridad alta". Si no aplicas la matriz, no estás triando: estás adivinando.
3. Un **intento** rechazado no es lo mismo que un **éxito**. Léelo en el `resumen`.
4. Un indicador aislado sube de prioridad cuando **correlaciona** con otros de la misma cola.

## Parte B — Correlación (10 min)

Varias alertas cuentan **la misma historia**. Agrúpalas: ¿cuáles pertenecen a un mismo
incidente en curso? Dibuja la secuencia (hora → activo → acción). Esa cadena es el caso que
abrirás en la Sesión 2.

## Parte C — Procedimiento de triaje de xest (para IC-E8)

Redacta el procedimiento del SOC (1-2 páginas) con, al menos:

- **Flujo L1 → L2 → L3**: quién clasifica, quién investiga, quién escala.
- **La matriz** (criticidad × alcance × confianza) con los rangos P1-P4 y su objetivo de
  atención.
- **La regla de oro** del cierre justificado por falso positivo.
- **Criterio de escalado**: cuándo una alerta P1 se convierte en caso y avisa al coordinador
  (usa la matriz de escalado de `IC/material/csirt/manual-csirt.md`).

**Verifica tu recuento** antes de entregar (no te fíes de tu propia hoja):

```bash
# Total de alertas (debe ser 20 + cabecera = 21 líneas)
wc -l cola-alertas-lab.csv
# Reparto por fuente
awk -F, 'NR>1{print $3}' cola-alertas-lab.csv | sort | uniq -c
```

**Entrega**: `NN-IC-E8-triaje.md` (procedimiento + matriz + tu registro de las 20 alertas).
