# Simulacro técnico UT7 — portal de xest comprometido (objetivo de laboratorio)
# Solo para la VLAN aislada de aula. NO exponer a Internet.
# La construcción requiere red una vez (descarga php:8.2-apache); en clase ya no.
FROM php:8.2-apache

# Portal legítimo (misma fuente que la copia verificada)
COPY seed/webroot/ /var/www/html/

# Guion que siembra la persistencia al arrancar (permite INCIDENTE_NIVEL=2)
COPY seed/seed-incidente.sh /usr/local/bin/seed-incidente.sh
RUN chmod +x /usr/local/bin/seed-incidente.sh \
    && chown -R www-data:www-data /var/www/html

ENTRYPOINT ["/usr/local/bin/seed-incidente.sh"]
CMD ["apache2-foreground"]
