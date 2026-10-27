<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>xest · Consola de diagnóstico de red</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body{font-family:system-ui,sans-serif;background:#0b1220;color:#e6edf3;margin:0}
    .wrap{max-width:520px;margin:8vh auto;padding:2rem;background:#111a2b;border-radius:12px}
    h1{font-size:1.15rem;margin-top:0}
    label{display:block;margin:.8rem 0 .3rem}
    input{width:100%;padding:.6rem;border-radius:6px;border:1px solid #33415a;background:#0b1220;color:#e6edf3}
    button{margin-top:1.2rem;padding:.7rem 1.2rem;border:0;border-radius:6px;background:#2f6feb;color:#fff;font-weight:600;cursor:pointer}
    .muted{color:#8b98a5;font-size:.85rem;margin-top:1rem}
  </style>
</head>
<body>
  <div class="wrap">
    <h1>Consola de diagnóstico · xest</h1>
    <!-- Herramienta interna de "comprobar conectividad". Vulnerable a propósito (aula). -->
    <form method="get" action="/ping.php">
      <label for="host">Host o IP a comprobar</label>
      <input id="host" name="host" placeholder="10.10.10.20" autocomplete="off">
      <button type="submit">Hacer ping</button>
    </form>
    <p class="muted">Escenario de laboratorio. Uso exclusivo en la VLAN de aula aislada.</p>
  </div>
</body>
</html>
