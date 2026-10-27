# Laboratorio de pivotaje UT7 — puesta a punto del profesor

Escenario de dos segmentos para practicar movimiento lateral (RA4.c) **sin necesidad de
Active Directory**: un host `pivote` expuesto en la DMZ y un `interna-app` que solo se alcanza
tunelizando a través de él. Enganche con HE-E13: la credencial `svc-backup:Password1` que el
alumnado **crackea** en la sesión 1 es la que abre `pivote` por SSH en la sesión 2.

## Levantar (una vez, antes de clase)

```bash
cd HE/UT7/laboratorio/pivote-lab
docker compose up -d --build
docker compose ps          # pivote (2222->22) e interna-app arriba
```

## Prueba de humo (debe dar OK antes de clase)

```bash
# 1) SSH a pivote con la credencial reutilizada (la del volcado NTLM):
sshpass -p 'Password1' ssh -o StrictHostKeyChecking=no -p 2222 svc-backup@127.0.0.1 'hostname; ip -4 a | grep 172.31'
#   -> pivote  ·  172.31.10.10 (dmz)  ·  172.31.20.10 (interna)

# 2) El objetivo interno NO se alcanza directamente desde el atacante:
curl -m 3 http://172.31.20.20/  ; echo "  <- debe fallar/timeout desde el host atacante"

# 3) Pero SÍ a través del túnel SOCKS (pivotaje):
ssh -o StrictHostKeyChecking=no -p 2222 -f -N -D 1080 svc-backup@127.0.0.1   # pide clave: Password1
curl -s --socks5-hostname 127.0.0.1:1080 http://172.31.20.20/ | grep FLAG
#   -> FLAG{xest-pivote-interna-172.31.20.20-OK}
pkill -f "ssh.*-D 1080"    # cerrar el túnel de prueba
```

> `sshpass` no viene en Kali por defecto: `sudo apt install sshpass`. En clase el alumnado
> teclea la contraseña; `sshpass` es solo para automatizar esta prueba de humo.

## Parar / reiniciar limpio

```bash
docker compose down          # entre grupos, para dejar el host sin persistencia residual
docker compose up -d --build # snapshot limpio para el siguiente grupo
```

## Notas de diseño

- `interna` es una red `internal: true`: Docker le niega ruta al exterior, así que el único
  camino a `interna-app` es el proxy que monte el alumnado sobre `pivote`. Pivotaje **real**,
  no simulado.
- El método enseñado como principal es **SSH dynamic forward** (`ssh -D`) porque funciona con
  un `sshd` pelado y sin privilegios de red. **chisel** es la alternativa equivalente. **ligolo-ng**
  (que crea una interfaz `tun`) necesita `NET_ADMIN`/`--privileged` o mejor una VM completa:
  se **demuestra proyectado**, no se exige a cada estación.
- La persistencia de HE-E14 se instala DENTRO de `pivote` (cron / `authorized_keys`), se
  documenta, se revierte y se verifica. `docker compose down && up` es la red de seguridad si
  alguien no revierte.
