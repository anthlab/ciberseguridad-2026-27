# IC 5021 — Cuaderno de entregables (enunciados para el alumnado)

Reglas: entrega por número de lista `NN-IC-EX-<nombre>`. Se opera sobre la plataforma del
SOC (`~/xest-lab/2026-2027/SOC/plataforma/`). **RA5 (UT8) es eliminatorio**: sin
notificar en plazo, el módulo no se supera.

---

## IC-E1 · Política y normativa del SOC (UT1 · I2/R2)
Política de ciberseguridad del SOC de xest (objeto, alcance, principios, roles, aprobación
de dirección) + normativa del puesto **exigible y verificable**. Distingue política /
normativa / procedimiento / registro. **Entrega**: `NN-IC-E1-gobierno.pdf`.

## IC-E2 · Plan de concienciación (UT2 · I2/R2)
Campaña de 4 semanas para el personal ficticio de xest: público segmentado, canales,
calendario, materiales y **métricas desde el diseño**. **Entrega**: `NN-IC-E2-plan.md` +
materiales.

## IC-E3 · Simulacro de phishing (UT2 · I1/R1)
Simulacro con GoPhish sobre **buzones de laboratorio y con consentimiento**, con métricas
(clic, reporte, tiempo al primer aviso) **leídas críticamente** + auditoría de cumplimiento.
**Entrega**: `NN-IC-E3-simulacro.md`.

## IC-E4 · Arquitectura de detección (UT3 · I1/R1)
Wazuh + Suricata desplegados con agentes en Windows y Linux de laboratorio **reportando al
panel**. **Entrega**: `NN-IC-E4-arquitectura.md` + capturas del panel.

## IC-E5 · Reglas Sigma y cobertura (UT3 · I3/R3)
Reglas Sigma propias convertidas al SIEM + **mapa de cobertura ATT&CK** con los puntos
ciegos señalados. **Entrega**: `reglas/*.yml` + `NN-IC-E5-cobertura.md`.

## IC-E6 · Detección física integrada (UT4 · I2/R2)
Inventario de controles físicos de xest y su **ruta de alerta** al SOC (qué evento físico
genera qué alerta lógica). **Entrega**: `NN-IC-E6-fisica.md`.

## IC-E7 · Vigilancia OSINT del dominio (UT4 · I1/R1)
Vigilancia de `xest.local`: certificados, subdominios, credenciales expuestas,
typosquatting, con **contraste de segunda fuente** antes de elevar y **descartes
justificados**. **Entrega**: `NN-IC-E7-osint.md`.

## IC-E8 · Procedimiento de triaje (UT5 · I2/R2)
Procedimiento de triaje del SOC + **matriz de priorización** (criticidad × alcance ×
confianza). **Entrega**: `NN-IC-E8-triaje.md`.

## IC-E9 · Caso en TheHive + contención (UT5 · I3/R3)
Caso completo en TheHive (observables, analizadores de Cortex, tareas, timeline, TLP) sobre
el incidente de HE, con **contención inicial que preserva la evidencia**.
**Entrega**: export del caso + `NN-IC-E9-caso.md`.

## IC-E10 · Adquisición y análisis forense (UT6 · I1/R1)
Adquisición (orden de volatilidad, hash de cada pieza) y análisis (Volatility 3,
Velociraptor) de la máquina comprometida por HE. **Entrega**: `NN-IC-E10-forense.md` +
hashes.

## IC-E11 · Timeline, causa raíz e intercambio (UT6 · I3/R3)
Línea de tiempo mapeada a ATT&CK, **causa raíz** (vector, no síntoma) e IoC compartidos en
**MISP/STIX 2.1** con TLP. Contrasta la reconstrucción con el documento HE-E12.
**Entrega**: `NN-IC-E11-investigacion.md` + export STIX.

## IC-E12 · Playbooks (UT7 · I2/R2)
Los **seis playbooks** del SOC (ransomware, phishing/BEC, malware, exfiltración, DDoS,
cuenta comprometida) con estructura NIST y decisión por fase.
**Entrega**: `playbooks/*.md`.

## IC-E13 · Respuesta ejecutada (UT7 · I3/R3)
Sobre el incidente de HE: **erradicación** (usando los IoC de HE-E14, sin dejar puertas) +
**recuperación desde copia verificada** + monitorización reforzada. **Entrega**:
`NN-IC-E13-respuesta.md` + evidencia de la verificación de ausencia de persistencia.

## IC-E14 · Lecciones aprendidas (UT7 · I2/R2)
Retrospectiva **sin culpables**: qué falló en el proceso + acciones correctoras con
**responsable y fecha** + retroalimentación a PPS y HE. **Entrega**: `NN-IC-E14-lecciones.md`.

## IC-E15 · Árbol de decisión de notificación (UT8 · I1/R1)
Dado el incidente del ejercicio: qué marcos aplican (RGPD 33/34, NIS2, ENS, DORA), con qué
**plazo** y a quién. **Entrega**: `NN-IC-E15-arbol.md`.

## IC-E16 · Notificaciones redactadas (UT8 · I2/R2)
Borrador de **notificación a la AEPD en 72 h** (`IC/material/notificacion/rgpd-72h.md`) y
**alerta temprana NIS2 en 24 h** (`nis2-24h.md`) para el incidente real. Redacción
cronometrada. **Entrega**: `NN-IC-E16-aepd.md` + `NN-IC-E16-nis2.md`.

## IC-E17 · Comunicación pública (UT8 · I4/R4)
Rueda de prensa simulada (portavoz único, mensaje base, preguntas hostiles) + prueba
objetiva escrita (la entrega el profesor en el aula). Se evalúa en vivo.
