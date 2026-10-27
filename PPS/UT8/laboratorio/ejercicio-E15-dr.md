# PPS-E15 · Recuperación ante desastres ensayada (alumnado)

**RA5 f · rúbrica R2 (informe)**. Entrega: `NN-PPS-E15-dr.md` (con el procedimiento y los
valores **medidos**) + el volcado de la ejecución.

## Contexto
Regla del módulo: **una copia que no se restaura no es una copia**, y **sin recuperación
ensayada no hay plan**. Los RTO/RPO se **miden en el ensayo**, no se estiman.

## Antes de empezar
```bash
cd PPS/UT8/laboratorio
python3 datos/seed_alertas.py datos/soc.db 500     # si no lo hiciste ya
docker compose -f docker-compose.canario.yml up -d estable
```

## Tareas
1. **Copia verificada.** Ejecuta `./dr/backup.sh` y explica por qué no basta con que el
   fichero exista: ¿qué comprobación adicional hace el script y por qué importa?
2. **Ensayo completo.** Ejecuta el ensayo y captura toda la salida:
   ```bash
   ./dr/medir-rto-rpo.sh | tee mi-ensayo-dr.txt
   ```
   Anota **RTO medido**, **RPO medido** y **datos perdidos**.
3. **Procedimiento reproducible.** Rellena `dr/procedimiento-dr-plantilla.md` con tus valores
   (objetivos vs medidos) y súbelo como parte de la entrega.
4. **Análisis.** ¿Se cumplieron los objetivos? Propón **una** mejora para reducir el RPO y
   **una** para reducir el RTO, y di qué tendrías que cambiar en el laboratorio para lograrlas.

## Criterio de superación
- La restauración se ensaya **de verdad**: el servicio vuelve a `/health = 200` tras el desastre.
- RTO y RPO son **medidos** (salen del cronómetro y del recuento), con su desviación respecto al objetivo.
- El procedimiento es reproducible por otra persona **solo con el documento**.
