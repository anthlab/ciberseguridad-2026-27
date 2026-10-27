# ============================================================================
# FICHERO DE PRUEBA — "el caso que DEBE fallar".
#
# Contiene un secreto FALSO (son las claves de EJEMPLO documentadas por AWS,
# no dan acceso a nada). Su único propósito es demostrar que la canalización de
# seguridad BLOQUEA la fusión cuando alguien intenta subir una credencial.
#
# Procedimiento (ver ficha PPS-E13): crea una rama, añade este fichero, abre un PR
# y comprueba que el job "Secretos — gitleaks" pone el build en ROJO y bloquea la
# fusión. Después revierte y deja la rama principal limpia.
# ============================================================================

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
