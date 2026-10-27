# Precisiones que aplicaremos durante el curso

## Evidencia y alcance

Un hash permite comprobar integridad respecto de una referencia; por sí solo no demuestra autoría, autenticidad, licitud ni toda la cadena de custodia. Conserva procedencia, fechas, responsables y transferencias.

Las salidas sintéticas de Volatility y Velociraptor son material de análisis. No incluyen una imagen `memoria.raw` ni acreditan una adquisición real. La ejecución sobre memoria necesita que el profesor prepare un volcado de laboratorio compatible y los símbolos correspondientes.

## Datos personales y autorización

Usaremos por defecto el caso OSINT sintético incluido y no buscaremos sus identidades en Internet. Un dato accesible públicamente no elimina las obligaciones de tratamiento. El consentimiento no es la única base jurídica posible y un documento de alcance no autoriza cualquier conducta. Los artículos 197 bis y 197 ter del Código Penal regulan supuestos distintos; no se debe enseñar que instalar una herramienta de doble uso sea por sí solo delito. [Código Penal, texto consolidado del BOE](https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444).

## Notificación de incidentes

En el ejercicio RGPD distingue brecha de datos, riesgo, alto riesgo y destinatario. La notificación a la autoridad competente debe efectuarse sin dilación indebida y, si es posible, dentro de 72 horas desde que se tiene constancia, salvo que sea improbable que suponga riesgo para derechos y libertades. Documenta también las brechas que no se notifican. La comunicación a afectados sigue su propio criterio de alto riesgo y no se resume en el mismo reloj de 72 horas. [AEPD: notificación de brechas](https://www.aepd.es/derechos-y-deberes/cumple-tus-deberes/medidas-de-cumplimiento/brechas-de-datos-personales-notificacion), [AEPD: comunicación a personas afectadas](https://www.aepd.es/preguntas-frecuentes/2-tus-obligaciones-como-responsable-del-tratamiento/11-brechas-de-datos-personales/FAQ-0254-a-quien-hay-que-comunicar-lo-ocurrido-en-una-brecha).

NIS2 se estudia como marco europeo: identifica ámbito, incidente significativo, alerta temprana, notificación y seguimiento. El artículo 23 contempla, con sus condiciones, hitos de 24 y 72 horas y un informe final. Antes de trasladarlo a un caso real hay que verificar transposición española vigente, autoridad y régimen sectorial; esta edición no certifica ese análisis jurídico caso por caso. No se asigna una autoridad solo por ser una entidad pública o privada. [Directiva (UE) 2022/2555, BOE](https://www.boe.es/buscar/doc.php?id=DOUE-L-2022-81963).

## Interpretar herramientas

La selección de seguridad high en DVWA no equivale a ausencia de vulnerabilidades. Se verifica el código y el comportamiento de la versión del laboratorio. Un JWT decodificado no está por ello validado. Una sonda de cabeceras no verifica todo ASVS. En ASVS registra edición e identificadores antes de contrastar requisitos. [ASVS oficial](https://owasp.org/projects/asvs).

El orden KEV → EPSS → CVSS es la regla simplificada del ejercicio de priorización; una decisión de parcheo real también considera el activo, exposición, dependencias y controles. Los snapshots son didácticos, no una fotografía certificada de amenazas actuales.

## Tiempo y coordinación

Se conservan 65 horas de referencia para PPS, 65 para HE y 80 para IC de la programación recuperada. El material original contiene ampliaciones que exceden esos tiempos. Las rutas de esta edición distinguen un núcleo de trabajo del banco ampliado de sesiones. La asignación final del centro y los festivos deben fijarse con su calendario real.

PPS se imparte el martes, IC el miércoles y HE el jueves según el horario guardado. Las evidencias que produce HE el jueves se investigan en IC el miércoles siguiente. HE UT8 requiere el servicio de PPS UT4–UT5; la parte de medición de ruido de HE-E10 requiere un sensor operativo de IC.
