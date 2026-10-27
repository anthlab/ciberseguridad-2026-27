# Procedimiento de recuperación ante desastres — portal SOC de xest

> Plantilla que rellena el alumnado para **PPS-E15**. Debe ser reproducible por otra
> persona con solo este documento. Los RTO/RPO se rellenan con los valores **medidos
> en el ensayo**, no con estimaciones.

## 1. Alcance
- Servicio: portal SOC de xest (`portal-estable`, BD de alertas `datos/soc.db`).
- Desastre cubierto: pérdida de la base de datos de alertas.

## 2. Objetivos declarados (antes del ensayo)
- RTO objetivo: ______ (lo que la organización se propone).
- RPO objetivo: ______ .

## 3. Qué se restaura, en qué orden, desde qué copia
1. Copia de origen: última `backups/soc-*.db` con `integrity_check = ok`.
2. Orden de restauración:
   1. Restaurar el fichero de BD.
   2. Reiniciar el contenedor del portal.
   3. Verificar `/health = 200`.
3. Verificación de éxito: `curl -s http://localhost:8091/health` devuelve `status: ok`.

## 4. Ejecución del ensayo (comandos)
```bash
./dr/backup.sh                 # copia verificada de partida
./dr/medir-rto-rpo.sh           # desastre controlado + restauración + medición
```

## 5. Resultado MEDIDO en el ensayo
| Métrica | Objetivo | Medido | Desviación |
|---|---|---|---|
| RTO (s) | ______ | ______ | ______ |
| RPO (s) | ______ | ______ | ______ |
| Datos perdidos (alertas) | — | ______ | — |

## 6. Conclusión y mejoras
- ¿Se cumplió el RTO/RPO? ______
- Acción para reducir el RPO (p. ej. copias más frecuentes): ______
- Acción para reducir el RTO (p. ej. restauración automatizada): ______
