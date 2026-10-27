# Ficha IC-E10 · Adquisición y análisis forense (para el alumnado)

**Evidencia**: IC-E10 · RA3 a,b · Instrumento I1 · Rúbrica **R1** (práctica de laboratorio).
**Caso**: intrusión que HE produjo en `xest` (máquina `WIN-XEST-ADM`, 10.10.10.50).
**Entorno**: VLAN aislada de laboratorio. Trabajas sobre el **snapshot** de la máquina
comprometida y el volcado `memoria.raw` que ha preparado el docente. Bolsa de evidencias de
referencia en `evidencias/`.

> Regla de aula: no se toca ningún host fuera de la VLAN de laboratorio. La memoria se
> analiza sobre copia; el original se preserva y se hashea. **Conserva integridad, procedencia y cadena de custodia; un hash por sí solo no acredita todo ello.**

## Parte A — Adquisición con criterio forense (RA3.a)

1. Ordena las evidencias por **volatilidad** (¿qué adquieres primero y por qué?).
2. Adquiere memoria y artefactos dirigidos con **Velociraptor**; genera el **hash** de cada
   pieza en el momento de la adquisición.
3. Abre la **cadena de custodia** (`plantilla-cadena-custodia.md`): una fila por evidencia con
   quién, cuándo, hash y dónde queda depositada.

**Comprobación**: `sha256sum -c` sobre tu manifiesto reproduce los hashes sin error.

## Parte B — Análisis de memoria con Volatility 3 (RA3.b)

Sobre `memoria.raw`, ejecuta y **guarda la salida** de:

```bash
vol -f memoria.raw windows.pslist
vol -f memoria.raw windows.pstree
vol -f memoria.raw windows.cmdline
vol -f memoria.raw windows.netscan
vol -f memoria.raw windows.malfind
```

Responde en tu informe (usa `plantilla-informe-forense.md`):

1. ¿Qué proceso es **anómalo** y por qué? (nombre, PID, ruta, proceso padre).
2. ¿A qué dirección y puerto abre **conexión de red** ese proceso? ¿Qué es?
3. ¿Qué evidencia de **código inyectado** encuentras? ¿En qué proceso(s)?
4. Descodifica la línea de comandos de `powershell.exe`. ¿Qué hace?
5. ¿Qué **persistencia** dejó el atacante? (revisa `velociraptor-autoruns.csv`).

**Entrega**: `NN-IC-E10-forense.md` (informe) + `hashes.txt` (manifiesto de integridad) +
las salidas `vol-*.txt`. Correlación fina y causa raíz → se completa en **IC-E11**.
