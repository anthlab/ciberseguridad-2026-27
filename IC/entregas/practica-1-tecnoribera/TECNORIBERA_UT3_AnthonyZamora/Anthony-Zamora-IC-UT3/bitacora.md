# TECNORIBERA · Bitácora del laboratorio Wazuh

**Módulo:** Incidentes de Ciberseguridad (IC 5021), práctica 1 — UT3  
**Alumno:** Anthony Zamora Martínez  
**Modalidad:** trabajo individual; he realizado el montaje y las pruebas yo solo  
**Fecha de actualización:** 28/10/2026  
**Empresa simulada:** TECNORIBERA, S. L. (18 equipos)

## 1. Mi SOC

Monté Wazuh **4.14.8** con Docker Compose en el ordenador principal (`anthlab-MS-7E28`, Ubuntu 26.04.1 LTS, arquitectura x86_64). La IP usada por los agentes para hablar con el Manager fue **172.29.230.164** (puede cambiar según la red). El Dashboard se abre en `https://localhost`.

El despliegue tiene tres contenedores: **manager, indexer y dashboard**. Comprobé los tres en estado `Up`. Durante la práctica configuré cuatro grupos: `ofimatica`, `direccion`, `desarrollo` y `servidores`. Los cuatro archivos `agent.conf` pasaron la validación de XML y `verify-agent-conf`.

## 2. Agentes que desplegué

| Equipo | SO | IP Host-only | Grupo | ID | Estado comprobado |
|---|---|---|---|---|---|
| `IT-SRV-ERP` | Ubuntu Server 24.04.5 LTS | `192.168.56.101` | `servidores` | `002` | Active y sincronizado |
| `DEV-NB-01` | Ubuntu Server 24.04.5 LTS | `192.168.56.102` | `desarrollo` | `003` | Active y sincronizado |

En el Dashboard los dos mostraban `10.0.2.15`, su IP NAT de VirtualBox. Para conectarme por SSH utilicé la red Host-only. **No instalé `FIN-PC-01` (Windows)** porque el profesor indicó dejarlo para más adelante. El inventario recoge 18 equipos: 2 desplegados y 16 planificados. El agente antiguo `kali-ic-equipo1` (ID `001`) estaba desconectado y no forma parte de esta práctica.

## 3. Configuración FIM de cada grupo

- **Ofimática:** `C:\Users` y carpeta `StartUp`; cada 12 horas. Política creada, todavía sin Windows para probarla.
- **Dirección:** `C:\Users`, `StartUp` y `C:\Program Files`; `report_changes`, cada 6 horas. Política creada, todavía sin Windows.
- **Desarrollo:** `/home`, `/etc` y `/opt/ic-lab/monitor`; se excluyen `.cache` y `node_modules`; cada 6 horas. Detecté cambios en `prueba.txt`.
- **Servidores:** `/etc`, `/root`, `/var/www`, `/opt`, y lectura de `/var/log/auth.log`; cada 4 horas. Detecté cambios de `/etc/passwd` y accesos SSH.

En la alerta FIM del servidor vi las etiquetas `criticality=muy_alta` y `location=valencia-sede`. La configuración de desarrollo define `criticality=alta`, pero no guardé una captura de esos campos en un evento de ese agente. Las etiquetas `department` y `owner` forman parte de la política del inventario, pero **no quedaron aplicadas** en los `agent.conf` probados.

## 4. Usuarios y permisos

- `admin`: contraseña inicial sustituida. La nueva se comprobó con un HTTP `200` en el Indexer. No incluyo credenciales.
- `analista.soc`: cuenta creada con rol personalizado `soc_analista_lectura` en OpenSearch y rol `readonly` en Wazuh. Pudo ver Threat Hunting.
- `auditor`: cuenta creada con rol personalizado `soc_auditor_lectura` en OpenSearch y rol `readonly` en Wazuh. Pudo ver Threat Hunting y al entrar en seguridad apareció **You have no permissions**.

Los roles tienen nombres distintos, pero tras corregir un error el auditor también obtuvo lectura sobre `*` en OpenSearch. **Queda pendiente separar mejor los permisos efectivos de ambos perfiles** y volver a iniciar sesión con ambos usuarios tras el cambio de contraseña de `admin`.

## 5. Pruebas de detección (28/10/2026)

| Prueba | Qué hice | Resultado |
|---|---|---|
| SSH | Desde `DEV-NB-01`, intentos de acceso a `IT-SRV-ERP` con `usuariofalso` | Reglas `5710` (nivel 5) y `5712` (fuerza bruta, nivel 10); también se observaron eventos `5715` de accesos correctos. |
| Usuario local | `sudo useradd -m ic-prueba`, comprobación con `getent` | Cuenta creada; cambió `/etc/passwd`. Wazuh detectó el cambio de ese fichero con regla `550`, nivel 7. **No se guardó alerta específica de `useradd`**. |
| Cambio posterior en `/etc/passwd` | Se buscó el usuario; ya no existía al intentar `userdel -r` | Una nueva alerta `550` confirmó otra modificación. No se puede atribuir esa alerta al `userdel` fallido. |
| FIM en desarrollo | Creé `prueba.txt` con `version=1` y añadí `version=2` | Regla `554`, nivel 5 (`added`) y regla `550`, nivel 7 (`modified`). |
| Prueba de punto ciego | Ejecuté una orden local por tubería con `printf ... | bash` | No aparecieron alertas que coincidieran con la búsqueda por la frase. No prueba que el proceso sea indetectable en cualquier configuración. |
| Regla propia | Registré `IC-ATAQUE-SIMULADO` con `logger` en `auth.log` | Se generaron **dos alertas** de regla `100100`, nivel 10. La segunda se debió probablemente al comando `sudo grep` que incluía el mismo marcador. |

## 6. Mi regla local

- **Archivo:** `/var/ossec/etc/rules/local_rules.xml` del Wazuh Manager.
- **ID:** `100100`.
- **Nivel:** `10`.
- **Descripción:** `IC lab: marcador de ataque simulado detectado por el alumnado.`
- **Condición:** evento de categoría syslog con la cadena exacta `IC-ATAQUE-SIMULADO`.
- **Prueba:** pasó `wazuh-logtest`, se reinició el Manager, se generó un mensaje con `logger` y apareció en Threat Hunting.

El PDF del ejercicio proponía `<decoded_as>syslog</decoded_as>`, pero en mi instalación apareció **Invalid decoder name: 'syslog'**. Se corrigió a `<category>syslog</category>` y funcionó.

## 7. Problemas y soluciones

1. **Dashboard no estaba listo.** Aunque el Indexer respondía en `localhost:9200`, el Dashboard agotaba el tiempo al conectar con `wazuh.indexer`. La regla temporal en `DOCKER-USER` para el tráfico `172.18.0.0/16` permitió recuperar la comunicación. Tras reiniciar Ubuntu fue necesario volver a aplicarla; **falta hacer una solución persistente y mejor acotada**.
2. **El contenedor Manager no tenía `nano`.** Escribí los `agent.conf` con `cat` y comprobé el XML y `verify-agent-conf`.
3. **Cambio de contraseña de admin.** El Indexer devolvía `401` porque el archivo editado en el host no coincidía con el archivo usado dentro del contenedor. Copié el YAML actualizado a `/tmp` y apliqué `securityadmin.sh -t internalusers`; la nueva contraseña dio HTTP `200`.
4. **Error 500 tras cambiar la contraseña.** El acceso volvió a funcionar en una ventana privada del navegador.
5. **Rol auditor demasiado limitado.** Al principio mostraba `getPatternList`; se amplió la lectura de índices y ya pudo ver el Dashboard. Falta refinar ese permiso para diferenciarlo del analista.
6. **Regla 100100 no cargaba.** Cambié `<decoded_as>syslog</decoded_as>` por `<category>syslog</category>` y probé la regla con éxito.

## 8. Punto ciego que encontré

No he instalado `auditd` ni otra fuente específica de procesos en Linux. Puedo ver registros SSH y cambios de archivos, pero algunas ejecuciones mediante tubería podrían no generar alertas con las fuentes que tengo ahora. Además, faltan telemetría Windows, red, identidad corporativa y nube. La explicación detallada está en `matriz-fuentes.md`.

## 9. ¿Qué mejoraría en una empresa real?

1. Instalaría `auditd` en Linux y Sysmon en los puestos Windows importantes, y probaría reglas para ejecuciones sospechosas.
2. Añadiría sensores de red (por ejemplo, Suricata) y conectaría fuentes de identidad corporativa y nube.
3. Separaría mejor los permisos del analista y del auditor, usaría un gestor de secretos y evitaría usar la cuenta `admin` para tareas diarias.
4. Haría persistentes y más específicas las reglas del cortafuegos de Docker, y supervisaría el estado de los componentes.
5. Terminaría el despliegue por oleadas y comprobaría cada equipo con evidencias antes de marcarlo como desplegado.

## 10. Qué queda pendiente

- Preparar Windows `FIN-PC-01`, cuando lo indique el profesor.
- Conseguir **3 agentes Active** de departamentos distintos, como exige el PDF.
- Verificar expresamente las etiquetas de `DEV-NB-01`, diferenciar los permisos efectivos del auditor y repetir el acceso con `analista.soc` y `auditor` tras la rotación de `admin`.
- Capturar en Wazuh una alerta **específica de creación de usuario**; el material disponible prueba la creación en terminal y la modificación FIM de `/etc/passwd`.
- Comprobar 30 minutos de estabilidad del stack sin reinicios y firmar personalmente el checklist.

**Nota:** He montado el laboratorio y realizado las pruebas Linux por mi cuenta. La práctica está avanzada y las detecciones probadas funcionan. No se afirma que los requisitos pendientes estén terminados.
