# Resultado observado de wazuh-logtest 4.14.9

Este es un resumen de mi salida, no una transcripción completa:

| Entradas consecutivas en la misma sesión | Regla | Nivel |
|---|---|---|
| Fallos 1 a 7 de tecnico desde 203.0.113.45 | 5760 | 5 |
| Fallo 8 | 5763 | 10 |
| Accepted password posterior | 40112 | 12 |
| Accepted password aislado, en una nueva sesión | 5715 | 3 |

En la salida de 5763 vi frequency=8; en la de 40112 frequency=2. No interpreto este último valor como un umbral genérico de dos fallos SSH: pertenece a la regla de correlación y requeriría revisar su definición y dependencias.

La captura 10 muestra el acceso aislado. El resultado de la secuencia completa lo recogí en texto durante la práctica; no dispongo aquí de una captura o fichero completo de esa sesión.
