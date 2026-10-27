# Matriz de priorización y triaje de alertas (IC · UT5)

Plantilla del entregable `IC-E8`. Convierte una alerta en una prioridad con criterio
reproducible: no depende de la intuición del analista de guardia.

---

## 1. Fórmula de prioridad

La prioridad combina tres factores, cada uno de 1 (bajo) a 3 (alto):

```
Prioridad = Criticidad_del_activo × Alcance × Confianza_en_la_detección
```

| Rango | Prioridad | Objetivo de atención |
|---|---|---|
| 18 – 27 | **P1 — Crítica** | Inmediata |
| 8 – 17 | **P2 — Alta** | < 1 h |
| 4 – 7 | **P3 — Media** | < 4 h |
| 1 – 3 | **P4 — Baja** | Registro / revisión diferida |

## 2. Definición de los factores

### Criticidad del activo
- **3**: sistema esencial, datos personales de categoría especial, dominio.
- **2**: sistema de negocio con datos personales ordinarios.
- **1**: sistema auxiliar, sin datos sensibles.

### Alcance
- **3**: múltiples sistemas o toda una red.
- **2**: un sistema completo.
- **1**: un único indicador aislado.

### Confianza en la detección
- **3**: regla de alta fidelidad, correlación de varias fuentes.
- **2**: regla razonable, una fuente.
- **1**: indicio débil, propenso a falso positivo.

## 3. Registro de triaje

| Alerta | Activo (1-3) | Alcance (1-3) | Confianza (1-3) | Prioridad | ¿Falso positivo? | Justificación | Analista |
|---|:--:|:--:|:--:|:--:|:--:|---|---|
| | | | | | | | |

## 4. Regla de oro

Todo cierre por **falso positivo** exige justificación escrita en la columna
correspondiente. Un cierre en blanco cuenta como error de triaje en la evaluación: en
un SOC real, es como se pierde el rastro de un incidente que sí era real.
