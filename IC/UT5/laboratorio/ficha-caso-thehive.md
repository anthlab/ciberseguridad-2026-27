# Ficha del alumnado — Gestión del caso en TheHive (IC-E9, parte 1)

**Objetivo**: abrir y documentar en **TheHive** el caso del incidente de `portal-soc`, con
observables enriquecidos por **Cortex**, tareas, línea de tiempo y **TLP**. Rúbrica R3.

**Entrada**: `caso-incidente-he.md` (parte del incidente) y `observables-caso.csv` (IoC).
**Plataforma**: `~/xest-lab/2026-2027/SOC/plataforma/` (TheHive + Cortex ya desplegados).

---

## Paso 1 — Abrir el caso

TheHive → **New Case**. Rellena:
- **Título**: `Compromiso de portal-soc.xest.local — webshell + C2 + exfiltración`.
- **Severidad**: alta. **TLP**: `AMBER`. **PAP**: `AMBER`.
- **Descripción**: pega el resumen ejecutivo del parte (una frase) + los activos afectados.

## Paso 2 — Cargar los observables

Añade los observables de `observables-caso.csv` (`Observables → Add`). Marca como **IoC** los
que lo sean. Respeta el **TLP por observable** (la webshell y su hash van en `RED`; el C2 en
`AMBER`). Fíjate en por qué el hash y la IP no llevan el mismo semáforo.

## Paso 3 — Enriquecer con Cortex

Lanza los analizadores sobre los observables (`Run analyzers`):
- IP `185.220.101.47` → reputación (AbuseIPDB / GreyNoise).
- Hash de la webshell → VirusTotal / MISP.
- Dominio `update-cdn-xest.link` → reputación / DNS.

> **Aula sin salida a Internet**: los analizadores que consultan servicios externos no
> resolverán. Usa el analizador **MISP local** contra el conjunto de IoC precargado, o registra
> el veredicto esperado que te indique el profesor. Lo que se evalúa es que **enriquezcas y
> registres la fuente**, no que tengas línea a Internet.

## Paso 4 — Tareas y línea de tiempo

Crea las tareas del caso (una por fase): `Triaje`, `Contención`, `Preservación de evidencia`,
`Handoff a forense (UT6)`. En cada tarea añade un **log con hora** conforme avanzas: así se
construye la **timeline** del caso. Copia las horas del parte (08:12 → 09:47).

## Paso 5 — Exportar

Exporta el caso (JSON del caso + lista de observables) para adjuntarlo a la entrega.

**Entrega (parte 1)**: `export` del caso de TheHive + `NN-IC-E9-caso.md` con capturas de:
caso abierto, observables cargados con TLP, un analizador de Cortex ejecutado y la timeline.
La **parte 2** (contención) se documenta en `ficha-contencion.md`.
