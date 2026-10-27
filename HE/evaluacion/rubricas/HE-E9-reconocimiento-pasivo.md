# Rúbrica HE-E9 — Informe de reconocimiento pasivo

**RA3 CE a** · UT5 · Instrumento **I2** (informe técnico, 25 % del módulo según
`docs/planificacion/rubricas.md`) · Rúbrica base **R2**.

Recordatorio: **RA sin compensación**. Si RA3 queda por debajo de 5, el módulo no está
superado aunque el resto vaya sobrado (`calcular_nota.py`).

| Criterio | Peso | 0-4 (No superado) | 5-6 (Suficiente) | 7-8 (Notable) | 9-10 (Sobresaliente) |
|---|---|---|---|---|---|
| **Marco legal y alcance** | 25 % | Objetivo no autorizado, o interacción con el objetivo en una fase pasiva → **entrega inválida** | Objetivo válido y consentimiento en regla | Justifica por qué su objetivo es válido y qué haría ilegal la misma técnica | Identifica el punto exacto de la práctica donde se cruzaría la línea y qué control lo impide |
| **Método por capas** | 25 % | Búsquedas sueltas sin estructura | Cubre buscadores y redes | Cubre ≥6 de las capas de la tabla, en orden y sin solapes | Justifica el orden de las capas por coste/ruido y descarta capas con motivo |
| **Trazabilidad de la fuente** | 20 % | Hallazgos sin fuente | Fuente citada en la mayoría | Toda afirmación con fuente + marca de tiempo | Además distingue observación de inferencia y anota la caducidad del dato |
| **Análisis y agregación** | 15 % | Lista de datos sin conclusión | Deduce algo del conjunto | Grafo coherente + vectores de ataque derivados con confianza declarada | Demuestra que una conclusión del conjunto no estaba en ninguna fuente aislada |
| **Falsos positivos** | 10 % | Ninguno o no razonados | Identifica ≥1 | ≥2 con la razón del descarte | Explica qué característica del método los generó y cómo evitarlos |
| **Minimización en el entregable** | 5 % | Incluye datos personales concretos (propios o de terceros) | Sin datos de terceros | Informe legible sin ningún dato personal concreto | El informe demuestra el hallazgo sin revelarlo (referencia indirecta verificable) |

## Cortes automáticos

- Objetivo fuera de la política de aula → **0** en el criterio 1 y repetición con opción B.
- Datos personales de un **tercero** en el entregable → se devuelve sin calificar; se
  reevalúa tras la retirada, con el criterio 6 a 0.
- Ejecución de técnica **activa** contra un objetivo no autorizado → incidencia
  disciplinaria además de la calificación; es exactamente lo que UT1 prohíbe.

## Nota sobre la calificación de la opción A

La nota **no depende del volumen de huella encontrada**. Un alumno con huella mínima que
documenta impecablemente 12 búsquedas negativas y justifica por qué son negativas obtiene
más que uno que vuelca 40 hallazgos sin fuente. Ausencia verificada de resultado es un
resultado — la regla `count=0` del módulo: un cero solo vale si se demuestra que la
consulta funcionó.
