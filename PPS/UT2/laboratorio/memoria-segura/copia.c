/* PPS · UT2 · Demo de (in)seguridad de memoria — SOLO LABORATORIO AISLADO.
 *
 * El mismo problema en tres lenguajes: copiar un dato de entrada (argv[1])
 * a un espacio de tamaño fijo. En C no hay comprobación de límites: si el
 * dato es más largo que el buffer, se machaca la pila. Ese es "dónde vive
 * el riesgo" en un lenguaje sin seguridad de memoria.
 *
 * Compilar (desactivando protecciones para VERLO, cosa que en producción
 * NUNCA se hace):
 *     gcc -fno-stack-protector -z execstack -O0 -o copia copia.c
 * Ejecutar:
 *     ./copia ana                                  -> OK
 *     ./copia $(python3 -c 'print("A"*64)')        -> desbordamiento
 */
#include <stdio.h>
#include <string.h>

void guardar_nombre(const char *entrada) {
    char buffer[16];          /* espacio fijo de 16 bytes */
    strcpy(buffer, entrada);  /* SINK: copia sin comprobar el tamaño */
    printf("Nombre guardado: %s\n", buffer);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "uso: %s <nombre>\n", argv[0]);
        return 1;
    }
    guardar_nombre(argv[1]);   /* ENTRADA: dato externo sin validar */
    printf("Fin del programa.\n");
    return 0;
}
