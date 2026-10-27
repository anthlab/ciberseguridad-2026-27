# HE-E5 · Captura y acceso Wi-Fi (UT3 · para el alumnado)

**Objetivo**: sobre la red **de laboratorio** `xest-lab`, capturar el handshake, romper la clave
**offline**, demostrar el acceso, **medir el tiempo** y concluir qué longitud/entropía lo habría
hecho inviable.

- **Alcance**: **SOLO `xest-lab`** (BSSID y canal en la pizarra), dentro de la VLAN aislada.
  Cualquier acción sobre otra red = **0** y protocolo de convivencia (rúbrica R1, salida cero).
- **RA/CE**: RA2.a, RA2.c, RA2.d. **Instrumento/Rúbrica**: I1 · **R1**.
- **Entrega**: `NN-HE-E5-wifi.md` + `captura-01.cap` (por número de lista, p. ej. `07-HE-E5-wifi.md`).

## Qué tienes que hacer

### 1. Modo monitor y descubrimiento
Pon tu adaptador en modo monitor y localiza `xest-lab`. Anota **BSSID** y **canal** (deben coincidir
con la pizarra) y confirma el cifrado (`WPA2 CCMP PSK`).

### 2. Captura del handshake
Fija airodump a ese BSSID/canal grabando a fichero y, en otra terminal, fuerza la reconexión de un
cliente **del laboratorio** con un deauth **corto** (`--deauth 5`, nunca `0`). Verifica que has
capturado el handshake:
```bash
aircrack-ng captura-01.cap        # debe decir: xest-lab  WPA (1 handshake)
```
> Si tu adaptador no entra en modo monitor, usa la captura de respaldo del aula e **indícalo** en el
> informe (no la presentes como tuya).

### 3. Crackeo offline
Rompe la clave por diccionario, con **cronómetro**:
```bash
time aircrack-ng -w /usr/share/wordlists/rockyou.txt captura-01.cap
# o la ruta hashcat:
hcxpcapngtool -o hash.22000 captura-01.cap
hashcat -m 22000 hash.22000 /usr/share/wordlists/rockyou.txt
```
Anota el **tiempo de diccionario** y la **velocidad** (`k/s` o `Speed` en H/s).

### 4. Demuestra el acceso
Conéctate a `xest-lab` con la clave recuperada (captura de pantalla):
```bash
nmcli dev wifi connect xest-lab password '<CLAVE>'
```

### 5. Mide la resistencia real (fuerza bruta)
Con **tu** velocidad medida, calcula cuánto tardaría una clave que **no** esté en el diccionario:
```bash
bash bench-wifi.sh                                  # tu H/s real
python3 tiempo_crackeo.py --rate <TU_H/s> --tabla   # tu tabla longitud x alfabeto
```

## Qué entregar (`NN-HE-E5-wifi.md`)

1. **Alcance y ROE**: solo `xest-lab`, BSSID/canal, referencia al ROE firmado (HE-E1).
2. **Captura**: comandos usados + evidencia `(1 handshake)`.
3. **Crackeo**: comando + evidencia `KEY FOUND!` / `Cracked` + la clave.
4. **Acceso demostrado**: captura de la conexión.
5. **Tiempo medido**: el de diccionario **y** el de fuerza bruta estimado con **tu** velocidad
   (incluye tu tabla de `tiempo_crackeo.py`).
6. **Conclusión de política**: qué longitud/entropía habría hecho inviable el ataque, con tus
   números, y por qué **WPA3** cambiaría el escenario.
7. Adjunta `captura-01.cap`.

## Cómo se evalúa (rúbrica R1 — resumen)
Ejecución técnica (llegas al acceso) · Evidencia y reproducibilidad (comandos y salidas que
permiten repetirlo) · **Verificación** (tu tiempo de fuerza bruta sale de TU medición, no copiado) ·
Higiene operativa (solo `xest-lab`, entorno restaurado) · Autonomía y tiempo. Detalle completo en
`~/xest-lab/2026-2027/docs/planificacion/rubricas.md`.
