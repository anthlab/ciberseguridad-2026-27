# Caso base — Compromiso de portal-soc.xest.local (procedente de HE)

> Este es el **parte de incidente** que llega a la cola del SOC. Reproduce el compromiso que
> el equipo de Hacking Ético documenta en `HE-E12` (intrusión) y cuyos IoC de persistencia
> entrega en `HE-E14`. En el aula real, sustituye este fichero por el parte que produzca HE
> sobre el mismo `xest`. Si HE aún no lo ha entregado, este caso sintético permite dar la
> sesión de forma autónoma. **Datos ficticios; VLAN aislada.**

## 1. Resumen ejecutivo (una frase)

Un atacante subió una **webshell** al portal `portal-soc.xest.local` explotando una subida de
fichero sin validar, la usó para establecer **mando y control (C2)**, saltó por **fuerza
bruta SSH** a la estación de administración `ws-admin`, creó **persistencia** (servicio y
cuenta de administrador) y **exfiltró 42 MB** desde el servidor de ficheros hacia el C2.

## 2. Activos afectados

| Activo | IP | Papel | Criticidad |
|---|---|---|---|
| `portal-soc.xest.local` | 10.10.10.10 | Portal público de xest (cara pública + formularios) | Alta (3) |
| `srv-files.xest.local` | 10.10.10.50 | Servidor de ficheros con datos personales | Alta (3) |
| `ws-admin` | 10.10.10.31 | Estación de administración (cuenta `jadmin`) | Media (2) |
| `soc.xest.local` | 10.10.10.20 | Plataforma SOC (Wazuh/TheHive/Cortex) | Alta (3) |
| Estación atacante (HE) | 10.10.10.100 | Origen de la intrusión, en la VLAN de laboratorio | — |

## 3. Línea de tiempo observada (2026-11-18)

| Hora | Evento | Fuente | Alerta en la cola |
|---|---|---|---|
| 08:12 | Intento de subida de fichero al portal | Suricata | A03 |
| 08:19 | Webshell `status.php` creada en `/var/www/html/uploads/` | Wazuh FIM | A05 |
| 08:24 | Baliza C2 HTTP del portal a `185.220.101.47` | Suricata | A07 |
| 08:31 | Resolución DNS del portal a `update-cdn-xest.link` | Wazuh | A09 |
| 08:48 | Barrido SYN del atacante a varios hosts | Suricata | A11 |
| 09:02 | Éxito de fuerza bruta SSH sobre `jadmin` en `ws-admin` | Wazuh | A12 |
| 09:20 | Exfiltración de 42 MB de `srv-files` al C2 | Suricata | A15 |
| 09:41 | Servicio `svc-update.service` creado en `ws-admin` | Wazuh FIM | A18 |
| 09:47 | Cuenta de administrador local `svc-update` creada | Wazuh | A19 |

## 4. Indicadores de compromiso (IoC)

Ver `observables-caso.csv` (formato importable a TheHive). Resumen:

- **C2**: IP `185.220.101.47`, dominio `update-cdn-xest.link`.
- **Webshell**: `/var/www/html/uploads/status.php`
  - SHA-256 `d41f8c9a2b7e6350f1a4c8d9b2e5760a3c9f1d2e8b4a6705c3e9f8d1a2b7c604`
  - MD5 `7b3e9a1c5d2f8046b1e4c7a0d3f69b2e`
- **Persistencia**: servicio `svc-update.service`, cuenta local `svc-update`, binario
  SHA-256 `a7c4e91f2d8b6350f9a1c4d7b0e3968a2c5f1d4e7b8a0c3d6f9b2e5a8c1d4f70`.
- **Cuenta comprometida**: `jadmin` (acceso por fuerza bruta).

## 5. Vector de entrada (raíz, para la contención)

El endpoint de subida del portal aceptaba cualquier extensión y guardaba el fichero **dentro
del raíz web ejecutable**. Es el hueco que hay que cerrar para que la reinfección no sea
trivial (la corrección completa del código es trabajo de PPS; aquí basta con documentarlo y
neutralizar el vector como parte de la contención).

```php
// VULNERABLE (lo que había en el portal): guarda cualquier fichero en un dir servido por PHP
move_uploaded_file($_FILES['f']['tmp_name'], "/var/www/html/uploads/".$_FILES['f']['name']);
```

```php
// CONTENCIÓN mínima del vector: lista blanca de extensión + directorio NO ejecutable
$permitidas = ['png','jpg','pdf'];
$ext = strtolower(pathinfo($_FILES['f']['name'], PATHINFO_EXTENSION));
if (!in_array($ext, $permitidas, true)) { http_response_code(415); exit('Tipo no permitido'); }
$destino = "/var/data/subidas/".bin2hex(random_bytes(16)).".".$ext;  // fuera del raíz web
move_uploaded_file($_FILES['f']['tmp_name'], $destino);
```

## 6. Qué NO está en el caso (a propósito)

El **análisis forense** de la memoria y el disco de `ws-admin`, la **causa raíz** completa y
el **timeline mapeado a ATT&CK** son de la **UT6** (IC-E10, IC-E11). La **erradicación** y la
**recuperación** son de la **UT7** (IC-E13). Aquí solo se **tría, se abre el caso y se
contiene** sin destruir la evidencia que necesitará el forense.
