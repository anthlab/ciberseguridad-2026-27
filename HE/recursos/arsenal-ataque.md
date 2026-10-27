# Arsenal de ATAQUE — herramientas ofensivas por fase (con GitHub e instalación)

"Si no atacan, no saben defender." Este es el set ofensivo real que el alumnado usa en el
laboratorio aislado. Organizado por fase del ataque. ⭐ = recomendada · la mayoría vienen en
**Kali** (`sudo apt install kali-tools-*`); se marca 🐹 lo que conviene instalar/actualizar
con `go install` o `pipx`.

> **Regla de aula (no negociable)**: todo esto se ejecuta **solo** sobre los objetivos del
> laboratorio (`*.xest.local` en la VLAN aislada, o los targets vulnerables de abajo), y
> **con el ROE firmado** (HE-E1). Fuera de ahí es delito (arts. 197 bis/ter, 264 CP). El
> objetivo de atacar es aprender a **detectar y defender**: cada ataque se contrasta con el
> SOC de Incidentes (rojo↔azul).

---

## 1. Reconocimiento activo y escaneo
| Herramienta | Repo | Para qué |
|---|---|---|
| **nmap** ⭐ | https://github.com/nmap/nmap | Escaneo de puertos, versiones, scripts NSE. La navaja suiza. |
| **masscan** | https://github.com/robertdavidgraham/masscan | Escaneo masivo ultrarrápido de rangos. |
| **RustScan** | https://github.com/RustScan/RustScan | Encuentra puertos abiertos en segundos y los pasa a nmap. |
| **naabu** 🐹 | https://github.com/projectdiscovery/naabu | Escaneo de puertos rápido y scriptable. |
| **AutoRecon** | https://github.com/Tib3rius/AutoRecon | Orquesta el recon automático de un objetivo (ideal para aprender el flujo). |

## 2. Auditoría web
| Herramienta | Repo | Para qué |
|---|---|---|
| **Burp Suite** ⭐ | https://portswigger.net/burp | Proxy de interceptación de referencia (Community gratis). |
| **OWASP ZAP** ⭐ | https://github.com/zaproxy/zaproxy | Alternativa libre, scriptable, con escáner activo. |
| **sqlmap** ⭐ | https://github.com/sqlmapproject/sqlmap | Explotación automática de inyección SQL. |
| **nuclei** 🐹 | https://github.com/projectdiscovery/nuclei | Escáner por plantillas (miles de checks mantenidos). |
| **ffuf** ⭐ | https://github.com/ffuf/ffuf | Fuzzing de rutas, parámetros, subdominios. |
| **feroxbuster** | https://github.com/epi052/feroxbuster | Descubrimiento recursivo de contenido. |
| **wpscan** | https://github.com/wpscanteam/wpscan | Auditoría de WordPress (plugins/temas/usuarios). |
| **dalfox** 🐹 | https://github.com/hahwul/dalfox | Descubre y verifica XSS. |
| **commix** | https://github.com/commixproject/commix | Inyección de comandos automatizada. |
| **XSStrike** | https://github.com/s0md3v/XSStrike | Detección avanzada de XSS con fuzzing y análisis. |
| **jwt_tool** | https://github.com/ticarpi/jwt_tool | Ataques a JSON Web Tokens (alg=none, claves débiles). |
| **Arjun** | https://github.com/s0md3v/Arjun | Descubre parámetros HTTP ocultos. |
| **nikto** | https://github.com/sullo/nikto | Barrido rápido de problemas de servidor web. |

## 3. Explotación
| Herramienta | Repo | Para qué |
|---|---|---|
| **Metasploit Framework** ⭐ | https://github.com/rapid7/metasploit-framework | Explotación, payloads (msfvenom), post-explotación. |
| **searchsploit / Exploit-DB** ⭐ | https://github.com/offensive-security/exploitdb | Base local de exploits (`searchsploit <producto>`). |
| **PayloadsAllTheThings** ⭐ | https://github.com/swisskyrepo/PayloadsAllTheThings | Chuletario imprescindible de payloads por técnica. |
| **HackTricks** ⭐ | https://github.com/carlospolop/hacktricks | Metodología y trucos por servicio/escenario. |

## 4. Contraseñas (online y offline)
| Herramienta | Repo | Para qué |
|---|---|---|
| **Hydra** ⭐ | https://github.com/vanhauser-thc/thc-hydra | Fuerza bruta de servicios de red (SSH, HTTP, RDP…). |
| **Medusa** | https://github.com/jmk-foofus/medusa | Alternativa a Hydra, muy paralela. |
| **hashcat** ⭐ | https://github.com/hashcat/hashcat | Crackeo por GPU de hashes (el más potente). |
| **John the Ripper** ⭐ | https://github.com/openwall/john | Crackeo versátil (jumbo con cientos de formatos). |
| **CeWL** | https://github.com/digininja/CeWL | Genera diccionarios a partir del sitio del objetivo. |
| **crunch** | (en Kali) | Genera diccionarios por patrón. |
| **name-that-hash** | https://github.com/HashPals/Name-That-Hash | Identifica el tipo de hash. |

## 5. Active Directory / movimiento lateral
| Herramienta | Repo | Para qué |
|---|---|---|
| **BloodHound CE** ⭐ | https://github.com/SpecterOps/BloodHound | Grafo de rutas de ataque en AD. |
| **SharpHound** | https://github.com/BloodHoundAD/SharpHound | Recolector para BloodHound. |
| **NetExec (nxc)** ⭐ | https://github.com/Pennyw0rth/NetExec | Sucesor de CrackMapExec: barrido y ejecución en AD/SMB/WinRM. |
| **impacket** ⭐ | https://github.com/fortra/impacket | psexec, wmiexec, secretsdump, ntlmrelayx… |
| **Kerbrute** | https://github.com/ropnop/kerbrute | Enumeración/fuerza bruta de usuarios Kerberos. |
| **Certipy** | https://github.com/ly4k/Certipy | Ataques a AD CS (plantillas de certificado). |
| **Responder** ⭐ | https://github.com/lgandx/Responder | Envenenamiento LLMNR/NBT-NS + captura de hashes. |
| **mimikatz** | https://github.com/gentilkiwi/mimikatz | Extracción de credenciales en Windows (lab). |

## 6. Túnel y pivotaje
| Herramienta | Repo | Para qué |
|---|---|---|
| **ligolo-ng** ⭐ | https://github.com/nicocha30/ligolo-ng | Pivotaje moderno vía interfaz tun. |
| **chisel** | https://github.com/jpillora/chisel | Túneles TCP/SOCKS sobre HTTP. |
| **sshuttle** | https://github.com/sshuttle/sshuttle | "VPN de pobre" sobre SSH. |

## 7. Command & Control (C2) — para demos controladas
| Herramienta | Repo | Para qué |
|---|---|---|
| **Sliver** ⭐ | https://github.com/BishopFox/sliver | C2 moderno en Go, gratis. El mejor para docencia. |
| **Havoc** | https://github.com/HavocFramework/Havoc | C2 con GUI, moderno. |
| **Empire** | https://github.com/BC-SECURITY/Empire | C2 clásico PowerShell/Python. |
| **Metasploit** | (arriba) | C2 básico con meterpreter. |

## 8. Inalámbrico y RF
| Herramienta | Repo | Para qué |
|---|---|---|
| **aircrack-ng** ⭐ | https://github.com/aircrack-ng/aircrack-ng | Suite Wi-Fi (captura + crackeo). |
| **wifite2** | https://github.com/kimocoder/wifite2 | Automatiza aircrack para docencia rápida. |
| **hcxdumptool / hcxtools** | https://github.com/ZerBea/hcxdumptool | Captura PMKID moderna → hashcat modo 22000. |
| **eaphammer** | https://github.com/s0lst1c3/eaphammer | Ataques a WPA-Enterprise (evil twin 802.1X). |
| **airgeddon** | https://github.com/v1s1t0r1sh3r3/airgeddon | Front-end todo-en-uno de auditoría Wi-Fi. |
| **bettercap** ⭐ | https://github.com/bettercap/bettercap | MITM, BLE, Wi-Fi, sniffing. |
| **Proxmark3 (Iceman)** | https://github.com/RfidResearchGroup/proxmark3 | RFID/NFC. |
| **HackRF / URH** | https://github.com/jopohl/urh | Análisis y replay de radiofrecuencia. |

## 9. Phishing / ingeniería social (con consentimiento del grupo)
| Herramienta | Repo | Para qué |
|---|---|---|
| **GoPhish** ⭐ | https://github.com/gophish/gophish | Campañas de phishing simuladas con métricas. |
| **Evilginx2** | https://github.com/kgretzky/evilginx2 | Proxy de phishing que captura sesión/2FA (demo avanzada). |
| **SET (Social-Engineer Toolkit)** | https://github.com/trustedsec/social-engineer-toolkit | Kit clásico de vectores de ingeniería social. |
| **Zphisher** | https://github.com/htr-tech/zphisher | Plantillas de phishing para laboratorio. |

## 10. Post-explotación y escalada de privilegios
| Herramienta | Repo | Para qué |
|---|---|---|
| **PEASS-ng (linpeas/winpeas)** ⭐ | https://github.com/peass-ng/PEASS-ng | El mejor descubridor de vías de escalada (Linux/Windows). |
| **GTFOBins** ⭐ | https://gtfobins.github.io | Binarios de Unix abusables para escalar. |
| **LOLBAS** | https://lolbas-project.github.io | Equivalente para Windows. |
| **pspy** | https://github.com/DominicBreuker/pspy | Ver procesos/cron sin ser root. |
| **Seatbelt** | https://github.com/GhostPack/Seatbelt | Enumeración de host Windows. |

## 11. Payloads, evasión y recursos
| Recurso | Repo | Para qué |
|---|---|---|
| **msfvenom** | (Metasploit) | Genera payloads a medida. |
| **Villain** | https://github.com/t3l3machus/Villain | Gestión de shells inversas y payloads. |
| **SecLists** ⭐ | https://github.com/danielmiessler/SecLists | Diccionarios de todo (usuarios, rutas, contraseñas, payloads). |
| **GTFOBins / LOLBAS / HackTricks / PayloadsAllTheThings** | (arriba) | Los 4 imprescindibles de consulta. |

---

## Objetivos vulnerables para practicar (laboratorio de ataque)

Se despliegan en la VLAN aislada. Los primeros ya están en `../../comun/entornos/objetivos/`.

| Objetivo | Repo / origen | Enfoque |
|---|---|---|
| **OWASP Juice Shop** ⭐ | https://github.com/juice-shop/juice-shop | Web moderna, OWASP Top 10, gamificada. |
| **DVWA** ⭐ | https://github.com/digininja/DVWA | Web clásica con niveles low/medium/high (ver la corrección). |
| **OWASP WebGoat** | https://github.com/WebGoat/WebGoat | Lecciones guiadas de vulnerabilidades web. |
| **bWAPP / Mutillidae** | https://github.com/webpwnized/mutillidae | Amplio catálogo OWASP para práctica dirigida. |
| **Metasploitable 2/3** ⭐ | https://github.com/rapid7/metasploitable3 | Máquina entera vulnerable: red + servicios + explotación real. |
| **VAmPI / crAPI** | https://github.com/erev0s/VAmPI · https://github.com/OWASP/crAPI | Vulnerabilidades de **API REST**. |
| **VulnHub** | https://www.vulnhub.com | Máquinas descargables tipo CTF. |
| **HackTheBox / TryHackMe** | hackthebox.com · tryhackme.com | Plataformas online con reglas propias (autorizadas). |
| **PortSwigger Academy** ⭐ | https://portswigger.net/web-security | Labs web gratuitos, excelentes para teoría+práctica. |

El **docker-compose ampliado** con WebGoat y VAmPI ya está listo en
[`../../comun/entornos/objetivos/docker-compose-avanzado.yml`](../../comun/entornos/objetivos/docker-compose-avanzado.yml)
(`docker compose -f docker-compose-avanzado.yml up -d`). crAPI y Metasploitable van por su
cuenta (multi-contenedor / VM): ver [`README-avanzado.md`](../../comun/entornos/objetivos/README-avanzado.md).
Desplegar bajo demanda por sesión (pesan).

---

## Mapa fase → herramienta → UT de HE
| Fase | Herramientas | UT |
|---|---|---|
| OSINT / recon | ver `arsenal-osint.md` | **UT5 (primero)** |
| Escaneo/enum | nmap, ffuf, nuclei | UT5 |
| Wi-Fi/RF | aircrack-ng, wifite2, bettercap, Proxmark3 | UT3-4 |
| MITM/explotación | bettercap, Responder, Metasploit, sqlmap | UT6 |
| Post-explotación | hashcat, impacket, BloodHound, NetExec, ligolo-ng, PEASS | UT7 |
| Web | Burp/ZAP, sqlmap, nuclei, dalfox | UT8 |
| Priorización | prioriza.py + KEV/EPSS/CVSS | UT2 |
