# PPS 5023 — Matriz de evidencias

Rúbricas oficiales: `~/xest-lab/2026-2027/docs/planificacion/rubricas.md`. Enunciados:
`entregables.md`. Semana según `../../calendario-semanal.md`.

| Evidencia | UT | RA·CE | Instrumento·Rúbrica | Semana | Descripción breve |
|---|---|---|---|---|---|
| PPS-E1 | UT1 | RA1 a-c | I2 · R2 | 3 | Lectura comparada entrada→sink en 3 modelos de ejecución |
| PPS-E2 | UT1 | RA1 d | I1 · R1 | 3 | Suite de pruebas + cobertura + test de regresión |
| PPS-E3 | UT2 | RA1 e | I2 · R2 | 4 | Dictamen de elección de lenguaje + evidencia de aislamiento seccomp |
| PPS-E4 | UT3 | RA2 a-c | I2 · R2 | 6 | Asignación de nivel ASVS + lista de requisitos trazada a pruebas |
| PPS-E5 | UT3 | RA2 d | I2 · R2 | 6 | Modelo de amenazas STRIDE sobre el DFD del portal |
| PPS-E6 | UT4 | RA3 a-d | I1 · R1 | 9 | Explotación documentada de 4 familias (inyección, XSS, sesión, IDOR) |
| PPS-E7 | UT4 | RA3 a-d | I3 · R3 | 9 | Corrección en el código + suite de regresión que cierra el hueco |
| PPS-E8 | UT5 | RA3 e | I1 · R1 | 11 | Migración del almacén de contraseñas a Argon2id (transparente) |
| PPS-E9 | UT5 | RA3 f,g | I2 · R2 | 11 | Bastionado del servidor con auditoría antes/después (testssl/lynis) |
| PPS-E10 | UT6 | RA4 a,b,e | I1 · R1 | 13 | Análisis estático móvil (MobSF+jadx): permisos, secretos, almacenamiento |
| PPS-E11 | UT6 | RA4 c,d | I2 · R2 | 13 | Interceptación de tráfico móvil + validación de compras en servidor |
| PPS-E12 | UT7 | RA5 b | I1 · R1 | 15 | Rama principal protegida + flujo de revisión documentado |
| PPS-E13 | UT7 | RA5 a,c,g | I3 · R3 | 15 | Canalización CI que **bloquea** (SAST/SCA/secretos/IaC), probada con caso que falla |
| PPS-E14 | UT8 | RA5 d,e | I3 · R3 | 17 | Despliegue canario con reversión automática demostrada |
| PPS-E15 | UT8 | RA5 f | I2 · R2 | 17 | Procedimiento DR ensayado con RTO/RPO medidos en el ensayo |

**Cobertura de RA**: RA1 (E1-E3) · RA2 (E4-E5) · RA3 (E6-E9) · RA4 (E10-E11) · RA5 (E12-E15).
RA3 (29 %) y RA5 (23 %) son los de mayor peso; sus retos integrados (E7, E13, E14) conectan
el código corregido y la CI con el SOC de IC (los SARIF de E13 los ingiere IC UT3).
