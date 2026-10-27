# Demo BloodHound CE — rutas de ataque en AD (RA4.c) — PROYECTADA, no por estación

El aula xest no monta un dominio Active Directory (el laboratorio de UT7 es Linux: `pivote-lab`).
El mapeo de rutas de ataque en AD se hace por tanto como **demostración proyectada** con el
**dataset de ejemplo** de BloodHound CE, no por estación. Es honesto con lo que hay y suficiente
para el criterio: el alumnado tiene que **entender la lectura de un grafo de rutas**, no montar
un DC.

## Montaje (una vez, en la máquina del profesor)
```bash
# BloodHound CE con docker compose (SpecterOps):
curl -L https://ghst.ly/getbhce -o docker-compose.yml
docker compose up -d
# credenciales iniciales en el log:
docker compose logs bloodhound | grep -i "Initial Password"
# UI: http://localhost:8080
```
Repos: https://github.com/SpecterOps/BloodHound · recolector https://github.com/BloodHoundAD/SharpHound

## Cargar datos de ejemplo (sin necesitar un DC)
- BloodHound CE trae un **conjunto de datos de ejemplo** cargable desde la propia UI
  (Administration → *Sample data* / *BHCE example data*). Si tu versión no lo incluye, usa el
  generador oficial **BadBlood** o **DBCreator** sobre un DC de laboratorio.
- Con los datos cargados, la demo consiste en ejecutar estas consultas prehechas:
  - *Shortest Paths to Domain Admins*
  - *Find Principals with DCSync Rights*
  - *Kerberoastable Users*

## Guion de la demo (5 min, proyectado)
1. Abre *Shortest Paths to Domain Admins*. Señala que el camino corto **no es un exploit**:
   es una arista de permiso (`AdminTo`, `MemberOf`, `GenericAll`, `HasSession`).
2. Recorre una arista: "este usuario puede resetear la contraseña de aquel, que es admin local
   de la máquina donde tiene sesión un Domain Admin → tres saltos, cero CVE".
3. Conecta con lo que sí hacen en el `pivote-lab`: "el `svc-backup` reutilizado es una arista
   `Valid Accounts` como estas; en un AD real BloodHound te la dibuja".

## Cierre
La lección transferible al reto HE-E14: el movimiento lateral se **planifica sobre relaciones
de identidad y permisos**, no sobre vulnerabilidades. Por eso el volcado de credenciales de la
sesión 1 y el grafo de la sesión 2 son la misma historia.
