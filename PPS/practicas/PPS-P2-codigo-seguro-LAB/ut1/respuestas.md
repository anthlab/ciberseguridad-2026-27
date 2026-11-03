# Práctica 2 · Código seguro

1. El sink que considero más peligroso en `validar.py` es `os.system()`.
   El nombre se concatena en un comando y la shell puede interpretar
   caracteres de la entrada como parte de ese comando.

2. Antes de corregir el fallo pasaban los 3 tests originales.
   La cobertura de `descuentos.py` era del 83 %.

3. Al probar descuentos del 150 % y del -5 %, pytest mostró
   `Failed: DID NOT RAISE ValueError`. La función calculaba el precio
   con esos porcentajes en vez de rechazarlos. Añadí una comprobación
   para admitir solo porcentajes entre 0 y 100, ambos incluidos.

4. El fuzzing encontró que un precio `nan` devolvía `nan` incluso con
   un descuento válido. Añadí una prueba para ese caso y comprobé que
   el precio fuera finito y no negativo antes de calcular el descuento.
   Al final pasaron los 6 tests y el fuzzing dio 0 fallos en 20.000 intentos.

5. Repositorio: https://github.com/anthlab/ciberseguridad-2026-27
