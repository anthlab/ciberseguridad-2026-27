#!/bin/bash
# Arranca cron (para la persistencia revertible) y sshd en primer plano.
set -e
service cron start
# Genera claves de host si faltan
ssh-keygen -A >/dev/null 2>&1 || true
echo "[pivote] listo. svc-backup en 172.31.10.10 (dmz) y 172.31.20.10 (interna)."
exec /usr/sbin/sshd -D -e
