# HE · UT5 — Reconocimiento pasivo y enumeración activa

**8 horas** · RA3 (a, b) · Servicio SOC: Prevención — gestión de la exposición · Evidencias `HE-E9`, `HE-E10`

---

## 1. Objetivo de la unidad

Reunir información sobre el objetivo, primero **sin tocarlo** (reconocimiento pasivo) y luego enumerando activamente sus activos, cuentas y vulnerabilidades potenciales. El objetivo del ejercicio es el servicio desplegado por el módulo PPS, con alcance autorizado.

## 2. Contenido

### 2.1 Reconocimiento pasivo (RA3.a)

Sin una sola conexión directa al objetivo:

- Registros de transparencia de certificados (**crt.sh**): subdominios a partir de los certificados emitidos.
- DNS histórico y pasivo (VirusTotal, SecurityTrails).
- Motores de exposición (**Shodan**, Censys, ZoomEye): puertos y servicios ya indexados.
- Filtraciones públicas (**HIBP**): correos y credenciales expuestas.
- Huella corporativa: dominios, personas, tecnologías, proveedores.

### 2.2 Enumeración activa (RA3.b)

Ya interactuando con el objetivo (genera ruido, detectable por el SOC):

- Barrido de puertos: `nmap`, `masscan`, `rustscan`.
- Descubrimiento HTTP: `httpx`, `katana`, `gobuster`, `ffuf`.
- Enumeración de servicios y directorios.
- Inventario: activos, cuentas de usuario, vulnerabilidades potenciales.

## 3. Laboratorio guiado

### Parte A — Reconocimiento pasivo (RA3.a)

```bash
# Subdominios desde certificados (sin tocar el objetivo)
curl -s "https://crt.sh/?q=%25.xest.local&output=json" | jq -r '.[].name_value' | sort -u

# Correos y hosts expuestos
theHarvester -d xest.local -b crtsh,duckduckgo

# Exposición ya indexada (requiere clave Shodan)
shodan search hostname:xest.local
```

1. Elabora la ficha del objetivo **sin conexión directa**: subdominios, tecnologías, personas, exposición conocida. Cita cada fuente.

### Parte B — Enumeración activa (RA3.b)

```bash
# Barrido de puertos del objetivo autorizado
nmap -sV -sC -oA nmap_objetivo objetivo.lab

# Descubrimiento HTTP
httpx -l hosts.txt -title -tech-detect -status-code -o httpx.txt
ffuf -u https://objetivo.lab/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302
nuclei -u https://objetivo.lab -severity critical,high
```

2. Construye el **inventario** de activos, cuentas y vulnerabilidades potenciales. Mide el ruido generado (¿cuántas alertas produjo en el SOC?).

## 4. Entregables

- **`HE-E9`** (informe, rúbrica R2): informe de reconocimiento pasivo con fuentes citadas y **sin** interacción con el objetivo.
- **`HE-E10`** (laboratorio, rúbrica R1): inventario de activos, cuentas y vulnerabilidades potenciales obtenido por técnicas activas.

## 5. Criterios de superación

- El reconocimiento pasivo no genera ni una conexión al objetivo y cita fuentes.
- El inventario activo es reutilizable en las fases de explotación siguientes.
- El alumno es consciente del ruido que genera y de que el SOC lo detecta.

## 6. Errores frecuentes

- Empezar por nmap saltándose el reconocimiento pasivo: se pierde información y se genera ruido innecesario.
- Confundir Deep Web con Dark Web al documentar las fuentes.

## 7. Referencias

- crt.sh, Shodan, theHarvester, amass, subfinder, httpx, nuclei — documentación.
- OWASP WSTG — Information Gathering.
- MITRE ATT&CK — Reconnaissance, Resource Development.
