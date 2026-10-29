# TECNORIBERA — Matriz de fuentes y puntos ciegos

**Práctica:** Incidentes de Ciberseguridad (UT3)  
**Fecha:** 28/10/2026

## 1. ¿Qué puedo ver con mi SOC?

| Fuente | Sensor que tengo hoy | Qué veo bien | Qué no veo (punto ciego) |
|---|---|---|---|
| Endpoint Linux (servidores y desarrollo) | Agentes Wazuh en `IT-SRV-ERP` y `DEV-NB-01`, FIM y registros de autenticación del servidor | Intentos SSH fallidos, alerta de fuerza bruta, cambios en `/etc/passwd` y creación/modificación de archivos monitorizados | No he instalado auditd ni una fuente específica para registrar todos los procesos y comandos ejecutados. |
| Endpoint Windows (ofimática y dirección) | Grupos y políticas `agent.conf` preparados, pero ningún agente Windows desplegado | Todavía no he verificado detecciones en Windows | No puedo ver eventos de Windows, PowerShell ni cambios en los equipos reales. Windows quedó pendiente por indicación del profesor. |
| Red | Sin Suricata ni otro sensor de red | No tengo visibilidad específica del tráfico | No puedo observar bien escaneos, comunicaciones de mando y control (C2) ni posibles exfiltraciones de red. |
| Identidad corporativa | Sin Active Directory ni proveedor de identidad conectado | Solo puedo ver la actividad local que registran mis agentes Linux | No puedo ver accesos a cuentas corporativas, SSO ni inicios de sesión sospechosos en servicios externos. |
| Nube | Sin integración con Microsoft 365, AWS o Google Cloud | No tengo eventos de la nube | No puedo detectar cambios de permisos, accesos no autorizados ni acciones en servicios cloud. |
| Aplicación web | Sin servidor web o aplicación empresarial monitorizada | No tengo registros de una aplicación web | No puedo ver intentos de explotación de una web, como inyecciones SQL o accesos sospechosos. |

## 2. Puntos ciegos y posibles categorías de incidentes

1. **Ejecución de comandos en Linux.** Probé una ejecución mediante una tubería hacia `bash` y no encontré una alerta con la cadena buscada. Esto no demuestra que sea imposible detectarla, pero sí que mi configuración no acredita esa visibilidad. **Categoría relacionada:** *Código dañino*, si un atacante ejecutara un script malicioso.
2. **Tráfico de red sin sensor.** Al no tener Suricata ni otro sensor equivalente, podría pasar por alto un reconocimiento o escaneo de puertos. **Categoría relacionada:** *Obtención de información*.
3. **Equipos Windows sin agente.** No puedo comprobar si alguien ejecuta malware o comandos sospechosos en esos puestos. **Categoría relacionada:** *Código dañino*.
4. **Identidad corporativa sin integrar.** No vería intentos de acceso a cuentas corporativas mediante un servicio de identidad externo. **Categoría relacionada:** *Intentos de intrusión*.

Estas categorías describen **riesgos posibles**, no incidentes que hayan ocurrido en el laboratorio. Se han relacionado de forma orientativa con la taxonomía de ENISA y la guía CCN-STIC 817.

## 3. ¿Qué punto ciego me preocupa más?

El que más me preocupa es la **falta de visibilidad sobre los procesos ejecutados en Linux**. Mi servidor `IT-SRV-ERP` es un equipo importante y he comprobado que Wazuh detecta accesos SSH y modificaciones de archivos, pero eso no significa que registre todos los comandos que se ejecutan. Un atacante podría realizar acciones que no generasen los registros que estamos recogiendo.

Para mejorar esto, añadiría **auditd** y configuraría la recogida de sus eventos en Wazuh. Después probaría una regla que detectase ejecuciones sospechosas y comprobaría que las alertas lleguen al Dashboard.

## 4. Conclusión

He conseguido detectar actividad de autenticación y cambios de archivos en los dos equipos Linux. Sin embargo, mi SOC todavía tiene puntos ciegos importantes. Tener Wazuh instalado no significa tener visibilidad completa: depende de las fuentes de datos y las reglas configuradas.

**Referencias para las categorías:** ENISA, *Reference Incident Classification Taxonomy*; CCN-CERT, *CCN-STIC 817 — Gestión de Ciberincidentes*.
