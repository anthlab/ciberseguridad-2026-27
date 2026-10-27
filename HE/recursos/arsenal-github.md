# Arsenal HE 5025 — las mejores herramientas por tema, con GitHub e instalación

> Catálogos ampliados: **[`arsenal-osint.md`](arsenal-osint.md)** (OSINT completo por objetivo,
> se empieza por aquí) y **[`arsenal-ataque.md`](arsenal-ataque.md)** (ofensivo por fase +
> objetivos vulnerables). Este fichero es el índice rápido por UT.


Catálogo del profesor. Para cada UT, la(s) herramienta(s) que se usan en clase, su
repositorio oficial y el comando de instalación. **Kali ya trae muchas**; se marca ⭐ la
recomendada de cada tema y 🐹 las que se instalan con `go install` (ProjectDiscovery y
similares) porque conviene tenerlas al día, no la versión de la distro.

Instalación base del stack Go (una vez, en la VM del atacante):

```bash
sudo apt install -y golang-go
# ProjectDiscovery installer (instala/actualiza todo su ecosistema)
go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest
~/go/bin/pdtm -ia        # instala subfinder, httpx, nuclei, dnsx, katana, naabu...
export PATH="$PATH:$HOME/go/bin"   # añadir a ~/.zshrc
```

---

## UT1 — Marco ético-legal y alcance
No hay herramienta de ataque; el "arsenal" es documental.
- **MITRE ATT&CK Navigator** ⭐ — mapa de tácticas/técnicas. https://github.com/mitre-attack/attack-navigator (o web: https://mitre-attack.github.io/attack-navigator/)
- **PTES / OSSTMM / OWASP WSTG** como metodología de referencia (enlaces en `metodologias.md`).
- Plantilla ROE: `~/xest-lab/2026-2027/HE/material/plantillas/ROE.md`.

## UT2 — Vulnerabilidades, priorización y arsenal
- **prioriza.py** ⭐ (propio, ya probado) — KEV>EPSS>CVSS. `~/xest-lab/2026-2027/HE/material/herramientas/prioriza.py`
- **nuclei** 🐹⭐ — escáner basado en plantillas. https://github.com/projectdiscovery/nuclei
- **nuclei-templates** — https://github.com/projectdiscovery/nuclei-templates
- Fuentes de priorización: CISA **KEV** https://www.cisa.gov/known-exploited-vulnerabilities-catalog · FIRST **EPSS** https://www.first.org/epss/ · **NVD** https://nvd.nist.gov
- **cve-prioritizer** (alternativa de referencia) — https://github.com/TURROKS/CVE_Prioritizer

## UT3 — Auditoría Wi-Fi
- **aircrack-ng** ⭐ (suite completa: airmon-ng, airodump-ng, aireplay-ng) — https://github.com/aircrack-ng/aircrack-ng · `sudo apt install aircrack-ng`
- **hcxdumptool** + **hcxtools** — captura PMKID moderna. https://github.com/ZerBea/hcxdumptool · https://github.com/ZerBea/hcxtools
- **hashcat** ⭐ — crackeo GPU del handshake/PMKID (modo 22000). https://github.com/hashcat/hashcat
- **bettercap** — https://github.com/bettercap/bettercap
- **wifite2** (automatiza aircrack para docencia rápida) — https://github.com/kimocoder/wifite2
- Hardware: adaptador con chipset compatible modo monitor (Alfa AWUS036ACH/NHA).

## UT4 — Otros inalámbricos + equipo morado
- **Proxmark3 / Iceman fork** ⭐ (RFID/NFC) — https://github.com/RfidResearchGroup/proxmark3
- **Flipper Zero firmware** — https://github.com/flipperdevices/flipperzero-firmware
- **Proxmark tooling / mfoc / mfcuk** (MIFARE Classic) — https://github.com/nfc-tools/mfoc · https://github.com/nfc-tools/mfcuk
- **HackRF / GNU Radio** (subgigahercio) — https://github.com/greatscottgadgets/hackrf
- **Universal Radio Hacker (URH)** ⭐ — análisis/replay de RF con GUI, ideal para docencia. https://github.com/jopohl/urh
- **Bluetooth**: bettercap (BLE), **Sniffle** (nRF) — https://github.com/nccgroup/Sniffle

## UT5 — Reconocimiento pasivo y enumeración activa (OSINT)
Reconocimiento pasivo:
- **theHarvester** ⭐ — correos/subdominios/hosts. https://github.com/laramies/theHarvester
- **subfinder** 🐹⭐ — subdominios pasivos. https://github.com/projectdiscovery/subfinder
- **amass** — mapeo de superficie de ataque (OWASP). https://github.com/owasp-amass/amass
- **crt.sh** (CT logs, sin instalar) — https://crt.sh
- **dnsx** 🐹 — resolución masiva. https://github.com/projectdiscovery/dnsx
- **maigret** — presencia de un usuario en N sitios (para el auto-OSINT). https://github.com/soxoj/maigret
- **holehe** — en qué servicios está registrado un correo. https://github.com/megadose/holehe
- **SpiderFoot** ⭐ — automatización OSINT con GUI, excelente para clase. https://github.com/smicallef/spiderfoot
- **Shodan CLI** — https://github.com/achillean/shodan-python · **Censys**, **ZoomEye** (web/API)
- **exiftool** (metadatos) — https://github.com/exiftool/exiftool

Enumeración activa:
- **nmap** ⭐ — https://github.com/nmap/nmap · **rustscan** (rápido) — https://github.com/RustScan/RustScan · **naabu** 🐹 — https://github.com/projectdiscovery/naabu
- **httpx** 🐹⭐ — sonda HTTP masiva. https://github.com/projectdiscovery/httpx
- **katana** 🐹 — crawler. https://github.com/projectdiscovery/katana
- **ffuf** ⭐ — fuzzing de contenido/parametros. https://github.com/ffuf/ffuf · **gobuster** — https://github.com/OJ/gobuster
- **feroxbuster** — https://github.com/epi052/feroxbuster

## UT6 — Interceptación, MITM y explotación
- **bettercap** ⭐ — MITM moderno (ARP/DNS spoof, sniff, proxy). https://github.com/bettercap/bettercap
- **Responder** ⭐ — LLMNR/NBT-NS/mDNS poisoning + captura de hashes. https://github.com/lgandx/Responder
- **mitmproxy** — interceptación HTTP(S) con GUI/scripting. https://github.com/mitmproxy/mitmproxy
- **Metasploit Framework** ⭐ — explotación. https://github.com/rapid7/metasploit-framework
- **sqlmap** — inyección SQL automatizada. https://github.com/sqlmapproject/sqlmap
- **Wireshark** — análisis del tráfico interceptado. https://github.com/wireshark/wireshark
- **Ettercap** (clásico, para comparar) — https://github.com/Ettercap/ettercap

## UT7 — Post-explotación: credenciales, pivotaje, persistencia
- **impacket** ⭐ — psexec/wmiexec/secretsdump. https://github.com/fortra/impacket
- **hashcat** ⭐ / **John the Ripper** — crackeo. https://github.com/hashcat/hashcat · https://github.com/openwall/john
- **BloodHound (CE)** ⭐ + **SharpHound** — rutas de ataque en AD. https://github.com/SpecterOps/BloodHound · https://github.com/BloodHoundAD/SharpHound
- **NetExec** (sucesor de CrackMapExec) ⭐ — barrido/lateral en AD. https://github.com/Pennyw0rth/NetExec
- **ligolo-ng** ⭐ — pivotaje/túnel moderno. https://github.com/nicocha30/ligolo-ng · **chisel** — https://github.com/jpillora/chisel
- **mimikatz** (Windows lab) — https://github.com/gentilkiwi/mimikatz
- **Sliver** (C2 para demostraciones controladas) — https://github.com/BishopFox/sliver

## UT8 — Auditoría de aplicaciones web
- **Burp Suite Community** ⭐ — proxy de interceptación de referencia. https://portswigger.net/burp/communitydownload
- **OWASP ZAP** ⭐ — alternativa libre, scriptable y con modo CI. https://github.com/zaproxy/zaproxy
- **nuclei** 🐹 — escaneo por plantillas. https://github.com/projectdiscovery/nuclei
- **sqlmap** — https://github.com/sqlmapproject/sqlmap
- **OWASP WSTG** (metodología del examen manual) — https://github.com/OWASP/wstg
- **Selenium** (flujos autenticados automatizados) — https://github.com/SeleniumHQ/selenium
- **nikto** (barrido rápido de servidor) — https://github.com/sullo/nikto
- Objetivos de práctica: **OWASP Juice Shop** https://github.com/juice-shop/juice-shop · **DVWA** https://github.com/digininja/DVWA

---

## Cómo mantener esto al día
- El stack ProjectDiscovery se actualiza con `pdtm -ua`.
- nuclei-templates: `nuclei -update-templates` antes de cada bloque de UT2/UT5/UT8.
- Revisar una vez por trimestre que los repos no han cambiado de organización (p. ej.
  CrackMapExec→NetExec, BloodHound Legacy→CE): un enlace muerto en clase es tiempo perdido.
