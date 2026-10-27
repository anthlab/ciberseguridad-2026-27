# Consentimiento informado para el simulacro de phishing (IC UT2 · IC-E3)

> Documento que **debe existir y estar firmado ANTES** de lanzar cualquier campaña. En el
> aula, el simulacro se realiza sobre **buzones de laboratorio** (`*@xest.local`, capturados
> por MailHog) o sobre el propio grupo de prácticas con su consentimiento. **Nunca** sobre
> personas no informadas ajenas al ejercicio. Sin este documento, no se lanza.

## 1. Objeto y alcance
Ejercicio de concienciación consistente en el envío de un correo de phishing **simulado** a
un conjunto acotado de buzones, con el fin de **medir** (no de evaluar ni sancionar a
personas) la respuesta de la organización ante un intento de suplantación.

- **Buzones incluidos**: los del grupo `grupo-destinatarios-lab.csv` (dominio `xest.local`,
  entorno de laboratorio). Ningún buzón real de personas ajenas al ejercicio.
- **Entorno**: VLAN aislada del aula. El correo lo captura MailHog; **no sale a Internet**.
- **Periodo**: sesión de laboratorio de la semana 4.

## 2. Qué se mide y qué NO
- **Se mide**, de forma **agregada por segmento**: tasa de apertura, tasa de clic, tasa de
  envío de credenciales, **tasa de reporte** y **tiempo hasta el primer reporte**.
- **No se usa** para señalar, evaluar ni sancionar a personas concretas. El objetivo es
  mejorar el plan de concienciación, no elaborar una lista de "quién picó".

## 3. Principios (mensaje sin culpabilizar)
Quien reporta ayuda; quien pica no es el culpable del ataque. La métrica que más importa es
la de **reporte**, porque es la que permite **contener** el incidente.

## 4. Tratamiento de datos
Los datos se conservan solo mientras dure la práctica y se **anonimizan/agrupan** para el
informe (IC-E2/IC-E3). No se almacenan contraseñas reales de personas: en producción se
mide el envío, no la credencial.

## 5. Autorización
| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Responsable del ejercicio (docente = "dirección" de xest) | | | |
| Responsable del laboratorio | | | |

> Recordatorio de la unidad y de las reglas del aula: **sin firma no está firmado** y **sin
> autorización formal no hay nada** (mismo principio que el ROE de Hacking Ético).
