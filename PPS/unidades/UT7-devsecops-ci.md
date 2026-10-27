# PPS · UT7 — DevSecOps: control de versiones, construcción e integración continua

**10 horas** · RA5 (a, b, c, g) · Servicio SOC: Prevención — canalización segura · Evidencias `PPS-E12`, `PPS-E13`

---

## 1. Objetivo de la unidad

Todo lo aprendido en las unidades anteriores se automatiza aquí: la canalización de integración continua ejecuta los controles de seguridad en cada cambio y **bloquea** el que no cumple. El criterio de la unidad es que la canalización impida el error, no que lo avise cuando ya está en producción.

## 2. Contenido

### 2.1 DevOps y DevSecOps (RA5.a)

- Principios: flujo (entregas pequeñas y frecuentes), retroalimentación rápida, experimentación continua.
- DevSecOps = mover la seguridad a la izquierda: los controles se ejecutan en el desarrollo, no en una auditoría final.

### 2.2 Control de versiones (RA5.b)

- Estrategia de ramas y **protección de la rama principal**: nada entra sin revisión y sin CI en verde.
- Revisión por pares obligatoria; roles y permisos mínimos.
- Firma de confirmaciones (opcional pero recomendable) para trazabilidad de autoría.

### 2.3 Construcción e integración continua (RA5.c)

Controles que ejecuta la canalización, cada uno emitiendo un artefacto (JSON/SARIF) que el SOC ingiere:

| Control | Herramienta | Qué detecta |
|---|---|---|
| SAST | Semgrep, Bandit | Vulnerabilidades en el código |
| SCA | Trivy fs, osv-scanner | Dependencias con CVE |
| Secretos | gitleaks | Credenciales en el repositorio |
| IaC | Checkov, tfsec | Mala configuración de infraestructura |
| Imagen | Trivy image | Vulnerabilidades en la imagen de contenedor |

### 2.4 Bucles de retroalimentación (RA5.g)

- Revisión de código como control de calidad y de seguridad.
- Métricas DORA (frecuencia de despliegue, tiempo de entrega, tasa de fallo, tiempo de recuperación).
- Retrospectivas que convierten incidentes en mejoras del proceso.

## 3. Laboratorio guiado

> Entorno: repositorio del proyecto. Canalización de referencia en `PPS/material/pipeline/` (GitHub Actions y equivalente GitLab CI).

### Parte A — Proteger la rama y el flujo de revisión (RA5.b)

1. Configura la protección de la rama principal: revisión obligatoria, CI requerido, prohibido el empuje directo.
2. Documenta el flujo: rama de trabajo → PR → revisión por par → CI en verde → fusión.

### Parte B — Canalización de seguridad (RA5.a, RA5.c)

3. Adapta la canalización de `PPS/material/pipeline/ci-seguridad.yml` al proyecto: SAST (Semgrep), SCA (Trivy), secretos (gitleaks), IaC (Checkov). Cada trabajo emite SARIF.

```bash
# Ejecutar los mismos controles en local antes de subir
semgrep --config p/owasp-top-ten --sarif -o semgrep.sarif .
trivy fs --format sarif -o trivy.sarif .
gitleaks detect --report-format sarif --report-path gitleaks.sarif
checkov -d . -o sarif > checkov.sarif
```

### Parte C — Demostrar el bloqueo (RA5.c, RA5.g)

4. Introduce **deliberadamente** un secreto de prueba y una dependencia vulnerable conocida en una rama, abre un PR y demuestra que la canalización **falla y bloquea** la fusión.
5. Revierte, deja la rama principal limpia y documenta la evidencia del bloqueo.

## 4. Entregables

- **`PPS-E12`** (reto integrado, rúbrica R3): canalización de integración continua ejecutable con al menos cuatro controles de seguridad y artefactos SARIF.
- **`PPS-E13`** (laboratorio, rúbrica R1): evidencia de que la canalización bloquea automáticamente ante un secreto y ante una dependencia vulnerable.

## 5. Criterios de superación

- La canalización **corre** en el repositorio (se ejecuta en cada PR), no es un fichero de ejemplo.
- La rama principal está protegida: no se puede fusionar con CI en rojo.
- El bloqueo se demuestra con un caso real (secreto + dependencia vulnerable).

## 6. Errores frecuentes

- Configurar los controles en modo aviso y no en modo bloqueo: informan pero no impiden nada.
- Proteger la rama pero permitir que el propietario del repositorio se salte la revisión.
- Emitir SARIF que nadie ingiere: el artefacto debe llegar a la gestión de vulnerabilidades del SOC.

## 7. Referencias

- OWASP **DevSecOps Maturity Model** — [dsomm.owasp.org](https://dsomm.owasp.org)
- NIST SP 800-218 (SSDF).
- Semgrep, Trivy, gitleaks, Checkov — documentación oficial.
- Estado del arte DORA (DevOps Research and Assessment).
