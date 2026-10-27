# HE · UT6 — Interceptación, ataque de intermediario y explotación de sistemas

**9 horas** · RA3 (c, d, e) · Servicio SOC: Protección — validación empírica de controles · Evidencias `HE-E11`, `HE-E12`

---

## 1. Objetivo de la unidad

Interceptar y manipular tráfico en un segmento de laboratorio, ejecutar un ataque de intermediario demostrable y explotar un servicio vulnerable hasta obtener acceso. Todo sobre entorno aislado y con el ROE firmado. La intrusión resultante se entrega al módulo IC como caso real.

## 2. Contenido

### 2.1 Interceptación de tráfico (RA3.c)

- Monitorización en segmento conmutado; **envenenamiento ARP** y suplantación DNS.
- Búsqueda de información sensible en el tráfico interceptado.

### 2.2 Ataque de intermediario (RA3.d)

- Situarse entre dos extremos, leer, insertar y **modificar** el tráfico.
- Degradación de TLS y sus límites (HSTS lo impide); por qué el cifrado bien configurado frustra el MITM.

### 2.3 Explotación (RA3.e)

- Ingeniería social y phishing como vector de acceso inicial (con consentimiento documentado sobre buzones propios del grupo).
- Explotación de servicios vulnerables y escalada de privilegios.

### 2.4 Defensa

Segmentación, inspección dinámica de ARP, DNSSEC, HSTS, firma SMB. Cada ataque tiene su contramedida, que se documenta.

## 3. Laboratorio guiado

> Entorno: **red de laboratorio aislada**. Nada de esto se ejecuta contra la red del centro.

### Parte A — Ataque de intermediario (RA3.c, RA3.d)

```bash
# Envenenamiento ARP + intercepción (solo en laboratorio aislado)
sudo bettercap -iface eth0
# » set arp.spoof.targets 10.10.10.20
# » arp.spoof on
# » net.sniff on
```

1. Sitúate entre dos máquinas de laboratorio y **demuestra la modificación** del contenido de una respuesta HTTP en claro. Repite contra un servicio con HSTS y documenta por qué falla.

### Parte B — Explotación y escalada (RA3.e)

```bash
# Explotar un servicio vulnerable de laboratorio
msfconsole -q
# » use exploit/...   set RHOSTS ...   run
# Escalada tras obtener shell
# enumeración local: sudo -l, SUID, kernel, credenciales en disco
```

2. Compromete un sistema de laboratorio y escala hasta administrador, documentando cada paso de forma **reproducible**.

### Parte C — Phishing controlado (RA3.e, opcional según ROE)

3. Campaña de phishing simulada contra buzones del **propio grupo**, previamente autorizada, para demostrar el vector de acceso inicial.

## 4. Entregables

- **`HE-E11`** (laboratorio, rúbrica R1): práctica de interceptación y ataque de intermediario con evidencia de la modificación del tráfico.
- **`HE-E12`** (reto integrado, rúbrica R3): compromiso de sistema remoto documentado paso a paso y reproducible, entregado a IC como caso.

## 5. Criterios de superación

- El MITM demuestra modificación real del tráfico y se comprueba que HSTS lo frustra.
- El compromiso es reproducible por un compañero con solo la documentación.
- La intrusión queda descrita para que IC pueda investigarla.

## 6. Advertencia

Interceptar tráfico ajeno o comprometer sistemas de terceros es delito (arts. 197 bis/ter, 264). Solo laboratorio aislado y ROE firmado. El phishing se realiza únicamente sobre buzones del propio grupo con consentimiento.

## 7. Referencias

- bettercap, Metasploit, Responder, mitmproxy.
- OWASP WSTG — pruebas de gestión de sesión y de cifrado en tránsito.
- MITRE ATT&CK — Adversary-in-the-Middle (T1557), Exploitation of Remote Services.
