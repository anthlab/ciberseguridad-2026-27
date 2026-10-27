# HE UT5 · Práctica 01 — Reconocimiento pasivo sobre objetivo consentido

**Módulo** 5025 Hacking Ético · **UT5** (8 h) · **RA3 CE a** — *"Se ha recopilado
información sobre la red y sistemas objetivo mediante técnicas pasivas"*.
**Evidencia** HE-E9 (informe, instrumento I2, 25 %).
**Prerrequisito bloqueante**: UT1 superada + consentimiento firmado
(`../../../comun/legal/consentimiento-autoosint.md`).

> HE-E10 (inventario por enumeración **activa**, I1) **no** se cubre aquí: la enumeración
> activa se hace sobre el objetivo institucional del laboratorio, no sobre una persona.
> Práctica 02.

## Elección de objetivo

| Opción | Objetivo | Requisito |
|---|---|---|
| **A** | Uno mismo | Consentimiento firmado (opción A del formulario) |
| **B** | Persona sintética `objetivo-sintetico/` | Ninguno — equivalente a efectos de nota |

Cualquier otro objetivo invalida la entrega: se califica 0 en el criterio de marco legal
y se repite con la opción B. Ver `../../../comun/legal/osint-aula-politica.md`.

## Sesión 1 (2 h) — Marco y superficie de partida

Recordatorio de UT1 aplicado a personas: qué significa "pasivo" cuando el objetivo es un
individuo (no hay ROE que firme un tercero; el único alcance válido es el propio),
diferencia dato público / dato libre de uso, y el mecanismo de **agregación**: se
construye en pizarra un perfil ficticio a partir de cinco datos inocuos y se cuenta qué
sale del ensamblado que no estaba en ninguna fuente.

Punto de partida del alumno: inventario de sus propios **identificadores** — nombres y
variantes, alias históricos (los de 2014 son los que más rinden), correos, teléfonos,
dominios propios, cuentas de repositorio.

## Sesión 2 (2 h) — Capas de recolección

Se ejecuta **por capas y citando la fuente de cada hallazgo**. Regla dura del módulo:
un resultado sin fuente citada y sin marca de tiempo no es un hallazgo, es un rumor.

| Capa | Técnica | Herramienta / fuente |
|---|---|---|
| Buscadores | Operadores avanzados sobre nombre, alias, teléfono, correo | `site:` `filetype:` `intext:` `inurl:` en Google/Bing/DuckDuckGo/Yandex |
| Histórico | Contenido borrado que sigue accesible | Wayback Machine, caché, `web.archive.org/cdx` |
| Identidad reutilizada | Un alias en N plataformas | `maigret`, `sherlock` (en el contenedor del lab) |
| Correo | Dónde está registrado ese correo | `holehe` — **solo sobre el correo propio** |
| Filtraciones | Aparición en volcados públicos | HIBP (API k-anonymity: se envían 5 caracteres del SHA-1, no la contraseña) |
| Metadatos | EXIF en fotos y documentos propios ya publicados | `exiftool` |
| Certificados / DNS | Si el objetivo tiene dominio propio | `crt.sh`, `dig`, DNS histórico |
| Repositorios | Correo real en cabeceras de commit, secretos en histórico | `git log --format='%ae'`, `trufflehog` sobre repo propio |
| Terceros | Registros públicos, boletines, tablones, listas de admitidos | BOE/DOGV, BORME si hay actividad económica |

**Prohibido en esta práctica**: cualquier intento de acceso (probar contraseñas, aunque
sean tuyas y aunque el servicio sea tuyo), ingeniería social sobre nadie, y contacto con
cualquier persona relacionada con el objetivo.

## Sesión 3 (2 h) — Análisis: de datos a perfil

No se entrega una lista de hallazgos: se entrega **qué se puede deducir del conjunto**.
Cada alumno construye, sobre su propio objetivo:

1. **Grafo de identidad**: nodos (alias, correo, teléfono, foto, dominio) y aristas
   (qué hallazgo une dos nodos y con qué fuerza). Formato NG: `nodes.csv` / `edges.csv`.
2. **Deducciones** con nivel de confianza: rutina, localización aproximada, entorno
   laboral/académico, tecnología que usa, red de contactos **sin nombrarlos**.
3. **Vectores** que ese perfil habilita: phishing dirigido creíble, respuesta a preguntas
   de recuperación, SIM swapping, suplantación.
4. **Falsos positivos**: al menos dos, con la razón por la que se descartaron. Aquí está
   el valor de trabajar sobre uno mismo: es el único caso con verdad terreno. Un
   homónimo, un perfil abandonado, un dato caducado.

## Sesión 4 (2 h) — Reducción de huella y cierre

Cada alumno **ejecuta** al menos tres medidas y documenta el resultado: borrado o cierre
de cuentas zombis, retirada de contenido de buscadores (derecho de supresión, art. 17
RGPD y formularios de retirada de Google), rotación de credenciales aparecidas en
filtraciones, activación de 2FA no-SMS, limpieza de EXIF, revisión de privacidad por
plataforma, cambio de correo de recuperación.

Cierre en común: **cuánto tardó cada uno en encontrar lo primero relevante**. El dato que
cambia la percepción del alumnado no es el hallazgo, es el tiempo. Y lectura del reverso:
esta misma capacidad, aplicada sin consentimiento a un tercero, es lo que se persigue
por acoso, descubrimiento y revelación de secretos (art. 197 CP) y sanciona la AEPD.

## Entregables

1. `NN-HE-E9-informe.md` — informe metodológico. **Sin datos personales concretos.**
2. `NN-HE-E9-grafo/{nodes,edges}.csv`.
3. `NN-HE-E9-reduccion.md` — las tres medidas ejecutadas y su verificación.

El anexo de hallazgos crudos **no se entrega** y no se almacena en el centro.

## Preparación del profesor (antes de la sesión 1)

- [ ] Sembrar la huella del objetivo sintético (`objetivo-sintetico/README.md`).
- [ ] Verificar `maigret`, `holehe`, `exiftool`, `trufflehog` en el contenedor del lab.
- [ ] Imprimir 20 consentimientos + 20 copias.
- [ ] Preparar el ejemplo de agregación de pizarra con datos inventados (nunca reales).
- [ ] Cuenta de correo desechable propia para las demos en vivo.
