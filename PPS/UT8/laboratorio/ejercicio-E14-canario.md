# PPS-E14 · Despliegue canario con reversión automática (alumnado)

**RA5 d,e · rúbrica R3 (reto integrado)**. Entrega: `NN-PPS-E14-despliegue.md` + el log del despliegue.

## Contexto
Vais a liberar la versión 2.0.0 del portal SOC. Regla del módulo: **sin reversión probada, no
se libera**. Lo demostráis provocando una degradación y viendo que el sistema **revierte solo**.

## Antes de empezar
```bash
cd PPS/UT8/laboratorio
python3 datos/seed_alertas.py datos/soc.db 500
docker compose -f docker-compose.canario.yml up -d estable
curl -s http://localhost:8091/health          # {"status":"ok", ...}
```

## Tareas
1. **Sonda que de verdad mide.** Explica en tu entrega por qué `/health` de este portal **no**
   puede quedarse siempre en "healthy": ¿qué comprueba antes de responder 200? Demuéstralo
   parando la dependencia (pista: `FAIL_MODE=db`).
2. **Canario degradado → reversión automática.** Lanza el despliegue de un canario roto y
   captura el log donde se ve la reversión:
   ```bash
   CANARY_FAIL=http5xx ./deploy-canario.sh
   ```
   El log `deploy-*.log` es tu evidencia. Debe verse: sondas en FALLO, tasa de error por
   encima del umbral y la línea `REVERSIÓN AUTOMÁTICA`.
3. **Canario sano → promoción.** Repite con un canario bueno y muestra que ahora **se promueve**:
   ```bash
   ./deploy-canario.sh
   ```
4. **Redacta** en `NN-PPS-E14-despliegue.md`: estrategia usada (canario), umbral de reversión
   elegido y por qué, y qué pasaría en producción con el proxy de reparto por peso.

## Criterio de superación
- La reversión se demuestra **funcionando ante una degradación real** (no descrita: ejecutada).
- El log adjunto prueba la secuencia sonda → umbral superado → reversión.
- Distingues "el gate está instalado" de "el gate está activo": lo pruebas con un caso que **debe** fallar.
