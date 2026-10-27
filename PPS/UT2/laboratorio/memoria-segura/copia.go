// PPS · UT2 · El mismo programa en Go — SOLO LABORATORIO.
//
// Go tiene seguridad de memoria: las cadenas y los slices llevan su longitud
// y el runtime comprueba los accesos. No existe "copiar más de lo que cabe":
// una cadena crece según su contenido y un acceso fuera de rango entra en
// pánico controlado (no ejecuta código del atacante). El desbordamiento clásico
// de C aquí NO es posible.
//
// Compilar y ejecutar:
//     go build -o copia_go copia.go
//     ./copia_go ana
//     ./copia_go $(python3 -c 'print("A"*64)')   -> imprime las 64 A, sin corromper nada
package main

import (
	"fmt"
	"os"
)

func guardarNombre(entrada string) {
	// No hay buffer de tamaño fijo que machacar: la cadena lleva su longitud.
	fmt.Printf("Nombre guardado: %s\n", entrada)
}

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintf(os.Stderr, "uso: %s <nombre>\n", os.Args[0])
		os.Exit(1)
	}
	guardarNombre(os.Args[1])
	fmt.Println("Fin del programa.")
}
