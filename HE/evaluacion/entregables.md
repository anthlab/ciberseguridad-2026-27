# HE 5025 — Cuaderno de entregables (enunciados para el alumnado)

Reglas generales de entrega:
- Todo se entrega **por número de lista**: `NN-HE-EX-<nombre>` (ej. `07-HE-E9-informe.md`).
- Formato Markdown o PDF; capturas dentro del propio entregable o en `evidencias/`.
- Marca de tiempo y fuente en cada hallazgo. **Sin ROE firmado (HE-E1) no se admite ningún
  entregable de práctica activa.**
- Nada ejecutado fuera de la VLAN de laboratorio: acción fuera de alcance = 0 (rúbrica R1).

---

## HE-E1 · ROE del curso (UT1 · I2/R2)
Redacta y firma el documento de alcance y reglas de enfrentamiento del ejercicio del curso
(objetivo: `*.xest.local`) sobre la plantilla `HE/material/plantillas/ROE.md` del repo.
**Debe incluir**: perímetro exacto (IP/puerto/dominio), ventana horaria, técnicas prohibidas,
regla de parada `stop-the-test` y quién la invoca, y gestión (cifrado/destrucción) de los
datos capturados. **Entrega**: `NN-HE-E1-roe.pdf` firmado con el rol docente.

## HE-E2 · Prueba objetiva de marco legal (UT1 · I5)
Prueba objetiva escrita (la entrega el profesor en el aula): terminología, arts. 197
bis/ter y 264/264 bis, fases del ataque y su correspondencia con ATT&CK.

## HE-E3 · Arsenal por perfil de organización (UT2 · I2/R2)
Cuadro comparativo de herramientas de monitorización y auditoría para **pyme /
administración ENS / entidad financiera**, con el **criterio de elección** de cada una (no
lista genérica). **Entrega**: `NN-HE-E3-arsenal.md`.

## HE-E4 · Priorización real (UT2 · I1/R1)
Enriquece el lote `UT2/laboratorio/lote_cves.txt` con `prioriza.py` (CVSS+EPSS+KEV), ordena
por prioridad real y **argumenta 3 discrepancias** respecto al orden por CVSS.
**Entrega**: `NN-HE-E4-priorizado.csv` + `NN-HE-E4-justificacion.md`.

## HE-E5 · Captura y acceso Wi-Fi (UT3 · I1/R1)
Sobre la red **de laboratorio** `xest-lab`: captura del handshake, crackeo offline, acceso
demostrado y **tiempo medido**. Conclusión sobre qué longitud/entropía lo habría hecho
inviable. **Entrega**: `NN-HE-E5-wifi.md` + `captura-01.cap`.

## HE-E6 · Contraste rojo-azul Wi-Fi (UT3 · I3/R3)
Documenta qué detectó el SOC del ataque inalámbrico (deauth, rogue AP) y **qué no**, y
propón la **regla de detección que faltaría**. **Entrega**: `NN-HE-E6-contraste.md`.

## HE-E7 · Informe de auditoría inalámbrica (UT4 · I2/R2)
Informe completo del clonado RFID/ataque RF de laboratorio: alcance, hallazgos con
evidencia, riesgo (probabilidad × impacto), remediación priorizada.
**Entrega**: `NN-HE-E7-informe.pdf`.

## HE-E8 · Defensa oral inalámbrica (UT4 · I4/R4)
Presenta y defiende el informe HE-E7 ante el grupo (≤10 min): traduce el hallazgo técnico a
riesgo de negocio. Se evalúa en vivo.

## HE-E9 · Reconocimiento pasivo (UT5 · I2/R2)
Informe metodológico de la práctica de auto-OSINT (`UT5/laboratorio/practica-01-autoosint.md`),
**sin datos personales concretos**, con fuentes citadas y sin una sola conexión al objetivo.
Rúbrica ampliada: `rubricas/HE-E9-reconocimiento-pasivo.md`.
**Entrega**: `NN-HE-E9-informe.md` + `grafo/{nodes,edges}.csv` + `NN-HE-E9-reduccion.md`.

## HE-E10 · Inventario por enumeración activa (UT5 · I1/R1)
Inventario de activos, cuentas y vulnerabilidades potenciales de `objetivo.xest.local` por
técnicas activas, con el **ruido medido** en el SOC. **Entrega**: `NN-HE-E10-inventario.md`
+ `nmap_objetivo.*`, `httpx.txt`.

## HE-E11 · MITM (UT6 · I1/R1)
Ataque de intermediario en el segmento de laboratorio con **evidencia de modificación** del
tráfico, y comprobación de que **HSTS lo frustra**. **Entrega**: `NN-HE-E11-mitm.md`.

## HE-E12 · Compromiso documentado (UT6 · I3/R3)
Compromete un sistema de laboratorio y escala a administrador, **documentado paso a paso y
reproducible** (un compañero debe poder repetirlo solo con tu documento). **Se entrega
también a IC** como caso a investigar. **Entrega**: `NN-HE-E12-compromiso.md`.

## HE-E13 · Ataque a credenciales (UT7 · I1/R1)
Crackeo de un volcado de laboratorio con hashcat/john, **midiendo** el tiempo por tipo de
contraseña, y conclusión de **política medible**. **Entrega**: `NN-HE-E13-credenciales.md`.

## HE-E14 · Pivotaje y persistencia con reversión (UT7 · I3/R3)
Cadena de pivotaje + un mecanismo de persistencia **documentado, revertido y verificado**
(captura de la ausencia tras revertir). Entrega de **IoC al equipo azul**. Sin la evidencia
de reversión, la práctica no está completa. **Entrega**: `NN-HE-E14-cadena.md` + `iocs.csv`.

## HE-E15 · Informe de auditoría web (UT8 · I2/R2)
Informe completo del portal SOC (`HE/material/plantillas/informe-pentest.md`): resumen
ejecutivo, metodología WSTG, hallazgos con evidencia, riesgo priorizado, remediación. Todo
hallazgo automático **verificado a mano**. **Entrega**: `NN-HE-E15-auditoria-web.pdf`.

## HE-E16 · Defensa de un crítico (UT8 · I4/R4)
Defiende un hallazgo crítico ante tribunal simulado (≤10 min + repreguntas): impacto de
negocio, prueba de concepto y remediación. Se evalúa en vivo.
