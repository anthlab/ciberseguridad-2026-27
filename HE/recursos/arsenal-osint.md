# Arsenal OSINT — las mejores herramientas por objetivo (con GitHub e instalación)

Catálogo ampliado para HE (reconocimiento) e IC UT4 (OSINT defensivo). Complementa
`arsenal-github.md` (que da lo básico por UT) con el set completo por categoría. ⭐ = la
recomendada de cada bloque · 🐹 = se instala con `go install` · ⚠️ = estado
discontinuado/inestable (verificar antes de usar en clase).

> **Regla de aula (no negociable)**: estas herramientas solo se usan sobre los objetivos
> permitidos por `../../comun/legal/osint-aula-politica.md` (uno mismo con consentimiento,
> persona jurídica pública, objetivo sintético del profesor, o entorno de práctica
> autorizado). Nunca sobre compañeros ni terceros. El auto-OSINT es el objetivo por defecto.

Instalación base recomendada (VM del alumno):
```bash
sudo apt install -y pipx tor golang-go exiftool
pipx ensurepath
```

---

## 0. Frameworks todo-en-uno (empezar aquí)
| Herramienta | Repo / URL | Instalación | Para qué |
|---|---|---|---|
| **SpiderFoot** ⭐ | https://github.com/smicallef/spiderfoot | `pipx install spiderfoot` → `sf.py -l 127.0.0.1:5001` | 200+ módulos, GUI web, correlaciona todo (dominios, correos, IP, brechas). El mejor para docencia. |
| **Recon-ng** ⭐ | https://github.com/lanmaster53/recon-ng | `pipx install recon-ng` | Framework tipo Metasploit para OSINT: workspaces, módulos, marketplace. |
| **theHarvester** | https://github.com/laramies/theHarvester | `pipx install theHarvester` | Correos, subdominios, hosts, personas desde buscadores y fuentes pasivas. |
| **Maltego CE** | https://www.maltego.com | descarga (freemium) | Grafo visual de entidades y relaciones. El estándar de la industria para presentar. |
| **sn0int** | https://github.com/kpcyrd/sn0int | `apt install sn0int` (o repo) | Motor OSINT semi-automático con base de datos de entidades. |
| **FinalRecon** | https://github.com/thewhiteh4t/FinalRecon | `pipx install finalrecon` | Reconocimiento web todo-en-uno (whois, DNS, headers, crawl, subdominios). |
| **OSINT Framework** | https://osintframework.com | web (sin instalar) | Mapa de recursos por categoría; úsalo como índice en clase. |

## 1. Nombre de usuario / alias (username enum)
| Herramienta | Repo | Instalación | Para qué |
|---|---|---|---|
| **Maigret** ⭐ | https://github.com/soxoj/maigret | `pipx install maigret` | Busca un usuario en 3000+ sitios y extrae datos del perfil. El más completo. |
| **Sherlock** ⭐ | https://github.com/sherlock-project/sherlock | `pipx install sherlock-project` | Rápido, 400+ redes. Clásico para el primer barrido. |
| **WhatsMyName** | https://github.com/WebBreacher/WhatsMyName | web + `whatsmyname` | Base de datos de detección de cuentas por usuario. |
| **Blackbird** | https://github.com/p1ngul1n0/blackbird | `git clone` + `pip install -r` | Búsqueda de cuentas por usuario/email con export. |

## 2. Correo electrónico
| Herramienta | Repo | Instalación | Para qué |
|---|---|---|---|
| **holehe** ⭐ | https://github.com/megadose/holehe | `pipx install holehe` | En qué 120+ servicios está registrado un correo (sin alertar al titular). |
| **h8mail** ⭐ | https://github.com/khast3x/h8mail | `pipx install h8mail` | Busca el correo en filtraciones (local o APIs: HIBP, Dehashed, IntelX). |
| **Mosint** 🐹 | https://github.com/alpkeskin/mosint | `go install github.com/alpkeskin/mosint/v3@latest` | Todo-en-uno para un correo: brechas, redes, reputación. |
| **GHunt** ⭐ | https://github.com/mxrch/GHunt | `pipx install ghunt` | Todo lo asociado a una cuenta **Google** (nombre, reseñas, fotos, dispositivos). |
| **Ignorant** | https://github.com/megadose/ignorant | `pipx install ignorant` | Si un número de teléfono está registrado en servicios (equivalente a holehe para tel). |

## 3. Teléfono
| Herramienta | Repo | Instalación | Para qué |
|---|---|---|---|
| **PhoneInfoga** ⭐ | https://github.com/sundowndev/phoneinfoga | binario / docker | Operador, tipo de línea, geografía y footprint de un número. El referente. |
| **Ignorant** | https://github.com/megadose/ignorant | `pipx install ignorant` | Registro de un número en Instagram/Amazon/etc. |

## 4. Dominio · infraestructura · subdominios (pasivo)
| Herramienta | Repo | Instalación | Para qué |
|---|---|---|---|
| **Amass** ⭐ | https://github.com/owasp-amass/amass | `apt install amass` / `go install` | Mapeo de superficie de ataque (subdominios, ASN, gráfico). OWASP. |
| **subfinder** 🐹 | https://github.com/projectdiscovery/subfinder | `go install .../subfinder@latest` | Subdominios pasivos, rápido. |
| **Photon** | https://github.com/s0md3v/Photon | `git clone` | Crawler OSINT: extrae correos, claves, enlaces, subdominios de un sitio. |
| **waybackurls** 🐹 | https://github.com/tomnomnom/waybackurls | `go install` | URLs históricas de un dominio (Wayback). |
| **gau** 🐹 | https://github.com/lc/gau | `go install` | "Get All URLs" de Wayback/CommonCrawl/OTX. |
| **crt.sh** | https://crt.sh | web / `curl` | Subdominios por Certificate Transparency (sin tocar el objetivo). |
| **DNSdumpster** | https://dnsdumpster.com | web | Mapa DNS visual de un dominio. |

**Motores de exposición** (cuentas gratuitas): **Shodan** (shodan.io), **Censys**
(censys.io), **ZoomEye** (zoomeye.org), **FOFA** (fofa.info), **Netlas** (netlas.io),
**SecurityTrails** (DNS histórico). Consulta lo ya indexado sin escanear.

## 5. Metadatos y documentos
| Herramienta | Repo | Instalación | Para qué |
|---|---|---|---|
| **ExifTool** ⭐ | https://github.com/exiftool/exiftool | `apt install libimage-exiftool-perl` | Metadatos de fotos/documentos (GPS, autor, software, fechas). |
| **Metagoofil** | https://github.com/opsdisk/metagoofil | `git clone` | Descarga documentos públicos de un dominio y extrae sus metadatos. |

## 6. Imágenes y geolocalización (GEOINT)
| Recurso | URL | Para qué |
|---|---|---|
| **Búsqueda inversa** | Google Images · Yandex ⭐ · Bing · TinEye | Yandex es el mejor para rostros/lugares. |
| **GeoSpy / GeoGuessr-style** | geospy.ai | Estimar localización de una foto por IA (verificar siempre). |
| **SunCalc** | suncalc.org | Deducir hora/orientación por sombras. |
| **Google Earth / Street View** | earth.google.com | Confirmar un lugar por referencias visuales. |
| **ExifTool** | (arriba) | Si la foto conserva GPS, es directo. |

## 7. Redes sociales
| Herramienta | Repo | Estado | Para qué |
|---|---|---|---|
| **snscrape** ⭐ | https://github.com/JustAnotherArchivist/snscrape | activo | Scraping sin API de X/Twitter, Telegram, Reddit, etc. |
| **Instaloader** | https://github.com/instaloader/instaloader | activo | Descarga posts/metadatos públicos de Instagram. |
| **Toutatis** | https://github.com/megadose/toutatis | activo | Datos de una cuenta de Instagram (correo/tel ofuscados, IDs). |
| **Osintgram** | https://github.com/Datalux/Osintgram | ⚠️ inestable (login IG) | Análisis de seguidores/seguidos de Instagram. |
| **Twint** | https://github.com/twintproject/twint | ⚠️ discontinuado | (histórico) scraping de Twitter; usar snscrape. |

## 8. Brechas y credenciales expuestas
| Recurso | URL | Para qué |
|---|---|---|
| **Have I Been Pwned** ⭐ | https://haveibeenpwned.com | ¿aparece un correo/contraseña en filtraciones? API k-anonymity. |
| **Intelligence X** | https://intelx.io | Buscador de filtraciones, pastes, dark web (freemium). |
| **DeHashed** | https://dehashed.com | Búsqueda en volcados (comercial). |
| **h8mail** | (arriba) | Automatiza consultas a varias de estas fuentes. |
| **breach-parse** | https://github.com/hmaverickadams/breach-parse | Buscar en volcados descargados localmente (lab). |

## 9. Google Dorking / buscadores
| Recurso | URL / Repo | Para qué |
|---|---|---|
| **Google Hacking DB (GHDB)** ⭐ | https://www.exploit-db.com/google-hacking-database | Catálogo de dorks por categoría. |
| **Pagodo** | https://github.com/opsdisk/pagodo | Automatiza dorks del GHDB. |
| Operadores | `site:` `filetype:` `intitle:` `inurl:` `intext:` `cache:` | Combinar en Google/Bing/**Yandex**/DuckDuckGo. |

## 10. Empresas / registros públicos
| Recurso | URL | Para qué |
|---|---|---|
| **OpenCorporates** | https://opencorporates.com | Sociedades y administradores a nivel mundial. |
| **BORME** | https://www.boe.es/diario_borme | Registro Mercantil español. |
| **Aleph (OCCRP)** | https://aleph.occrp.org | Buscador periodístico de filtraciones y registros. |

## 11. Dark web (con Tor, solo metodológico)
| Herramienta | Repo / URL | Para qué |
|---|---|---|
| **Ahmia** ⭐ | https://ahmia.fi | Buscador de servicios .onion (clearnet). |
| **TorBot** | https://github.com/DedSecInside/TorBot | Crawler de sitios .onion. |
| **OnionScan** | https://github.com/s-rah/onionscan | Analiza fugas de OpSec en servicios ocultos. |
| Tor Browser | https://www.torproject.org | Acceso; en aula, con las precauciones del centro. |

---

## Cómo se usa esto en el curso
- **HE UT5** (reconocimiento) y la **práctica de auto-OSINT** son el primer contacto: se
  empieza por los bloques 0, 1, 2 y 5 sobre **uno mismo**.
- **IC UT4** reutiliza los bloques 4 y 8 en clave **defensiva** (vigilancia de marca,
  credenciales corporativas expuestas, typosquatting).
- Mantener al día: los repos con `pipx upgrade-all` y `go install ...@latest`. Revisar ⚠️
  antes de cada curso: el ecosistema OSINT de redes sociales cambia rápido.
