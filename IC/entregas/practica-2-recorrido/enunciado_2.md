# Miércoles 28 de octubre de 2026 — Seguimos con Wazuh

Chicos y chicas, hoy vamos a continuar el SOC que ya tenéis instalado con Docker **en vuestro propio equipo**. Lo importante no es ejecutar comandos sin más: quiero que comprobéis qué funciona, sepáis investigar los errores y expliquéis lo que aparece en el panel.

**Objetivos:** comprobar los componentes, verificar un agente, buscar eventos y redactar un pequeño informe. **Duración:** 4 horas.

## Antes de empezar (30 minutos)

1. Abre la terminal en la carpeta donde instalaste Wazuh y ejecuta `docker compose ps`. Comprueba el estado del Manager, Indexer y Dashboard.
2. Si hay algún contenedor parado, revisa `docker compose logs --tail=50` y anota el mensaje relevante. No borres datos ni reinstales sin analizarlo.
3. Abre el Dashboard con tu dirección local y revisa los agentes registrados. Anota si el agente de tu equipo está activo y cuándo comunicó por última vez.

## Recorrido A — Si tienes pendiente la práctica anterior (90 minutos)

Termina la [Práctica 0, instalación de Wazuh](./IC%20%C2%B7%20ALUMNADO%20%C2%B7%20Pr%C3%A1ctica%200%20%E2%80%94%20Monta%20tu%20Wazuh%20SOC%20paso%20a%20paso.pdf) y la [Práctica 1, despliegue del SOC](./IC%20%C2%B7%20ALUMNADO%20%C2%B7%20Pr%C3%A1ctica%201%20%28UT3%29%20%E2%80%94%20Despliega%20el%20SOC%20en%20una%20empresa%20real.pdf). Revisa el [checklist de problemas habituales](./IC%20%C2%B7%20ALUMNADO%20%C2%B7%20Wazuh%20%E2%80%94%20Checklist%20y%20troubleshooting%20de%20aula.pdf). Cuando tengas un agente comunicando, pasa al siguiente apartado.

## Recorrido B — Si ya estás al día (90 minutos)

1. Identifica el agente desde el Dashboard y anota nombre, estado y última conexión.
2. Genera un intento de autenticación fallida **solo con una cuenta de prueba propia**. Registra la hora exacta.
3. Busca el registro o alerta en Wazuh filtrando por agente y hora. Si no aparece, comprueba la fuente de registros y explica la posible causa; **no inventes ninguna alerta**.
4. Realiza la actividad ya publicada de [FIM y análisis](./IC%20%C2%B7%20ALUMNADO%20%C2%B7%20Extra%20%E2%80%94%20FIM%20y%20mini%20reto%20de%20an%C3%A1lisis.pdf). Modifica únicamente un archivo de prueba en una ruta supervisada. Comprueba la periodicidad de FIM antes de concluir que no funciona.

## Investigación y entrega (120 minutos)

Quiero un informe breve que incluya: estado de Docker, estado del agente, una tabla con **hora / equipo / tipo de evento / evidencia / interpretación**, dos capturas propias sin credenciales, los problemas encontrados y una medida de mejora. Si no consigues generar una alerta, documenta qué revisaste y qué prueba harías después.

**Antes de irte:** comprueba que no has publicado puertos vulnerables a la red del centro. No copies contraseñas, tokens ni datos de compañeros a GitHub. Trabajamos con sistemas autorizados y cada uno con su propio laboratorio.
