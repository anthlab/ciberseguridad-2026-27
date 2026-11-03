# PPS-E1 · Lectura de los validadores

| Fichero | Punto de entrada | Sink(s) | Validación | Dónde puede fallar |
|---|---|---|---|---|
| `validar.py` (interpretado) | `sys.argv[1]` | `con.execute(consulta)`, `os.system(...)` y `eval(regla)` | Comprueba que el nombre tenga entre 1 y 32 caracteres. Las comillas pasan ese filtro. | El nombre se concatena en una consulta SQL, en un comando de shell y en una expresión de Python. Al probar `ana` obtuve `True`. Con `' OR '1'='1`, el programa llegó a `eval(regla)` y lanzó `SyntaxError` en la línea 30. |
| `Validar.java` (bytecode / JVM) | `args[0]` | `st.executeQuery(consulta)` | Comprueba que el nombre no sea `null` y que tenga entre 1 y 32 caracteres. | La consulta concatena el nombre, así que una comilla puede cambiar el SQL. Además, al decompilar el `.class` se puede recuperar el valor de ejemplo de `apiKey`. |
| `validar.c` (nativo) | `argv[1]` | `strcpy(buffer, nombre)` | `argc > 1` comprueba si hay un argumento. La longitud del nombre queda sin comprobar. | El buffer tiene 32 bytes y `strcpy` también copia el terminador `\0`. Con 32 letras `A`, el terminador se escribiría fuera del buffer. |

## ¿Cómo lo corregiría?

- **Python.** Usaría una consulta parametrizada, registraría el acceso con `logging` y cambiaría `eval(regla)` por `len(nombre) > 0`.
- **Java.** Usaría `PreparedStatement` con `WHERE nombre = ?` y pasaría el nombre con `setString(1, nombre)`. Una clave real la guardaría fuera del código.
- **C.** Antes de copiar, rechazaría el nombre si `strlen(nombre) >= sizeof buffer`, para dejar espacio para el terminador.
