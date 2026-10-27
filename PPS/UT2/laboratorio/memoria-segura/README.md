# Demo · Seguridad de memoria en tres lenguajes (PPS · UT2)

> El mismo problema —copiar un dato de entrada a un espacio de tamaño fijo— en C, Go y Python.
> Objetivo: **ver** que el lenguaje decide si un dato demasiado largo corrompe la memoria o no.
> Solo laboratorio aislado de xest. Las opciones que desactivan protecciones (`-fno-stack-protector
> -z execstack`) NO se usan jamás fuera de una demostración didáctica.

## C — sin seguridad de memoria (el riesgo vive en el binario)

```bash
gcc -fno-stack-protector -z execstack -O0 -o copia copia.c
./copia ana
./copia $(python3 -c 'print("A"*64)')
```

Salida esperada:

```
# entrada corta -> OK
Nombre guardado: ana
Fin del programa.

# entrada de 64 bytes en un buffer de 16 -> se machaca la pila
Segmentation fault (core dumped)
```

Como hemos compilado con `-fno-stack-protector`, el programa **no** avisa con "stack smashing
detected" (ese mensaje lo emite justamente el protector que hemos desactivado): la corrupción
pasa desapercibida y el proceso muere con un **fallo de segmentación** (código de salida 139).
Según cómo caiga la pila, puede que ni siquiera imprima `Nombre guardado:`; lo constante es que
**`Fin del programa.` nunca se imprime** — el flujo de control se ha perdido. Ahí es donde, en un
servicio real, el atacante coloca su código.

> Comprueba el código de salida: `./copia $(python3 -c 'print("A"*64)'); echo $?` → **139**
> (128 + señal 11, SIGSEGV). Si recompilas **con** protector (quita `-fno-stack-protector`),
> verás en su lugar `*** stack smashing detected ***` y `Aborted`: el protector lo detecta y
> aborta ordenadamente. Ese contraste enseña para qué sirve el protector.

## Go y Python — con seguridad de memoria (la corrupción no ocurre)

```bash
go build -o copia_go copia.go && ./copia_go $(python3 -c 'print("A"*64)')
python3 copia.py $(python3 -c 'print("A"*64)')
```

Salida esperada (ambos):

```
Nombre guardado: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Fin del programa.
```

La entrada larga se imprime entera y el programa **termina normalmente**: no hay buffer fijo
que desbordar. La cadena lleva su longitud y el runtime comprueba los accesos.

## La idea que se lleva el alumnado

| Lenguaje | ¿Seguridad de memoria? | Qué pasa con la entrada larga |
|---|---|---|
| C / C++ | **No** (salvo mitigación explícita) | Corrompe la pila → posible ejecución de código |
| Go, Rust, Java, C#, Python | **Sí**, de serie | La entrada se maneja sin corromper nada |

El riesgo de memoria no desaparece porque "programemos con cuidado": desaparece **por diseño
del lenguaje**. Elegir C para un servicio expuesto a Internet es asumir toda esa familia de
fallos salvo que se mitigue una a una. Esa decisión es la que se documenta en el dictamen PPS-E3.
