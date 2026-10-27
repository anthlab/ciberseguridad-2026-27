# Hacking Ético — Curso 2026-2027

**CIPFP Cheste · Sesiones de jueves (4 horas) · 8 unidades**

En este módulo aprenderás a planificar, ejecutar y documentar auditorías de seguridad **siempre en sistemas expresamente autorizados**. El resultado de cada práctica será un informe reproducible con evidencias, alcance y propuestas de mejora.

## Antes de comenzar

1. Lee las reglas de uso del laboratorio y delimita los sistemas autorizados.
2. Prepara un entorno aislado y comprueba la posibilidad de restaurar una instantánea.
3. No hagas enumeración activa, escaneos ni pruebas de explotación fuera del alcance aprobado.
4. No incluyas credenciales, información de terceros ni capturas con datos personales en tus entregas.
5. Documenta herramienta, versión, hora, objetivo, acción, resultado e interpretación.
6. Al acabar, detén las máquinas de prácticas y verifica la restauración.

## Itinerario y resultados

| Unidad | Contenidos | Entregable |
| --- | --- | --- |
| UT1 | Ética, legalidad, alcance, autorización y ROE | Documento de alcance y auto-OSINT |
| UT2 | Vulnerabilidades y priorización (KEV, EPSS, CVSS) | Matriz razonada de riesgos |
| UT3 | Seguridad Wi-Fi en laboratorio aislado | Informe de auditoría autorizada |
| UT4 | Seguridad inalámbrica y revisión conjunta | Registro de observaciones del equipo azul |
| UT5 | Reconocimiento y OSINT | Inventario de fuentes y evidencias |
| UT6 | Interceptación y explotación en entorno controlado | Informe técnico y evidencias anonimizadas |
| UT7 | Post-explotación y reversión | Bitácora de restauración |
| UT8 | Auditoría web del servicio construido en PPS | Informe con correcciones recomendadas |

**Secuencia docente:** UT1 sesiones 1 y 2 → UT5 pasiva → UT2 → UT3/UT4 → UT6/UT7 → UT8. La parte **activa** de UT5 se realizará cuando la detección del SOC de Incidentes esté operativa y exista autorización formal.

## Práctica inicial: alcance y auto-OSINT

**Objetivo:** diferenciar fuentes públicas y acciones activas, registrar evidencias y redactar reglas de enfrentamiento (ROE).

1. Crea un directorio de trabajo `he/ut1/evidencias` fuera del control de versiones y añádelo a tu `.gitignore`.
2. Redacta en `alcance.md` una tabla con objetivo, titular, permiso, ventana de trabajo, técnicas permitidas, límites y contacto de emergencia.
3. Sobre **tu propia identidad o datos ficticios**, identifica tres fuentes públicas que permitan obtener información, sin registrar datos de terceros.
4. Para cada fuente anota URL, fecha y hora, dato relevante, fiabilidad y riesgo de exposición. Evita almacenar la información personal en el repositorio.
5. Redacta tres medidas de reducción de exposición y una conclusión de 150-250 palabras.
6. Revisa el material con tu compañero: ¿qué actividad requiere autorización explícita?, ¿cuál no debe realizarse en la red del centro?

**Entrega:** `alcance.md` y `informe-ut1.md` (sin datos personales). Incluye portada, procedimiento, fuentes, hallazgos, limitaciones y conclusiones. El docente comprobará que el alcance sea verificable y no se haya excedido.

## Conexión con otros módulos

En PPS se construye y bastiona el servicio que después se auditará en HE UT8. Las evidencias sintéticas generadas en HE UT6/UT7 alimentarán las investigaciones de IC UT5/UT6/UT7. La práctica roja se ejecutará exclusivamente en el laboratorio autorizado.

## Material disponible en GitHub

- [UT1 · Sesión 1: guía de clase y actividades](./UT1/sesion-1.md)

Las próximas sesiones, manuales y presentaciones se incorporarán aquí como archivos del repositorio una vez revisados para uso del alumnado. No se requiere entrar en Drive para consultar la sesión 1. Los materiales de evaluación reservados al profesor no se publicarán.

**Material de aula — José Picón.**
