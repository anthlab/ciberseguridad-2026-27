# Ficha IC-E4 · Arquitectura de detección de xest (para el alumnado)

- **Evidencia**: IC-E4 · **RA2.b** · Instrumento I1 · Rúbrica **R1** (práctica de laboratorio).
- **Entrega**: `NN-IC-E4-arquitectura.md` + capturas del panel (`NN` = número de lista).
- **Dónde**: plataforma del SOC en `~/xest-lab/2026-2027/SOC/plataforma/`. Objetivos en
  `~/docencia/.../comun/entornos/objetivos/`. **Todo en la VLAN aislada de xest.**

> Una regla de oro para toda la ficha: **un sensor silencioso está roto hasta que se demuestre
> lo contrario.** No basta con desplegar: hay que probar que la telemetría llega.

---

## Parte A — Catálogo de taxonomía de incidentes de xest

1. Abre el fichero `taxonomia-incidentes-xest.csv` (12 incidentes de ejemplo de xest).
2. Para **cada** categoría ENISA/eCSIRT.net presente, anota su equivalente en **CCN-STIC 817**
   y el nivel de **peligrosidad** que le asignarías (CRÍTICO / ALTO / MEDIO / BAJO), justificando
   el porqué en una frase.
3. Construye la **matriz de fuentes de detección**: por cada fuente de evento (endpoint, red,
   identidad, nube, aplicación), qué sensor la recoge en el SOC de xest y qué categorías de
   incidente permite ver. Rellena esta tabla:

| Fuente de evento | Sensor en xest | Qué categorías de incidente detecta |
|---|---|---|
| Endpoint (procesos, ficheros) | | |
| Red (conexiones, DNS, protocolos) | | |
| Identidad (autenticaciones) | | |
| Nube (actividad de cuenta) | | |
| Aplicación (logs de la app) | | |

4. **Pregunta de cierre**: mirando tu matriz, ¿qué categoría de incidente del CSV **no** tiene
   hoy un sensor que la vea bien? Ése es tu primer punto ciego.

---

## Parte B — Desplegar los sensores y verificar que reportan

5. **Prerrequisito del anfitrión** (una vez):
   ```bash
   sudo sysctl -w vm.max_map_count=262144
   ```
6. Levanta el stack SIEM + NIDS (Wazuh + Suricata):
   ```bash
   cd ~/xest-lab/2026-2027/SOC/plataforma
   docker compose --profile nids up -d
   docker compose ps
   ```
   Espera a que todos los servicios estén `healthy`. Entra al panel en
   `https://<ip-del-soc>:5601` (o `soc.xest.local`) con las credenciales del `.env`.

7. **Agente Linux**: instala el agente Wazuh en una máquina Linux de laboratorio y regístrala
   contra el manager. Verifica en el panel que el agente aparece como **Active**.

8. **Agente Windows**: instala el agente Wazuh en un Windows de laboratorio. Para tener
   `process_creation` en Windows, integra **Sysmon**. Verifica que reporta.

9. **Telemetría de endpoint en Linux**: comprueba que el manager recibe eventos de creación de
   proceso (auditd/execve o Sysmon-for-Linux). Sin esto, muchas reglas nunca dispararán.

10. **Suricata (NIDS)**: comprueba que genera `eve.json` y que Wazuh lo ingiere. Genera algo de
    tráfico contra un objetivo de laboratorio y localiza el evento en el panel.

11. **CHECKPOINT obligatorio**: dispara **una** alerta de verdad y encuéntrala en el panel.
    ```bash
    # en la máquina Linux con agente, dentro de la VLAN:
    sudo bash generar-actividad.sh reverse
    ```
    Debe aparecer una alerta de "reverse shell candidata" en *Threat Hunting*. Captura la pantalla.

---

## Qué entregar (`NN-IC-E4-arquitectura.md`)

- El **catálogo de taxonomía** (Parte A) y la **matriz de fuentes** rellena.
- Evidencia de despliegue: salida de `docker compose ps`, captura de los **agentes Active**.
- **Prueba de telemetría**: la captura de la alerta del CHECKPOINT (paso 11), con la marca de
  tiempo. Esto es lo que demuestra que el SOC *ve* de verdad.
- Tus **puntos ciegos** iniciales (pregunta 4 y paso 10 fallido si lo hubo).

> R1 valora especialmente la **verificación del resultado** (20 %): no vale "desplegado", vale
> "desplegado y **comprobado** con un evento real que llega al panel".
