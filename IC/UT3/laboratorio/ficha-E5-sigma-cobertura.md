# Ficha IC-E5 · Reglas Sigma propias y mapa de cobertura (para el alumnado)

- **Evidencia**: IC-E5 · **RA2.b** · Instrumento I3 · Rúbrica **R3** (reto integrado).
- **Entrega**: `reglas/*.yml` (tus reglas) + `NN-IC-E5-cobertura.md` (informe + capa ATT&CK).
- **Requisito previo**: IC-E4 desplegado y con telemetría de proceso verificada.
- **Todo en la VLAN aislada de xest.**

> Consigna central: **una regla que no se ha disparado con un evento real no está validada.**
> Cada regla que escribas la validarás generando la actividad que debe detectar.

---

## Parte A — Escribe DOS reglas Sigma propias (nuevas)

Parte de los 5 ejemplos base en `~/xest-lab/2026-2027/SOC/plataforma/sigma/` **sin
copiarlos**. Elige dos técnicas ATT&CK que hoy sean punto ciego y escribe una regla para cada
una. Sugerencias (elige 2, o propón las tuyas justificándolo):

1. **Descarga y ejecución en una línea** — `curl|bash` / `wget|sh` (T1105 + T1059.004).
2. **Lectura de ficheros de credenciales** — `/etc/shadow`, `~/.ssh/id_rsa` (T1003.008/T1552).
3. **Fuerza bruta SSH** — N fallos de login del mismo origen en poco tiempo (T1110).
4. **Minería de cripto** — proceso con CPU sostenida al 100 % + dominio de pool (T1496).

Cada regla debe tener, como mínimo: `title`, `id` (UUID nuevo), `logsource`, `detection` con
al menos un `condition`, `tags` ATT&CK, `falsepositives` **realistas** y `level`.

## Parte B — Convierte las reglas al lenguaje del SIEM

```bash
cd ~/xest-lab/2026-2027/SOC/plataforma/sigma
./convertir.sh tu_regla.yml > /tmp/tu_regla.xml
cat /tmp/tu_regla.xml
```
Copia la regla resultante a `local_rules.xml` del manager y recarga:
```bash
docker compose exec wazuh.manager /var/ossec/bin/wazuh-control reload
# si tu versión no aplica reload en caliente:
docker compose restart wazuh.manager
```

## Parte C — Valida cada regla con un evento REAL

En la máquina Linux de laboratorio con agente, dentro de la VLAN:
```bash
sudo bash generar-actividad.sh download   # dispara la regla curl|bash
sudo bash generar-actividad.sh            # dispara las cuatro técnicas
```
Localiza **cada** alerta en el panel de Wazuh. Anota: regla, marca de tiempo, campo que hizo
match. Si una regla **no** dispara con su evento, corrígela: casi siempre falta el campo en la
fuente o el `logsource` no coincide. Repite hasta que dispare.

**Al terminar, limpia el entorno**:
```bash
sudo bash generar-actividad.sh --limpiar
```

## Parte D — Mapa de cobertura ATT&CK

1. Abre **MITRE ATT&CK Navigator** (`https://mitre-attack.github.io/attack-navigator/`).
2. Marca en **verde** las técnicas que el SOC detecta con reglas **validadas** (las 5 base +
   tus 2 nuevas), y en **rojo** los **puntos ciegos** que has identificado.
3. Exporta la capa como JSON y adjúntala.

---

## Qué entregar (`NN-IC-E5-cobertura.md` + `reglas/*.yml` + capa JSON)

- Tus **2 reglas Sigma** (`reglas/`), con la justificación de la técnica elegida.
- **Evidencia de validación**: por cada regla, la captura de la alerta disparada con
  `generar-actividad.sh` y el campo que hizo match. Sin esto, la regla no cuenta como validada.
- La **capa ATT&CK Navigator** (JSON) con verde = cubierto, rojo = punto ciego.
- Los **puntos ciegos priorizados**: cuál cerrarías primero y por qué (impacto × probabilidad).

> R3 valora **automatización y repetibilidad** (20 %) y **verificación**: tu entrega debe poder
> repetirse desde cero con `convertir.sh` + `generar-actividad.sh`. Y valora la **integración**
> (25 %): tus puntos ciegos alimentan el triaje de UT5 y la investigación de UT6.
