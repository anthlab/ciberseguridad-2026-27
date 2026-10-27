# Laboratorio de triaje · IC 04/11/2026

Material para la práctica de triaje de alertas con Wazuh.

- `alertas-SINTETICAS-2026-11-02.jsonl`: cola de 27 alertas en el mismo formato que
  `alerts.json` de Wazuh. **Son datos inventados** para practicar: los equipos, usuarios
  e IP no existen (203.0.113.0/24 es un rango reservado para documentación). Las reglas,
  niveles y descripciones son las que asigna Wazuh 4.14.8 a esos registros. Las alertas
  están desordenadas a propósito.
- `ver_alertas.py`: visor sin dependencias para quien no tenga `jq`. Sirve también para
  tus alertas reales.
- `plantilla-triaje.md`: tabla para clasificar las alertas.

    python3 ver_alertas.py alertas-SINTETICAS-2026-11-02.jsonl
    python3 ver_alertas.py alertas-SINTETICAS-2026-11-02.jsonl --min-nivel 10
