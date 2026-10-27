# Curso de Ciberseguridad 2026-2027

CE Ciberseguridad en Entornos de las Tecnologías de la Información · CIPFP Cheste
Prof. José Picón

**Web del curso: https://jmpicon.github.io/curso-ciberseguridad-2026-27/** (temario, prácticas y laboratorios descargables; también funciona sin Internet en el aula, ver [plataforma/](plataforma/README.md)).

Aquí tienes todo el material de mis tres módulos:

| Módulo | Código | Día | Material |
|---|---|---|---|
| Puesta en Producción Segura (PPS) | 5023 | Martes | [PPS/](PPS/) |
| Incidentes de Ciberseguridad (IC) | 5021 | Miércoles | [IC/](IC/) |
| Hacking Ético (HE) | 5025 | Jueves | [HE/](HE/) |

## Cómo está organizado

Cada módulo tiene dos partes:

1. `practicas/`: lo que usamos en clase cada semana (enunciados, diapositivas y laboratorios). Si dudas, empieza por aquí.
2. `UT1` … `UT8` y `unidades/`: el temario completo por unidad, con su guía, su laboratorio y sus fichas. Los entregables de cada módulo están en `evaluacion/entregables.md`.

En `comun/` tienes lo que sirve para los tres módulos: instalación del puesto, herramientas, plantilla de informe y los laboratorios (`comun/entornos/`). En `SOC/` están las reglas Sigma y los playbooks que usamos en IC.

El índice completo de unidades está en [INICIO.md](INICIO.md).

## Para empezar

```
git clone https://github.com/jmpicon/curso-ciberseguridad-2026-27.git
cd curso-ciberseguridad-2026-27
```

Cuando subamos material nuevo, actualiza tu copia con `git pull`.

Tu trabajo va en **tu propio repositorio**, no en este. No subas contraseñas, tokens, datos personales ni capturas con información de compañeros.

## Normas del laboratorio

- Todo lo ofensivo se hace contra los objetivos del laboratorio (`*.xest.local`) o contra lo que yo te indique en clase. Nada contra Internet, la red del centro ni equipos de otras personas.
- Los contenedores vulnerables se levantan en tu puesto y se paran al terminar. No publiques sus puertos.
- Antes de la práctica de OSINT de HE, lee la política y firma el consentimiento (`comun/legal/`).

## Formación complementaria

Cursos gratuitos que te recomiendo para casa: [comun/CURSOS-ONLINE.md](comun/CURSOS-ONLINE.md).

---

`legacy/cursopps/` es la plataforma de PPS del curso pasado. La dejo como consulta, pero este curso no la usamos.
