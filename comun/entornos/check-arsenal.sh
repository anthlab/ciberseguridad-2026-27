#!/usr/bin/env bash
# check-arsenal.sh — verifica que el arsenal de HE (OSINT + ataque) está instalado en la Kali.
# Ejecutar en la estación/plantilla ANTES de la primera clase que use cada bloque.
# No instala nada: informa qué falta y con qué comando instalarlo. Salida con código != 0 si
# falta algo en el/los bloque(s) pedido(s), para poder usarlo en un pipeline de preparación.
#
# Uso:
#   ./check-arsenal.sh              # comprueba TODO
#   ./check-arsenal.sh osint        # solo el arsenal OSINT (HE UT5)
#   ./check-arsenal.sh ut6 ut7      # solo esos bloques
# Bloques: osint · web(UT8) · recon(UT5-act) · wifi(UT3-4) · ut6 · ut7 · wordlists · objetivos
set -u
GREEN=$'\e[32m'; RED=$'\e[31m'; YEL=$'\e[33m'; DIM=$'\e[2m'; RST=$'\e[0m'
OK=0; MISS=0; MISSING_LIST=""

have() { command -v "$1" >/dev/null 2>&1; }
pyhave() { python3 -c "import $1" >/dev/null 2>&1; }

# check "etiqueta" "test" "sugerencia de instalación"
check() {
  local label=$1 test=$2 hint=$3
  if eval "$test" >/dev/null 2>&1; then
    printf "  ${GREEN}[ OK ]${RST} %-22s\n" "$label"; OK=$((OK+1))
  else
    printf "  ${RED}[FALTA]${RST} %-22s ${DIM}→ %s${RST}\n" "$label" "$hint"
    MISS=$((MISS+1)); MISSING_LIST="$MISSING_LIST $label"
  fi
}

SEL="$*"

blk_osint() {
  echo "${YEL}== OSINT (HE UT5) — arsenal-osint.md ==${RST}"
  check "spiderfoot"   "have sf.py || have spiderfoot"        "pipx install spiderfoot"
  check "recon-ng"     "have recon-ng"                        "pipx install recon-ng"
  check "theHarvester" "have theHarvester || have theharvester" "pipx install theHarvester"
  check "maigret"      "have maigret"                         "pipx install maigret"
  check "sherlock"     "have sherlock"                        "pipx install sherlock-project"
  check "holehe"       "have holehe"                          "pipx install holehe"
  check "h8mail"       "have h8mail"                          "pipx install h8mail"
  check "ghunt"        "have ghunt"                           "pipx install ghunt"
  check "phoneinfoga"  "have phoneinfoga"                     "ver github.com/sundowndev/phoneinfoga"
  check "exiftool"     "have exiftool"                        "apt install libimage-exiftool-perl"
  check "amass"        "have amass"                           "apt install amass"
  check "subfinder"    "have subfinder"                       "go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"
  check "gau"          "have gau"                             "go install github.com/lc/gau/v2/cmd/gau@latest"
  check "waybackurls"  "have waybackurls"                     "go install github.com/tomnomnom/waybackurls@latest"
  check "snscrape"     "have snscrape"                        "pipx install snscrape"
  check "instaloader"  "have instaloader"                     "pipx install instaloader"
  check "trufflehog"   "have trufflehog"                      "ver github.com/trufflesecurity/trufflehog"
  check "jq"           "have jq"                              "apt install jq"
}

blk_recon() {
  echo "${YEL}== Recon activo / enumeración (HE UT5) ==${RST}"
  check "nmap"       "have nmap"       "apt install nmap"
  check "rustscan"   "have rustscan"   "ver github.com/RustScan/RustScan"
  check "naabu"      "have naabu"      "go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest"
  check "httpx"      "have httpx"      "go install github.com/projectdiscovery/httpx/cmd/httpx@latest"
  check "dnsx"       "have dnsx"       "go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest"
  check "katana"     "have katana"     "go install github.com/projectdiscovery/katana/cmd/katana@latest"
  check "ffuf"       "have ffuf"       "apt install ffuf"
  check "feroxbuster" "have feroxbuster" "apt install feroxbuster"
  check "nuclei"     "have nuclei"     "go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest"
}

blk_wifi() {
  echo "${YEL}== Inalámbrico / RF (HE UT3-4) ==${RST}"
  check "aircrack-ng"  "have aircrack-ng"  "apt install aircrack-ng"
  check "airodump-ng"  "have airodump-ng"  "apt install aircrack-ng"
  check "hcxdumptool"  "have hcxdumptool"  "apt install hcxdumptool"
  check "hcxpcapngtool" "have hcxpcapngtool" "apt install hcxtools"
  check "wifite"       "have wifite"       "apt install wifite"
  check "bettercap"    "have bettercap"    "apt install bettercap"
  check "hashcat"      "have hashcat"      "apt install hashcat"
}

blk_ut6() {
  echo "${YEL}== MITM / explotación (HE UT6) ==${RST}"
  check "bettercap"   "have bettercap"                     "apt install bettercap"
  check "responder"   "have responder || have Responder"  "apt install responder"
  check "ntlmrelayx"  "have ntlmrelayx.py || have impacket-ntlmrelayx" "pipx install impacket"
  check "mitmproxy"   "have mitmproxy"                     "pipx install mitmproxy"
  check "msfconsole"  "have msfconsole"                    "apt install metasploit-framework"
  check "msfvenom"    "have msfvenom"                      "apt install metasploit-framework"
  check "searchsploit" "have searchsploit"                 "apt install exploitdb"
  check "sqlmap"      "have sqlmap"                        "apt install sqlmap"
  check "netexec"     "have nxc || have netexec"           "pipx install netexec"
  check "wireshark/tshark" "have tshark || have wireshark" "apt install tshark"
}

blk_ut7() {
  echo "${YEL}== Post-explotación (HE UT7) ==${RST}"
  check "hashcat"     "have hashcat"                       "apt install hashcat"
  check "john"        "have john"                          "apt install john"
  check "impacket"    "have secretsdump.py || have impacket-secretsdump" "pipx install impacket"
  check "netexec"     "have nxc || have netexec"           "pipx install netexec"
  check "ligolo-ng"   "have ligolo-ng || have proxy"       "ver github.com/nicocha30/ligolo-ng (agent+proxy)"
  check "chisel"      "have chisel"                        "ver github.com/jpillora/chisel"
  check "proxychains" "have proxychains || have proxychains4" "apt install proxychains4"
  echo "  ${DIM}Nota: linpeas/winpeas y GTFOBins/LOLBAS son scripts/webs, no binarios de sistema:${RST}"
  echo "  ${DIM}      linpeas → github.com/peass-ng/PEASS-ng · GTFOBins → gtfobins.github.io${RST}"
}

blk_web() {
  echo "${YEL}== Auditoría web (HE UT8) ==${RST}"
  check "zaproxy"    "have zaproxy || have zap.sh || have owasp-zap" "apt install zaproxy"
  check "burpsuite"  "have burpsuite"                     "apt install burpsuite (o descarga PortSwigger)"
  check "sqlmap"     "have sqlmap"                        "apt install sqlmap"
  check "nuclei"     "have nuclei"                        "go install .../nuclei@latest"
  check "nikto"      "have nikto"                         "apt install nikto"
  check "dalfox"     "have dalfox"                        "go install github.com/hahwul/dalfox/v2@latest"
  check "arjun"      "have arjun"                         "pipx install arjun"
  check "jwt_tool"   "have jwt_tool || have jwt_tool.py"  "pipx install jwt-tool (o clona ticarpi/jwt_tool)"
  check "commix"     "have commix"                        "apt install commix"
  check "selenium"   "pyhave selenium"                    "pip install selenium"
}

blk_wordlists() {
  echo "${YEL}== Diccionarios ==${RST}"
  check "seclists"        "[ -d /usr/share/seclists ]"                 "apt install seclists"
  check "rockyou.txt"     "[ -f /usr/share/wordlists/rockyou.txt ]"    "gunzip /usr/share/wordlists/rockyou.txt.gz"
  check "best64.rule"     "[ -f /usr/share/hashcat/rules/best64.rule ]" "apt install hashcat"
}

blk_objetivos() {
  echo "${YEL}== Objetivos del laboratorio (host con Docker) ==${RST}"
  check "docker"          "have docker"                    "apt install docker.io"
  check "docker compose"  "docker compose version"         "apt install docker-compose-plugin"
  echo "  ${DIM}Levantar: cd objetivos && docker compose up -d  (avanzados: -f docker-compose-avanzado.yml)${RST}"
  echo "  ${DIM}Prueba de humo de objetivos vivos: bash smoke-test.sh${RST}"
}

# --- ejecutar los bloques pedidos ---
run() { if [ -z "$SEL" ] || case " $SEL " in *" $1 "*) true;; *) false;; esac; then "blk_$1"; echo; fi; }

echo "== check-arsenal.sh — $( [ -z "$SEL" ] && echo 'TODOS los bloques' || echo "bloques: $SEL") =="
echo
run osint
run recon
run wifi
run ut6
run ut7
run web
run wordlists
run objetivos

echo "──────────────────────────────────────────────"
printf "Resultado: ${GREEN}%s OK${RST} · ${RED}%s FALTA${RST}\n" "$OK" "$MISS"
if [ "$MISS" -gt 0 ]; then
  echo "Faltan:${MISSING_LIST}"
  echo "Instala con la sugerencia de cada línea y vuelve a ejecutar. (pipx: 'apt install pipx && pipx ensurepath')"
  exit 1
fi
echo "Arsenal completo en los bloques comprobados. Listo para clase."
