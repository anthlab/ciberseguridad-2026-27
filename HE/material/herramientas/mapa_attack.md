# Mapa de fases del ejercicio a MITRE ATT&CK (HE · UT1/UT8)

Hoja de trabajo para cotejar cada fase y técnica del ejercicio con las tácticas de
MITRE ATT&CK. Sirve para dos cosas: dar un lenguaje común con el equipo azul (IC) y
poder medir la cobertura de detección del SOC (qué TTP se detectó y cuál no).

Rellena la columna «Detectado por el SOC» durante los ejercicios morados.

| Fase del ejercicio | Táctica ATT&CK | Técnica (ejemplo) | Unidad HE | Detectado por el SOC |
|---|---|---|---|---|
| Reconocimiento pasivo | Reconnaissance (TA0043) | Gather Victim Network Info (T1590) | UT5 | |
| Enumeración activa | Reconnaissance / Discovery | Active Scanning (T1595) | UT5 | |
| Acceso inicial (web) | Initial Access (TA0001) | Exploit Public-Facing Application (T1190) | UT6, UT8 | |
| Acceso inicial (phishing) | Initial Access | Phishing (T1566) | UT6 | |
| Acceso inicial (Wi-Fi) | Initial Access | (acceso por red inalámbrica) | UT3 | |
| Ataque de intermediario | Credential Access / Collection | Adversary-in-the-Middle (T1557) | UT6 | |
| Ejecución | Execution (TA0002) | Command and Scripting Interpreter (T1059) | UT6 | |
| Acceso a credenciales | Credential Access (TA0006) | Brute Force (T1110), OS Credential Dumping (T1003) | UT7 | |
| Movimiento lateral | Lateral Movement (TA0008) | Remote Services (T1021) | UT7 | |
| Pivotaje / túnel | Command and Control (TA0011) | Protocol Tunneling (T1572) | UT7 | |
| Persistencia | Persistence (TA0003) | Scheduled Task/Job (T1053), Create Account (T1136) | UT7 | |
| Escalada de privilegios | Privilege Escalation (TA0004) | Exploitation for Privilege Escalation (T1068) | UT6, UT7 | |

## Cómo usarlo en el ejercicio morado

1. El equipo rojo ejecuta la técnica y anota la fila correspondiente.
2. El equipo azul revisa el SOC y marca si generó alerta y con qué regla (Sigma/KQL).
3. Toda fila con «Detectado por el SOC» vacío es una **regla de detección que falta**: se
   entrega al módulo IC como mejora del SOC.

Referencia: [attack.mitre.org](https://attack.mitre.org) · MITRE D3FEND para el mapeo a controles defensivos.
