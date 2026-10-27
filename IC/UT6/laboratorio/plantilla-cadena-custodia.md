# Cadena de custodia — Incidente xest (plantilla para el alumnado)

**Incidente**: ______________________  **Referencia SOC**: IC-CASE-____________
**Analista responsable**: ______________________  **Fecha de apertura**: __________

> Toda evidencia entra en esta tabla en el momento de adquirirse, con su hash. Cualquier
> traspaso (a AF para análisis en profundidad, por ejemplo) añade una fila de custodia. Un
> hueco en la cadena invalida la evidencia como prueba.

## 1. Registro de evidencias adquiridas

| # | Descripción de la evidencia | Origen (host/IP) | Método/herramienta | Fecha-hora (UTC) | Algoritmo | Hash | Adquirida por |
|---|---|---|---|---|---|---|---|
| E1 | Volcado de memoria RAM | WIN-XEST-ADM (10.10.10.50) | | | SHA256 | | |
| E2 | Recolección dirigida (procesos, red, persistencia) | WIN-XEST-ADM | Velociraptor | | SHA256 | | |
| E3 | Copia de disco / MFT / registro | WIN-XEST-ADM | | | SHA256 | | |
| E4 | Log del portal (access.log) | portal-soc (10.10.10.10) | | | SHA256 | | |
| E5 | | | | | SHA256 | | |

## 2. Traspasos de custodia

| Evidencia | De | A | Motivo | Fecha-hora | Hash verificado (S/N) | Firma |
|---|---|---|---|---|---|---|
| E1 | Analista IC | Módulo AF | Análisis del binario en profundidad | | | |
| | | | | | | |

## 3. Verificación de integridad

- Comando usado: `sha256sum -c manifiesto.txt`
- Resultado (pegar salida): __________________________________________
- Los hashes de depósito **coinciden** con los de adquisición:  ☐ Sí  ☐ No

## 4. Depósito final

- Ubicación del contenedor de evidencias (cifrado): __________________________
- Responsable de custodia: ______________  Acceso restringido a: ______________
