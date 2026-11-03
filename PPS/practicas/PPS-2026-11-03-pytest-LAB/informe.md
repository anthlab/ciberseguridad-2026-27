# PPS · Práctica de pytest del 3 de noviembre

## Resultados

Al principio pasaron las 5 pruebas originales, con un 80 % de cobertura.
Después de añadir las pruebas de R1 a R5 y corregir los fallos,
pasaron las 32 pruebas y la cobertura de líneas llegó al 100 %.
La salida final está en `salida-pytest.txt`.

## Fallos encontrados y correcciones

| Regla | Dato de prueba | Resultado inicial | Corrección |
|---|---|---|---|
| R1 | `12345678z` | Devolvía `False`. | Convertí la letra a mayúscula antes de compararla. |
| R1 | `0000001R` y `000000001R` | Devolvía `True` con 7 y 9 cifras. | Exigí exactamente 8 cifras en la expresión regular. |
| R2 | `" ana@ejemplo.es "` | Devolvía `True` porque quitaba los espacios. | Eliminé `strip()` de la validación del correo. |
| R4 | 25 años con y sin desempleo | Devolvía 30 € con desempleo y 60 € sin desempleo. | Cambié `< 25` por `<= 25`. Ahora devuelve 20 € y 40 €, respectivamente. |
| R5 | `+x`, `-x`, `@x`, `\tx` y `\rx` | Se guardaban sin la comilla simple inicial. | Amplié `startswith()` para reconocer los seis prefijos de la regla, incluido `=`. |

Las tres pruebas de R3 pasaron desde el principio. El código ya
normalizaba los nombres y rechazaba los que quedaban vacíos.

## Preguntas del apartado 10

1. La cobertura inicial era del 80 %. La cobertura indica qué líneas
   se ejecutaron. Por ejemplo, los tests originales ejecutaban el
   cálculo de la cuota, pero no comprobaban el límite de los 25 años.
2. Con `parametrize` puedo probar varios datos con una sola función.
   Pytest muestra cada caso por separado y así veo cuál falla.
3. `tmp_path` crea una carpeta temporal para cada caso. Así las pruebas
   no comparten el CSV ni dejan archivos en la carpeta del proyecto.
4. Si alguien se inscribe con el nombre `=1+1`, la hoja de cálculo
   podría mostrar `2` al abrir el CSV. La comilla simple inicial sirve
   para que el valor se trate como texto.
5. El retorno de carro fue el caso menos visible porque es un carácter
   de control. La prueba de R5 con `"\rx"` comprobó que, al leer el
   nombre guardado en el CSV, faltaba la comilla simple inicial.
