# Ejercicio · La cadena de suministro del propio lenguaje (PPS · UT2)

> El intérprete y su gestor de paquetes también son superficie de ataque. Un `pip install`
> de un nombre mal escrito puede traer código malicioso a producción. Aquí lo cazamos.

## Contexto

Alguien ha propuesto este `requirements.txt` para el portal SOC de xest. Antes de que
entre en el repositorio, es tu trabajo revisarlo. Fichero: `requirements-sospechoso.txt`.

## Qué es un typosquat

Un paquete malicioso publicado con un nombre **casi idéntico** a uno legítimo y popular
(`colorama` → `colourama`, `requests` → `reqeusts`), a la espera de que alguien se equivoque
al teclear. Al instalarse ejecuta código (en el `setup.py` o al importarse). Campañas reales
de este tipo han afectado a PyPI y npm repetidamente.

## Tarea

1. Recorre las 12 líneas de `requirements-sospechoso.txt`.
2. Marca cada dependencia como **legítima** o **sospechosa (typosquat / nombre no oficial)**.
   Para cada sospechosa, escribe **cuál es el nombre correcto** al que se parece y **por qué
   lo consideras sospechoso** (distancia de edición pequeña, nombre que no existe en PyPI,
   colisión con la biblioteca estándar…).
3. Escribe el `requirements-corregido.txt` con solo las dependencias legítimas y los nombres
   bien escritos.

## Pista metodológica

No lo hagas "a ojo" y ya está: **contrasta con una fuente**. Compara cada nombre con una lista
de paquetes legítimos conocidos. La comparación por parecido la puede hacer una función de la
biblioteca estándar de Python (`difflib.get_close_matches`): si un nombre se parece mucho a uno
oficial **pero no es exactamente ese**, enciende la alarma. Ese es el patrón que automatizará la
CI en la UT7 (análisis de composición de software, SCA).

## Entrega parcial

Tu tabla `legítima / sospechosa / nombre correcto / motivo` alimenta el apartado de **cadena de
suministro** del dictamen PPS-E3. No es un entregable independiente: es munición para el informe.

> Regla del módulo: no basta con *sospechar*; hay que **verificar contra una segunda fuente**.
> Un cero sin verificar no vale, y un "parece legítimo" tampoco.
