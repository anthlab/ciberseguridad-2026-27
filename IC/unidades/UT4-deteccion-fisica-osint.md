# IC · UT4 — Detección de incidentes de seguridad física e inteligencia de fuentes abiertas

**8 horas** · RA2 (c, d) · Servicio SOC: Detección — vigilancia y alerta temprana · Evidencias `IC-E6`, `IC-E7`

---

## 1. Objetivo de la unidad

No todos los incidentes empiezan en la red. Esta unidad cubre dos fuentes de alerta que el SIEM clásico no ve: la **seguridad física** (con impacto lógico) y la **inteligencia de fuentes abiertas** (OSINT) como alerta temprana de exposición y filtración.

## 2. Contenido

### 2.1 Detección de incidentes físicos (RA2.c)

- Telemetría física integrable en el SIEM: control de accesos, CCTV, sensores ambientales.
- Incidentes físicos con impacto lógico: sustracción de equipo, acceso a rack, *tailgating*, USB no autorizado.
- Ruta de alerta: del control físico al SOC.

### 2.2 OSINT como alerta temprana (RA2.d)

- Filtraciones de credenciales (HIBP, foros, canales).
- Exposición de activos (certificados, subdominios, puertos indexados).
- Typosquatting: dominios parecidos registrados para phishing.
- Menciones de la organización en foros y darknets.

### 2.3 Higiene de la investigación OSINT (RA2.d)

- Legalidad y proporcionalidad: solo fuentes abiertas, sin acceso no autorizado.
- Trazabilidad: cada hallazgo con su fuente y fecha.
- **Verificación con segunda fuente** antes de elevar a alerta: un dato sin contrastar es un rumor, no una alerta.

## 3. Laboratorio guiado

### Parte A — Detección física integrada (RA2.c)

1. Diseña el inventario de controles físicos de xest (accesos, CCTV, sensores) y define su **ruta de alerta** hacia el SOC: qué evento físico genera qué alerta lógica.

### Parte B — Vigilancia OSINT del dominio (RA2.d)

```bash
# Subdominios y certificados
curl -s "https://crt.sh/?q=%25.xest.local&output=json" | jq -r '.[].name_value' | sort -u
# Credenciales expuestas (comprobación por dominio)
# Consulta a HIBP u equivalente autorizado
# Dominios similares (typosquatting)
dnstwist xest.local
```

2. Vigila el dominio de xest: certificados, subdominios, credenciales expuestas, dominios similares. **Contrasta cada hallazgo con una segunda fuente** antes de elevarlo.

### Parte C — Descarte justificado

3. Para cada hallazgo, decide si es alerta o falso positivo y **justifica el descarte**. Un descarte sin argumento cuenta como error.

## 4. Entregables

- **`IC-E6`** (informe, rúbrica R2): procedimiento de detección física integrado en el SOC.
- **`IC-E7`** (reto integrado, rúbrica R3): informe de vigilancia OSINT con hallazgos verificados y descartados, y la justificación de cada descarte.

## 5. Criterios de superación

- El procedimiento físico conecta el evento físico con la alerta en el SOC.
- Cada hallazgo OSINT está contrastado con segunda fuente antes de elevarse.
- Los descartes están justificados.

## 6. Ética y legalidad

OSINT solo sobre fuentes abiertas y de forma proporcionada. No se accede a sistemas ni
a cuentas; no se explota nada. La investigación se documenta con trazabilidad de la
fuente.

## 7. Referencias

- CCN-STIC 896 — vigilancia y alerta.
- crt.sh, dnstwist, HIBP.
- CCN-STIC 817 — clasificación de incidentes.
