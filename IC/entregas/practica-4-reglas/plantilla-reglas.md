# IC 11/11 · Reglas propias y línea temporal

Nombre: Anthony Zamora Martínez
Versión de Wazuh: 4.14.9

## 1. Comprobaciones iniciales

| Comprobación | Orden | Resultado |
|---|---|---|
| Manager en marcha en `anthwatch-wazuh` | `systemctl is-active wazuh-manager` | `active`. Wazuh está instalado directamente en la VM. |
| Estado del agente | `sudo /var/ossec/bin/agent_control -l` | `anthwatch-server`, ID `001`, figuraba como `Disconnected` porque la VM estaba apagada durante las pruebas iniciales. |

## 2. Antes del decodificador

Probé una línea de acceso fallido al portal con `wazuh-logtest`. En la fase 1, Wazuh reconoció la fecha, el equipo `srv-web01` y el programa `portal-nominas`. En la fase 2 mostró `No decoder matched`, así que no extrajo la acción, el usuario ni la IP y el evento no generó una alerta.

Al copiar los ejemplos a mano comprobé que el syslog clásico usa dos espacios entre el mes y el día cuando el día tiene una sola cifra (`Nov  9`). Los archivos del laboratorio ya venían con ese formato. Con la cabecera corregida, el evento de control de SSH activó la regla `5715` de nivel 3.

## 3. Pruebas de mis reglas con wazuh-logtest

| Línea de prueba | Regla que esperaba | Regla que sale | Nivel | ¿Correcto? |
|---|---|---|---|---|
| Fallo de `admin` desde `203.0.113.77` | `100101` | `100101` | 5 | Sí |
| Acceso correcto de `lucia` desde `10.20.0.31` | `100102` | `100102` | 3 | Sí |
| Exportación de 4812 registros en la prueba de reglas simples | `100103` | `100103` | 3 | Sí |
| Quinto fallo consecutivo desde `203.0.113.77` | `100110` | `100110` | 10 | Sí |
| Acceso correcto desde otra IP después de la ráfaga | `100102` | `100102` | 3 | Sí |
| Acceso correcto desde la misma IP después de la ráfaga | `100111` | `100111` | 12 | Sí |
| Exportación de 4812 registros desde una IP externa con las reglas completas | `100112` | `100112` | 10 | Sí |

**Errores y ajustes**

- VirtualBox rechazaba el módulo `vboxdrv` con Secure Boot activo. Registré la clave MOK y confirmé que el módulo cargaba.
- Usé `100104` como regla raíz del portal porque `100100` ya estaba ocupada por una regla SSH de mi laboratorio.
- El resumen no encontraba eventos porque parte de la salida de `wazuh-logtest` iba por stderr. Añadí `2>&1` para guardar ambas salidas en el mismo fichero.

## 4. Línea temporal del 9 de noviembre en srv-web01

Todas las horas son locales.

| Hora | Fuente | Qué ocurre | Regla y nivel | ¿Lo sé o lo supongo? |
|---|---|---|---|---|
| 07:52:10–07:53:02 | Portal | `director` entra y exporta 3 registros desde `198.51.100.23`. | `100102` (3), `100112` (10) | Registrado. El caso indica que esa IP está autorizada para el director los lunes. |
| 08:01:44–08:10:05 | Portal | `lucia` entra y exporta 12 registros desde la IP interna `10.20.0.31`. | `100102` (3), `100103` (3) | Registrado. Sirve de referencia para comparar con el acceso externo posterior. |
| 09:05:31–09:06:20 | Portal | `marcos` falla dos veces y luego entra desde `10.20.0.44`. | `100101` (5), `100102` (3) | Registrado. Se desconoce el motivo de los fallos. |
| 09:08:01–09:09:30 | SSH | `203.0.113.77` intenta autenticarse como `admin` y `root`. El último registro muestra un cierre antes de la autenticación. | `5710` (5), `5760` (5), `5722` (0) | Registrado. No consta un acceso SSH exitoso desde esa IP. |
| 09:12:02–09:12:35 | Portal | Seis fallos como `admin` desde `203.0.113.77`. El quinto, a las `09:12:28`, activa la correlación. | `100101` (5), `100110` (10) | Registrado. Los cinco primeros fallos ocurrieron en 26 segundos. |
| 09:13:40–09:15:20 | Portal | Dos fallos como `administrador` y dos como `lucia` desde la misma IP. | `100101` (5), `100110` (10) en `logtest` | Los cuatro fallos constan en el log. La segunda `100110` se debe al procesamiento acelerado del fichero. |
| 09:16:05 | Portal | Acceso correcto con la cuenta `lucia` desde `203.0.113.77`. | `100111` (12) | El acceso consta. El posible uso indebido de la cuenta es una hipótesis. |
| 09:17:12 | Portal | La cuenta `lucia` exporta 4812 registros desde esa misma IP externa. | `100112` (10) | La exportación consta. La identidad de quien la realizó queda por confirmar. |

**Resumen del incidente**

Desde `203.0.113.77` se registraron intentos fallidos por SSH y luego diez fallos en el portal. A las 09:16:05 se produjo un acceso correcto con la cuenta `lucia` desde esa IP y, 67 segundos después, una exportación de 4812 registros. La secuencia sugiere un posible compromiso de la cuenta, aunque los registros no identifican a la persona que accedió.

**Alerta benigna esperada**

La regla `100112` de las 07:53:02 detectó la exportación de 3 registros del director. Era una actividad autorizada porque `198.51.100.23` era su IP externa permitida los lunes.

## 5. Prueba en vivo con mi agente

| Hora local de `simular-portal.sh` | Hora UTC de la alerta | Regla | Nivel | Agente |
|---|---|---|---|---|
| 08:03:40 | 07:03:41.632 | `100110` | 10 | `anthwatch-server` |
| 08:03:46 | 07:03:47.629 | `100111` | 12 | `anthwatch-server` |
| 08:03:49 | 07:03:49.943 | `100112` | 10 | `anthwatch-server` |

## 6. Respuestas a las preguntas

1. Antes de añadir el decodificador, Wazuh reconocía la cabecera del evento en la fase 1, pero en la fase 2 no tenía un decodificador para el portal. Por eso no extraía los campos necesarios para aplicar las reglas del portal.
2. La regla raíz agrupa los eventos del portal y sirve de padre para las reglas específicas mediante `if_sid`. Su nivel 0 hace que por sí sola no genere una alerta. En mi laboratorio su ID es `100104`.
3. Sin `same_source_ip`, Wazuh podría sumar fallos de IP distintas. Por ejemplo, al reproducir el fichero de golpe podría mezclar los tres fallos de `marcos` desde `10.20.0.44` con los dos primeros fallos de `admin` desde `203.0.113.77`.
4. La segunda `100110`, a las 09:15:20, no habría saltado en tiempo real. Entre las 09:13:20 y las 09:15:20 solo hay cuatro fallos desde esa IP, contando el actual. `wazuh-logtest` procesa el fichero de golpe y usa el tiempo de procesamiento para la correlación.
5. Antes de ir al portal hubo intentos de acceso por SSH como `admin` y `root` desde `203.0.113.77`. Esos intentos solo se ven al revisar también el registro SSH.
6. Me falta evidencia que vincule la sesión a una persona o dispositivo. Revisaría los registros de sesión y de MFA, si existen, y contrastaría la actividad con Lucía. El nombre de la cuenta y la IP no bastan para identificar a quien accedió.
