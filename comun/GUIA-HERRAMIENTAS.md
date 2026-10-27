# Herramientas del curso: para qué sirven y cómo comprobarlas

La herramienta se elige después de definir la pregunta. En cada práctica registra versión, entrada, opciones, resultado y limitaciones. Las alternativas de los arsenales de HE son recursos de ampliación: no necesitas instalar todas para completar el itinerario básico.

## 1. Base común

| Herramienta | Uso en el curso | Instalación en la VM de preparación | Primera comprobación |
|---|---|---|---|
| Git | Historial, ramas y evidencias de cambios | `sudo apt install git` | `git --version`; crear repo de prueba y comprobar un commit |
| Python | Scripts y análisis local | `sudo apt install python3 python3-venv` | `python3 --version`; ejecutar verificador del material |
| curl | Peticiones y cabeceras HTTP | `sudo apt install curl` | `curl -I --max-time 10 http://127.0.0.1:8080/` con portal arrancado |
| jq | Consultar JSON | `sudo apt install jq` | `printf '{"ok":true}\n' | jq -e '.ok'` |
| Docker/Compose | Objetivos y servicios | Guía de instalación | Cliente, daemon, compose y respuesta funcional del servicio |
| Navegador | Aplicaciones, HTTP y material | Incluido en la VM | Abrir índice local y pestaña Red de las herramientas de desarrollo |

En el aula sin Internet estas instalaciones deben estar ya hechas o llevar todos los paquetes y dependencias. `apt --download-only` sobre una máquina que ya tiene paquetes instalados **no garantiza** un repositorio suficiente para otra máquina limpia.

## 2. PPS: desarrollo y pruebas

**pytest y coverage.** Se instalan dentro del entorno virtual de la práctica con `python -m pip install pytest coverage pytest-cov`. Desde `PPS/UT1/laboratorio/miniproyecto` ejecuta `python -m pytest -q`, después `python -m coverage run -m pytest` y `python -m coverage report -m`. Debes distinguir número de pruebas, resultado y líneas no ejercitadas. Si pytest no encuentra tests, verifica el directorio de trabajo; cero tests no es una suite aprobada.

**Flask.** Es el framework de los pequeños portales del curso. Instala las dependencias del `requirements.txt` de la práctica dentro de su venv. Arranca con el comando de su README y abre la URL indicada. Si un import falla, comprueba `which python` y `python -m pip show flask`; suele haberse instalado en otro intérprete. Las aplicaciones vulnerables se mantienen en laboratorio.

**Argon2id.** En Python se usa `argon2-cffi`, importado como `argon2`. Instala en venv y ejecuta las pruebas de migración de la UT5. La comprobación no es solo que el hash empiece por un prefijo: verifica alta, autenticación incorrecta y migración transparente sin perder acceso.

**C, Java y Go.** Se utilizan para comparar modelos de ejecución y gestión de memoria. Instala `build-essential`, `default-jdk` y `golang-go` en la VM preparada. Comprueba `gcc --version`, `java -version`, `javac -version` y `go version`. Ejecuta los ejemplos únicamente en el laboratorio y separa fallo deliberado del ejercicio de error de compilación.

**strace y seccomp.** `strace` muestra llamadas al sistema; seccomp filtra las que puede realizar un proceso. Instala `strace` en la imagen que utiliza la ficha. La prueba de aceptación compara la misma llamada y los mismos privilegios con y sin perfil. Un error por falta de capacidad no acredita por sí solo que seccomp la haya bloqueado.

## 3. PPS: análisis y canalización

| Control | Herramienta | Preparación | Aceptación |
|---|---|---|---|
| Código | Semgrep | Venv/pipx y reglas locales del laboratorio; registrar versión | Detecta el ejemplo vulnerable y devuelve el código de salida exigido por CI |
| Dependencias e imágenes | Trivy | Binario oficial compatible y bases precargadas | Identifica imagen/lockfile, fecha de base y hallazgo conocido |
| Secretos | Gitleaks | Release oficial compatible con arquitectura | Detecta marcador sintético configurado y permite el caso limpio |
| Infraestructura como código | Checkov | Entorno Python aislado | Señala el control incumplido del `infra/main.tf` de prueba |
| Proxy/reverse proxy | nginx | Imagen fijada en compose | Configuración válida y operación HTTP/TLS antes/después |
| TLS | testssl.sh | Copia del repositorio/release oficial preparado | Informe del endpoint TLS exacto, no de un puerto HTTP |
| Host | Lynis | Paquete de la distribución | Informe del sistema analizado con permisos y alcance registrados |

Las fichas de UT7 contienen los comandos del ejercicio. Antes de copiarlos consulta `--help` en la versión instalada: algunas interfaces cambian. En preparación descarga también reglas, acciones de CI y bases; no basta guardar el ejecutable. Si falta la base de Trivy, la ausencia de resultados no significa ausencia de vulnerabilidades.

Referencias de instalación: [Semgrep](https://semgrep.dev/docs/getting-started/), [Trivy](https://trivy.dev/), [Gitleaks](https://github.com/gitleaks/gitleaks), [Checkov](https://www.checkov.io/), [testssl.sh](https://testssl.sh/), [Lynis](https://cisofy.com/lynis/). Son enlaces de preparación; el aula utiliza la versión ensayada y registrada, no una actualización improvisada.

## 4. PPS: móvil

**jadx** convierte bytecode Android en una representación de código legible. Prepara la release oficial o el paquete de Kali y comprueba `jadx --version`. Usa un APK del laboratorio y registra su hash. La carpeta `salida_jadx` incluida permite el análisis de fuentes sin APK, pero se debe declarar esa modalidad.

**MobSF** automatiza parte del análisis móvil. Prepara su contenedor o despliegue oficial, con sus dependencias e imagen almacenadas antes de entrar en el aula. Comprueba que permite subir el APK y generar un informe. El JSON de ejemplo de UT6 es material de análisis, no prueba de haber ejecutado MobSF.

**mitmproxy** permite observar tráfico HTTP y TLS de los clientes del laboratorio. Instálalo en un entorno aislado o mediante el paquete de la VM; comprueba `mitmproxy --version`. Configura el proxy en el cliente y, solo en el entorno de prueba, la CA necesaria. La aceptación consiste en ver una petición propia; para pinning, documenta el rechazo esperado y su causa. No desactives la verificación TLS como solución general.

## 5. HE: OSINT y reconocimiento

Empieza con el kit local de HE UT5: usa Python, Git, CSV y el navegador. No requiere buscar a personas ni disponer de cuentas externas. El cuaderno de octubre explica las fuentes, el grafo, los descartes y la entrega.

| Familia | Herramientas disponibles en el catálogo | Qué aportan | Dependencia importante |
|---|---|---|---|
| Metadatos | ExifTool | Campos de un fichero | Disponer del original; los metadatos pueden ser modificados |
| Alias | Sherlock, Maigret | Coincidencias por nombre de usuario | Acceso a sitios; coincidencia no acredita identidad |
| Correo/dominio | theHarvester, subfinder, Amass | Referencias, subdominios y fuentes | APIs, cuotas y conectividad según módulos |
| Agregación | SpiderFoot, Recon-ng | Organizar y cruzar fuentes | Revisar cada módulo: puede ser activo y requerir API |
| Web histórica | Wayback, gau | URLs observadas históricamente | Archivos externos; resultado histórico no acredita estado actual |
| Certificados | crt.sh y capturas locales | Nombres incluidos en certificados | Fecha y alcance de la fuente; certificado no prueba servicio accesible |
| Exposición | HIBP y simulaciones | Referencias a incidentes | Cuenta/servicio y datos autorizados; aula usa simulación |

Para ExifTool en Kali prepara `libimage-exiftool-perl`; comprueba `exiftool -ver` y analiza un fichero didáctico. Para las aplicaciones Python usa el proyecto oficial y pipx/venv; no copies una lista de nombres a pip asumiendo que son todos paquetes válidos. Los recursos y enlaces de cada familia están en `HE/recursos/arsenal-osint.md` y en el cuaderno revisado de octubre.

**Nmap** enumera puertos y servicios del objetivo permitido. Prepara `nmap` desde Kali y comprueba `nmap --version`. En el portal local, un ensayo acotado es `nmap -sT -p 8080 127.0.0.1`; el puerto debe coincidir con el servicio arrancado. Un puerto cerrado no acredita que el equipo no exista. HE-E10 exige documentar opciones y alcance.

**ffuf/feroxbuster** prueban rutas a partir de diccionarios; **httpx de ProjectDiscovery** sondea servicios HTTP; **Nuclei** aplica plantillas. Cada uno produce candidatos a revisar. El binario `httpx` de una biblioteca Python no es necesariamente el de ProjectDiscovery. Comprueba fabricante/versión y una petición local antes de clase. Las plantillas y wordlists deben estar descargadas.

## 6. HE: auditoría web

**Burp Suite Community / OWASP ZAP.** Prepara el instalador oficial o el paquete de Kali y abre la interfaz antes de exportar la VM. Configura el navegador de prácticas para su proxy, comprueba una petición al objetivo local y desactiva el proxy al finalizar. Para HTTPS, instala la CA solo en ese perfil de navegador. Identifica exactamente qué funciones están disponibles en la edición instalada.

**sqlmap, Nikto, Nuclei y herramientas XSS/JWT** amplían pruebas; no sustituyen el examen manual. Usa las opciones concretas de la ficha, objetivo autorizado y límites previstos. Una lista de alertas sin peticiones verificables no constituye un informe. El JWT puede decodificarse sin conocer el secreto: eso no demuestra que su firma sea válida ni que pueda modificarse sin rechazo.

**Selenium** automatiza navegación y regresiones. Necesita navegador, controlador compatible y dependencias Python. Prepara todo con Internet y comprueba una navegación local tras desconectar. Las descargas automáticas del controlador pueden fallar en clase; deja el controlador validado incluido en la VM.

## 7. HE: infraestructura, credenciales y radio

| Herramientas | Función docente | Preparación y criterio de aceptación |
|---|---|---|
| Metasploit / searchsploit | Relacionar fallo, condiciones y demostración de laboratorio | Paquetes de Kali, base local disponible y objetivo vulnerable de la ficha; registrar sesión y efecto |
| Bettercap / Responder | Observar intercepción y autenticación en segmento didáctico | Interfaces y VMs del ejercicio; captura de referencia y contramedida contrastada |
| Impacket / NetExec | Examinar protocolos y permisos del dominio de pruebas | Entorno de instalación oficial aislado; usar cuentas ficticias y verificar una operación autorizada |
| BloodHound CE | Analizar relaciones y caminos de acceso | Despliegue propio y dataset de laboratorio importado; grafo con nodos y relaciones esperados |
| John / Hashcat | Contrastar resistencia de credenciales sintéticas | Formato/hash correcto, backend CPU/GPU compatible y diccionario de la práctica; registrar resultado y tiempo |
| Aircrack-ng / hcxtools | Analizar capturas Wi-Fi | Adaptador/driver compatibles y AP propio, o captura suministrada marcada como tal |
| Proxmark / URH | Prácticas RFID y radio | Hardware compatible, firmware y dispositivo didáctico; verificar lectura/recepción antes de plantear emisión |
| Herramientas de túnel | Comprender segmentación y rutas | Solo topología del laboratorio; comparar conectividad antes/después y retirar el túnel al terminar |

En máquinas virtuales, el acceso USB, el modo monitor y la GPU no se deducen de que un paquete esté instalado. Si falta hardware, utiliza los datasets y registra la modalidad. No des por cumplida una evidencia de captura/emisión real con un análisis de fichero.

Los catálogos de HE conservan C2 y otros recursos avanzados como ampliación. No se instalan como parte del arranque básico ni se incluyen en la prueba general de todas las unidades.

## 8. IC: servicios y análisis

**Wazuh** reúne manager, indexer y dashboard; los agentes envían eventos. Utiliza el despliegue recuperado en `SOC/plataforma`, su `.env.example`, hashes internos y certificados. No basta ejecutar compose: revisa la guía SOC de esta edición. La aceptación es un evento conocido convertido en alerta, con agente y hora correctos.

**Suricata** analiza el tráfico visible en una interfaz. Antes de arrancar anota interfaz, red monitorizada y reglas. Valida configuración y un caso positivo/negativo. Sin mirror/SPAN o topología equivalente no ve por arte de magia todo el tráfico del aula.

**TheHive/Cortex** organizan casos y análisis de observables. Prepara el stack y sus dependencias, cuentas y permisos. Crea un caso ficticio con tarea y observable para verificarlo. Los analizadores que llaman a servicios externos no funcionarán offline salvo alternativa local configurada.

**MISP/STIX** permiten estructurar e intercambiar inteligencia. Valida sintaxis JSON, esquema STIX y, por separado, importación y consulta del objeto. No subas indicadores del aula a comunidades reales.

**Velociraptor** recoge artefactos; **Volatility** analiza memoria adquirida. Prepara versiones compatibles, símbolos y máquinas de prueba. Comprueba un artefacto controlado o una imagen conocida. El curso incluye salidas sintéticas para trabajar el razonamiento cuando no haya adquisición real; deben etiquetarse como tales.

**GoPhish/MailHog** se usan para simulación local de concienciación. Verifica el circuito con destinatarios ficticios y buzón sumidero. Una métrica de apertura puede proceder de automatismos y necesita interpretación.

## 9. Registro de instalación que debes conservar

Por herramienta: nombre, versión, fuente oficial, fecha, SO/arquitectura, método de instalación, dependencias, datos/reglas/API, comando de comprobación, prueba funcional, resultado y solución de errores. La plantilla `REGISTRO-ENTORNO.csv` permite recogerlo. Marca como pendiente cualquier prueba que no hayas ejecutado.
