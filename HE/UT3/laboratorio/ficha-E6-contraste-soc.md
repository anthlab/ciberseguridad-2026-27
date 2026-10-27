# HE-E6 · Contraste rojo-azul Wi-Fi (UT3 · para el alumnado)

**Objetivo**: documentar **qué detectó el SOC** del ataque inalámbrico (deauth, rogue AP, uso de la
credencial) y **qué no**, y proponer la **regla de detección que faltaría**.

- **RA/CE**: RA2.d. **Instrumento/Rúbrica**: I3 · **R3** (reto integrado — pesa más).
- **Se entrega también a Incidentes (IC UT3)** como caso de ingeniería de detección.
- **Entrega**: `NN-HE-E6-contraste.md` (por número de lista).

## Qué tienes que hacer

### 1. Reproduce el ataque con marca de tiempo
Repite el deauth y, después, **usa la clave** para conectarte, anotando la **hora exacta** de cada
acción (es tu *ground truth* para correlacionar):
```bash
date; sudo aireplay-ng --deauth 5 -a <BSSID> -c <MAC_cliente> wlan0mon
date; nmcli dev wifi connect xest-lab password '<CLAVE>'
```

### 2. Ve al SOC y busca cada acción
En el SOC de xest (`soc.xest.local`, Wazuh/Suricata), filtra por tu ventana horaria y comprueba,
**con evidencia** (captura o salida), qué aparece de cada cosa:
```bash
grep -i "deauth\|dot11\|80211" /var/log/suricata/eve.json | head   # ¿algo? (probablemente NADA)
```
Rellena la tabla:

| Acción del ataque | ¿La ve tu SOC? | Evidencia |
|---|---|---|
| Modo monitor / captura | | |
| Deauth | | |
| Crackeo offline | | |
| Conexión con la clave robada | | |

### 3. Identifica el punto ciego
Explica **por qué** el SOC no ve (o ve poco): ¿en qué capa ocurre el ataque y dónde "mira" el SOC?

### 4. Propón la regla que falta
Diseña la detección que cubriría el hueco: **qué fuente** hace falta, **qué umbral**, y **qué regla**
(esboza una regla de Wazuh o describe la alerta del sensor). Asóciala a su técnica **MITRE ATT&CK**.

### 5. Remediación priorizada
Ordena las defensas por impacto/coste (¿qué es gratis y ya está en el estándar?).

## Qué entregar (`NN-HE-E6-contraste.md`)
1. Qué atacaste y **cuándo** (marcas horarias).
2. Tabla **qué vio / qué no vio** con evidencia de cada celda.
3. El **punto ciego** identificado con precisión.
4. **La regla que falta**: fuente + umbral + regla + técnica ATT&CK.
5. **Remediación priorizada**.
6. Nota de **entrega a IC**: qué debería hacer Incidentes con esto.

## Cómo se evalúa (rúbrica R3 — resumen)
Integración con el SOC (tu pieza conecta con lo que hará IC) · Solución técnica (eliges y justificas)
· Automatización/repetibilidad (la detección es reproducible) · Trabajo en el repositorio ·
Iteración sobre la retroalimentación. Detalle en
`~/xest-lab/2026-2027/docs/planificacion/rubricas.md`.
