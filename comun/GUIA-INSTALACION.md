# Preparar el puesto de trabajo · Curso 2026–2027

Vamos a preparar un entorno que podamos repetir y recuperar. Primero comprobaremos el puesto, después el material y, por último, la práctica concreta. Cada comprobación produce una evidencia: un programa instalado todavía no demuestra que el ejercicio funcione.

## 1. Qué necesitas y dónde se ejecuta cada cosa

| Elemento | Función | Lugar |
|---|---|---|
| Windows del aula | Anfitrión de la máquina virtual | PC físico |
| VirtualBox | Ejecuta la máquina de prácticas | Windows |
| Kali Linux | Terminal, herramientas y objetivos locales | Máquina virtual |
| Docker Engine + Compose | Ejecutan aplicaciones del laboratorio | Dentro de Kali |
| Python y entornos virtuales | Scripts, pruebas y análisis de datos | Dentro de Kali |
| SOC | Recibe eventos y permite investigar | Servidor Linux o VM dedicada del profesor |
| Paquete de alumnado | Apuntes, fichas, datos y scripts | `~/xest-lab/2026-2027` dentro de Kali |

Los comandos de esta guía se ejecutan en la **terminal de Kali**, salvo que el paso diga Windows o servidor. `localhost` siempre significa el equipo o la VM donde estás ejecutando el navegador/comando. El navegador de Windows no comparte el localhost de Kali.

Como punto de partida para el laboratorio básico, reserva 4 vCPU, 8 GB de RAM y 60 GB de disco para Kali si el anfitrión puede asumirlo. Es una propuesta de preparación, no una medición del aula. Con menos memoria, arranca solo los servicios de la sesión. El SOC completo necesita recursos aparte; no lo arranques junto a todos los objetivos en cada puesto.

## 2. Importar Kali en Windows

1. Utiliza la máquina del aula preparada por el profesor. Registra el nombre de la imagen, fecha, arquitectura y hash SHA-256.
2. Si recibes una `.ova`, abre VirtualBox → **Importar servicio virtualizado** y selecciona el fichero. Si recibes la imagen oficial comprimida `.7z`, extráela y utiliza **Añadir** sobre el fichero `.vbox`: no se importa como OVA.
3. Revisa RAM, CPU y carpeta de almacenamiento antes de iniciar. La imagen debe corresponder a la arquitectura del equipo: la imagen amd64 del aula no es una VM ARM para un Mac Apple Silicon.
4. Arranca Kali con las credenciales facilitadas. En la imagen oficial, cambia las credenciales iniciales tras el primer acceso; no publiques las de la plantilla del aula.
5. Comprueba teclado, pantalla y terminal. Ejecuta `uname -m`, `python3 --version` y `df -h` y guarda la salida.
6. Apaga Kali y crea una instantánea llamada `base-curso-validada` cuando las comprobaciones de esta guía estén completas. Una instantánea no sustituye la copia de tus entregas fuera de la VM.

Fuente de la distinción `.ova`/`.vbox`: [documentación oficial de Kali para VirtualBox](https://www.kali.org/docs/virtualization/import-premade-virtualbox/).

## 3. Red del laboratorio

Para prácticas web locales, el navegador y las herramientas funcionan dentro de la misma Kali y los puertos se publican en `127.0.0.1`. Así no necesitan estar expuestos a la LAN.

Las prácticas de interceptación, directorio activo o sensores requieren la topología específica de su ficha. Utiliza una **red interna de VirtualBox** con las VMs participantes, o una red de laboratorio aislada configurada por el profesor. La red interna de VirtualBox no conecta automáticamente con el servidor físico ni con un switch externo.

Para recibir el material, usa USB/carpeta compartida o una conexión aprobada al servidor de aula. Si se utiliza adaptador puente, debe estar conectado a la red aislada de prácticas y verificarse su alcance. NAT se utiliza para preparar actualizaciones con Internet; no da visibilidad automática al sensor sobre otros equipos.

Anota IP, máscara, puerta de enlace y nombre de interfaz:

```bash
ip -br addr
ip route
```

No copies la IP de un ejemplo como si fuera la asignada a tu equipo. Antes de una práctica activa verifica el objetivo exacto del ROE.

## 4. Instalar la base con Internet (preparación de la VM)

Este apartado se realiza en la preparación, no en el aula desconectada. En una Kali limpia se puede usar su repositorio para Docker:

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-v2 python3 python3-venv python3-pip git curl jq unzip
sudo systemctl enable --now docker
sudo usermod -aG docker "$USER"
```

Cierra sesión y vuelve a entrar para cargar el grupo. Después:

```bash
docker version
docker compose version
docker info
```

Debe aparecer información del cliente y del servidor Docker, y Compose debe reconocer `docker compose`. Si tu edición de Kali no ofrece `docker-compose-v2`, consulta los paquetes disponibles con `apt-cache search docker-compose`; prepara una edición compatible o instala el plugin desde la documentación oficial. No mezcles a ciegas paquetes `docker.io` con `docker-ce`.

Errores habituales:

| Error | Qué comprobar | Cómo continuar |
|---|---|---|
| Permission denied en docker.sock | `id -nG` | Cierra sesión y entra otra vez; verifica que perteneces al grupo docker |
| Cannot connect to Docker daemon | `systemctl status docker` | Arranca el servicio y vuelve a ejecutar `docker info` |
| compose no es un comando | `docker compose version` | Falta Compose v2 en esa máquina |
| No space left on device | `df -h` y `docker system df` | Amplía espacio o revisa imágenes prescindibles; conserva las de las prácticas offline |
| Exec format error | `uname -m` y arquitectura de la imagen/binario | Usa artefactos para la arquitectura de la VM |

El grupo docker permite operaciones privilegiadas sobre el equipo; se utiliza en la VM de prácticas. [Instalación Docker en Kali](https://www.kali.org/docs/containers/installing-docker-on-kali/) y [alternativa oficial Docker Engine para Debian y derivados](https://docs.docker.com/engine/install/debian/).

## 5. Copiar y comprobar el material sin Internet

1. Copia el paquete **ALUMNADO** completo; conserva su estructura de carpetas.
2. Coloca la carpeta `2026-2027` dentro de `~/xest-lab/`. No la mezcles con una entrega antigua.
3. Abre `INICIO.html` en el navegador: es un índice local y no requiere servidor ni cuenta.
4. Comprueba los archivos con el verificador incluido:

```bash
cd ~/xest-lab/2026-2027
python3 comun/verificar-material.py
```

El resultado debe mostrar cero archivos ausentes o modificados respecto a la distribución. Ejecuta esta comprobación **antes** de editar las prácticas. Copia los ejercicios a una carpeta de trabajo si quieres conservar intactos los originales.

## 6. Python sin romper los paquetes de Kali

Cada práctica con dependencias usa un entorno virtual. No instales paquetes del curso en el Python del sistema con `sudo pip`.

Con Internet, durante la preparación:

```bash
python3 -m venv ~/venvs/curso
source ~/venvs/curso/bin/activate
python -m pip install pytest pytest-cov coverage flask argon2-cffi requests
python -m pip freeze > ~/venvs/curso/versiones.txt
```

Sin Internet, el profesor debe haber preparado las ruedas para **la misma versión de Python, sistema y arquitectura**:

```bash
python3 -m venv ~/venvs/curso
source ~/venvs/curso/bin/activate
python -m pip install --no-index --find-links ~/xest-repo/wheels -r ~/xest-repo/requirements-lock.txt
```

Comprueba `python -c "import pytest, flask, argon2, requests; print('Importaciones OK')"`. Si falta una rueda, no continúes fingiendo una instalación completa: utiliza la VM preparada o completa el repositorio en un equipo con Internet. Un `pip freeze` de macOS no es un repositorio offline para Kali.

## 7. Cargar las imágenes y arrancar objetivos

El paquete de documentos no incluye las imágenes de varios gigabytes. El profesor proporciona una VM preparada o un repositorio de imágenes exportado tras validar la arquitectura del aula.

```bash
# Repite para cada .tar recibido y verificado:
docker load -i ~/xest-repo/images/objetivos.tar
cd ~/xest-lab/2026-2027/comun/entornos/objetivos
docker compose config --quiet
docker compose images
```

Arranca únicamente lo necesario:

```bash
# PPS UT3: portal de referencia
docker compose up -d --pull never portal-soc
curl -fS --connect-timeout 3 --max-time 10 http://127.0.0.1:8080/

# Prácticas web: Juice Shop y DVWA (incluye su base de datos)
docker compose up -d --pull never juice-shop dvwa
```

`--pull never` evita depender de una descarga en clase. Si la imagen falta, Docker debe avisar: cargarla es un requisito, no un paso opcional. `docker compose config` comprueba la configuración, pero no demuestra que arranque ni que la aplicación funcione.

| Servicio | URL en el navegador de Kali | Comprobación funcional |
|---|---|---|
| Portal SOC de referencia | `http://127.0.0.1:8080` | Página visible y contenido reconocible |
| Juice Shop | `http://127.0.0.1:3000` | Catálogo carga; registro/login con cuenta ficticia |
| DVWA | `http://127.0.0.1:8081/setup.php` | Crear/resetear BD solo al iniciar el laboratorio; después login |
| Vuln-web histórico | `http://127.0.0.1:8082` | Solo para la ficha que lo requiera |
| bWAPP histórico | `http://127.0.0.1:8083` | Inicializar siguiendo la imagen; verificar login y ejercicio |

DVWA necesita su servicio de base de datos; esta edición lo incluye. El nivel de seguridad se comprueba en la interfaz de DVWA y se registra en cada evidencia. No se da por aplicado por una variable de entorno del compose. Consulta [DVWA oficial](https://github.com/digininja/DVWA).

Si una aplicación devuelve 200 pero no permite entrar o completar la operación, aún no está validada. Consulta `docker compose ps` y `docker compose logs --tail=100 NOMBRE-SERVICIO`. No publiques logs que contengan claves.

## 8. Nombres de laboratorio y puertos

Las fichas usan nombres como `juice.xest.local` o `portal-soc.xest.local` en lugar de direcciones. Así el mismo comando sirve tanto si el objetivo está en tu puesto como si está en un servidor del aula: lo único que cambia es a qué dirección resuelve el nombre.

| Dónde está el servicio | Fichero de nombres | Dirección |
|---|---|---|
| Objetivos web (Juice Shop, DVWA, portal, bWAPP) en tu Kali — **modo por defecto** | `entornos/objetivos/hosts-puesto` | `127.0.0.1` |
| SOC (Wazuh, TheHive, MISP) y objetivos servidos por el profesor | `entornos/objetivos/hosts-aula` o DNS del laboratorio | IP de la VLAN que indique el profesor |

Añade las líneas solo si el nombre aún no existe, y nunca mezcles las dos versiones del mismo nombre:

```bash
getent hosts juice.xest.local || sudo tee -a /etc/hosts < comun/entornos/objetivos/hosts-puesto
getent hosts portal-soc.xest.local      # debe mostrar 127.0.0.1 en modo puesto
curl -I --max-time 10 http://portal-soc.xest.local:8080/
```

Si `curl` responde `Connection refused`, el nombre resuelve pero el contenedor no está levantado (`docker compose ps`). Si responde `Could not resolve host`, falta la línea en `/etc/hosts`. Si tarda y acaba en `timed out`, el nombre apunta a una IP del aula que no existe en tu red: revisa que no hayas copiado `hosts-aula` para los objetivos locales.

Varios laboratorios usan el puerto 8080 (portal, proxy, mitmproxy). No los arranques simultáneamente: detén el servicio anterior o aplica el puerto alternativo previsto en la ficha. Confirma con `ss -ltnp`.

## 9. Cómo añadir herramientas por necesidad

Antes de instalar, identifica la ficha y el resultado que necesitas. El catálogo histórico contiene alternativas y recursos online; no todos son requisitos del curso ni funcionan offline. La guía de herramientas explica los grupos y las pruebas de aceptación.

- Paquete de Kali: `apt-cache policy NOMBRE`, después `sudo apt install NOMBRE` en preparación.
- Aplicación Python: usa `pipx` o un entorno virtual y el proyecto oficial; no deduzcas el nombre del paquete a partir del nombre comercial.
- Binario Go: compila la versión elegida en una máquina compatible y conserva `go version -m RUTA_BINARIO`.
- Contenedor: registra etiqueta, digest, arquitectura, puertos, volúmenes y prueba funcional.
- Servicio con API: registra cuenta/plan, permisos y límites. No lo conviertas en dependencia de una clase sin Internet.

Para preparar una OVA, instala las herramientas de cada bloque, abre las aplicaciones gráficas al menos una vez, precarga datos/reglas y reinicia sin conexión antes de exportar. Un verificador de nombres de ejecutables no sustituye ese ensayo.

## 10. Cierre de sesión y recuperación

Guarda informe, comandos, versiones, salidas y hashes antes de detener el entorno. `docker compose stop` permite parar; `docker compose down` elimina contenedores y redes del proyecto, pero normalmente conserva volúmenes. No utilices `down -v` como cierre rutinario: elimina datos persistentes.

Si necesitas repetir desde cero, usa la instantánea inicial o el procedimiento de reinicio de la práctica, conservando fuera las evidencias. Anota qué has restaurado: código, base de datos, VM o todos ellos.
