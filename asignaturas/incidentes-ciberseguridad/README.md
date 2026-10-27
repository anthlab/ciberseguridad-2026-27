# Incidentes de Ciberseguridad — Curso 2026-2027

**CIPFP Cheste · Sesiones de miércoles (4 horas) · 8 unidades / 80 horas**

Aprenderás a detectar, registrar, priorizar, investigar, contener y comunicar incidentes de seguridad mediante evidencias verificables y escenarios de laboratorio.

## Reglas del laboratorio

- Usa únicamente registros sintéticos o datos expresamente autorizados.
- No publiques credenciales, logs con datos personales, identificadores de clientes ni material forense real.
- Toda actuación debe quedar registrada con hora, responsable, justificación, evidencia y resultado.
- No conectes servicios deliberadamente vulnerables ni el SOC de clase a Internet.
- El despliegue de Wazuh, Suricata, TheHive, Cortex o MISP requiere una validación previa de recursos, autenticación y aislamiento. **No está certificado para el aula solo por aparecer aquí**.

## Itinerario de las unidades

| Unidad | Contenidos | Evidencia de aprendizaje |
| --- | --- | --- |
| UT1 | Gobierno, políticas y normativa | Auditoría documental y propuesta de mejoras |
| UT2 | Concienciación | Campaña y métricas de un simulacro autorizado |
| UT3 | SOC, Wazuh, Suricata, Sigma y ATT&CK | Regla de detección y evento observado |
| UT4 | Detección física y OSINT defensivo | Registro de alertas y procedimiento |
| UT5 | Triaje y contención | Ticket priorizado y decisiones justificadas |
| UT6 | Investigación y análisis forense | Cronología, hipótesis y cadena de custodia |
| UT7 | Respuesta, erradicación y recuperación | Playbook ejecutado en simulación |
| UT8 | Comunicación y notificación | Borrador de notificación y registro de tiempos |

## Práctica inicial: análisis de una política de seguridad

**Escenario:** una empresa ficticia dispone de una política de contraseñas, una política de copias de seguridad y un procedimiento de respuesta. El responsable solicita revisar si estos documentos son aplicables y cómo comprobar su cumplimiento.

1. Abre una carpeta de trabajo `ic/ut1` y crea `revision-politicas.md`.
2. Define una matriz con estas columnas: control, objetivo, evidencia esperada, riesgo de incumplimiento, prioridad y medida correctora.
3. Incluye al menos ocho controles: autenticación multifactor, privilegio mínimo, rotación de accesos, copias, restauración, registros, escalado de incidentes y protección de datos.
4. Clasifica los riesgos en alto, medio o bajo y **explica el criterio** para cada nivel.
5. Crea un procedimiento de cinco pasos para comunicar un incidente a la persona responsable.
6. Termina con una recomendación ejecutiva de entre 200 y 300 palabras.

**Entrega:** `revision-politicas.md` y `conclusion.md`, sin información real de terceros. Se valoran trazabilidad, claridad, razonamiento y utilidad de las acciones propuestas.

## Caso conjunto con Hacking Ético

HE genera eventos **solo en un entorno expresamente autorizado**; IC recibe logs o evidencias anonimizadas y documenta detección, análisis y recuperación. Es necesario planificar el desfase de clases: el evento del jueves podrá investigarse en IC el miércoles siguiente.

## Material de referencia de la asignatura

- [Guía oficial del módulo en Drive](https://docs.google.com/document/d/1rKWTmwklCHz6ErYjyzHoNfGDSMNcQ3-bDgFEhN_UnFs/edit)
- [Práctica 1: gobierno y análisis de políticas](https://docs.google.com/document/d/1WPByplcoJ8iyhoZI6ZzwYWnwKBKsd6qb2wNtI0wz4Cw/edit)
- [Manual del alumnado (revisión 12/10/2026)](https://drive.google.com/file/d/1Nj5Q5cixP00bab5y48MTDbG0WcBiDHBe/view)
- [Diapositivas del curso](https://drive.google.com/file/d/1vFquryv_UJd8ZmOLHtlv5pGZlRH_PufF/view)

**Importante:** comprueba los permisos de lectura de Drive antes de facilitar estos enlaces a la clase. Los laboratorios avanzados y la validez de los plazos normativos se revisarán antes de impartirse.

> Material de aula — José Picón.
