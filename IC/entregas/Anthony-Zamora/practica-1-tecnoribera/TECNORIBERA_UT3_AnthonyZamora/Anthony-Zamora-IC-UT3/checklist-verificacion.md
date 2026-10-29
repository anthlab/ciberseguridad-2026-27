# TECNORIBERA · Checklist de verificación operativa

**Práctica:** IC 5021 — UT3, sesión 2  
**Fecha de revisión:** 28/10/2026  
**Alumno:** Anthony Zamora Martínez  
**Modalidad:** trabajo individual, realizado y verificado por mí  
**Situación:** he desplegado dos agentes Linux. He dejado Windows para más adelante por indicación del profesor.

> Marco solo las comprobaciones que he realizado. Tener una política creada no significa que haya probado su funcionamiento en Windows.

| Comprobación solicitada | Estado | Evidencia / comentario |
|---|---|---|
| [ ] Los tres contenedores llevan 30 minutos sin reinicios. | **Sin verificar** | Los tres llegaron a estar `Up`, pero no he registrado una comprobación continua de 30 minutos tras los reinicios. |
| [ ] Hay al menos 3 agentes `Active` de tres grupos distintos. | **Pendiente** | Hay **2 Active**: `IT-SRV-ERP` (`servidores`) y `DEV-NB-01` (`desarrollo`). Windows aplazado por el profesor. |
| [x] Los agentes de esta práctica no quedan en `default`. | **Comprobado** | IDs `002` y `003` en sus grupos; el Kali antiguo `001` está en `default` y desconectado, fuera del despliegue actual. |
| [x] Nombres de agente según la política. | **Comprobado** | `IT-SRV-ERP` y `DEV-NB-01` siguen el formato acordado. |
| [ ] En **cada** agente desplegado aparecen `criticality` y `location`. | **Parcial** | Las etiquetas `muy_alta` y `valencia-sede` se ven en una alerta de `IT-SRV-ERP`; en `DEV-NB-01` están configuradas pero falta una captura equivalente. |
| [ ] FIM de `ofimatica` monitoriza `C:\Users` y `StartUp`. | **Configurado, no probado** | `agent.conf` validado; no hay Windows desplegado. |
| [ ] FIM de `direccion` monitoriza `C:\Users`, `StartUp` y `C:\Program Files` con `report_changes`. | **Configurado, no probado** | `agent.conf` validado; no hay Windows desplegado. |
| [ ] FIM de `desarrollo` vigila `/home`, `/etc` e ignora `.cache` y `node_modules`. | **Parcial** | Rutas configuradas, archivo XML validado y FIM operativo en `/opt/ic-lab/monitor/`; no se probó de forma independiente cada exclusión. |
| [x] FIM de `servidores` vigila `/etc`, `/root`, `/var/www`, `/opt` y lee `auth.log`. | **Comprobado en lo esencial** | Se observaron las rutas activadas en los logs del agente, alertas de `/etc/passwd` y alertas SSH de `/var/log/auth.log`; no se forzaron cambios en todas las rutas. |
| [ ] Hay dos usuarios aparte de `admin` con **permisos efectivamente distintos**. | **Parcial** | `analista.soc` y `auditor` existen y tienen roles personalizados diferentes; ambos se probaron con lectura, pero el auditor terminó con acceso a índices `*` para corregir un error. Falta distinguir de verdad los alcances. |
| [x] La contraseña de `admin` ya no es la inicial. | **Comprobado** | Autenticación al Indexer con contraseña nueva: HTTP `200`; acceso al Dashboard recuperado. Sin guardar contraseñas. |
| [x] `inventario.csv` incluye los 18 equipos, con estado real. | **Comprobado** | **2 desplegados y 16 planificados**, a fecha 28/10/2026. |

### Verificaciones adicionales de la sesión

- [x] `agent_groups -S -i 002` y `-i 003`: ambos sincronizados.
- [x] Detectada la fuerza bruta SSH: regla `5712`, nivel `10`.
- [x] Detectada modificación de `/etc/passwd`: regla `550`, nivel `7`.
- [x] Detectadas creación y modificación de `/opt/ic-lab/monitor/prueba.txt`: reglas `554` y `550`.
- [x] Regla propia `100100`, nivel `10`, validada con `wazuh-logtest` y disparada en Threat Hunting.
- [ ] Captura de una alerta **específica de `useradd`** en Wazuh (hasta ahora he recogido el comando y una alerta FIM de `/etc/passwd`).
- [ ] Repetir login con `analista.soc` y `auditor` tras cambiar la contraseña de `admin` (sus accesos se probaron antes).

### Aceptación y firmas

**Conclusión:** He montado y probado yo solo el SOC con las dos máquinas Linux. Me quedan Windows y algunas verificaciones. **No doy por completado todo el despliegue.**

**Alumno (ejecución y comprobación):** Anthony Zamora Martínez  **Firma:** _____________________

**Modalidad:** trabajo individual, sin compañero verificador.

**Fecha:** _____________________
