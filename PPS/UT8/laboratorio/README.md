# PPS · UT8 — Laboratorio: despliegue canario, resiliencia y DR

Material de manos para las dos sesiones de UT8. Todo corre en la **VLAN de aula aislada**;
nada se expone a Internet. Solo biblioteca estándar de Python + Docker + sqlite3.

## Piezas

| Fichero | Para qué |
|---|---|
| `portal/app.py` | Portal SOC mínimo con `/health` que comprueba **de verdad** su dependencia (la BD). |
| `datos/seed_alertas.py` | Genera un dataset **sintético** de alertas del SOC (sin datos reales). |
| `docker-compose.canario.yml` | Dos versiones del portal (`estable` v1.0.0 / `canario` v2.0.0) + proxy de reparto. |
| `nginx-canario.conf` | Reparto por peso 90/10 y reintento al estable si el canario da 5xx. |
| `deploy-canario.sh` | Despliegue canario con sonda y **reversión automática** → evidencia **PPS-E14**. |
| `sonda.sh` | Sonda de disponibilidad reutilizable (URL, muestras, intervalo). |
| `caos.sh` | Inyección de fallo (SIGKILL) y **MTTR medido** por la política de reinicio. |
| `dr/backup.sh` | Copia **verificada** (integrity_check) de la BD. |
| `dr/restore.sh` | Restaura la última copia buena. |
| `dr/medir-rto-rpo.sh` | Ensayo DR completo con **RTO y RPO medidos** → evidencia **PPS-E15**. |
| `dr/procedimiento-dr-plantilla.md` | Plantilla del procedimiento que rellena el alumnado. |

## Puesta en marcha (una vez, antes de clase)

```bash
cd PPS/UT8/laboratorio
python3 datos/seed_alertas.py datos/soc.db 500        # crea el dataset sintético
docker compose -f docker-compose.canario.yml up -d estable
curl -s http://localhost:8091/health                  # debe dar {"status":"ok",...}
```

## Sesión 1 — canario y caos

```bash
CANARY_FAIL=http5xx ./deploy-canario.sh   # canario roto -> REVERSIÓN AUTOMÁTICA (PPS-E14)
./deploy-canario.sh                        # canario sano -> promoción
./caos.sh                                  # mata el portal y mide el MTTR real
```

## Sesión 2 — recuperación ante desastres

```bash
./dr/backup.sh                             # copia verificada
./dr/medir-rto-rpo.sh                       # desastre + restauración + RTO/RPO medidos (PPS-E15)
```

## Puertos

- `8091` → portal **estable** (acceso directo).
- `8092` → portal **canario** (acceso directo, solo durante el despliegue).
- `8080` → **proxy** de reparto (solo con `--profile proxy`).

## Nota de seguridad de aula

Los objetivos son deliberadamente frágiles y las IP de los datos son de rangos de
documentación (RFC 5737) o privados (RFC 1918). **No enrutar fuera de la VLAN aislada.**
