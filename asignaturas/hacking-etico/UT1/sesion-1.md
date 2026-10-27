# Hacking Ético · UT1 · Sesión 1
## Marco ético-legal, fases de auditoría y MITRE ATT&CK

**Duración:** 4 horas. **Modalidad:** teoría aplicada, ejercicios individuales y en parejas. **Producto:** ficha de casos, mapa ATT&CK y reflexión final.

### Qué aprenderás
Al finalizar podrás distinguir una auditoría autorizada de una actuación fuera de alcance; reconocer conceptos de pentesting; describir las fases de una auditoría; relacionar tácticas con técnicas de MITRE ATT&CK; justificar las condiciones que deben recogerse en las reglas de enfrentamiento (ROE).

### Requisitos y normas
Necesitarás un navegador, un editor Markdown y acceso a la documentación pública de MITRE ATT&CK. No se realizará escaneo, ataque o consulta de información personal de terceros. Las acciones activas sobre infraestructura solo estarán permitidas después de que se apruebe por escrito el alcance del laboratorio. El uso de herramientas no implica autorización.

### Guía de la sesión
| Minutos | Actividad |
| --- | --- |
| 0–15 | Presentación del caso y objetivos. |
| 15–25 | Qué es UT1 y qué evidencia tendrás que entregar. |
| 25–45 | Diferencias entre pentest, hacking ético, equipo rojo y actividades no autorizadas. |
| 45–85 | Casos prácticos: identificar límites de autorización. |
| 85–115 | Marco jurídico español: acceso no autorizado, interceptación, daños y privacidad. |
| 115–135 | Descanso. |
| 135–155 | Confidencialidad, integridad, disponibilidad y autenticidad. |
| 155–205 | Fases de auditoría y mapeo ATT&CK. |
| 205–230 | Reglas del laboratorio y preparación de ROE. |
| 230–240 | Entrega y reflexión. |

### Conceptos esenciales
Una auditoría de seguridad necesita un **objetivo identificado**, un **titular que autoriza**, un **alcance escrito**, una **ventana temporal**, reglas de parada y un **informe final**. Reconocimiento y enumeración no son sinónimos: el primero busca información sobre el objetivo, mientras que el segundo obtiene detalles técnicos; ciertas formas de enumeración son activas y requieren autorización.

MITRE ATT&CK describe comportamientos adversarios. Una **táctica** explica el objetivo perseguido; una **técnica** explica cómo podría lograrse. Las fases de un pentest y las tácticas ATT&CK no se corresponden necesariamente una a una. No confundas una metodología de auditoría con una descripción del comportamiento de un adversario.

### Actividad 1 · ¿Dónde está el límite?
Para cada caso responde: (a) ¿hay autorización suficiente? (b) ¿se ha superado el alcance? (c) ¿qué riesgo hay? (d) ¿qué harías antes de continuar?
1. Un auditor autorizado para una aplicación descubre una segunda aplicación en el mismo servidor y decide probarla.
2. Un administrador te pide verbalmente que revises la Wi-Fi de una organización, sin documentar alcance ni fecha.
3. Encuentras accidentalmente datos personales durante una prueba autorizada. Un compañero propone adjuntarlos completos al informe.
4. Un alumno detecta un servidor que parece vulnerable fuera de la red de laboratorio y plantea escanearlo para practicar.

Escribe un párrafo que complete: «Una actividad de auditoría es aceptable cuando… y debe detenerse cuando…».

### Actividad 2 · Seguridad e impacto
Construye una tabla con columnas `situación | confidencialidad | integridad | disponibilidad | autenticidad | justificación`. Añade cuatro situaciones ficticias: fuga de información, modificación no autorizada de un registro, interrupción de servicio y suplantación de identidad. Razona los impactos; puede haber varios por situación.

### Actividad 3 · MITRE ATT&CK
1. Accede a la documentación oficial: https://attack.mitre.org/ y al Navigator: https://mitre-attack.github.io/attack-navigator/.
2. Crea una capa o tabla con las fases **reconocimiento, enumeración, análisis, explotación, post-explotación e informe**.
3. Para cada fase identifica, cuando exista correspondencia, una táctica ATT&CK, su identificador y una técnica con identificador. Justifica las fases sin correspondencia directa.
4. Explica por qué el informe final es imprescindible y por qué no equivale a una táctica adversaria.
5. Exporta la capa o guarda la tabla como `mapeo-attack.md`.

### Actividad 4 · Preparar el ROE de la siguiente sesión
Crea `borrador-roe.md` con: propietario del sistema ficticio, activos permitidos, sistemas excluidos, fechas, técnicas prohibidas, protección de evidencias, contacto de emergencia y criterio de parada. Este borrador **no concede autorización**.

### Entrega y comprobación
Entrega en tu repositorio de trabajo `casos.md`, `impacto.md`, `mapeo-attack.md` y `borrador-roe.md`. No subas datos personales ni evidencias sensibles. Comprueba que cada conclusión tenga una razón, que los identificadores ATT&CK existan y que quede claro cuándo hay que detener una prueba. En la siguiente sesión revisaremos y formalizaremos el ROE antes de cualquier actividad activa.

**Material de aula — José Picón.**
