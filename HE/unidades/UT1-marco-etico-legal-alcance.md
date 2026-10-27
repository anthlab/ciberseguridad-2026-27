# HE · UT1 — Marco ético-legal y alcance del test de intrusión

**8 horas** · RA1 (a, b, c, d, e) · Servicio SOC: Protección — gobierno del ejercicio ofensivo · Evidencias `HE-E1`, `HE-E2`

---

## 1. Objetivo de la unidad

Antes de tocar una sola tecla contra un sistema, el auditor tiene que saber **qué puede hacer, con qué permiso y qué pasa si se pasa de la raya**. Esta unidad es la condición de acceso a todo lo demás del módulo: sin el documento de alcance y reglas de enfrentamiento firmado (`HE-E1`), no se ejecuta ninguna acción activa en el laboratorio.

## 2. Contenido

### 2.1 Terminología (RA1.a)

- **Hacking**: uso creativo de un sistema más allá de su diseño. No es delito por sí mismo.
- **Hacking ético / test de intrusión**: evaluación ofensiva **autorizada** y con alcance delimitado.
- **Equipo rojo**: emulación de un adversario real, con objetivos y sin avisar al equipo defensivo.
- **Hacktivismo**: acción no autorizada con motivación política. Es delito.

La diferencia entre auditor y delincuente no es la técnica: es la **autorización**.

### 2.2 Marco legal español (RA1.b)

| Artículo del Código Penal | Conducta |
|---|---|
| **197 bis** | Acceso no autorizado a un sistema de información |
| **197 ter** | Facilitar o interceptar sin autorización |
| **197 quinquies** | Cometido por organización criminal |
| **264** | Daños: borrar, alterar, suprimir datos ajenos |
| **264 bis** | Obstaculizar el funcionamiento de un sistema |

Marco complementario: **Convenio de Budapest** sobre la Ciberdelincuencia (BOE-A-2010-14221) y **RGPD** para cualquier dato personal capturado (arts. 5, 6, 32).

### 2.3 Alcance y reglas de enfrentamiento (RA1.c)

El documento de **Rules of Engagement (ROE)** define:

- Perímetro exacto: IPs, dominios, aplicaciones, cuentas de prueba.
- Ventana horaria y de calendario.
- Técnicas prohibidas (p. ej. denegación de servicio real, ingeniería social sobre plantilla no informada).
- Canal de comunicación y persona de contacto ante incidente colateral.
- Regla de parada (`stop-the-test`) y quién puede invocarla.
- Manejo de los datos capturados: cifrado y destrucción tras el informe.

### 2.4 Dimensiones de la seguridad (RA1.d)

Confidencialidad, integridad, disponibilidad y autenticidad. Cada hallazgo se clasifica por cuál de estas propiedades rompe.

### 2.5 Fases del ataque (RA1.e)

Reconocimiento → enumeración → análisis de vulnerabilidades → explotación → post-explotación → informe. Se corresponden con las tácticas de **MITRE ATT&CK**, que se usarán como taxonomía en todo el módulo.

## 3. Laboratorio guiado

### Parte A — Casos reales fuera de alcance (RA1.b)

1. Estudio de casos de auditorías que se salieron del alcance y sus consecuencias penales. Discusión: dónde estuvo la línea y qué la cruzó.

### Parte B — Redactar el ROE del curso (RA1.c)

2. Con la plantilla `HE/material/plantillas/ROE.md`, redacta el documento de alcance y reglas de enfrentamiento del ejercicio del curso (objetivo: el servicio desplegado por el módulo PPS). Fírmalo con la contraparte (rol docente).

### Parte C — Mapa de fases a ATT&CK (RA1.e)

3. Cotejar cada fase del ataque con las tácticas de ATT&CK correspondientes. Rellenar la hoja `HE/material/herramientas/mapa_attack.md`.

## 4. Entregables

- **`HE-E1`** (informe, rúbrica R2): documento de alcance y reglas de enfrentamiento firmado, con regla de parada y gestión de datos capturados.
- **`HE-E2`** (prueba objetiva, rúbrica de plantilla): marco legal, terminología y fases del ataque. Prueba escrita sin material de apoyo; la entrega el profesor en el aula.

## 5. Criterios de superación

- El ROE define perímetro, ventana, técnicas prohibidas, regla de parada y gestión de datos.
- El alumno distingue con precisión las conductas tipificadas en los artículos 197 bis/ter y 264/264 bis.

## 6. Advertencia

Ninguna técnica del módulo se ensaya sobre sistemas ajenos sin autorización expresa por escrito. Actuar fuera del alcance autorizado puede constituir delito y califica la práctica con 0, además de activar el protocolo de convivencia del centro.

## 7. Referencias

- Código Penal español, arts. 197 bis/ter/quinquies, 264, 264 bis.
- Convenio de Budapest (BOE-A-2010-14221).
- CCN-STIC 484 — Auditoría técnica de seguridad.
- MITRE ATT&CK — [attack.mitre.org](https://attack.mitre.org)
