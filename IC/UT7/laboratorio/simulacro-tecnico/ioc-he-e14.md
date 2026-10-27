# IoC del incidente — entregado por Hacking Ético (HE-E14)

> Indicadores de compromiso documentados por el equipo de HE durante la investigación
> del incidente de xest (UT6, evidencia HE-E14 / IC-E11). **Esta es tu lista de caza**:
> cada puerta trasera del sistema comprometido debería corresponder a uno de estos IoC.
> Recuerda la regla del curso: los IoC son el **suelo** de tu búsqueda, no el techo.

## Contexto

- **Vector de entrada**: subida de fichero sin validación en el portal de xest → webshell.
- **Sistema afectado**: `portal-comprometido` (portal SOC de xest, VLAN de laboratorio).
- **Actor**: infraestructura de laboratorio del equipo HE (`attacker@he-lab`).

## Indicadores

| # | Tipo | Indicador | Dónde buscar |
|---|---|---|---|
| 1 | Fichero (webshell) | `.php` oculto en `assets/` con `eval(` / `base64_decode(` | `/var/www/html` |
| 2 | Cuenta | Usuario `svc-backup` (UID 1000, shell `/bin/bash`) | `/etc/passwd` |
| 2b | Clave SSH | Clave pública `attacker@he-lab` (`ssh-ed25519 ...LABONLY...`) | `/home/svc-backup/.ssh/authorized_keys` |
| 3 | Persistencia | Tarea cron con reverse shell a `10.10.66.66:4444` | `/etc/cron.d/`, `/etc/cron.*` |
| 4 | Persistencia | Binario **SUID root** fuera de rutas de sistema (`/tmp/.x`) | `find / -perm -4000` |

## Red

- **IP C2 del atacante**: `10.10.66.66` (laboratorio; no existe fuera del aula).
- **Puerto de la reverse shell**: `4444/tcp`.

## Nota de la investigación (HE)

> "Confirmamos cuatro mecanismos de persistencia. Priorizamos la contención sobre la
> caza exhaustiva por el reloj regulatorio, así que **no descartamos que quede algún
> mecanismo adicional no capturado**. El equipo de respuesta debe verificar de forma
> independiente que no queda ninguna puerta, no fiarse solo de esta lista."
