# Ficha HE-E13 · Ataque a credenciales y política de contraseñas (RA4.b · rúbrica R1)

> Solo VLAN de laboratorio. Los ficheros `hashes-lab.txt` (NTLM del volcado AD) y
> `shadow-lab.txt` (sha512crypt del host Linux) son **sintéticos**: ningún dato real.

## Objetivo
Recuperar el máximo de contraseñas de dos volcados de laboratorio, **midiendo** qué tipo de
ataque rompe cada una y **cuánto cuesta**, para concluir una **política de contraseñas medible**
(no "usa contraseñas fuertes", sino "≥ N caracteres / tal función de derivación").

## Material
- `hashes-lab.txt` — volcado estilo *secretsdump* (NTLM, rápido). 9 cuentas.
- `shadow-lab.txt` — volcado `/etc/shadow` (sha512crypt, lento por diseño). 3 cuentas.
- `rockyou.txt` (`/usr/share/wordlists/rockyou.txt`) y reglas de hashcat (`/usr/share/hashcat/rules/`).

## Pasos

1. **Prepara los hashes NT.** Del volcado *secretsdump* solo se ataca el campo NT:
   ```bash
   cut -d: -f4 hashes-lab.txt > nt.txt
   ```
2. **Diccionario recto** (NTLM, modo 1000):
   ```bash
   hashcat -m 1000 -a 0 nt.txt /usr/share/wordlists/rockyou.txt --potfile-path e13.pot
   ```
   Anota **cuántas cae** y **el tiempo** (`Time.Started`/`Time.Estimated` en la salida).
3. **Diccionario + reglas** (mutaciones: mayúsculas, sufijos, l33t):
   ```bash
   hashcat -m 1000 -a 0 nt.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --potfile-path e13.pot
   ```
4. **Máscara / híbrido** para el patrón corporativo `Palabra + Año + símbolo`:
   ```bash
   # híbrido: palabra de rockyou + 4 dígitos + 1 símbolo
   hashcat -m 1000 -a 6 nt.txt /usr/share/wordlists/rockyou.txt '?d?d?d?d?s' --potfile-path e13.pot
   ```
5. **Muestra lo crackeado** y crúzalo con el usuario:
   ```bash
   hashcat -m 1000 nt.txt --show --potfile-path e13.pot
   # para asociar hash->usuario usa el volcado con --username:
   hashcat -m 1000 -a 0 hashes-lab.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --username --show
   ```
6. **Repite contra el shadow Linux** (modo 1800, sha512crypt) y **compara el tiempo** con NTLM:
   ```bash
   hashcat -m 1800 -a 0 shadow-lab.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule
   ```
   > Observa que con la MISMA wordlist el sha512crypt va **mucho** más lento. Ese es el punto.

## Qué entregar (`NN-HE-E13-credenciales.md`)
- Tabla: **usuario → contraseña → ataque que la rompió → tiempo/velocidad (H/s)**.
- Cuántas cuentas quedaron **sin romper** y por qué.
- Al menos **una reutilización de contraseña** detectada y su implicación.
- **Conclusión de política medible**: longitud/entropía mínima que habría hecho inviable el
  crackeo en tu hardware, y por qué el algoritmo de almacenamiento (NTLM vs sha512crypt vs
  Argon2) cambia el resultado. Conecta con **PPS UT5** (almacenamiento seguro de secretos).

## Preguntas de cierre
1. ¿Por qué el hash NT vacío (`31d6cfe0...`) aparece "roto" al instante? ¿Qué representa?
2. Dos cuentas comparten el mismo hash NT. ¿Qué significa y qué riesgo añade?
3. Si el volcado fuese Argon2id en vez de NTLM, ¿cambiaría tu estrategia? ¿Cuál sería?
