# Primera sesión práctica: terminal, Git y servicio web

Al terminar podrás explicar qué fichero estás sirviendo, qué cambio has guardado en Git y qué diferencia hay entre imagen y contenedor. Trabajaremos dentro de Kali y conservaremos evidencias de cada paso.

## 1. Situarte en el sistema

```bash
pwd
mkdir -p ~/trabajo-curso/arranque
cd ~/trabajo-curso/arranque
pwd
```

`pwd` muestra la carpeta actual; `mkdir -p` crea el directorio si falta; `cd` cambia a él. El segundo `pwd` debe terminar en `/trabajo-curso/arranque`. Si no coincide, corrige la ruta antes de crear archivos.

## 2. Crear una página mínima

```bash
cat > index.html <<'HTML'
<!doctype html>
<html lang="es">
<meta charset="utf-8">
<title>Mi laboratorio</title>
<h1>Laboratorio de ciberseguridad</h1>
<p>Primera versión del servicio de prácticas.</p>
</html>
HTML
cat index.html
```

`cat >` guarda el texto en el archivo. El marcador HTML delimita el contenido; no forma parte del archivo. Abre `index.html` desde el navegador para distinguir un documento local de una respuesta servida por HTTP.

## 3. Registrar el cambio con Git

```bash
git init
git config user.name "Alumno NN"
git config user.email "alumno-nn@xest.example"
git status
git add index.html
git commit -m "Crea la página inicial del laboratorio"
git log --oneline -1
```

Cambia NN por tu número de lista. La configuración se aplica solo a este repositorio. `add` prepara el contenido que entrará al commit; `commit` crea un punto del historial. Un commit no implica que hayas subido nada a Internet.

Modifica la frase de la página con el editor y ejecuta `git diff`. Comprueba que aparece exactamente tu cambio; guarda otro commit. Explica qué representa cada identificador del historial.

## 4. Servir la página por HTTP

Comprueba que la imagen nginx fijada del curso está disponible. Con el fichero de bloqueo o compose proporcionado, el profesor debe haber cargado la imagen antes de clase. Para este ejercicio se utiliza la misma referencia fijada:

```bash
docker run --rm --name curso-arranque-nn -d \
  -p 127.0.0.1:18090:80 \
  --mount "type=bind,source=$PWD,target=/usr/share/nginx/html,readonly" \
  nginx:1.27-alpine@sha256:65645c7bb6a0661892a8b03b89d0743208a18dd2f3f17a54ef4b76fb8e2f2a10
curl -i --max-time 10 http://127.0.0.1:18090/
```

El contenedor ejecuta nginx. `-p` conecta el puerto local 18090 con el 80 del contenedor. El montaje permite leer tus archivos desde nginx y es de solo lectura dentro del contenedor. `--rm` elimina el contenedor cuando se detiene; no borra tu carpeta de trabajo.

Debes observar una respuesta HTTP satisfactoria y el texto de tu página. Abre la misma URL en el navegador de Kali. Cambia una frase, recarga y explica por qué se ve el cambio sin construir una imagen nueva.

## 5. Cerrar y justificar

```bash
docker logs curso-arranque-nn
docker stop curso-arranque-nn
git status
```

Entrega un informe corto con: ruta del proyecto, dos commits, petición/respuesta HTTP, explicación del montaje y diferencia entre abrir un archivo y pedirlo a un servidor. Si el puerto estaba ocupado, documenta cómo lo comprobaste y qué puerto alternativo utilizaste. No sustituyas comandos fallidos por capturas de ejemplo.
