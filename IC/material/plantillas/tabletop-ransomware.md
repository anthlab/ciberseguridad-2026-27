# Ejercicio de mesa (tabletop) — Ransomware

Escenario para la UT7 (`IC-E13`). Se ejecuta con **reloj real**: cada inyecto tiene su
momento y el equipo decide sobre la marcha. Al final se evalúa la **autocrítica**, no si
el incidente salió bien.

---

## Preparación

- **Duración**: 90 minutos.
- **Roles** (del manual CSIRT): coordinador, L1, L2, portavoz, enlace jurídico.
- **Regla**: el facilitador va soltando inyectos; el equipo decide y documenta cada decisión con su hora.
- **Materiales**: manual CSIRT, playbook de ransomware, plantillas de notificación.

## Escenario base

El SOC de xest presta servicio a una organización con 400 puestos. Es lunes, 08:15.

## Inyectos (cronología)

| T+ | Inyecto | Qué debe decidir el equipo |
|---|---|---|
| **00:00** | Varios usuarios reportan que no pueden abrir sus ficheros; aparece una nota `README_RECOVER.txt`. Wazuh dispara alertas de cifrado masivo en tres endpoints. | Clasificación inicial, activación del CSIRT, primera contención |
| **00:10** | La detección muestra propagación por SMB hacia un servidor de ficheros. | ¿Segmentar la red? ¿Aislar el servidor? ¿Cómo sin destruir evidencia? |
| **00:20** | El servicio de facturación (esencial) deja de responder. | Priorización de recuperación, comunicación interna, decisión sobre RTO |
| **00:30** | Se confirma que la variante exfiltra datos antes de cifrar (doble extorsión). Hay datos personales. | Valoración RGPD, ¿aplica art. 33? Reloj de 72 h en marcha |
| **00:40** | La nota exige pago en 48 h. La dirección pregunta si se paga. | Decisión sobre el pago (nunca por defecto), postura y justificación |
| **00:50** | Un medio local llama preguntando por una «caída informática». | Activación del portavoz, mensaje base, qué se dice y qué no |
| **01:00** | Se localiza el paciente cero: un correo de phishing del viernes. | Causa raíz preliminar, ¿NIS2 24 h?, escalado a INCIBE-CERT |
| **01:10** | Hay copias de seguridad; falta verificar que no están cifradas. | Verificación de copias antes de restaurar, plan de recuperación |

## Preguntas de cierre (autocrítica)

1. ¿En qué momento se activó formalmente el CSIRT? ¿Se tardó de más?
2. ¿La contención preservó la evidencia o la destruyó?
3. ¿Se cumplieron los relojes regulatorios (RGPD 72 h, NIS2 24 h)?
4. ¿La decisión sobre el pago estaba fundamentada o fue improvisada?
5. ¿Qué regla de detección habría dado más margen? (retroalimentación a UT3 y a HE)
6. ¿Qué medida de PPS/BAST habría evitado la propagación? (retroalimentación a PPS)

## Evaluación

Se valora la **calidad de las decisiones bajo presión** y la **honestidad de la
autocrítica**, no que el incidente se resolviera sin errores. Las acciones correctoras
salen con responsable y fecha de verificación.
