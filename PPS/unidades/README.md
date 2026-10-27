# PPS — Unidades de trabajo

Desarrollo de las 8 unidades del módulo **Puesta en producción segura (5023)**. Cada
unidad incluye contenido, guion de laboratorio con comandos reales y entregables con
su rúbrica. Marco y evaluación en `PROGRAMACION.md` (referencia del material de origen; consulta la guía de la unidad).

| UT | Título | Horas | RA | Unidad |
|---|---|---:|---|---|
| UT1 | Código, modelos de ejecución y pruebas de software | 9 | RA1 | [abrir](UT1-codigo-modelos-ejecucion-pruebas.md) |
| UT2 | Seguridad del lenguaje y del entorno de ejecución | 5 | RA1 | [abrir](UT2-seguridad-lenguaje-entorno-ejecucion.md) |
| UT3 | Nivel de verificación de seguridad: OWASP ASVS y superficie de riesgo | 8 | RA2 | [abrir](UT3-asvs-superficie-riesgo.md) |
| UT4 | Vulnerabilidades web I: entrada, inyección, sesión y control de acceso | 11 | RA3 | [abrir](UT4-vulnerabilidades-web-i.md) |
| UT5 | Vulnerabilidades web II: credenciales, bastionado y contramedidas | 8 | RA3 | [abrir](UT5-vulnerabilidades-web-ii-bastionado.md) |
| UT6 | Seguridad en aplicaciones para dispositivos móviles | 9 | RA4 | [abrir](UT6-seguridad-aplicaciones-moviles.md) |
| UT7 | DevSecOps: control de versiones, construcción e integración continua | 10 | RA5 | [abrir](UT7-devsecops-ci.md) |
| UT8 | Despliegue automatizado, resiliencia y recuperación ante desastres | 5 | RA5 | [abrir](UT8-despliegue-resiliencia-recuperacion.md) |

## Material de apoyo

- [`material/pipeline/ci-seguridad.yml`](../material/pipeline/ci-seguridad.yml) — canalización de integración continua con SAST, SCA, secretos e IaC (UT7).
- [`material/baseline/nginx-hardening.conf`](../material/baseline/nginx-hardening.conf) — baseline de bastionado de Nginx alineada con CCN-STIC 652 y CIS (UT5).
- [`material/plantillas/checklist_asvs.md`](../material/plantillas/checklist_asvs.md) — hoja de verificación ASVS nivel 2 (UT3).
- [`material/plantillas/informe-vulnerabilidad.md`](../material/plantillas/informe-vulnerabilidad.md) — plantilla del entregable vulnerabilidad→corrección→prueba (UT4/UT5).
