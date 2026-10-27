# Caja de herramientas del atacante — estación de aula

Dos opciones. En clase 100 % práctica conviene la **VM Kali plantilla** (todo preinstalado,
clonado en 2 min por estación) y dejar el contenedor como alternativa ligera.

## Opción A — VM Kali (recomendada para HE)

1. Descargar Kali Linux (imagen VirtualBox/VMware pre-hecha):
   https://www.kali.org/get-kali/#kali-virtual-machines
2. Arrancar y actualizar: `sudo apt update && sudo apt full-upgrade -y`.
3. Instalar el metapaquete de pentest web + inalámbrico:
   ```bash
   sudo apt install -y kali-tools-web kali-tools-wireless kali-tools-802-11 \
       seclists jq golang-go pipx
   pipx ensurepath
   ```
4. Herramientas Go/pipx que no vienen o conviene actualizar (ver `HE/recursos/arsenal-github.md`).
5. Exportar como plantilla `.ova` y clonar por estación. **Snapshot limpio** antes de cada
   práctica para volver atrás en segundos.

Kali ya trae: nmap, masscan, aircrack-ng, bettercap, metasploit, sqlmap, hydra, john,
hashcat, wireshark, burpsuite (community), zaproxy, gobuster, ffuf, nikto, theharvester,
dnsrecon, impacket, responder, proxychains, seclists, wordlists (rockyou).

## Opción B — Contenedor `attacker` (ligero, sin GUI)

Para prácticas de línea de comandos sin necesitar VM completa:

```bash
docker run -it --rm --name attacker --net host \
  kalilinux/kali-rolling bash
# dentro:
apt update && apt install -y nmap ffuf gobuster nuclei sqlmap hydra john \
  theharvester dnsrecon seclists jq curl
```

Para las herramientas Go modernas (subfinder, httpx, katana, nuclei, dnsx, naabu),
ver los `go install` en `HE/recursos/arsenal-github.md`.

## Wordlists de referencia (compartidas en el aula)

- **SecLists** — la colección estándar: https://github.com/danielmiessler/SecLists
  (`sudo apt install seclists` → `/usr/share/seclists`).
- `rockyou.txt` — `/usr/share/wordlists/rockyou.txt` (descomprimir en Kali).
- Para fuzzing web: `SecLists/Discovery/Web-Content/raft-*` y `directory-list-2.3-medium.txt`.

## Verificación previa a clase

`bash ../smoke-test.sh` comprueba que los objetivos responden y que las herramientas
básicas están. Ejecutarlo **antes** de cada sesión práctica.
