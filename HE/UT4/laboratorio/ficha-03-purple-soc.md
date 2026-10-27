# HE · UT4 · Ficha 03 — Ejercicio de equipo morado: ¿qué vio el SOC?

> **Entorno**: VLAN aislada. El equipo **rojo** ejecuta; el **azul** analiza los registros del
> SOC **en la misma sesión**. **Vinculación**: RA2.f · produce el catálogo detectado/no
> detectado y la **regla que falta**, que entra en el informe **HE-E7** y en IC (UT3).

## Escenario

Durante la madrugada, el equipo rojo ejecutó tres técnicas contra xest-lab:

1. **Deauth flood + rogue AP** (evil twin del SSID `xest-lab`) — técnica de la UT3.
2. **Uso de una tarjeta RFID clonada** en los lectores de acceso (la de la Ficha 01, UID
   `DEADBEEF`).
3. **Replay de RF** del mando de garaje de código fijo (Ficha 02).

Tenéis los registros que dejó el SOC:

- `datos/soc-eventos/soc-alertas.json` — alertas del WIDS/Suricata/Wazuh.
- `datos/soc-eventos/lector-rfid.log` — accesos del control de puertas.

## Tarea (equipo azul)

1. Revisa las alertas del SOC:

   ```bash
   cd datos/soc-eventos
   cat soc-alertas.json | python3 -m json.tool 2>/dev/null || cat soc-alertas.json
   ```

2. Ejecuta la regla de detección de clon que el SOC **no** tenía:

   ```bash
   python3 detecta_clon_rfid.py lector-rfid.log
   ```

3. Rellena el **catálogo de contraste** (`NN-HE-UT4-ficha03.md`):

   | Técnica del rojo | ¿La detectó el SOC? | Evidencia (regla/alerta) | Regla que faltaría |
   |---|---|---|---|
   | Deauth flood | | | |
   | Rogue AP (evil twin) | | | |
   | RFID clonado usado | | | |
   | Replay RF garaje | | | |

4. **P1.** ¿Qué técnicas **sí** vio el SOC y con qué regla exacta?
5. **P2.** ¿Qué técnicas **no** vio? Para cada una, propón la **regla concreta** que faltaría
   (fuente de datos + condición). Para el RFID, apóyate en la salida de `detecta_clon_rfid.py`.
6. **P3.** El replay de RF no aparece en ningún log. ¿Por qué? ¿Qué haría falta para tener
   visibilidad de un ataque sub-GHz?
7. **[RETO azul]** Traduce el hallazgo de RFID a una **regla de correlación** en lenguaje
   natural lista para el SOC (formato "SI … Y … ENTONCES alerta"), lista para que IC la
   implemente en la UT3.

## Evidencia a guardar

- Catálogo de contraste completo + P1-P3 + regla del reto.
- **Esto cierra el ejercicio morado y da el hallazgo H-03 (rogue AP) y las recomendaciones de
  detección de tu informe HE-E7.** El listado "qué no detectó el azul" se entrega a IC.
