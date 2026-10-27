# Ficha PPS-E13 — La canalización que BLOQUEA

**UT7 · RA5 a,c,g · Instrumento I3 · Rúbrica R3 (reto integrado) · Semana 15**
Entrega: PR en el repo + captura del build **en rojo** que bloquea la fusión.

## Objetivo

Montar en el repositorio del proyecto una canalización de integración continua con **cuatro
controles de seguridad** (SAST, SCA, secretos, IaC) configurada en **modo bloqueo**, y demostrar
con un **caso que debe fallar** que impide la fusión. No vale que avise: tiene que **impedir**.

## Punto de partida

- Mini-servicio vulnerable: `portal-mini/` (SQLi + dependencias con CVE + Dockerfile/Terraform
  mal configurados). Es lo que los controles deben detectar.
- Canalización de referencia (modo aviso): `~/xest-lab/2026-2027/PPS/material/pipeline/ci-seguridad.yml`.
- Canalización endurecida (modo bloqueo): `ci/ci-seguridad-bloquea.yml`.
- Regla Semgrep propia del curso: `semgrep-reglas/sqli-concat.yml`.

## Parte A — Ensaya los controles en LOCAL (antes de subir)

```bash
cd portal-mini
semgrep --config p/owasp-top-ten --config ../semgrep-reglas/sqli-concat.yml --sarif -o semgrep.sarif .
trivy fs --format sarif -o trivy.sarif .
gitleaks detect --source . --report-format sarif --report-path gitleaks.sarif --redact
checkov -d . --output sarif --output-file-path .
```

Abre cada SARIF y localiza **qué** encontró cada herramienta y **en qué fichero/línea**. Anótalo:
esos artefactos son los que el SOC de Incidentes (IC) ingiere.

## Parte B — Monta la canalización en modo bloqueo

1. Copia `ci/ci-seguridad-bloquea.yml` al repo como `.github/workflows/ci-seguridad.yml`.
2. Comprueba que **ningún** control lleva `|| true` ni `soft-fail`: un hallazgo debe dar exit 1.
3. La rama `main` (PPS-E12) exige que este workflow pase en verde para poder fusionar.

## Parte C — El caso que DEBE fallar

1. Crea una rama, añade `caso-que-debe-fallar/config-con-secreto.py` (secreto **falso**) y, opcionalmente,
   deja las dependencias con CVE de `portal-mini/requirements.txt`.
2. Abre un PR contra `main`.
3. **Comprueba y captura** que la CI se pone en **rojo** (falla al menos el job de secretos y el de
   SCA) y que **la fusión queda bloqueada**.
4. Revierte: quita el secreto, deja la rama principal limpia y documenta la evidencia del bloqueo.

## Qué entregas

- El PR con el workflow en el repositorio (ejecutándose en cada PR, no un fichero de ejemplo).
- Captura del **build en rojo** con la fusión bloqueada + qué control lo paró.
- Breve nota: qué encontró cada control en local (Parte A) y dónde llegan los SARIF (SOC de IC).

## Se valora (R3, resumen)

- **Automatización y repetibilidad**: la CI corre sola en cada PR y es reproducible desde cero.
- **Integración con el SOC**: los SARIF llegan a la gestión de vulnerabilidades de IC.
- **Prueba del bloqueo**: la evidencia decisiva es el **caso que falla**, no la CI en verde.
  Una canalización que solo has visto pasar en verde **no está probada** como barrera.
