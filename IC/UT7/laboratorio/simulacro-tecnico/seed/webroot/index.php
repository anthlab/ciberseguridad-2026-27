<?php
// index.php — Portal SOC de xest (contenido legítimo de laboratorio).
$host = gethostname();
$now  = date('Y-m-d H:i:s');
?>
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Portal SOC de xest</title>
  <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
  <header>
    <h1>Portal SOC de xest</h1>
    <p class="sub">Centro de Operaciones de Seguridad &middot; entorno de laboratorio</p>
  </header>
  <main>
    <section class="card">
      <h2>Estado del servicio</h2>
      <p>Servicio <strong>operativo</strong>.</p>
      <ul>
        <li>Nodo: <code><?php echo htmlspecialchars($host); ?></code></li>
        <li>Hora del servidor: <code><?php echo htmlspecialchars($now); ?></code></li>
      </ul>
    </section>
    <section class="card">
      <h2>Servicios internos</h2>
      <ul>
        <li>Panel Wazuh</li>
        <li>TheHive &middot; Cortex</li>
        <li>MISP</li>
      </ul>
    </section>
  </main>
  <footer>
    <p>xest.local &middot; uso interno &middot; VLAN de laboratorio aislada</p>
  </footer>
</body>
</html>
