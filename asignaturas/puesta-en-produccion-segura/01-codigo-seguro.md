# Puesta en Producción Segura — Sesión: revisión de código seguro
**Fecha:** 27 de octubre de 2026 · **Duración prevista:** 4 horas

## Lo que vamos a trabajar
En esta sesión vamos a identificar riesgos habituales en aplicaciones Python, corregirlos y justificar cómo verificamos las mejoras. Cada cambio debe quedar documentado para que otra persona pueda reproducir el resultado.

## Antes de empezar
Necesitáis Git, Python 3.12 o superior y un editor. Trabajad en un entorno virtual y no utilicéis credenciales reales. Cread una rama con el formato `practica/codigo-seguro-apellido`.

## Actividad 1 — Reconocer el problema (40 minutos)
Leed el siguiente fragmento, sin ejecutarlo contra una base de datos real:

```python
def consulta_insegura(conexion, usuario):
    return conexion.execute(f"SELECT id FROM users WHERE name = '{usuario}'")
```

Explicad por escrito qué podría ocurrir si el argumento `usuario` contiene caracteres especiales y por qué no conviene construir consultas SQL mediante interpolación.

## Actividad 2 — Aplicar una corrección (50 minutos)
Partid de una conexión `sqlite3` creada exclusivamente para la práctica. Implementad una consulta parametrizada:

```python
def buscar_usuario(conexion, usuario: str):
    return conexion.execute(
        "SELECT id FROM users WHERE name = ?",
        (usuario,),
    ).fetchall()
```

Probad con un nombre habitual, una cadena vacía y un nombre que incluya un apóstrofo. Anotad el resultado y explicad la diferencia entre datos y código SQL.

## Actividad 3 — Comprobar la corrección (45 minutos)
Preparad una prueba con `unittest` o `pytest` utilizando una base SQLite en memoria. La prueba debe crear una tabla, insertar datos de ejemplo y comprobar que la función devuelve exclusivamente el registro solicitado. Incluid al menos un caso de entrada con un apóstrofo.

## Actividad 4 — Revisar y documentar (45 minutos)
Revisad el código con `python -m compileall .` y, si está disponible, ejecutad Bandit sobre los archivos Python de la práctica. Describid qué problemas habéis encontrado y cuáles son falsos positivos. No incorporéis secretos al repositorio.

## Entrega (20 minutos)
Subid la rama con: (1) código corregido, (2) prueba automatizada, (3) `INFORME.md` con descripción del riesgo, cambios y evidencias, y (4) instrucciones de ejecución. Abrid una pull request para revisión; no fusionéis directamente.

## Revisión de aprendizaje (20 minutos)
Repasaremos Git, GitHub y Docker con el Kahoot correspondiente, accesible desde [el índice del curso](../../KAHOOT-Y-TEST.md). La actividad de preguntas sobre código seguro se incorporará cuando esté publicada.

## Criterios que revisaré
- Identificación técnica del riesgo y explicación: 25 %.
- Corrección adecuada mediante parámetros: 30 %.
- Pruebas reproducibles, incluido caso especial: 25 %.
- Calidad de la documentación y de la entrega: 20 %.

**Material complementario:** [práctica preparada en Drive](https://drive.google.com/file/d/1bw1sd5WXydWSM7hGc36O2kpfu6VTYTbL/view). Consultadla únicamente si tenéis acceso autorizado; este documento ofrece un itinerario que podéis realizar sin depender del enlace.
