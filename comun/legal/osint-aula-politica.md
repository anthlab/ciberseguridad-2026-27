# Política de objetivos OSINT en el aula — HE UT5 · IC UT4

Documento de referencia del profesor. Se explica al alumnado en la primera sesión de
HE UT1 y se aplica sin excepción en todas las prácticas de reconocimiento.

## Regla

**Un objetivo es válido si, y solo si, cae en una de estas cuatro categorías.**

| # | Categoría | Ejemplos | Base |
|---|---|---|---|
| 1 | **Uno mismo** (auto-OSINT) | tu propio nombre, alias, correos, teléfono, fotos, repos | Consentimiento propio, revocable |
| 2 | **Persona jurídica pública** | empresa cotizada, administración, ONG, universidad | Datos de la organización, no de personas físicas; solo fuentes públicas y sin interacción con sus sistemas |
| 3 | **Objetivo sintético** del profesor | persona ficticia con huella sembrada en el laboratorio | No hay interesado real |
| 4 | **Entorno de práctica autorizado** | CTF, HTB/THM, plataformas con reglas de uso propias | Autorización del titular |

**Cualquier otro objetivo está fuera de alcance.** En particular y de forma expresa:

- ❌ **Compañeros de clase, profesorado o personal del centro.** Ni con "es para
  aprender", ni por parejas, ni de forma anónima, ni con consentimiento verbal entre
  alumnos. La asimetría del aula hace que ese consentimiento no sea libre.
- ❌ Familiares, ex-parejas, vecinos, "un amigo que ha dicho que le da igual".
- ❌ Personas físicas identificables ajenas a la práctica, incluso si son "famosillos"
  locales o perfiles públicos en redes.
- ❌ Menores, en cualquier categoría.

## Por qué esta regla existe (y se evalúa)

1. **RGPD / LO 3/2018.** Recopilar y agregar datos personales de fuentes abiertas es
   tratamiento. Que un dato sea público no lo hace libre de uso: hace falta base legal y
   finalidad. Un ejercicio de clase no la da sobre un tercero que no ha consentido.
2. **Doxing por agregación.** Diez datos individualmente inocuos (foto de perfil, gimnasio
   que etiqueta, matrícula en una foto, horario en Strava) componen un perfil que ninguna
   de las fuentes publicó. El daño no está en el dato: está en el ensamblado.
3. **Categorías especiales (art. 9).** En redes sociales aparecen salud, orientación
   sexual, religión y afiliación política sin que nadie los busque. Un perfilado de una
   persona real acaba, casi siempre, tocando art. 9. El alumnado no puede controlar eso a
   priori, y por tanto no puede asumir el riesgo.
4. **Es el contenido del módulo.** HE UT1 enseña que sin ROE firmado no se toca nada.
   Empezar el módulo violando esa regla enseña lo contrario de lo que evalúa.

## Aplicación al profesorado

La misma regla, con más fuerza. El profesor **no perfila a su alumnado**: la relación
docente es de autoridad y evaluación, y un dossier sobre un alumno construido por quien
le pone la nota no tiene ninguna finalidad legítima que lo justifique. Si en la
corrección de una entrega aparecen datos personales de terceros, se devuelve la entrega
para que los retire; no se archivan.

## Cómo se consigue el efecto didáctico sin cruzar la línea

El impacto de la primera clase de OSINT no viene de investigar a alguien: viene de que
**cada uno se vea a sí mismo**. El auto-OSINT (categoría 1) produce ese momento de "esto
está ahí fuera y yo no lo sabía", y además:

- El alumno es la verdad terreno: sabe qué es correcto, qué está desactualizado y qué es
  un falso positivo. Con un objetivo ajeno nadie puede corregir el error.
- Se puede actuar: la práctica termina con un plan de reducción de huella ejecutado.
- No genera un entregable que el centro no pueda custodiar.

Ver el guion en `../../HE/UT5/laboratorio/practica-01-autoosint.md`.
