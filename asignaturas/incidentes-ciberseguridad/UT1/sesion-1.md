# Incidentes de Ciberseguridad · UT1 · Sesión 1
## Gobierno, estructura documental y políticas de seguridad

**Duración:** 4 horas. **Producto:** análisis de políticas y borrador de política del SOC de la empresa ficticia XEST.

### Objetivos
Distinguir políticas, normas, procedimientos y registros; identificar quién aprueba los controles; convertir requisitos genéricos en reglas verificables; justificar qué evidencia confirma el cumplimiento de cada norma.

### Escenario de partida
Son las 09:05 y una persona abre un adjunto sospechoso. A las 09:12 varios archivos dejan de estar disponibles. A las 09:20 aparecen alertas de conexiones inusuales. Responde por escrito: ¿quién declara el incidente?, ¿quién puede aislar el equipo?, ¿qué datos debes preservar?, ¿a quién se comunica?, ¿quién puede autorizar una interrupción del servicio? No hay una respuesta automática para cualquier organización: debes justificarla con las responsabilidades asignadas.

### Plan de clase
| Minutos | Actividad |
| --- | --- |
| 0–15 | Miniincidente y preguntas iniciales. |
| 15–30 | Gobierno y responsabilidad. |
| 30–60 | Aprobación y respaldo de la dirección. |
| 60–90 | Política, norma, procedimiento y registro. |
| 90–110 | Normas del puesto de trabajo. |
| 110–130 | Descanso. |
| 130–200 | Comparación de tres políticas ficticias. |
| 200–225 | Primer borrador de la política del SOC. |
| 225–235 | Relación con PPS y Hacking Ético. |
| 235–240 | Comprobación y cierre. |

### Conceptos esenciales
- **Política:** orientación y compromiso aprobados por la dirección.
- **Normativa:** reglas concretas que deben cumplirse.
- **Procedimiento:** pasos, roles y herramientas para cumplir una norma.
- **Registro:** evidencia fechada de que se ha ejecutado o comprobado una actividad.

Un control útil tiene responsable, alcance, criterio observable y evidencia. Compara siempre el contexto: el ENS (Real Decreto 311/2022) y la familia ISO/IEC 27000 no son intercambiables ni aplican automáticamente de la misma manera a todas las entidades.

### Actividad 1 · Clasifica y mejora
Clasifica estos enunciados como política, normativa, procedimiento o registro. Después reescribe los que no sean verificables:
1. «Nos tomamos muy en serio la ciberseguridad».
2. «El puesto se bloqueará al ausentarse su usuario».
3. «En el alta de personal, el responsable entregará instrucciones para activar MFA».
4. «Informe mensual de cuentas con MFA activado».
5. «Se harán copias de seguridad con frecuencia».

Para cada frase define: responsable, forma de comprobarla y periodicidad.

### Actividad 2 · Tres organizaciones, tres borradores de política
Analiza estos ejemplos **ficticios**, no documentos de organizaciones reales:
- **A: Ayuntamiento.** Documento aprobado y fechado por alcaldía, con responsables asignados, inventario, revisión anual y referencia al ENS.
- **B: Startup.** Documento que promete proteger datos y equipos, pero no identifica aprobador, responsables, calendario de revisión ni registros exigidos.
- **C: Industria.** Documento aprobado por dirección, con alcance definido, responsables de activos, revisión y evaluación de riesgos alineada con ISO/IEC 27001.

Crea `analisis-politicas.md` con una tabla de criterios: alcance, aprobación, roles, controles, revisión, evidencias y acciones de mejora. Evalúa los tres borradores. Tu conclusión debe justificar qué cambios harías antes de aprobarlos.

### Actividad 3 · Normas del aula
Escribe cinco normas aplicables al puesto de laboratorio (por ejemplo, bloqueo de pantalla, dispositivos extraíbles, autenticación, manejo de archivos, comunicación de alertas). Para cada una define cómo podría verificarse sin recopilar datos privados de compañeros.

### Actividad 4 · Proyecto IC-E1: política SOC de XEST
Empieza `politica-soc-xest.md` con este índice: 1. Objeto. 2. Alcance. 3. Aprobación. 4. Principios. 5. Estructura documental. 6. Roles y responsabilidades. 7. Revisión. 8. Cumplimiento. Redacta al menos los tres primeros apartados y un esquema de los demás. El caso es ficticio y no debe contener información de producción.

### Entrega
Sube `miniincidente.md`, `analisis-politicas.md`, `normas-aula.md` y `politica-soc-xest.md` a tu espacio de trabajo. Comprueba que cada decisión tenga responsable y que cada norma permita obtener evidencia. En la sesión 2 completaremos IC-E1 y realizaremos revisión cruzada de la política.

**Material de aula — José Picón.**
