# HE · UT3 — Auditoría de redes inalámbricas Wi-Fi

**10 horas** · RA2 (a, b, c, d) · Servicio SOC: Protección — emulación de adversarios · Evidencias `HE-E5`, `HE-E6`

## Qué vamos a conseguir

Evaluar una red Wi-Fi de laboratorio y sus contramedidas.

## Antes de empezar

Herramientas: Adaptador USB compatible con modo monitor, AP propio, aircrack-ng/hashcat; capturas de apoyo.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Lee README-montaje-lab-wifi.md y verifica adaptador, controlador y asignación USB a la VM.

2. Anota BSSID y canal del AP autorizado. Comprueba que no eliges un AP vecino por nombre parecido.

3. Sigue ficha-E5-captura-crackeo.md con las restricciones del ejercicio y guarda el fichero original con hash.

4. Explica qué material contiene la captura y qué condiciones permiten comprobar la clave de prueba.

5. Cambia el control previsto y repite la comprobación. Relaciona la diferencia con la configuración.

6. Completa ficha-E6-contraste-soc.md correlacionando tiempos y sensor. Si solo usas una captura proporcionada, declara análisis offline, no captura propia.

## Cómo comprobar que está hecho

AP exacto identificado; evidencia conservada; contraste de control y observación.

> Un adaptador Wi-Fi virtual de la VM no aporta por sí mismo modo monitor; la prueba depende del hardware.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT3-auditoria-wifi.md).
- [ficha-E5-captura-crackeo](laboratorio/ficha-E5-captura-crackeo.md)
- [ficha-E6-contraste-soc](laboratorio/ficha-E6-contraste-soc.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
