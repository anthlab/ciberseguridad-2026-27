# PPS-E3 · Dictamen de elección de lenguaje y entorno + evidencia de aislamiento

> Plantilla del entregable. Rúbrica **R2** (informe técnico). Entrega como `NN-PPS-E3-dictamen.md`
> (NN = tu número de lista) **más la captura** de la syscall bloqueada por seccomp.
> Rellena TODOS los apartados. Un dictamen sin criterios explícitos no supera el nivel 2.

---

## 1. Escenario

Servicio HTTP expuesto a Internet que **procesa ficheros subidos por el usuario** (por ejemplo,
recibe adjuntos, los parsea y extrae metadatos). Elige el lenguaje y el entorno de ejecución
para ese servicio entre **Go, Python y C**.

## 2. Criterios de evaluación (con peso)

Justifica el peso que das a cada criterio para ESTE escenario (procesar ficheros no confiables
inclina el peso hacia la seguridad de memoria y la superficie de dependencias).

| Criterio | Peso (%) | Por qué pesa lo que pesa aquí |
|---|---|---|
| Seguridad de memoria | | |
| Madurez del ecosistema de seguridad | | |
| Facilidad de despliegue aislado | | |
| Superficie de la cadena de suministro | | |
| (opcional) Rendimiento / otros | | |
| **Total** | **100** | |

## 3. Matriz de decisión

Puntúa cada lenguaje en cada criterio (1 = malo … 5 = excelente) y multiplica por el peso.

| Criterio (peso) | Go | Python | C |
|---|---|---|---|
| Seguridad de memoria ( %) | | | |
| Ecosistema de seguridad ( %) | | | |
| Despliegue aislado ( %) | | | |
| Cadena de suministro ( %) | | | |
| **Puntuación ponderada** | | | |

## 4. Recomendación

Un párrafo. Nombra el lenguaje elegido y **por qué gana según los criterios**, no por
familiaridad del equipo. Menciona explícitamente el criterio que ha sido decisivo.

## 5. Evidencia de aislamiento (seccomp)

Adjunta:

1. El **comando** con el que aplicaste el perfil `../perfil-restrictivo.json`.
2. La **salida** que demuestra que una syscall prohibida (`mount` vía `mount(2)`, o `ptrace`)
   es **rechazada** con `Operation not permitted`.
3. Una frase: **qué superficie** reduce ese perfil respecto al contenedor por defecto.

```text
(pega aquí tu comando y su salida — la captura de la syscall bloqueada)
```

## 6. Conclusión

Dos líneas: la elección de lenguaje contiene el daño *antes* de que ocurra (menos superficie);
el aislamiento lo contiene *cuando* ocurre (menos de lo que un proceso comprometido puede hacer).
