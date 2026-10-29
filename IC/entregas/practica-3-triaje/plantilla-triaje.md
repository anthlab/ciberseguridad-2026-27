# Triaje de alertas con Wazuh

**Alumno:** Anthony Zamora Martínez  
**Práctica:** 04/11/2026 · Incidentes de Ciberseguridad  
**Fecha real de ejecución:** 29/10/2026 · Trabajo individual

## Mi laboratorio y comprobación inicial

He reutilizado mi laboratorio del portfolio. En `anthwatch-wazuh` (192.168.56.103) tengo Wazuh 4.14.9 como servicios, en lugar del Docker del enunciado. He comprobado manager, indexer y dashboard: los tres estaban activos. Inicialmente el manager mostraba los dos agentes desconectados. Después comprobé `anthwatch-server` (192.168.56.102): el agente estaba activo, apuntaba a 192.168.56.103 y había iniciado FIM en tiempo real. La llegada posterior de las alertas confirma la comunicación durante las pruebas. No he necesitado usar `anthwatch-client`.

## Mis alertas reales

He conservado `mis-alertas.jsonl` tal como lo exporté: 124 alertas, incluidas otras anteriores y del manager. Al filtrar `anthwatch-server` desde las 17:09 UTC obtengo 32. Las horas de esta tabla son las de las alertas, no necesariamente el instante exacto del comando. La hora local es Europe/Madrid (+01:00).

| Hora UTC, 29/10 | Hora local | Agente | Regla | Nivel | Qué hice yo para provocarla | ¿Aparece? |
|---|---|---|---|---|---|---|
| 17:09:20.914 | 18:09:20.914 | anthwatch-server | 5503 | 5 | Introduje una contraseña incorrecta en sudo. | Sí |
| 17:09:28.922 | 18:09:28.922 | anthwatch-server | 5404 | 10 | Fallé tres veces al ejecutar sudo true. | Sí |
| 17:11:54.056 | 18:11:54.056 | anthwatch-server | 5901 | 8 | Creé ic-prueba; useradd creó también su grupo. | Sí |
| 17:11:54.056 | 18:11:54.056 | anthwatch-server | 5902 | 8 | Creé ic-prueba con -M y shell nologin. | Sí |
| 17:11:54.056 | 18:11:54.056 | anthwatch-server | 5903 | 3 | Borré ic-prueba con userdel. | Sí |
| 17:12:59.693 | 18:12:59.693 | anthwatch-server | 5901 | 8 | Creé ic-prueba; useradd creó también su grupo. | Sí |
| 17:12:59.693 | 18:12:59.693 | anthwatch-server | 5902 | 8 | Creé ic-prueba con -M y shell nologin. | Sí |
| 17:13:07.978 | 18:13:07.978 | anthwatch-server | 5903 | 3 | Borré ic-prueba con userdel. | Sí |
| 17:14:47.227 | 18:14:47.227 | anthwatch-server | 554 | 5 | Creé /opt/ic-lab/monitor/triaje.txt. | Sí |
| 17:15:02.329 | 18:15:02.329 | anthwatch-server | 550 | 7 | Añadí segunda línea a triaje.txt. | Sí |
| 17:15:20.251 | 18:15:20.251 | anthwatch-server | 553 | 7 | Borré triaje.txt. | Sí |

He repetido la creación y borrado del usuario: hay una secuencia sobre las 18:11:53 y otra entre las 18:12:59 y las 18:13:07. Los PID distintos y los registros useradd/userdel prueban dos ejecuciones; no las he contado como duplicados de indexación. Al terminar, `id ic-prueba` indicó que el usuario no existía.

En FIM he observado creación, modificación y borrado en tiempo real. El archivo pasó de 13 a 28 bytes al añadir la segunda línea. En las alertas también aparecen ejecuciones correctas de sudo y aperturas/cierres PAM, coherentes con los comandos de la prueba.

A las 18:15:20 (+01:00), 17:15:20 UTC, ejecuté `logger "IC-LAB triaje inicio $(hostname)"`. He comprobado el mensaje en journald, pero no una alerta correspondiente en el fichero recogido. No lo interpreto como prueba de que el manager lo recibiera ni de que no lo recibiera. Revisaría las fuentes del agente y probaría la línea con logtest. La ausencia de una regla aplicable puede explicar que un mensaje recogido no produzca alerta.

## Cola sintética

He analizado las 27 alertas inventadas del 02/11/2026, separadas de mis pruebas reales del 29/10. Sus timestamps llevan +0100: las horas siguientes son locales; para UTC resto una hora.

### Recuento por regla

| Regla | Cantidad |
|---|---|
| 550 | 2 |
| 554 | 1 |
| 2902 | 1 |
| 5401 | 1 |
| 5403 | 2 |
| 5710 | 7 |
| 5712 | 1 |
| 5715 | 1 |
| 5760 | 8 |
| 5763 | 1 |
| 40112 | 1 |
| 40501 | 1 |

Hay cuatro alertas de nivel 10 o superior. La IP 203.0.113.45 aparece en 17 alertas; 10.20.0.5 y 10.20.0.57 aparecen en una cada una. Ocho alertas no tienen data.srcip. He evitado descartarlas: incluyen sudo, creación de usuario y FIM. He observado tres eventos FIM: cambio de /usr/bin/openssl (03:00:41), alta de uploads/img.php (10:52:33) y cambio de index.php (10:53:10).

### Clasificación y prioridad por grupos

| Grupo | Horas locales | Agente | Reglas | Clasificación | Gravedad | Prioridad | Justificación |
|---|---|---|---|---|---|---|---|
| Secuencia SSH y actividad posterior (21 alertas) | 10:41:05–10:53:10 | srv-web01 | 5710, 5712, 5760, 5763, 40112, 5403, 40501, 554, 550 | Verdadero positivo para los intentos; sospecha fuerte de compromiso | Crítica | 1 | Misma IP en fallos y éxito de tecnico; después hay sudo bash como root, usuario soporte2 y cambios web. La atribución de todas las acciones a una sesión sigue pendiente. |
| Fallo SSH aislado (1) | 12:30:44 | pc-aula07 | 5760 | No concluyente | Baja con los datos disponibles | 2 | Fallo de alumno07 desde la IP del propio equipo; no veo repetición ni éxito posterior. No basta para afirmar ataque o error legítimo. |
| SSH con clave (1) | 11:15:00 | pc-aula07 | 5715 | Benigno esperado provisional | Baja | 3 | Acceso de profe con clave desde 10.20.0.5; confirmaría autorización y titularidad de la clave. Ser interno no garantiza legitimidad. |
| Sudo de mantenimiento (2) | 08:58:03–08:58:20 | pc-secretaria | 5401, 5403 | Benigno esperado provisional | Baja | 4 | marta falla una vez y 17 s después ejecuta apt update con igual usuario, terminal y directorio. Confirmaría que estaba autorizado. |
| Actualización de OpenSSL (2) | 03:00:12–03:00:41 | srv-web01 | 2902, 550 | Benigno esperado provisional | Baja | 5 | dpkg instala openssl y 29 s después cambia /usr/bin/openssl. Confirmaría la actualización y la integridad del paquete. |

La suma es 27 alertas. No he forzado una clasificación de falso positivo: una detección correcta de actividad legítima es benigna esperada. Las prioridades 3–5 son relativas y cambiarían si no se confirmase la autorización.

## Cronología del incidente principal

| Hora local (UTC) | Qué ocurre | Evidencia (regla y log) |
|---|---|---|
| 10:41:05–10:41:40 (09:41:05–09:41:40) | Se prueban admin, test, oracle, ubuntu, pi, git, postgres y user. | 5710 y 5712: Invalid user desde 203.0.113.45. |
| 10:43:10–10:43:52 (09:43:10–09:43:52) | Hay ocho fallos de contraseña de tecnico desde la misma IP. | 5760 y 5763: Failed password for tecnico. |
| 10:46:02 (09:46:02) | Se acepta la contraseña de tecnico. | 40112: Accepted password for tecnico from 203.0.113.45. |
| 10:47:15 (09:47:15) | tecnico ejecuta Bash con sudo como root. | 5403: USER=root; COMMAND=/usr/bin/bash; TTY=pts/0. |
| 10:48:01 (09:48:01) | Se crea soporte2 con shell /bin/bash. | 40501: useradd; UID=1002; from=/dev/pts/0. |
| 10:52:33 (09:52:33) | Aparece un PHP en uploads. | 554: /var/www/html/uploads/img.php added. |
| 10:53:10 (09:53:10) | Cambia la página principal. | 550: /var/www/html/index.php modified. |

**Lo que sé:** los registros muestran esos accesos, comandos y cambios. El propietario root que aparece en FIM no identifica por sí solo al proceso o a la persona que escribió el archivo.

**Lo que supongo:** podría tratarse de fuerza bruta con éxito, uso de privilegios, una cuenta para persistencia y cambios web maliciosos. No he demostrado una vulnerabilidad explotada, que img.php sea una webshell, una desfiguración web ni exfiltración. La continuidad temporal y pts/0 son indicios; pediría más trazabilidad para atribuir todas las acciones al mismo acceso.

## Siguientes comprobaciones que haría

1. Conservaría alertas y registros originales de SSH, sudo, useradd y FIM del intervalo. Pediría registros de sesión y procesos para relacionar tecnico, pts/0 y las acciones posteriores.
2. Consultaría al responsable si reconocía el acceso desde 203.0.113.45, el sudo de tecnico, el alta de soporte2 y los cambios web, y contrastaría las respuestas con cambios autorizados.
3. Solicitaría copias de img.php e index.php, metadatos, hashes, versiones previas y registros de acceso/error web. Buscaría peticiones a img.php y analizaría su contenido sin ejecutarlo.

No he realizado contención en el supuesto sintético.

## Ampliación: wazuh-logtest

He pegado las ocho líneas Failed password de tecnico y después Accepted password en una misma sesión de wazuh-logtest 4.14.9. Los siete primeros fallos dispararon 5760 (nivel 5), el octavo 5763 (nivel 10) y el éxito posterior 40112 (nivel 12). En una nueva sesión pegué solo Accepted password y obtuve 5715 (nivel 3).

Concluyo que el historial de eventos influye en la correlación. Esta reproducción introduce las líneas consecutivamente; no he reproducido con esperas los intervalos originales ni demostrado con esta prueba los límites temporales de la regla. Logtest simula el análisis: no equivale a generar accesos reales ni garantiza alertas nuevas en el Dashboard.

### Técnicas MITRE de las alertas más graves

| Técnica | Qué significa con mis palabras | Alcance en este caso |
|---|---|---|
| T1110, Brute Force | Probar credenciales reiteradamente. | Los intentos repetidos son compatibles con esta técnica. |
| T1078, Valid Accounts | Abusar de una cuenta que ya existe. | El éxito de tecnico tras los fallos hace sospechar ese abuso; debo confirmar autorización. |
| T1136, Create Account | Crear una cuenta para mantener acceso. | Sé que se creó soporte2; su finalidad de persistencia es una hipótesis. |
| T1068, Exploitation for Privilege Escalation | Explotar una vulnerabilidad para obtener más permisos. | Figura en la regla 40501, pero los logs no prueban explotación. |
| T1203, Exploitation for Client Execution | Explotar una aplicación cliente para ejecutar código. | Figura en la misma regla; no hay evidencia específica de esa técnica. |

Referencias oficiales consultadas: https://attack.mitre.org/techniques/T1110/ · https://attack.mitre.org/techniques/T1078/ · https://attack.mitre.org/techniques/T1136/ · https://attack.mitre.org/techniques/T1068/ · https://attack.mitre.org/techniques/T1203/
