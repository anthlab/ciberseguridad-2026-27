# PPS · UT8 — Despliegue automatizado, resiliencia y recuperación ante desastres

**5 horas** · RA5 (d, e, f) · Servicio SOC: Prevención — continuidad del despliegue · Evidencias `PPS-E14`, `PPS-E15`

---

## 1. Objetivo de la unidad

Cierra el módulo: llevar el software a producción de forma que un fallo no se convierta en una caída del servicio, y tener un procedimiento de recuperación **probado**, no supuesto. El criterio: sin reversión probada, no se libera; sin recuperación ensayada, no hay plan.

## 2. Contenido

### 2.1 Estrategias de despliegue (RA5.d)

| Estrategia | Cómo funciona | Cuándo |
|---|---|---|
| **Azul-verde** | Dos entornos idénticos; se conmuta el tráfico | Servicios sin estado |
| **Canario** | Se envía un % del tráfico a la versión nueva | Validar con tráfico real antes de generalizar |
| **Indicadores de funcionalidad** | Desacoplan despliegue de activación | Activar/desactivar sin re-desplegar |
| **Reversión** | Volver a la versión previa buena | Siempre: probada antes de liberar |

### 2.2 Resiliencia y autorreparación (RA5.e)

- Gestión automatizada de configuración y orquestación de contenedores.
- Sondas de vida y disponibilidad (liveness/readiness) que reinician lo que no responde.
- Escalado automático ante carga.
- **Ingeniería del caos**: inyectar fallos controlados para verificar que el sistema se recupera solo.

### 2.3 Recuperación ante desastres (RA5.f)

- **RTO** (Recovery Time Objective): cuánto puede tardar en volver el servicio.
- **RPO** (Recovery Point Objective): cuánto dato se puede permitir perder.
- Copias verificadas (una copia que no se restaura no es una copia).
- Procedimiento escrito **y ensayado**, con RTO/RPO medidos en el ensayo, no estimados.

## 3. Laboratorio guiado

### Parte A — Despliegue canario con reversión (RA5.d, RA5.e)

1. Despliega el portal del SOC en modo canario (p. ej. dos réplicas y enrutado por peso, o dos servicios y conmutación).
2. Configura una sonda de disponibilidad y una condición de reversión automática ante degradación (código 5xx por encima de un umbral).
3. Provoca la degradación en la versión canaria y demuestra la **reversión automática**.

```bash
# Ejemplo de sonda de disponibilidad en Docker Compose
# healthcheck:
#   test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
#   interval: 10s
#   retries: 3
docker compose ps          # ver estado de salud
docker compose logs -f app # observar reinicio/reversión
```

### Parte B — Inyección de fallo y medición (RA5.e)

4. Inyecta un fallo controlado (detén un contenedor, satura CPU) y **mide** el tiempo de recuperación real.

### Parte C — Recuperación ante desastres (RA5.f)

5. Redacta el procedimiento de recuperación ante desastres del servicio (qué se restaura, en qué orden, desde qué copia).
6. **Ensaya** una restauración completa desde copia y mide RTO y RPO reales. Documenta la desviación respecto a los objetivos.

## 4. Entregables

- **`PPS-E14`** (reto integrado, rúbrica R3): plan de despliegue con reversión probada y evidencia del ensayo (degradación → reversión automática).
- **`PPS-E15`** (informe, rúbrica R2): procedimiento de recuperación ante desastres con RTO y RPO **medidos** en el ensayo, no estimados.

## 5. Criterios de superación

- La reversión se demuestra funcionando ante una degradación real.
- La recuperación se ensaya de verdad y los RTO/RPO son medidos.
- El procedimiento es reproducible por otra persona con solo el documento.

## 6. Errores frecuentes

- Declarar RTO/RPO sin haber restaurado nunca: son deseos, no objetivos.
- Confiar en copias que nunca se han restaurado.
- Reversión "manual" no documentada: en un incidente real no está disponible.

## 7. Referencias

- Google SRE Book — capítulos de despliegue y gestión de la carga.
- NIST SP 800-34 — Contingency Planning Guide (RTO/RPO).
- OWASP DevSecOps Maturity Model — despliegue y operación.
