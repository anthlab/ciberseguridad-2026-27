# Jueves 29 de octubre de 2026 — Continuamos TECNORIBERA

Chicos y chicas, hoy seguimos con la empresa ficticia TECNORIBERA. Algunos todavía tenéis la práctica de enumeración activa pendiente y otros ya la habéis terminado. Por eso vamos a trabajar con dos recorridos: ninguno necesita esperar a los demás.

**Objetivo:** identificar servicios de un laboratorio autorizado, interpretar resultados y presentar un informe técnico. **Duración:** 4 horas.

## Comprueba el alcance (20 minutos)

Levanta **solo tu laboratorio Docker** y revisa que los servicios vulnerables no estén expuestos a la red del centro. Comprueba las IP y puertos autorizados. No realices pruebas sobre equipos ajenos, Internet o la infraestructura real del instituto.

## Recorrido A — Si tienes la práctica anterior pendiente (100 minutos)

Abre la [guía paso a paso de enumeración de TECNORIBERA](./HE%20%C2%B7%20ALUMNADO%20%C2%B7%20Pr%C3%A1ctica%204%20%28UT5%20S2%29%20%E2%80%94%20Enumeraci%C3%B3n%20activa%20de%20TECNORIBERA%20%28paso%20a%20paso%20explicado%29.pdf). Completa las pruebas que te faltan y anota, para cada una, **qué querías descubrir**, **qué comando usaste** y **qué conclusión permiten los datos**.

## Recorrido B — Si ya estás al día (100 minutos)

1. Prepara una tabla de activos: host de laboratorio, puerto, servicio, versión observada y método de comprobación.
2. Ejecuta, solo contra tu objetivo autorizado, `nmap -sV -p <PUERTOS_AUTORIZADOS> <IP_LAB>`. Sustituye los valores por los de tu laboratorio.
3. Para servicios web de prueba puedes consultar cabeceras con `curl -I http://<HOST_LAB>:<PUERTO>` o usar OWASP ZAP **en modo pasivo**.
4. Elige tres hallazgos y distingue lo confirmado de lo que todavía es una hipótesis. Una versión anunciada no demuestra por sí sola que sea posible explotar una vulnerabilidad.
5. Propón para cada hallazgo una mitigación concreta.

## Informe y entrega (120 minutos)

Entrega un documento con **alcance, metodología, inventario, hallazgos, evidencias, limitaciones y recomendaciones**. Si algo no funciona, documenta el error y cómo intentaste resolverlo. No hace falta explotar sistemas para hacer una buena enumeración.

**Recordad:** las herramientas son un medio, no el objetivo. Me interesa que sepáis interpretar sus resultados y justificar vuestras conclusiones. Detened los contenedores vulnerables al terminar y no compartáis credenciales.
