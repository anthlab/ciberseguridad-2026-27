# HE · UT2 — Vulnerabilidades, tipos de ataque y arsenal de auditoría

**8 horas** · RA1 (f, g, h, i) · Servicio SOC: Prevención — gestión de vulnerabilidades · Evidencias `HE-E3`, `HE-E4`

---

## 1. Objetivo de la unidad

Saber clasificar vulnerabilidades y ataques, elegir la herramienta adecuada para cada organización y —lo más importante— **priorizar por explotabilidad real**, no por la puntuación que da un escáner. Un CVSS 9.8 que nadie explota puede esperar; un CVSS 6.5 en el catálogo KEV de CISA no.

## 2. Contenido

### 2.1 Clasificación de vulnerabilidades (RA1.f, RA1.h)

- **CWE**: taxonomía de tipos de debilidad (p. ej. CWE-89 inyección SQL).
- **CVE**: identificador de una vulnerabilidad concreta en un producto.
- **CVSS**: puntuación de severidad (0–10). Mide *gravedad potencial*, no probabilidad de explotación.
- **EPSS**: probabilidad de que una vulnerabilidad sea explotada en los próximos 30 días. Complementa a CVSS.
- **KEV** (CISA): catálogo de vulnerabilidades **explotadas de forma activa**. Prioridad máxima.

### 2.2 Priorización correcta (RA1.i)

El error clásico es ordenar por CVSS descendente. El criterio profesional combina las tres señales:

1. ¿Está en **KEV**? → prioridad inmediata, se explota ya.
2. ¿**EPSS** alto? → probable que se explote pronto.
3. **CVSS** como desempate de gravedad.

Cuando las tres discrepan, hay que **justificar** la decisión. Ese razonamiento es el entregable, no el número.

### 2.3 Tipología de ataques (RA1.g)

Por superficie (red, aplicación web, inalámbrica, física) y por objetivo (acceso, denegación, exfiltración, persistencia).

### 2.4 Arsenal por fase (RA1.i)

| Fase | Herramientas |
|---|---|
| Reconocimiento | theHarvester, amass, subfinder, crt.sh, Shodan |
| Escaneo | nmap, masscan, httpx, nuclei |
| Explotación | Metasploit, sqlmap, hydra, hashcat |
| Post-explotación | impacket, BloodHound, chisel |
| Informe | plantilla propia, CVSS/EPSS/KEV |

### 2.5 Tipos de auditoría (RA1.g)

- **Caja negra**: sin información previa; simula atacante externo.
- **Caja gris**: información parcial (credenciales de usuario estándar).
- **Caja blanca**: acceso a código y arquitectura; máxima cobertura.

### 2.6 ClearNet, Deep Web, Dark Web (RA1.f)

Diferencias y herramientas de acceso: **Tor**, **I2P**, ZeroNet, Freenet. Como fuente de inteligencia (filtraciones, foros) y como riesgo. Uso metodológico con las precauciones operativas del centro.

## 3. Laboratorio guiado

### Parte A — Priorización real (RA1.h, RA1.i)

1. Se entrega un lote de **30 vulnerabilidades** (CVE con su CVSS). Enriquece cada una con EPSS y KEV usando la herramienta `HE/material/herramientas/prioriza.py`.

```bash
python3 HE/material/herramientas/prioriza.py --cve-list lote_cves.txt --salida priorizado.csv
```

2. Ordena el lote por prioridad real y **argumenta las discrepancias** entre el orden CVSS y el orden final.

### Parte B — Selección de arsenal (RA1.i)

3. Para tres perfiles de organización (pyme, administración pública ENS, entidad financiera), selecciona y justifica las herramientas de monitorización y auditoría adecuadas a cada una.

### Parte C — Fuentes en darknets (RA1.f, refuerzo)

4. Consulta metodológica de una fuente en Tor (índice de filtraciones) con las precauciones del centro, documentando la diferencia entre ClearNet, Deep y Dark Web.

## 4. Entregables

- **`HE-E3`** (informe, rúbrica R2): cuadro comparativo de herramientas por tipo de organización con criterio de elección.
- **`HE-E4`** (laboratorio, rúbrica R1): ejercicio de priorización con justificación de las discrepancias entre CVSS, EPSS y KEV.

## 5. Criterios de superación

- La priorización usa las tres señales (CVSS, EPSS, KEV) y justifica los desempates.
- La selección de herramientas se adecua al perfil de organización, no es una lista genérica.

## 6. Errores frecuentes

- Ordenar por CVSS y llamarlo priorización.
- Ignorar KEV: una vulnerabilidad explotada activamente con CVSS medio es más urgente que una teórica con CVSS alto.

## 7. Referencias

- CISA **KEV Catalog** · FIRST **EPSS** · NVD (CVE/CVSS) · MITRE **CWE**.
- CCN-STIC 484.
