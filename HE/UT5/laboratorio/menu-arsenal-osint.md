# Menú de arsenal OSINT por capa — HE UT5 (material de aula)

Mapa de **qué herramienta usar en cada capa** de la práctica de reconocimiento. En clase se
ejecuta en vivo la marcada ⭐; las demás son **alternativas** (si la ⭐ falla, si quieres
ampliar, o para grupos avanzados). Catálogo completo con repos e instalación:
[`arsenal-osint.md`](../../recursos/arsenal-osint.md).

> Regla de aula: solo sobre **uno mismo** (consentimiento) o el **objetivo sintético**
> (`kestrel_ova` / `ova.kestrel@mail.xest.local`). Nunca sobre terceros. `holehe`/`ignorant`
> **solo sobre tu propio** correo/teléfono.

## Capa 0 — Framework todo-en-uno (consolidador)
| Herramienta | Comando de ejemplo | Nota |
|---|---|---|
| **SpiderFoot** ⭐ | `sf.py -l 127.0.0.1:5001` → web → New Scan sobre el alias/correo | Automatiza y **correlaciona** las capas de abajo. Se enseña *después* de hacerlas a mano. |
| Recon-ng | `recon-ng` → `marketplace install all` → workspaces/módulos | Framework tipo Metasploit para OSINT. |

## Capa 1 — Buscadores y dorking
| Herramienta | Comando de ejemplo |
|---|---|
| Operadores ⭐ | `"Óscar Valcárcel Aínsa" filetype:pdf` · `"kestrel_ova" site:foro.xest.local` (Google/**Yandex**/DuckDuckGo) |
| GHDB | catálogo en exploit-db.com/google-hacking-database |
| Pagodo | `python3 pagodo.py -d xest.local -g dorks.txt` (automatiza dorks) |

## Capa 2 — Histórico (contenido borrado)
| Herramienta | Comando de ejemplo |
|---|---|
| Wayback CDX ⭐ | `curl -s "http://web.archive.org/cdx/search/cdx?url=xest.local*&output=text&fl=original&collapse=urlkey"` |
| waybackurls 🐹 | `echo xest.local \| waybackurls` |
| gau 🐹 | `gau xest.local` |

## Capa 3 — Identidad reutilizada (alias)
| Herramienta | Comando de ejemplo |
|---|---|
| **Maigret** ⭐ | `maigret kestrel_ova --timeout 15` (3000+ sitios, extrae datos) |
| Sherlock | `sherlock kestrel_ova` (rápido, 400+ sitios) |
| WhatsMyName | web whatsmyname.app |

## Capa 4 — Correo
| Herramienta | Comando de ejemplo | Nota |
|---|---|---|
| **holehe** ⭐ | `holehe ova.kestrel@mail.xest.local` | Solo TU correo. |
| h8mail | `h8mail -t ova.kestrel@mail.xest.local` | Filtraciones (local o APIs). |
| GHunt | `ghunt email ova.kestrel@gmail.example` | Solo cuentas **Google**. |

## Capa 5 — Teléfono (ampliación)
| Herramienta | Comando de ejemplo | Nota |
|---|---|---|
| **PhoneInfoga** ⭐ | `phoneinfoga scan -n "+34600000000"` | Operador, tipo de línea, footprint. |
| Ignorant | `ignorant 34 600000000` | Registro en servicios. Solo TU número. |

## Capa 6 — Filtraciones / credenciales
| Herramienta | Comando de ejemplo |
|---|---|
| HIBP (k-anonymity) ⭐ | `printf '%s' 'clave' \| sha1sum` → `curl -s https://api.pwnedpasswords.com/range/<5 primeros>` |
| IntelX | intelx.io (buscador de filtraciones/pastes) |
| h8mail | (ver capa 4) |

## Capa 7 — Metadatos y documentos
| Herramienta | Comando de ejemplo |
|---|---|
| **ExifTool** ⭐ | `exiftool avatar.jpg \| grep -iE 'gps\|date\|model'` |
| Metagoofil | `metagoofil -d xest.local -t pdf,docx -o docs/` |

## Capa 8 — Dominio propio / infraestructura del sujeto
| Herramienta | Comando de ejemplo |
|---|---|
| crt.sh ⭐ | `curl -s "https://crt.sh/?q=%25.xest.local&output=json" \| jq -r '.[].name_value' \| sort -u` |
| Amass | `amass enum -passive -d xest.local` |
| Photon | `python3 photon.py -u http://foro.xest.local` (extrae correos/claves/enlaces) |

## Capa 9 — Repos y secretos
| Herramienta | Comando de ejemplo |
|---|---|
| git log ⭐ | `git log --format='%ae' \| sort -u` (correo real en las cabeceras) |
| **trufflehog** ⭐ | `trufflehog git file://. --only-verified` (secretos en TODO el histórico) |

## Capa 10 — Redes sociales (ampliación)
| Herramienta | Comando de ejemplo | Nota |
|---|---|---|
| snscrape ⭐ | `snscrape --max-results 50 twitter-user <alias>` | Sin API (X, Telegram, Reddit). |
| Instaloader | `instaloader --no-pictures --no-videos profile <perfil>` | Metadatos públicos de Instagram. |
| Toutatis | `toutatis -u <perfil> -s <sessionid>` | Datos de cuenta IG (correo/tel ofuscados). |

## Capa 11 — Imágenes / geolocalización (GEOINT, ampliación)
| Recurso | Uso |
|---|---|
| Búsqueda inversa ⭐ | **Yandex** Images (el mejor para rostros/lugares), Google, Bing, TinEye |
| ExifTool | si la foto conserva GPS, directo (ver capa 7) |
| SunCalc / Street View | confirmar hora/lugar por sombras y referencias |

---

## Cómo se usa en la práctica
1. En clase se ejecuta la ⭐ de las capas 1-4 y 6-9 sobre el objetivo (auto o sintético).
2. Las capas 5, 10 y 11 son **ampliación**: hazlas si tu objetivo tiene teléfono/redes/fotos.
3. Al final, **SpiderFoot** (capa 0) para ver cómo un framework automatiza y correlaciona todo
   lo que hiciste a mano —pero solo tiene sentido *después* de entender cada capa.
