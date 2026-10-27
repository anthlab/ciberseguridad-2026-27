<?php
// ping.php — comprobación de conectividad.
//
// *** VULNERABILIDAD SEMBRADA A PROPÓSITO (aula, HE UT6) ***
// El parámetro `host` se concatena SIN sanear dentro de un comando de shell.
// Cualquier metacarácter de shell (; | & $() `) permite ejecutar comandos arbitrarios
// como el usuario del servidor web (www-data). Es una inyección de comandos de manual.
//
// Corrección (lo que el alumnado debe saber recomendar): NO invocar la shell con
// entrada del usuario. Validar `host` contra una lista blanca (regex de IP/FQDN) y
// usar una API sin shell (p. ej. exec con argumentos separados y escapeshellarg()).

header('Content-Type: text/plain; charset=utf-8');

$host = $_GET['host'] ?? '';
if ($host === '') {
    echo "Uso: /ping.php?host=IP_o_dominio\n";
    exit;
}

// Línea vulnerable: concatenación directa en la shell.
$salida = shell_exec('ping -c 1 -W 1 ' . $host . ' 2>&1');
echo $salida;
