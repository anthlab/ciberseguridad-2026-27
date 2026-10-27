/* PPS UT1 · Validador de nombre de usuario — versión C (COMPILADO A NATIVO).
 *
 * Ejercicio PPS-E1: localiza PUNTO DE ENTRADA, SINK y VALIDACIÓN y señala
 * DÓNDE PUEDE FALLAR este modelo.
 * Pista: C no tiene seguridad de memoria. Copiar sin comprobar el tamaño de
 * destino desborda el buffer -> corrupción de memoria / ejecución de código.
 *
 * Compilar para la demo (con protecciones desactivadas, SOLO laboratorio):
 *   gcc -fno-stack-protector -z execstack -o validar validar.c
 * Probar el desbordamiento:
 *   ./validar $(python3 -c 'print("A"*100)')
 */
#include <stdio.h>
#include <string.h>

/* VALIDACIoN (ausente): esta funcion NO comprueba la longitud antes de copiar. */
void buscar_usuario(const char *nombre) {
    char buffer[32];                 /* destino de tamano fijo */
    /* SINK (memoria): strcpy copia sin mirar el tamano -> desbordamiento de pila. */
    strcpy(buffer, nombre);          /* PUNTO DE ENTRADA 'nombre' -> SINK inseguro */
    printf("acceso de %s\n", buffer);
}

int main(int argc, char **argv) {
    /* PUNTO DE ENTRADA: argumento de linea de comandos (dato externo). */
    buscar_usuario(argc > 1 ? argv[1] : "ana");
    return 0;
}

/* Corregido seria: usar snprintf/strncpy con el tamano del destino,
 * o validar length(nombre) < sizeof(buffer) antes de copiar. */
