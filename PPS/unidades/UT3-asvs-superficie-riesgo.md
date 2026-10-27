# PPS · UT3 — Nivel de verificación de seguridad: OWASP ASVS y superficie de riesgo

**8 horas** · RA2 (a, b, c, d) · Servicio SOC: Prevención — gestión de la exposición · Evidencias `PPS-E4`, `PPS-E5`

---

## 1. Objetivo de la unidad

Antes de corregir vulnerabilidades hay que decidir **cuánta seguridad necesita** la aplicación. No todo servicio requiere el mismo rigor: una web informativa no se verifica como un sistema de pago. Esta unidad enseña a asignar un nivel de verificación con un estándar reconocido (OWASP ASVS) y a modelar de dónde vendrá el ataque (STRIDE), de modo que el esfuerzo posterior sea proporcional al riesgo.

## 2. Contenido

### 2.1 OWASP ASVS — Application Security Verification Standard

ASVS define **qué** hay que verificar en una aplicación web, organizado en tres niveles:

| Nivel | Para qué aplicación | Ejemplo |
|---|---|---|
| **Nivel 1** | Toda aplicación; verificable desde fuera sin acceso al código | Web pública sin datos sensibles |
| **Nivel 2** | Aplicaciones con datos sensibles; la mayoría de las de negocio | Portal con cuentas de usuario, el SOC de xest |
| **Nivel 3** | Aplicaciones críticas (salud, finanzas, vidas) | Sistema de pago, historia clínica |

Cada nivel es un conjunto de **requisitos de verificación** numerados (V1 autenticación, V2 gestión de sesión, V3 control de acceso, V5 validación, etc.). El nivel asignado determina qué requisitos son de obligado cumplimiento.

### 2.2 OWASP Top Ten como catálogo de riesgo

El Top Ten (web y móvil) no es un estándar de verificación sino un **mapa de las categorías de riesgo más frecuentes**: control de acceso roto, fallos criptográficos, inyección, diseño inseguro, mala configuración, componentes vulnerables, fallos de identificación y autenticación, etc. Sirve para no dejarse ninguna familia fuera del modelado.

### 2.3 Modelado de amenazas con STRIDE

STRIDE clasifica las amenazas por lo que atacan:

| Letra | Amenaza | Propiedad que rompe |
|---|---|---|
| **S** | Spoofing (suplantación) | Autenticidad |
| **T** | Tampering (manipulación) | Integridad |
| **R** | Repudiation (repudio) | No repudio |
| **I** | Information disclosure (fuga) | Confidencialidad |
| **D** | Denial of service | Disponibilidad |
| **E** | Elevation of privilege | Autorización |

Se aplica sobre un **diagrama de flujo de datos**: por cada elemento (proceso, almacén, flujo, frontera de confianza) se pregunta qué amenaza STRIDE aplica y qué control lo mitiga.

## 3. Laboratorio guiado

> Entorno: portal del SOC de xest. Referencia: OWASP ASVS 4.0.3 (hoja de requisitos en `PPS/material/plantillas/checklist_asvs.md`).

### Parte A — Asignación de nivel ASVS (RA2.a, RA2.b, RA2.c)

1. Se presentan tres aplicaciones de perfil distinto (web informativa, portal con cuentas, pasarela de pago).
2. Asigna a cada una su nivel ASVS y **justifica** por qué, en función de los datos que trata y el impacto de un compromiso.
3. Para el portal del SOC (nivel 2), extrae de la hoja ASVS la **lista de requisitos aplicables** y trázala a las pruebas que los verificarán.

### Parte B — Modelado STRIDE (RA2.d)

4. Dibuja el diagrama de flujo de datos del portal del SOC: navegador, servidor de aplicación, base de datos, servicio de autenticación, y las fronteras de confianza entre ellos.
5. Por cada elemento y flujo, enumera las amenazas STRIDE que aplican y el control que las mitiga.
6. Prioriza las amenazas por impacto y probabilidad (matriz de riesgo).

## 4. Entregables

- **`PPS-E4`** (informe, rúbrica R2): dictamen de nivel ASVS de la aplicación del proyecto y catálogo de requisitos de verificación aplicables, trazados a pruebas.
- **`PPS-E5`** (laboratorio, rúbrica R1): modelo de amenazas STRIDE con diagrama de flujo de datos y riesgos priorizados.

## 5. Criterios de superación

- El nivel ASVS asignado se justifica por el dato y el impacto, no por defecto.
- El modelo STRIDE cubre todos los elementos del diagrama y cada amenaza tiene un control asociado.
- Los requisitos ASVS son trazables a las pruebas que los comprobarán en las unidades siguientes.

## 6. Errores frecuentes

- Asignar nivel 3 "por si acaso" a todo: infla el coste y diluye el foco.
- Modelar STRIDE sin diagrama de flujo: se olvidan las fronteras de confianza, que es donde está el riesgo.
- Confundir el Top Ten (categorías de riesgo) con ASVS (requisitos de verificación).

## 7. Referencias

- OWASP **ASVS 4.0.3** — [owasp.org/www-project-application-security-verification-standard](https://owasp.org/www-project-application-security-verification-standard/)
- OWASP **Top Ten** web y móvil.
- Microsoft **STRIDE** y OWASP Threat Modeling Cheat Sheet.
