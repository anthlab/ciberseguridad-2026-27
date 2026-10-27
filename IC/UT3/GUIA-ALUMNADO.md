# IC · UT3 — Taxonomía de incidentes y arquitectura de detección

**12 horas** · RA2 (a, b) · Servicio SOC: Detección — recogida y correlación de eventos · Evidencias `IC-E4`, `IC-E5`

## Qué vamos a conseguir

Comprobar el camino completo desde un evento hasta una alerta.

## Antes de empezar

Herramientas: Wazuh, agentes Linux/Windows, Sigma; Suricata cuando haya visibilidad de red.

Consulta la [guía de instalación](../../comun/GUIA-INSTALACION.md), la [guía de herramientas](../../comun/GUIA-HERRAMIENTAS.md) y las [precisiones del curso](../../comun/PRECISIONES-DEL-CURSO.md). Prepara una carpeta propia para resultados; conserva intactos los datos de partida.

## Ruta de trabajo

1. Dibuja la arquitectura con fuentes, transporte, procesamiento, almacenamiento y analista.

2. Sigue ficha-E4-arquitectura.md y comprueba identidad, reloj y conectividad de cada agente.

3. Genera una actividad de prueba controlada y busca el evento bruto con su marca temporal.

4. Escribe la detección de ficha-E5-sigma-cobertura.md; identifica campos y backend antes de convertir Sigma.

5. Prueba un caso que debe alertar y otro que no debe hacerlo. Mide retraso y explica falsos positivos.

6. Completa el mapa ATT&CK con cobertura demostrada y puntos ciegos. Un servicio levantado sin eventos todavía no es una detección validada.

## Cómo comprobar que está hecho

Evento bruto localizado; positivo y negativo probados; alerta trazable al evento.

> Suricata solo ve el tráfico que llega a su interfaz. Una VLAN o contenedor no le da visibilidad automática.

## Desarrollo y fichas

- [Explicación completa de la unidad](../unidades/UT3-taxonomia-arquitectura-deteccion.md).
- [ficha-E4-arquitectura](laboratorio/ficha-E4-arquitectura.md)
- [ficha-E5-sigma-cobertura](laboratorio/ficha-E5-sigma-cobertura.md)

## Entrega y revisión

Los nombres y formatos están en el [cuaderno de entregables](../evaluacion/entregables.md). Antes de entregar, comprueba alcance, pasos reproducibles, resultados, interpretación y límites. Identifica tu trabajo por número de lista, módulo y evidencia.

Incluye una dificultad que hayas resuelto y explica por qué la solución funciona. Si utilizas una salida de ejemplo, declárala; no la presentes como ejecución propia.
