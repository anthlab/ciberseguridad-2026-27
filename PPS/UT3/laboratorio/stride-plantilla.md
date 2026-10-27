# Laboratorio UT3 · Parte B — Hoja de modelado STRIDE (alumnado)

> Plantilla del entregable **PPS-E5**. Recorre el DFD (`dfd-portal-soc.md`) elemento a
> elemento. Por cada amenaza STRIDE que aplique, anota **el control que la mitiga** y un
> **riesgo** = impacto × probabilidad. Entrega: `NN-PPS-E5-stride.md` + diagrama.

## Recordatorio STRIDE

| Letra | Amenaza | Propiedad que rompe | Pregunta guía |
|---|---|---|---|
| **S** | Suplantación (spoofing) | Autenticidad | ¿Puede alguien hacerse pasar por otro? |
| **T** | Manipulación (tampering) | Integridad | ¿Se puede alterar el dato en tránsito o en reposo? |
| **R** | Repudio (repudiation) | No repudio | ¿Puede negar que hizo una acción? |
| **I** | Fuga (information disclosure) | Confidencialidad | ¿Se puede leer un dato que no debería? |
| **D** | Denegación (denial of service) | Disponibilidad | ¿Se puede tumbar el servicio? |
| **E** | Elevación (elevation of privilege) | Autorización | ¿Puede ganar permisos que no le tocan? |

## Escala para la matriz de riesgo

- **Impacto**: Bajo (1) · Medio (2) · Alto (3).
- **Probabilidad**: Baja (1) · Media (2) · Alta (3).
- **Riesgo** = Impacto × Probabilidad (1-9). Prioriza de mayor a menor.

## Tabla STRIDE por elemento (rellénala)

| Elem. | Amenaza (STRIDE) | Descripción concreta en el portal | Control mitigador (requisito ASVS) | Imp. | Prob. | Riesgo |
|---|:--:|---|---|:--:|:--:|:--:|
| F1 | S | | | | | |
| F1 | T | | | | | |
| F1 | I | | | | | |
| P1 | T | | | | | |
| P1 | E | | | | | |
| P2 | S | | | | | |
| P2 | D | | | | | |
| D1 | I | | | | | |
| D1 | R | | | | | |
| … | … | | | | | |

## Matriz de riesgo (coloca cada amenaza por su id)

| ↑ Impacto \\ Prob. → | Baja (1) | Media (2) | Alta (3) |
|---|---|---|---|
| **Alto (3)** | | | |
| **Medio (2)** | | | |
| **Bajo (1)** | | | |

## Plan de trabajo (salida del modelado)

Lista las 3-5 amenazas de mayor riesgo. Cada una se convierte en un **requisito ASVS a
verificar** en UT4/UT5. El modelado no es un dibujo: es tu lista de tareas priorizada.

1.
2.
3.
