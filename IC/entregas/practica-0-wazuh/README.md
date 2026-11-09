# Práctica 0 · Mi primer laboratorio con Wazuh

En mi primera entrega de Incidentes de Ciberseguridad partí de una instalación de Wazuh con Docker en Ubuntu. Conecté Kali Linux como agente y realicé dos pruebas: recoger un mensaje de un registro propio y detectar un cambio en un archivo con FIM.

- [Enunciado de la práctica](montar_un_wazuh.pdf)
- [Mi informe con las capturas](Informe_Wazuh_AnthonyZamora.pdf)

## 1. Cómo comprobé el montaje

| Componente | Dónde lo tenía | Para qué lo utilicé |
| --- | --- | --- |
| Agente | En Kali, como servicio de Linux | Recoger registros y vigilar archivos de Kali |
| Manager | En un contenedor en Ubuntu | Recibir los eventos y aplicar las reglas de detección |
| Indexer | En otro contenedor en Ubuntu | Indexar los datos para poder buscarlos |
| Dashboard | En otro contenedor en Ubuntu | Ver el estado del agente y consultar alertas |

1. Ejecuté `docker compose ps` y vi los tres contenedores centrales en estado `Up`.
2. Abrí el dashboard en `https://localhost:5601` desde el equipo que alojaba Wazuh. Si hubiera usado `localhost` desde Kali, habría apuntado al propio Kali.
3. Hice ping desde Kali a la IP de Ubuntu para comprobar la conectividad. Después comprobé la comunicación con Wazuh en el panel.
4. Vi el agente `kali-ic-equipo1`, con ID `001`, en estado `Active`. El enunciado también pedía un agente Windows. En mi informe documenté el de Kali.

## 2. Docker, instalación directa y disponibilidad

En clase usé Docker Compose. Me permitió partir de una configuración común para desplegar los tres componentes y consultar sus registros con `docker compose logs`. Si recreo los contenedores, los datos y la configuración que quiera conservar tienen que estar en almacenamiento persistente.

En mi laboratorio **Anthwatch** instalé Wazuh directamente en una VM de Ubuntu y administro sus servicios con `systemctl`. También podría instalar Docker dentro de una VM de VirtualBox y ejecutar allí los contenedores.

Si tuviera que desplegar Wazuh en una empresa, elegiría según cómo trabaje el equipo que lo va a mantener. Usaría Docker si ya administra contenedores en producción. Si su entorno se basa en VMs y servicios Linux, elegiría una instalación directa en una VM dedicada.

Me pregunté si Docker era mejor por la disponibilidad. Distinguí dos fallos:

- **Falla el proceso del manager.** Docker o `systemd` pueden volver a arrancarlo en la misma máquina si configuro una política de reinicio.
- **Falla el servidor físico.** Para que otro manager pueda asumir el servicio, tendría que prepararlo en otro servidor. Dos VMs en mi mismo PC siguen dependiendo de ese PC. Si quiero mantener también la consulta de alertas, tengo que considerar el indexer y el dashboard.

## 3. Qué configuré en el agente

En Kali trabajé con `/var/ossec/etc/ossec.conf`. Si tuviera otro agente Kali, encontraría su propio archivo en la misma ruta, pero en la otra máquina.

| Bloque | Qué puedo configurar |
| --- | --- |
| `<client>` | A qué manager se conecta el agente |
| `<localfile>` | Qué fuente de registros recoge |
| `<syscheck>` | Qué archivos y directorios vigila con FIM |

`<localfile>` y `<syscheck>` van al mismo nivel dentro de `<ossec_config>`. Para aplicar un cambio local puedo reiniciar el agente con `sudo systemctl restart wazuh-agent` después de validar la configuración.

Al probar el archivo con Python obtuve `junk after document element`. El analizador XML esperaba un único elemento raíz, mientras que Wazuh admite varios bloques `<ossec_config>`. Revisé la estructura del archivo, los registros y el estado del agente.

## 4. Cómo probé la recogida de registros

Primero generé un mensaje con `logger` y lo encontré con `journalctl`. Así confirmé que el mensaje se había guardado localmente en Kali.

Después preparé `/var/log/ic-aula.log` para controlar exactamente qué escribía y en qué archivo. Añadí una línea de prueba con este comando:

```bash
echo "Oct 14 12:30:00 kali ic-aula: prueba de recoleccion IC" \
  | sudo tee -a /var/log/ic-aula.log
```

`tee -a` añade la línea al final del archivo. Para configurar la recogida de un archivo como este, el bloque sería:

```xml
<localfile>
  <log_format>syslog</log_format>
  <location>/var/log/ic-aula.log</location>
</localfile>
```

En `/var/ossec/logs/ossec.log` vi que **Logcollector** había incorporado `ic-aula.log` a la recogida. Eso comprobaba que el agente tenía configurada la fuente. Para demostrar que el manager había recibido esa línea concreta habría necesitado otra evidencia.

En una empresa recogería el registro que ya genera el servicio. Por ejemplo, si SSH deja sus mensajes en `/var/log/auth.log`, configuraría esa fuente y su formato. Creé `ic-aula.log` porque en la prueba yo hacía de aplicación y escribía los mensajes a mano.

## 5. Qué averigüé con wazuh-logtest

Como no encontré una alerta para el mensaje de prueba, ejecuté esta herramienta dentro del contenedor del manager:

```bash
sudo docker compose exec wazuh.manager /var/ossec/bin/wazuh-logtest
```

Pegué la línea manualmente. Wazuh reconoció la fecha, el equipo `kali` y el programa `ic-aula`. En la fase de decodificación apareció `No decoder matched`, que significa que ningún decodificador coincidió con ese registro. En esa prueba tampoco vi una regla que generara una alerta.

Un decodificador me sirve para extraer campos, como el usuario y la IP de origen de un fallo SSH. Si solo quiero detectar un texto concreto, también puedo probar una regla que busque ese texto directamente.

Usaría `wazuh-logtest` para averiguar qué regla coincide, investigar por qué una línea no alerta o probar un decodificador nuevo. Puedo automatizar esas pruebas con un script. En el funcionamiento habitual, el manager ya analiza automáticamente lo que recibe. Como en `logtest` introduje la línea a mano, comprobé el análisis del mensaje. Para verificar el envío desde Kali tendría que probar el recorrido real.

## 6. Cómo detecté un cambio con FIM

Creé `/opt/ic-lab` en Kali y preparé `prueba.txt` con el contenido `version=1`. Elegí esa carpeta para hacer un cambio controlado. Podría haber usado otro nombre o vigilar una ruta que ya existiera, como `/etc/ssh`, si quisiera detectar cambios en la configuración de SSH.

Añadí esta línea **dentro de `<syscheck>`** en el `ossec.conf` del agente:

```xml
<directories realtime="yes" check_all="yes">/opt/ic-lab</directories>
```

Con `realtime="yes"` activé la vigilancia en tiempo real para esa ruta. Con `check_all="yes"` activé las comprobaciones de integridad disponibles para esa entrada.

Esperé a que terminara el análisis inicial para que FIM tuviera un estado de referencia. Después añadí `version=2` y encontré un evento `modified` con la **regla 550, nivel 7**, descrito como `Integrity checksum changed`. La alerta indicaba un cambio en el archivo. En mi caso fue un cambio esperado que provoqué yo.

| Lo que quería comprobar | Qué configuré |
| --- | --- |
| Qué mensaje se había escrito en `ic-aula.log` | `<localfile>` para que Logcollector recogiera la línea |
| Si había cambiado `prueba.txt` | `<syscheck>` para que FIM vigilara su integridad |

## 7. Cómo aplicaría la vigilancia a un grupo

Para vigilar una carpeta solo en Kali, editaría el `ossec.conf` de Kali. Si quisiera aplicar la misma configuración a varios servidores, la definiría en el manager, en `/var/ossec/etc/shared/NOMBRE_DEL_GRUPO/agent.conf`, dentro de `<agent_config>`.

Por ejemplo, si configurara el grupo `servidores` para vigilar `/etc/ssh`, el manager distribuiría la configuración y cada agente vigilaría su propia carpeta `/etc/ssh`. Así aplicaría una política común a varios equipos, como en la práctica de TECNORIBERA.
