# Laboratorio L1 · Detección física integrada en el SOC (IC · UT4, Sesión 1)

> Ficha del alumnado. Trabajas sobre `datos/` de esta carpeta y sobre la plataforma SOC
> (`~/xest-lab/2026-2027/SOC/plataforma/`). Todo ocurre en la **VLAN aislada del aula**.
> Al terminar habrás producido el borrador de **IC-E6**.

## Objetivo

Conectar la seguridad física con el SOC: que un **evento físico** (rack abierto, USB,
tailgating) se convierta en una **alerta lógica** con regla, nivel y prioridad. Un control
físico que no llega al SOC es un punto ciego.

## Materiales

- `datos/eventos-fisicos.log` — 11 eventos del PACS de xest (control de accesos, CCTV, USB).
- `datos/inventario-controles-fisicos.csv` — inventario parcial de controles (hay filas por completar).
- `wazuh/local_decoder-fisica.xml` y `wazuh/local_rules-fisica.xml` — decoder y reglas.
- `probar-reglas.sh` — banco de pruebas offline si no tienes Wazuh a mano.
- Plantilla del entregable: `plantillas/IC-E6-ruta-de-alerta.md`.

## Parte A · Leer los eventos físicos (10 min)

1. Mira el formato del log: `head -3 datos/eventos-fisicos.log`. Identifica los campos
   `event`, `zone`, `asset`, `actor`, `result`, `out_of_hours`.
2. Cuenta cuántos eventos hay de cada tipo:
   ```bash
   grep -oP 'event=\K\S+' datos/eventos-fisicos.log | sort | uniq -c | sort -rn
   ```
3. **Pregunta**: ¿cuáles de esos eventos deberían generar una alerta y cuáles son actividad
   normal? Anótalo antes de seguir.

## Parte B · Instalar decoder + reglas y probar (25 min)

**Opción 1 — con Wazuh levantado** (SOC/plataforma):
```bash
# copiar decoder y reglas al manager
sudo cat wazuh/local_decoder-fisica.xml >> /var/ossec/etc/decoders/local_decoder.xml
sudo cat wazuh/local_rules-fisica.xml   >> /var/ossec/etc/rules/local_rules.xml
sudo /var/ossec/bin/wazuh-control restart
# probar una línea con el banco de pruebas de Wazuh
sudo /var/ossec/bin/wazuh-logtest
# pega:  Nov 04 22:14:05 pacs01 xestpacs: event=rack_open zone=cpd asset=rackA actor=UNKNOWN result=unknown out_of_hours=yes
```

**Opción 2 — sin Wazuh** (banco de pruebas offline):
```bash
bash probar-reglas.sh datos/eventos-fisicos.log
```

Anota, para cada alerta que dispara: **regla (id), nivel y por qué**.

## Parte C · Completar el inventario y la ruta de alerta (35 min)

Abre `datos/inventario-controles-fisicos.csv`. Cuatro controles tienen `integrado_soc = NO`
y sin evento/alerta. Decide, para cada uno, si debe integrarse y con qué evento y alerta.
Rellena la plantilla `plantillas/IC-E6-ruta-de-alerta.md`:

- Tabla de inventario completa (10 filas).
- Tabla de **ruta de alerta**: evento físico → control → regla SOC → alerta lógica (nivel) → prioridad.
- Sección de **puntos ciegos** declarados.

## Entrega

El borrador de `NN-IC-E6-fisica.md` a partir de la plantilla, con la salida de verificación
pegada (Parte B). Se termina y pule como IC-E6 (rúbrica R2).

## Reglas del aula

Nada de esto se ejecuta contra la red del centro ni contra Internet: solo la VLAN aislada.
Los datos del PACS son sintéticos; no hay personas reales.
