# HE UT6 · Ficha 02 — Captura de credenciales con Responder (puente a UT7)

**Módulo** 5025 · **UT6** · **RA3 c** · Refuerza HE-E11 y **siembra HE-E13** (UT7).
**Entorno**: VLAN de laboratorio aislada. Envenenar LLMNR/NBT-NS fuera de aquí es delito.

> No hay que "hackear" a nadie: basta con que un usuario teclee mal el nombre de un
> servidor. Ese es el punto de la práctica — cuánto tráfico regala una red por defecto.

## Objetivo

Envenenar LLMNR/NBT-NS/mDNS en el segmento de laboratorio, capturar un hash **NetNTLMv2**
de la estación víctima cuando intenta alcanzar un recurso inexistente, y dejarlo preparado
en el formato de crackeo de UT7.

## Tareas

1. **Escucha.** Lanza Responder en tu interfaz de la VLAN.
2. **Disparo.** El profesor ejecuta en la estación víctima el acceso a un recurso de red que
   no existe en el DNS (unidad mal escrita). Observa cómo tu equipo contesta la consulta.
3. **Captura.** Recoge el hash NetNTLMv2 del usuario víctima. Identifica sus campos
   (`usuario::DOMINIO:...`).
4. **Formato de crackeo.** Guarda el hash en un fichero apto para `hashcat -m 5600`. **No lo
   crackees aquí**: eso es UT7 (HE-E13). Solo lo dejas listo y explicas qué modo de hashcat
   le corresponde y por qué.
5. **Contramedida.** ¿Qué habría impedido esta captura? (pista: LLMNR/NBT-NS y firma SMB).

## Verificación

Comprueba que el hash está **completo** (los cinco campos separados por `:`, el `blob` no
truncado). Un NetNTLMv2 a medias no cracked. Contrasta el nombre de usuario capturado con
el que el profesor introdujo en la víctima.

## Higiene operativa

El hash es un dato sensible: guárdalo cifrado y decláralo para su **destrucción** tras la
práctica, según el ROE (gestión de datos capturados).

## Entregable

No genera evidencia propia calificable, pero **el hash capturado alimenta HE-E13** en UT7.
Adjunta en tu bitácora: comando de Responder, campo por campo del NetNTLMv2, modo hashcat
que le corresponde y la contramedida. Mapea a **MITRE ATT&CK T1557.001** (LLMNR/NBT-NS
Poisoning and SMB Relay).
