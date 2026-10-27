# HE UT5 · Práctica 02 — Enumeración activa del portal institucional

**Módulo** 5025 Hacking Ético · **UT5** (8 h) · **RA3 CE b** — *"Se ha obtenido un inventario
de activos, cuentas y vulnerabilidades potenciales mediante técnicas activas de enumeración"*.
**Evidencia** HE-E10 (inventario de laboratorio, instrumento I1, 20 %) · Rúbrica **R1**.
**Prerrequisito bloqueante**: UT1 superada + **ROE del curso firmado** (HE-E1). Sin ROE no se
ejecuta ni una acción activa.

> HE-E9 (reconocimiento **pasivo** sobre una persona) es la Práctica 01 y **no** se mezcla con
> esta. Aquí el objetivo es un **servicio del laboratorio** con alcance autorizado, no una
> persona. Toda la práctica ocurre en la **VLAN aislada** de xest.

## Objetivo del ejercicio

Construir el **inventario** de `objetivo.xest.local` (el portal SOC de xest) por técnicas
activas: activos y servicios con su versión, superficie HTTP (rutas y endpoints), y
vulnerabilidades **potenciales** — potenciales porque aquí se **descubren y verifican**, no se
explotan (la explotación es UT6/UT8). Y medir el **ruido** que genera cada herramienta en el SOC.

## Alcance y reglas (leer antes de tocar nada)

- Objetivos autorizados: **solo** `objetivo.xest.local` y los hosts `*.xest.local` de la VLAN
  del aula (`comun/entornos/objetivos/hosts-aula`).
- Cualquier acción sobre una IP/host fuera de ese alcance → **0** en la práctica y protocolo de
  convivencia del centro (rúbrica R1, salida cero). Un `nmap` a Internet "para probar" ya cuenta.
- Snapshot limpio de la Kali antes de empezar; restaurar el entorno al terminar.
- Regla del módulo: un hallazgo **sin comando, salida y marca de tiempo** no es evidencia.

## Preparación (5 min)

```bash
# 1. Comprobar que el objetivo resuelve y responde (sin esto, no empieces)
getent hosts objetivo.xest.local
# 2. Stack ProjectDiscovery al día
pdtm -ua && nuclei -update-templates
# 3. Crear carpeta de trabajo por número de lista
mkdir -p NN-HE-E10 && cd NN-HE-E10
```

## Fase 0 — Pasivo institucional (sin tocar el objetivo) · 20 min

Aunque el objetivo sea una máquina, se empieza por lo gratis e invisible.

```bash
# Subdominios desde Certificate Transparency (consultas a crt.sh, NO al objetivo)
curl -s "https://crt.sh/?q=%25.xest.local&output=json" | jq -r '.[].name_value' | sort -u
# Subdominios pasivos + correos/hosts
subfinder -d xest.local -silent | tee subs_pasivos.txt
theHarvester -d xest.local -b crtsh,duckduckgo
```

**Entregable parcial**: `subs_pasivos.txt` con la lista de hosts candidatos y su fuente.
Marca cuáles vas a enumerar activamente (solo los `*.xest.local` autorizados).

## Fase 1 — Enumeración activa · 90 min

A partir de aquí **el SOC te ve**. Ejecuta en orden y **guarda todas las salidas**.

```bash
# Resolución + hosts vivos
subfinder -d xest.local -silent | dnsx -silent -a -resp | tee hosts.txt

# Barrido de puertos y versiones del objetivo autorizado
nmap -sV -sC -oA nmap_objetivo objetivo.xest.local

# Sondeo HTTP: título, tecnología, servidor, código
httpx -l hosts.txt -title -tech-detect -status-code -server -o httpx.txt

# Fuzzing de contenido (rutas no enlazadas)
ffuf -u http://objetivo.xest.local/FUZZ \
     -w /usr/share/seclists/Discovery/Web-Content/common.txt \
     -mc 200,301,302,401,403 -of csv -o ffuf.csv

# Escaneo por plantillas
nuclei -u http://objetivo.xest.local -severity critical,high,medium -o nuclei.txt
```

> El pipeline completo está automatizado en `recon-pipeline.sh` (mismo orden, misma evidencia).
> Puedes usarlo, pero **debes entender cada paso**: en la defensa te preguntaré por uno al azar.

## Fase 2 — Verificación manual · 30 min

Ningún hallazgo automático entra en el inventario sin verificarlo a mano.

```bash
# ¿nuclei dice que falta HSTS y que se filtra la versión? Compruébalo:
curl -sI http://objetivo.xest.local/ | grep -iE 'server|strict-transport|content-security|x-content-type'
# ¿Listado de directorios en /static?
curl -s http://objetivo.xest.local/static/ | head
# ¿Método TRACE habilitado?
curl -s -X TRACE http://objetivo.xest.local/ -i | head
```

Para cada vulnerabilidad potencial anota: **cómo la verificaste** y si quedó **confirmada**.

## Fase 3 — Medir el ruido (con IC) · 25 min

Con el equipo de Incidentes (SOC de xest), abre el panel de alertas y responde:

- ¿Cuántas alertas generó `nmap`? ¿Y `ffuf`? ¿Y `nuclei`?
- ¿Qué **no** apareció en el SOC? (pista: toda la Fase 0 pasiva).
- ¿Qué **regla de detección faltaría** para cazar antes el fuzzing?

## Fase 4 — Inventario y cierre · 30 min

Rellena la plantilla `plantilla-inventario-HE-E10.md` con tres tablas: **activos**,
**cuentas/endpoints** y **vulnerabilidades potenciales** (con la columna *verificado a mano*).

## Entregables

Todo por número de lista, en la carpeta `NN-HE-E10/`:

1. `NN-HE-E10-inventario.md` — las tres tablas, cada hallazgo con su evidencia.
2. `nmap_objetivo.nmap` / `.gnmap` / `.xml`, `httpx.txt`, `ffuf.csv`, `nuclei.txt`, `subs_pasivos.txt`.
3. Tabla de **ruido medido** en el SOC (nº de alertas por herramienta) — Fase 3.

**Corte automático (R1, salida cero)**: cualquier acción activa contra un objetivo no
autorizado califica la práctica con 0 y activa el protocolo de convivencia.

## Criterios de superación (resumen de R1)

- **Ejecución**: el inventario está completo y es coherente con el objetivo.
- **Reproducibilidad**: comandos + salidas permiten repetir el ejercicio desde cero.
- **Verificación**: cada hallazgo automático contrastado a mano.
- **Higiene**: alcance respetado, entorno restaurado.
- Rúbrica completa: `~/xest-lab/2026-2027/docs/planificacion/rubricas.md` (R1).

## Enganche

Este inventario **no se tira**: es la entrada de **UT6** (explotación: los servicios y rutas
descubiertos son los puntos de entrada) y de **UT8** (auditoría web sobre el portal ya
bastionado por PPS). El ruido medido conecta con **IC** (qué firma deja un atacante enumerando).
