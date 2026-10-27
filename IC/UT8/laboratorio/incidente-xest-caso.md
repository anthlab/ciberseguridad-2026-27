# Caso del incidente de xest — briefing para notificación (IC UT8)

> Material de manos para el alumnado. Es el **mismo incidente** que HE provocó, IC detectó
> (UT3-UT5), investigó (UT6) y respondió (UT7). Ahora toca lo último del ciclo:
> **notificarlo en plazo**. Sobre este caso se construyen IC-E15 (árbol), IC-E16
> (notificaciones AEPD 72 h y NIS2 24 h) e IC-E17 (rueda de prensa).
>
> Datos **sintéticos**. Ninguna persona, dominio ni entidad es real.

---

## 1. La organización afectada

**xest, S.L.** — empresa privada que presta un servicio digital de gestión académica
(matrícula, expedientes, comunicación con familias) a una red de centros de formación.

- Sector: proveedor de servicios digitales de gestión (SaaS educativo).
- Tamaño: 62 empleados. Presta servicio a 18 centros y a sus usuarios.
- Datos que trata: identificativos y de contacto de alumnado y familias; **datos de salud**
  de una parte del alumnado (adaptaciones curriculares, informes médicos justificativos de
  faltas) → **categorías especiales, RGPD art. 9**.
- Marco propio: es empresa **privada** (no sector público → no le aplica el ENS) y **no es
  entidad financiera** (no le aplica DORA). Por su actividad y volumen, está clasificada como
  **entidad importante** en el ámbito de NIS2 (proveedor de servicios digitales).
- Delegado de Protección de Datos: sí, designado (dpd@xest.example).

## 2. Cronología del incidente (la que produce HE/IC)

| Momento | Hecho |
|---|---|
| **D-9, 03:14** | Compromiso inicial del servidor del portal vía vulnerabilidad web (la que explota HE). |
| **D-4** | Movimiento lateral. El atacante alcanza el servidor de base de datos. |
| **D-2, 02:40** | **Exfiltración**: copia de la base de datos de usuarios (identificativos, contacto y una tabla con datos de salud). |
| **D-1, 04:10** | Despliegue de **ransomware**: se cifran el portal y los ficheros compartidos. Nota de rescate. |
| **D-0, 08:05** | El SOC de xest **detecta** el cifrado y la nota de rescate. **Se declara el incidente.** |
| **D-0, 08:05** | ← **Este es el instante en que xest "tiene constancia".** Aquí arrancan TODOS los relojes. |

## 3. Alcance confirmado por la investigación (UT6)

- Registros exfiltrados: **4.230 usuarios** (alumnado y familias de los 18 centros).
- De ellos, **612 registros** contienen **datos de salud** (categoría especial art. 9).
- Parte del alumnado afectado es **menor de edad**.
- Servicios interrumpidos: portal de matrícula y comunicación con familias (servicio esencial
  de xest hacia sus clientes) → caído desde D-0.
- Origen: **acto ilícito** (intrusión + extorsión). Hay indicios de posible **impacto
  transfronterizo** (dos de los centros clientes operan sedes fuera de España).
- Vector raíz (de HE-E12 / IC-E11): vulnerabilidad en la aplicación web del portal.

## 4. Lo que la organización SÍ sabe a las pocas horas (D-0)

Que hubo intrusión, cifrado y **con alta probabilidad** exfiltración de datos personales,
incluidos datos de salud. No conoce aún el recuento exacto ni la lista nominal de afectados.

> Esto importa: a las 24 h y a las 72 h **no se tiene todo**. La notificación temprana se hace
> **con lo que se sabe**, marcada como preliminar, y se completa después. No notificar por
> "esperar a tenerlo todo" es incumplir el plazo.

## 5. Datos de contacto para las notificaciones (ficticios)

- Responsable del tratamiento: xest, S.L. · NIF B00000000 (ficticio).
- DPD: dpd@xest.example · +34 900 000 000.
- Persona de contacto del incidente (coordinador): coord-ir@xest.example.
- Sede AEPD (donde se presenta la de 72 h): sedeagpd.gob.es.
- CSIRT de referencia (NIS2, sector privado): **INCIBE-CERT**.

---

**Para el aula**: todo el trabajo de esta UT se hace sobre la plataforma del SOC
(`~/xest-lab/2026-2027/SOC/plataforma/`) y con las plantillas del repo. No se envía nada
a ninguna autoridad real: son **borradores de laboratorio**. Las direcciones `*.example` son
reservadas y no resuelven.
