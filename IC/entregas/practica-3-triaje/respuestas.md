# Respuestas · Anthony Zamora Martínez

## 1. Nivel y prioridad
El nivel lo asigna la regla. Yo decido la prioridad con el contexto, la importancia del equipo y los indicios de éxito. Una alerta de nivel bajo puede ser importante dentro de una secuencia de ataque.

## 2. El mensaje de logger
Lo he encontrado en journald, pero no como alerta en el fichero recogido. Un mensaje puede no cumplir ninguna regla que genere alerta. Con esa ausencia no puedo determinar si el manager lo recibió: revisaría la recogida y probaría la línea con logtest.

## 3. Un grupo benigno esperado
He clasificado provisionalmente así la instalación de openssl y el cambio de /usr/bin/openssl 29 segundos después. Coinciden el paquete y el binario. Confirmaría que la actualización estaba autorizada y que el archivo pertenece al paquete legítimo.

## 4. La alerta más importante
Destacaría 40112, nivel 12, porque registra un acceso correcto después de los fallos. No es la de mayor nivel, pero señala un posible cambio de intento a acceso conseguido. La 40501, nivel 15, añade preocupación por la cuenta nueva. Investigo el grupo completo, no solo la alerta más alta.

## 5. Qué me falta para confirmar compromiso
Necesito confirmar la autorización del acceso y de los cambios, relacionarlos con la sesión de tecnico, revisar el contenido de img.php y los cambios de index.php y contrastar los registros web y de procesos. Hay indicios fuertes, pero no puedo llamar webshell a un archivo solo por su nombre o extensión.
