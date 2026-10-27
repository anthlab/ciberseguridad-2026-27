# HE · UT7 — Post-explotación: credenciales, pivotaje y persistencia

**8 horas** · RA4 (a, b, c, d) · Servicio SOC: Protección — emulación de adversarios · Evidencias `HE-E13`, `HE-E14`

---

## 1. Objetivo de la unidad

Una vez dentro de un sistema, un adversario real busca credenciales, se mueve a otros sistemas y garantiza acceso futuro. Esta unidad practica esas técnicas en laboratorio con una regla innegociable: **toda persistencia instalada se revierte y se verifica antes de cerrar la práctica**, y los indicadores generados se entregan al equipo defensivo.

## 2. Contenido

### 2.1 Administración remota (RA4.a)

Shells inversas, SSH, WinRM, herramientas de **impacket** (psexec, wmiexec). Operar el sistema comprometido por línea de comandos.

### 2.2 Ataques a credenciales (RA4.b)

- **Diccionario**, **tablas rainbow** y **fuerza bruta** contra resúmenes capturados.
- La lección defensiva: qué política de contraseñas resiste cada ataque (longitud, función de derivación de coste).

```bash
# Ataque de diccionario contra un volcado de hashes de laboratorio
hashcat -m 1000 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
john --wordlist=rockyou.txt --format=nt hashes.txt
```

### 2.3 Movimiento lateral y pivotaje (RA4.c)

- Mapear rutas de ataque en Active Directory con **BloodHound/SharpHound**.
- Pivotar a segmentos no accesibles directamente: `chisel`, `ligolo-ng`.

### 2.4 Persistencia (RA4.d)

- Puertas traseras controladas, tareas programadas, servicios.
- **Documentación y reversión obligatorias**: cada mecanismo instalado se registra y se elimina, verificando que ya no está.

## 3. Laboratorio guiado

> Entorno: laboratorio de Active Directory / máquinas aisladas.

### Parte A — Credenciales (RA4.b)

1. Recupera contraseñas de un volcado de laboratorio con hashcat. **Mide** cuánto tarda cada tipo de contraseña y concluye qué política las habría hecho inviables.

### Parte B — Pivotaje (RA4.c)

```bash
# Túnel para alcanzar un segmento interno desde el host comprometido
ligolo-ng   # agente en el host comprometido, proxy en el atacante
# o
chisel server -p 8080 --reverse        # en el atacante
chisel client atacante:8080 R:socks    # en el comprometido
```

2. Alcanza un segmento no accesible directamente y demuestra el acceso.

### Parte C — Persistencia y reversión (RA4.d)

3. Instala un mecanismo de persistencia, **documéntalo**, y a continuación **revíértelo y verifica** que ha desaparecido. Entrega al equipo azul los indicadores generados (hashes, rutas, marcas temporales).

## 4. Entregables

- **`HE-E13`** (laboratorio, rúbrica R1): práctica de ataque a credenciales con conclusiones sobre política de contraseñas.
- **`HE-E14`** (reto integrado, rúbrica R3): cadena de pivotaje y persistencia documentada, con **evidencia de la reversión** y de los indicadores entregados.

## 5. Criterios de superación

- El ataque a credenciales concluye con una recomendación de política medible.
- La persistencia se revierte y se **verifica** su desaparición; sin esa evidencia, la práctica no está completa.
- Los indicadores generados se entregan a IC.

## 6. Advertencia

Estas técnicas fuera de laboratorio son delito (arts. 197 bis, 264). La persistencia no revertida en un ejercicio real es una brecha que tú has abierto: revertir es parte de la ética profesional y se evalúa.

## 7. Referencias

- impacket, BloodHound, hashcat, John the Ripper, chisel, ligolo-ng.
- MITRE ATT&CK — Credential Access, Lateral Movement, Persistence.
