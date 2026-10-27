# vuln-app — objetivo DELIBERADAMENTE vulnerable para HE UT6 (HE-E12).
# Dos fallos sembrados, encadenables:
#   1) Inyección de comandos en ping.php  -> RCE como www-data.
#   2) SUID root sobre /usr/bin/find       -> escalada www-data -> root (GTFOBins).
# NO usar fuera de la VLAN de laboratorio.
FROM php:8.2-apache

# ping (para el ejercicio de "diagnóstico de red") y find (binario objetivo del SUID).
RUN apt-get update \
    && apt-get install -y --no-install-recommends iputils-ping findutils \
    && rm -rf /var/lib/apt/lists/*

# La aplicación web vulnerable (Apache la sirve como www-data).
COPY src/ /var/www/html/

# --- Vulnerabilidad de escalada sembrada a propósito ---
# find con bit SUID de root: cualquier usuario puede pedirle a find que ejecute algo,
# y find lo ejecuta con privilegios de root. Es el clásico de GTFOBins.
RUN chmod u+s /usr/bin/find

# La "bandera" que demuestra el compromiso total: solo root puede leerla.
RUN printf 'flag{xest-ut6-root-2f9c1a-compromiso-reproducible}\n' > /root/flag.txt \
    && chmod 600 /root/flag.txt \
    && chown root:root /root/flag.txt

# Un fichero de log que motiva el ejercicio de enumeración (pista hacia el SUID).
RUN printf 'app arrancada; tarea de mantenimiento: backups con find (ver crontab de root)\n' \
    > /var/log/app.log

EXPOSE 80
