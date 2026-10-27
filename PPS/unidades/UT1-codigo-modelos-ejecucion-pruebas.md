# PPS · UT1 — Código, modelos de ejecución y pruebas de software

**9 horas** · RA1 (a, b, c, d) · Servicio SOC: Prevención — calidad del software · Evidencias `PPS-E1`, `PPS-E2`

---

## 1. Objetivo de la unidad

Un analista de puesta en producción segura no escribe todo el software que revisa, pero tiene que **leerlo, probarlo y decidir si es apto para producción**. Esta unidad establece la base: cómo se ejecuta el código según el lenguaje, qué partes del fuente hay que saber leer y cómo se prueba de forma que un fallo no llegue al usuario. Todo lo que viene después —ASVS, corrección de vulnerabilidades, canalización— se apoya en saber distinguir un programa correcto de uno que solo *parece* correcto.

## 2. Contenido

### 2.1 Lenguajes: compilados, interpretados y de máquina virtual

| Modelo | Ejemplos | Qué se despliega | Consecuencia de seguridad |
|---|---|---|---|
| **Compilado a nativo** | C, C++, Rust, Go | Binario máquina | Sin seguridad de memoria salvo Rust/Go; superficie en el propio binario (desbordamientos, cadena de formato) |
| **Interpretado** | Python, PHP, Ruby, JavaScript (Node) | Código fuente + intérprete | El fuente viaja al servidor: secretos y lógica quedan expuestos si el repositorio o la imagen se filtran |
| **Máquina virtual** | Java (JVM), C# (.NET) | Bytecode | Decompilable con facilidad (`jadx`, `dnSpy`); no confiar en la ofuscación como control |

**Regla operativa:** el modelo de ejecución determina *dónde* está el riesgo. En un servicio Python, el `.py` está en el servidor; en un binario Go, el riesgo es de memoria y de dependencias enlazadas.

### 2.2 Elementos del código fuente que hay que saber leer

- **Puntos de entrada**: dónde entra dato del exterior (parámetros HTTP, ficheros, variables de entorno, argumentos). Es la superficie de ataque.
- **Puntos de salida (sinks)**: dónde ese dato acaba (consulta SQL, comando de shell, respuesta HTML, ruta de fichero). Es donde se materializa la vulnerabilidad.
- **Flujo entre ambos**: si un dato de entrada llega a un sink sin validación ni codificación, hay vulnerabilidad. Este es el modelo mental de todo el análisis estático.
- Dependencias, gestión de errores y gestión de secretos.

### 2.3 Pruebas de software

| Tipo | Qué comprueba | Herramienta ejemplo |
|---|---|---|
| **Unitaria** | Una función en aislamiento | `pytest`, `JUnit` |
| **Integración** | Varias piezas juntas | `pytest`, `testcontainers` |
| **Regresión** | Que un fallo corregido no vuelve | La propia suite en CI |
| **Cobertura** | Qué porcentaje de líneas ejecuta la suite | `coverage.py`, `JaCoCo` |
| **Fuzzing** | Entradas malformadas que rompen el parser | `atheris`, `AFL++` |

La cobertura no mide calidad, mide *alcance*: un 90 % de cobertura con aserciones triviales no prueba nada. Se exige cobertura **más** aserciones significativas.

## 3. Laboratorio guiado

> Entorno: la aplicación web del proyecto (portal del SOC de xest) o, si aún no está, el repositorio de laboratorio que facilita el docente. Python 3.12 con `pytest` y `coverage`.

### Parte A — Lectura comparada (RA1.a, RA1.b, RA1.c)

1. Se entregan tres implementaciones equivalentes de un mismo validador de entrada (en Python, Java y C).
2. Para cada una, localiza: punto de entrada, sink y validación. Señala **dónde puede fallar** cada modelo de ejecución (p. ej., desbordamiento en C, deserialización en Java, `eval` en Python).
3. Rellena la tabla del entregable `PPS-E1`.

### Parte B — Suite de pruebas y cobertura (RA1.d)

```bash
# Instalar dependencias de prueba
python3 -m pip install pytest coverage

# Ejecutar la suite midiendo cobertura
python3 -m coverage run -m pytest -v
python3 -m coverage report -m
python3 -m coverage html   # informe navegable en htmlcov/index.html
```

4. Añade al menos **tres pruebas unitarias** nuevas a una función del proyecto que hoy no esté cubierta.
5. Escribe **una prueba de regresión** que reproduzca un fallo conocido (cadena vacía, número negativo, entrada no ASCII) y verifica que falla antes de arreglar la función y pasa después.

### Parte C — Fuzzing básico (refuerzo)

```bash
python3 -m pip install atheris
# Ejemplo de arnés de fuzzing sobre un parser
python3 fuzz_parser.py -atheris_runs=100000
```

6. Si el fuzzer encuentra una entrada que provoca una excepción no controlada, documéntala como caso de prueba de regresión.

## 4. Entregables

- **`PPS-E1`** (informe, rúbrica R2): tabla comparada de los tres lenguajes desde la perspectiva de seguridad, con el fallo característico de cada modelo de ejecución identificado sobre el código real.
- **`PPS-E2`** (laboratorio, rúbrica R1): suite ejecutable con las nuevas pruebas y el informe de cobertura (`coverage report` y captura del HTML), incluida la prueba de regresión que demuestra el ciclo fallo→corrección→prueba.

## 5. Criterios de superación

- El informe distingue correctamente entrada, sink y flujo en las tres implementaciones.
- La suite **ejecuta** (`pytest` en verde) y la prueba de regresión demuestra que cierra el fallo.
- La cobertura mejora respecto a la línea base y las aserciones son significativas, no triviales.

## 6. Errores frecuentes

- Confundir cobertura alta con código seguro. Cobertura es alcance de la prueba, no ausencia de vulnerabilidades.
- Escribir la prueba de regresión *después* de arreglar el fallo sin verificar que fallaba antes: entonces no prueba nada.
- Analizar el código buscando "funciones peligrosas" en vez de seguir el flujo entrada→sink.

## 7. Referencias

- OWASP Code Review Guide.
- NIST SP 800-218 (SSDF), práctica PW.7 (revisión de código) y PW.8 (pruebas).
- `pytest` y `coverage.py` — documentación oficial.
