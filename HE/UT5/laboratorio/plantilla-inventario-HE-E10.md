# NN-HE-E10 · Inventario por enumeración activa — `objetivo.xest.local`

> Plantilla del entregable HE-E10. Sustituye `NN` por tu número de lista. Cada celda de
> evidencia debe apuntar a un fichero de salida real (`nmap_objetivo.*`, `httpx.txt`,
> `ffuf.csv`, `nuclei.txt`, `verificacion_manual.txt`). Un hallazgo sin evidencia no cuenta.

- **Autor (nº lista)**:
- **Fecha / ventana horaria**:
- **Objetivo autorizado**: `objetivo.xest.local` (VLAN de laboratorio xest)
- **Alcance**: solo hosts `*.xest.local` autorizados. Ninguna acción fuera de la VLAN.

## 1. Activos y servicios

| Host | IP | Puerto | Servicio | Versión | Evidencia |
|---|---|---|---|---|---|
| objetivo.xest.local |  | 80/tcp | http (nginx) |  | `nmap_objetivo.nmap` |
|  |  |  |  |  |  |

## 2. Cuentas y endpoints de autenticación

| Endpoint | Método | Descubierto por | Evidencia |
|---|---|---|---|
| /login | POST | crawling / lectura del HTML | `httpx.txt`, ffuf |
|  |  |  |  |

## 3. Vulnerabilidades potenciales

> "Potenciales": aquí se **descubren y verifican**, no se explotan. La explotación es UT6/UT8.

| ID | Hallazgo | Severidad | Detectado por | **Verificado a mano** | Cómo se verificó |
|---|---|---|---|---|---|
| V1 | Versión de servidor expuesta (`Server: nginx/…`) | Baja | nuclei/httpx | sí/no | `curl -sI` |
| V2 | Listado de directorios en `/static/` | Media | nuclei/ffuf | sí/no | `curl /static/` |
| V3 | Falta cabecera HSTS | Media | nuclei | sí/no | `curl -sI` |
| V4 | Falta cabecera CSP | Media | nuclei | sí/no | `curl -sI` |
| V5 | Falta `X-Content-Type-Options` | Baja | nuclei | sí/no | `curl -sI` |
| V6 | Método TRACE habilitado | Media | nmap/nuclei | sí/no | `curl -X TRACE` |
|  |  |  |  |  |  |

## 4. Ruido medido en el SOC (con IC)

| Herramienta | Nº de alertas / eventos | Tipo de firma |
|---|---|---|
| nmap -sV -sC |  | barrido de puertos |
| ffuf |  | ráfaga de 404 |
| nuclei |  | patrones de plantilla |
| Fase 0 pasiva | 0 (esperado) | — (no toca el objetivo) |

**Regla de detección que faltaría** (propuesta):

## 5. Conclusión y enganche

- Priorización real de los hallazgos (no todos pesan igual):
- Qué de este inventario entra en **UT6** (explotación) y **UT8** (auditoría web):
- Comprobación futura: tras el bastionado de PPS, estos hallazgos deberían desaparecer.
