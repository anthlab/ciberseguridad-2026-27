# Rúbricas de evaluación

Rúbricas comunes a **Puesta en producción segura (5023)**, **Hacking ético (5025)** e **Incidentes de ciberseguridad (5021)**. Cada evidencia declarada en `unidades_trabajo.json` (referencia del material de origen; consulta la guía de la unidad) se corrige con una de estas cuatro rúbricas, o con plantilla cerrada si el instrumento es una prueba objetiva (I5).

Escala común, sobre 10:

| Nivel | Rango | Lectura |
|---|---|---|
| **4 — Experto** | 9 – 10 | Entregable defendible ante un cliente o un tribunal sin retoques. |
| **3 — Competente** | 7 – 8,9 | Correcto y completo; detalles menores mejorables. |
| **2 — En desarrollo** | 5 – 6,9 | Cumple el mínimo profesional; faltan verificación, rigor o alcance. |
| **1 — Insuficiente** | 0 – 4,9 | No acredita el criterio de evaluación. |

Un criterio de evaluación se considera **superado a partir del nivel 2**. La nota de cada resultado de aprendizaje es la media ponderada de sus evidencias; **no se compensan resultados de aprendizaje entre sí**: con un RA por debajo de 5 el módulo no está superado.

---

## R1 — Práctica de laboratorio

| Criterio | Peso | 4 — Experto | 3 — Competente | 2 — En desarrollo | 1 — Insuficiente |
|---|---|---|---|---|---|
| **Ejecución técnica** | 30 % | Alcanza el objetivo y explica por qué funciona; resuelve los imprevistos sin ayuda. | Alcanza el objetivo con alguna consulta puntual. | Alcanza el objetivo con guía continua. | No alcanza el objetivo. |
| **Evidencia y reproducibilidad** | 25 % | Comandos, salidas, hashes y capturas permiten repetir el ejercicio desde cero. | Evidencia suficiente; falta algún paso intermedio. | Evidencia parcial: no se puede repetir sin preguntar. | Sin evidencia o evidencia no comprobable. |
| **Verificación del resultado** | 20 % | Comprueba el efecto en el destino y contrasta con una segunda fuente o medición. | Comprueba el efecto en el destino. | Da por bueno el resultado sin comprobarlo. | Reporta como correcto algo que no lo es. |
| **Higiene operativa** | 15 % | Alcance respetado, entorno restaurado, credenciales y datos gestionados con criterio. | Alcance respetado y entorno restaurado. | Restauración incompleta del entorno. | Actúa fuera de alcance o deja el laboratorio inservible. |
| **Autonomía y tiempo** | 10 % | Termina holgadamente y ayuda a documentar al grupo. | Termina en plazo. | Termina fuera de plazo. | No entrega. |

> Salida cero: cualquier acción sobre un sistema fuera del alcance autorizado califica la práctica con 0 y activa el protocolo de convivencia del centro.

---

## R2 — Informe técnico o entregable documental

| Criterio | Peso | 4 — Experto | 3 — Competente | 2 — En desarrollo | 1 — Insuficiente |
|---|---|---|---|---|---|
| **Corrección técnica** | 30 % | Sin errores; distingue lo verificado de lo inferido y lo declara. | Sin errores relevantes. | Errores menores que no invalidan la conclusión. | Errores que invalidan la conclusión. |
| **Estructura y trazabilidad** | 20 % | Resumen ejecutivo utilizable por dirección + detalle técnico + trazabilidad hallazgo→evidencia→remediación. | Estructura completa y coherente. | Estructura presente pero desequilibrada. | Sin estructura reconocible. |
| **Fundamento normativo y metodológico** | 20 % | Cita norma, guía o estándar aplicable y justifica por qué aplica **ese** y no otro. | Cita la referencia correcta. | Cita genérica sin conectar con el caso. | Ausente o incorrecta. |
| **Priorización del riesgo** | 20 % | Riesgo argumentado por impacto y explotabilidad real, no solo por puntuación automática. | Riesgo coherente y justificado. | Riesgo asignado sin justificar. | Riesgo ausente o arbitrario. |
| **Redacción y presentación** | 10 % | Precisa, sin relleno, apta para el destinatario declarado. | Clara y correcta. | Comprensible con esfuerzo. | Confusa o copiada sin criterio. |

---

## R3 — Reto integrado en el SOC de xest (aprendizaje basado en proyectos)

| Criterio | Peso | 4 — Experto | 3 — Competente | 2 — En desarrollo | 1 — Insuficiente |
|---|---|---|---|---|---|
| **Integración con el resto del SOC** | 25 % | Su pieza encaja con las de los demás módulos y lo demuestra funcionando end-to-end. | Su pieza encaja y está documentada. | Su pieza funciona aislada. | No integra. |
| **Solución técnica** | 25 % | Elige entre alternativas y justifica la elección con datos propios. | Solución correcta y justificada. | Solución correcta sin justificar. | Solución que no resuelve el reto. |
| **Automatización y repetibilidad** | 20 % | Reproducible desde cero con un comando o un procedimiento escrito y probado. | Reproducible siguiendo el procedimiento. | Reproducible solo por quien lo hizo. | No reproducible. |
| **Trabajo en el repositorio** | 15 % | Historial limpio, confirmaciones atómicas y descriptivas, revisión por pares aprovechada. | Historial correcto y comprensible. | Confirmaciones desordenadas. | Trabajo sin trazabilidad en el repositorio. |
| **Iteración sobre la retroalimentación** | 15 % | Incorpora la crítica recibida y demuestra la mejora medida. | Incorpora la crítica recibida. | Incorpora parte de la crítica. | Ignora la retroalimentación. |

---

## R4 — Defensa oral y demostración en vivo

| Criterio | Peso | 4 — Experto | 3 — Competente | 2 — En desarrollo | 1 — Insuficiente |
|---|---|---|---|---|---|
| **Dominio del contenido** | 30 % | Responde a repreguntas fuera del guion y reconoce los límites de lo que sabe. | Responde con solvencia a lo previsible. | Responde con apoyo del material. | No sostiene su propio trabajo. |
| **Demostración en vivo** | 25 % | Funciona y tiene plan B preparado. | Funciona. | Funciona con incidencias resueltas sobre la marcha. | No funciona y no hay alternativa. |
| **Adecuación al interlocutor** | 20 % | Traduce el impacto técnico a consecuencias de negocio sin perder rigor. | Adapta el registro al público. | Registro uniforme y técnico. | Ininteligible para el destinatario. |
| **Estructura y tiempo** | 15 % | Mensaje claro, cierre con recomendación accionable, dentro del tiempo. | Ordenada y en tiempo. | Se desvía o se excede. | Sin estructura ni control del tiempo. |
| **Ética profesional** | 10 % | Explicita alcance, autorización y limitaciones sin que se lo pregunten. | Los explicita al ser preguntado. | Los menciona de pasada. | Los omite o los tergiversa. |

---

## Instrumentos y su peso en la calificación del módulo

| Instrumento | Rúbrica | Peso orientativo sobre el módulo |
|---|---|---|
| **I3** — Reto integrado en el SOC de xest | R3 | 35 % |
| **I2** — Informe técnico o entregable documental | R2 | 25 % |
| **I1** — Práctica de laboratorio guiada | R1 | 20 % |
| **I4** — Defensa oral y demostración | R4 | 15 % |
| **I5** — Prueba objetiva de conocimiento | plantilla | 5 % |

El peso efectivo de cada instrumento en un resultado de aprendizaje concreto se deriva de las evidencias que lo acreditan; los porcentajes de la tabla son el reparto agregado del módulo, y su desviación real por RA se calcula a partir de `matriz_ce_ut.csv` (referencia del material de origen; consulta la guía de la unidad).

---

## Recuperación

- **Durante el curso**: toda evidencia calificada por debajo de 5 admite una entrega de mejora en un plazo de dos semanas, con la nota limitada a 7 salvo que la primera entrega no se hubiera podido realizar por causa justificada.
- **Al final del módulo**: se recuperan **resultados de aprendizaje completos**, no notas globales. El alumnado con un RA suspenso realiza una prueba práctica específica de ese RA, con la misma rúbrica.
- **Copia o suplantación**: la evidencia se califica con 0 y se recupera obligatoriamente en la convocatoria final, con defensa oral añadida.
