# OPERACIÓN GEOGHOST — CUADERNO DEL ALUMNADO
**Hacking ético · OSINT · 15 de octubre de 2026**

## Objetivos
1. Distinguir datos observados, hipótesis y conclusiones.
2. Analizar metadatos de fotografías; interpretar EXIF y ausencia de GPS.
3. Investigar un alias ficticio, validar correos, teléfonos y direcciones de ejemplo y revisar dominios autorizados.
4. Geolocalizar una fotografía de un lugar público y sustentar la respuesta en dos fuentes independientes.

## Reglas
Trabajad en parejas o tríos. No investiguéis a personas reales ni a compañeros, no consultéis servicios con números privados y no uséis cuentas ajenas. Los materiales se han preparado como simulación. Toda herramienta o búsqueda debe ir acompañada de una captura o anotación de evidencia.

## Parte A — Pistas digitales (35 min)
- Alias de prueba: `geo_ghost_demo_2026`. ¿Qué evidencia sería insuficiente para concluir que dos perfiles pertenecen a la misma persona?
- Correo de laboratorio: `contacto@ejemplo.invalid`. Identificad parte local, dominio y por qué `.invalid` no sirve para correspondencia real.
- Teléfono simulado: `+34 600 000 000` (dato ficticio; no llamar ni introducir en servicios externos). Descomponed prefijo nacional y formato; explicad qué NO puede deducirse.
- Dominio docente: `example.org` (dominio de ejemplo; no escanear). Identificad de forma conceptual DNS, MX, TXT y CAA; usad `dig example.org` solo como demostración pasiva si el docente lo autoriza.
- Dirección de práctica: `Plaza Mayor, Salamanca` (espacio público). Diferenciad dirección pública frente a domicilio particular.

## Parte B — Fotografía y verificación (40 min)
1. Descargad SOLO la foto indicada por el profesor y guardad copia original.
2. Calculad SHA-256: `sha256sum foto.jpg` (Linux) o `Get-FileHash foto.jpg -Algorithm SHA256` (PowerShell).
3. Inspeccionad: `exiftool -a -G1 -s foto.jpg`. Anotad fecha, cámara, GPS si existiera, autoría si existiera y software. Sin etiquetas NO implica que sean falsas.
4. Observad texto, soportales, materiales, fachadas, iluminación, señales, monumentos. Describid al menos cinco pistas.
5. Formulad tres hipótesis de ubicación; descartad dos usando cartografía/fuentes de referencia.
6. Contrastad una fuente independiente (mapa, foto pública, organismo de turismo); distinguíd la página fuente de la imagen editada.

## CTF FINAL — 60 MINUTOS (100 puntos + bonus)
**Misión:** un equipo de investigación ha recibido `ctf_foto.jpg`. Localizad el espacio público representado y entregad un informe reproducible. Las respuestas no deben identificar personas ni domicilios.

**Entrega:** `equipo_N_informe.md` con ciudad, nombre del lugar, coordenadas aproximadas, precisión justificada, mínimo 2 enlaces públicos, 3 capturas y metodología; flag en formato `GEOGHOST{CIUDAD_LUGAR}` (mayúsculas y sin tildes ni espacios; usar `_`).

**Cronómetro:** 0–10 min examen visual; 10–20 min EXIF; 20–40 min búsquedas/verificación; 40–50 min coordenadas y fuentes; 50–60 min entrega y revisión.

**Rúbrica:** metadatos 20; indicios visuales 20; corroboración independiente 20; ubicación justificada 30; informe reproducible 10. Bonus +10 si detectáis y explicáis una pista engañosa.

**Pistas desbloqueables:** Pista 1 (min 20): «Fijaos en la arquitectura de una gran plaza porticada española». Pista 2 (min 35): «Explorad capitales de provincia del oeste de España». El uso de pistas resta 5 puntos por pista, si el profesor así lo decide.

**Evaluación crítica:** una coordenada atribuida al archivo por una web externa puede ser el lugar del fotógrafo, un punto aproximado o metadatos incorporados posteriormente; justifícalo.

**Fuentes disponibles:** el profesor proporciona `ctf_foto.jpg`; si no está disponible, usad la página del recurso indicada en `recursos/INSTRUCCIONES_FOTO.txt`, sin consultar el nombre descriptivo del archivo hasta terminar el reto.
