# Curso 2026-2027 — Ciberseguridad (Cheste)

Repositorio de trabajo del alumnado para **Puesta en Producción Segura**, **Hacking Ético** y **Gestión de Incidentes**. La documentación anterior de CursoPPS debe considerarse histórica hasta completar las pruebas del laboratorio.

## Importante antes de ejecutar

1. Clona `https://github.com/jmpicon/PPS-jmpicon.git` (cuando la PR 1 esté fusionada): `git clone https://github.com/jmpicon/PPS-jmpicon.git`.
2. Copia `cp .env.example .env`. Introduce un `ACCESS_CODE` único y un `SECRET_KEY` aleatorio de al menos 32 caracteres. No compartas ni subas `.env`.
3. Comprueba `docker compose config` y arranca **solo en un equipo o red de laboratorio autorizada** mediante `docker compose up -d --build`.
4. Abre `http://127.0.0.1:8088`; la interfaz solo escucha en localhost por defecto. No publiques el puerto ni expongas la aplicación a Internet.
5. **La terminal web Kali está deshabilitada por defecto** (`/terminal/` devuelve 403) porque la implementación histórica no demuestra un control de acceso independiente. No la habilites sin aislar el laboratorio y revisar autenticación, WebSocket y permisos.

## Curso y material

- Puesta en Producción Segura: [carpeta de Drive](https://drive.google.com/drive/folders/11_Tz-rT3bCcY5ELkTzPSpHINXTi6pDtD).
- Clase del 27/10: [práctica de código seguro](https://drive.google.com/file/d/1bw1sd5WXydWSM7hGc36O2kpfu6VTYTbL/view).
- [Guía del módulo](https://docs.google.com/document/d/1Fw5AyGyt3BvqKbCub_gRftDxvTGoakZaP-INeGj53Ek/edit).
- [Catálogo de cuestionarios y Kahoot](./KAHOOT-Y-TEST.md).
- [Cursos online gratuitos y formación complementaria](./CURSOS-ONLINE.md).

**Aviso:** los enlaces a Drive solo funcionarán para alumnos con permisos concedidos; no se publican soluciones ni claves. No redistribuir el material del profesor desde el repositorio del alumnado.

## Antes de entregar el repositorio a alumnos

Pendiente validar la seguridad y funcionamiento real de Docker, las rutas de API y WebSocket, el manejo de secretos, las dependencias y las prácticas. La PR 1 debe seguir en borrador hasta comprobarlo. No se ha realizado una prueba de despliegue en los equipos de clase.
