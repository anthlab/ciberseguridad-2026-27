# Objetivos vulnerables avanzados — para practicar el ataque a fondo

Complementan a los objetivos básicos (`docker-compose.yml`: Juice Shop, DVWA, bWAPP,
portal-soc). Estos pesan más y se levantan **bajo demanda**, solo la sesión que se usan, en
la VLAN aislada. Arsenal ofensivo asociado: `../../../HE/recursos/arsenal-ataque.md`.

## Se levantan con Docker (aquí)

```bash
docker compose -f docker-compose-avanzado.yml up -d      # WebGoat + VAmPI
docker compose -f docker-compose-avanzado.yml down       # al terminar (liberan RAM)
```

| Objetivo | URL de aula | Para qué | UT |
|---|---|---|---|
| **WebGoat** | `http://webgoat.xest.local:8085/WebGoat` | Lecciones guiadas de OWASP Top 10, paso a paso. Ideal para aprender la técnica antes de aplicarla en Juice Shop. | HE UT8 |
| **WebWolf** | `http://webgoat.xest.local:9095/WebWolf` | Compañero de WebGoat (recibe callbacks, correos, hosting de payloads). | HE UT8 |
| **VAmPI** | `http://vampi.xest.local:8086` | API REST vulnerable (OWASP API Security Top 10): BOLA/IDOR de API, JWT, mass assignment. Lo que una SPA como Juice Shop toca por encima. | HE UT8 |

Añade estos nombres a `hosts-aula` (o al DNS del lab) apuntando a la IP del host del laboratorio.

## Van por su cuenta (multi-contenedor o VM)

| Objetivo | Cómo se despliega | Para qué |
|---|---|---|
| **crAPI** (OWASP) | Su propio `docker-compose` (varios servicios): `git clone https://github.com/OWASP/crAPI && cd crAPI/deploy/docker && docker compose up -d` | API realista completa (coches): BOLA, JWT, SSRF, mass assignment. El mejor lab de API. |
| **Metasploitable 2** | Imagen de VM (VirtualBox) o `docker pull tleemcjr/metasploitable2` (no oficial) | Máquina entera vulnerable: red + servicios + explotación con Metasploit (repaso de HE UT6). |
| **Metasploitable 3** | Vagrant (`vagrant up`) | Windows/Linux vulnerables modernos para AD y post-explotación (HE UT7). |
| **VulnHub** | Descargar `.ova` de https://www.vulnhub.com e importar | Máquinas tipo CTF, boot-to-root. |
| **HackTheBox / TryHackMe** | Plataformas online (cuenta propia) | Retos autorizados; útiles como tarea/ampliación. |
| **PortSwigger Web Security Academy** | https://portswigger.net/web-security (online, gratis) | Labs web temáticos con teoría; excelentes para reforzar WSTG. |

## Requisitos y avisos

- **RAM**: WebGoat + VAmPI son ligeros; crAPI y Metasploitable3 piden bastante. No levantar
  todo a la vez si el aula va justa: solo el target de la sesión.
- **Aislamiento**: todo en la VLAN de laboratorio. Metasploitable es **muy** vulnerable a
  propósito; jamás en una red con salida.
- **Verificación previa**: la primera vez, `docker pull <imagen>` y una prueba de humo
  (`curl` a la URL) antes de la clase. Fijar el digest observado para reproducibilidad.
