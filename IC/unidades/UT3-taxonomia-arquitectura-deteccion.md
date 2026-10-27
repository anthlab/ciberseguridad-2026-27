# IC · UT3 — Taxonomía de incidentes y arquitectura de detección

**12 horas** · RA2 (a, b) · Servicio SOC: Detección — recogida y correlación de eventos · Evidencias `IC-E4`, `IC-E5`

---

## 1. Objetivo de la unidad

Clasificar los incidentes con una taxonomía reconocida y montar la arquitectura que los detecta: fuentes de evento, SIEM/XDR, reglas de correlación y detección propia con Sigma. Es donde el SOC empieza a *ver*.

## 2. Contenido

### 2.1 Taxonomía de incidentes (RA2.a)

- **ENISA / eCSIRT.net v2** y **CCN-STIC 817**: categorías (código dañino, intrusión, disponibilidad, fraude, contenido abusivo...) y niveles de peligrosidad e impacto.
- Una taxonomía común permite priorizar, comparar y notificar con criterio.

### 2.2 Fuentes de evento (RA2.b)

| Fuente | Qué aporta | Sensor |
|---|---|---|
| Endpoint | Procesos, ficheros, persistencia | EDR/HIDS (Wazuh) |
| Red | Conexiones, protocolos, C2 | NIDS (Suricata/Zeek) |
| Identidad | Autenticaciones, cambios de permiso | Logs de directorio |
| Nube | Actividad de la cuenta | Logs del proveedor |
| Aplicación | Errores, accesos | Logs de la app |

### 2.3 SIEM/XDR (RA2.b)

Ingesta → normalización → correlación → reglas → alertas. La plataforma del proyecto está en [`SOC/plataforma/`](../../SOC/plataforma/): Wazuh (SIEM/XDR/HIDS) + Suricata (NIDS).

### 2.4 Ingeniería de detección (RA2.b)

- **Sigma**: reglas de detección portables, convertibles al lenguaje de cada SIEM.
- **MITRE ATT&CK** como taxonomía de TTPs y mapa de cobertura: qué técnicas detectamos y cuáles son puntos ciegos.

## 3. Laboratorio guiado

### Parte A — Desplegar sensores (RA2.b)

```bash
cd SOC/plataforma
# Wazuh single-node (SIEM/XDR/HIDS) + Suricata (NIDS) ya definidos en el compose
docker compose up -d
# Verificar que los agentes reportan y que Suricata genera eventos
docker compose ps
```

1. Despliega agentes Wazuh sobre un Windows y un Linux de laboratorio e integra Suricata como sensor de red. Verifica que las alertas llegan al panel.

### Parte B — Escribir reglas Sigma propias (RA2.b)

2. Escribe **dos reglas Sigma** nuevas (p. ej. shell inversa en Linux, comando PowerShell codificado). Parte de los ejemplos en [`SOC/plataforma/sigma/`](../../SOC/plataforma/sigma/).

```bash
# Convertir una regla Sigma al lenguaje del SIEM
sigma convert -t <backend> SOC/plataforma/sigma/mi_regla.yml
```

3. Despliega las reglas y **valídalas con un evento real** de laboratorio (genera la actividad y comprueba que dispara la alerta).

### Parte C — Mapa de cobertura ATT&CK (RA2.a, RA2.b)

4. Construye el mapa de cobertura del SOC de xest: qué técnicas ATT&CK detecta y cuáles no. Los huecos son la lista de trabajo.

## 4. Entregables

- **`IC-E4`** (informe, rúbrica R2): catálogo de taxonomía de incidentes de xest y matriz de fuentes de detección.
- **`IC-E5`** (reto integrado, rúbrica R3): reglas Sigma propias desplegadas y validadas con un evento real de laboratorio.

## 5. Criterios de superación

- Los sensores reportan de verdad (se comprueba que la telemetría llega).
- Las reglas Sigma se validan disparándolas con actividad real, no solo escribiéndolas.
- El mapa de cobertura identifica los puntos ciegos.

## 6. Errores frecuentes

- Dar por buena una regla porque «se escribió bien», sin generar el evento que la dispara.
- Un sensor silencioso toda la semana: está roto hasta que se demuestre lo contrario.

## 7. Referencias

- **CCN-STIC 817** · ENISA eCSIRT.net taxonomy.
- Sigma — [github.com/SigmaHQ/sigma](https://github.com/SigmaHQ/sigma)
- Wazuh, Suricata — documentación. MITRE ATT&CK Navigator.
