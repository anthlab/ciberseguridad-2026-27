# Laboratorio UT3 · Parte B — Diagrama de flujo de datos del portal SOC (referencia)

> Base para el modelado STRIDE (evidencia **PPS-E5**). Este DFD es el punto de partida: el
> alumnado lo redibuja (draw.io/excalidraw/papel) y sobre él enumera las amenazas.
> Referencia: OWASP Threat Modeling; unidad `PPS/unidades/UT3-asvs-superficie-riesgo.md`.

## Convención de un DFD para modelado de amenazas

- **Entidad externa** (rectángulo): actor fuera de nuestro control (usuario, atacante).
- **Proceso** (círculo): código que transforma datos (la app, el servicio de auth).
- **Almacén de datos** (dos líneas paralelas): base de datos, ficheros, caché.
- **Flujo de datos** (flecha): por dónde viaja un dato entre elementos.
- **Frontera de confianza** (línea discontinua): dónde cambia el nivel de confianza. **El
  riesgo vive en las fronteras**: un dato que las cruza debe validarse/autenticarse.

## DFD del portal SOC de xest

```mermaid
flowchart LR
    subgraph EXT["Zona no confiable (Internet / VPN)"]
        A["Analista SOC<br/>(navegador)"]
    end

    subgraph DMZ["Frontera 1 · perímetro web"]
        P["Portal SOC<br/>(app web / nginx+backend)"]
    end

    subgraph INT["Zona confiable (backend)"]
        AUTH["Servicio de<br/>autenticación"]
        DB[("Base de datos<br/>usuarios · sesiones · incidentes")]
    end

    A -- "1. HTTPS: usuario/contraseña" --> P
    P -- "2. verifica credenciales" --> AUTH
    AUTH -- "3. ok/ko + rol" --> P
    P -- "4. consulta datos (parametrizada)" --> DB
    DB -- "5. incidentes/alertas" --> P
    P -- "6. HTML + cookie de sesión" --> A

    %% Fronteras de confianza:
    %% F1 Internet<->Portal (flujos 1 y 6)
    %% F2 Portal<->Auth   (flujos 2 y 3)
    %% F3 Portal<->BD     (flujos 4 y 5)
```

## Inventario de elementos (lo que STRIDE debe recorrer, sin dejarse ninguno)

| # | Elemento | Tipo | Frontera que toca |
|---|---|---|---|
| E1 | Analista SOC (navegador) | Entidad externa | F1 |
| P1 | Portal SOC (app web) | Proceso | F1, F2, F3 |
| P2 | Servicio de autenticación | Proceso | F2 |
| D1 | Base de datos (usuarios, sesiones, incidentes) | Almacén | F3 |
| **F1** | Internet/VPN ↔ Portal | Frontera de confianza | — |
| **F2** | Portal ↔ Auth | Frontera de confianza | — |
| **F3** | Portal ↔ Base de datos | Frontera de confianza | — |

> Regla del ejercicio: **cada proceso, almacén, flujo y frontera** debe aparecer en la tabla
> STRIDE. Un elemento sin fila es un elemento sin analizar. Y cada amenaza debe llevar su
> **control mitigador**: una amenaza sin control está *nombrada*, no *modelada*.
