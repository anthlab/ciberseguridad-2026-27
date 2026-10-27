# Playbook 05 — Denegación de servicio (DDoS)

| Categoría | Severidad | Criticidad | SLA respuesta |
|---|---|---|---|
| Availability — DoS / DDoS | Alta | P1 si servicio crítico afectado | 15 min |

## Precondiciones
- Contrato de mitigación DDoS con el proveedor upstream (Cloudflare, AWS Shield, Arbor, Akamai, o el propio ISP).
- Runbook técnico del proveedor documentado y contacto 24/7.
- Suricata capturando en interfaz externa para tipificar el ataque.
- Wazuh con logs de WAF, LB, servidor web y firewall perimetral.

## Fase 1 — Detección y análisis
Indicadores:
- Pico de tráfico entrante ≥ 3× baseline en < 5 min.
- Wazuh dispara reglas de LB/WAF: `rule.groups: [ddos]`, `429`, `503`, `connection_flood`.
- Suricata: `ET DoS`, patrones SYN flood, HTTP flood, DNS amplification, NTP monlist.
- Alertas de monitorización (Prometheus / Grafana) sobre CPU LB, sesiones, latencia p95/p99.

Tipificar rápidamente:
| Vector | Firma típica | Mitigación |
|---|---|---|
| **SYN flood** | Muchos SYN sin ACK | SYN cookies + rate limit L4 |
| **UDP amplification** | UDP puerto 53/123/389/1900 con volumen | Bloqueo por origen, contactar upstream |
| **HTTP flood** | Muchas peticiones legítimas por segundo | WAF rate limit + JS challenge |
| **Slowloris** | Conexiones HTTP muy lentas | `mod_reqtimeout` / cierre conexiones inactivas |
| **DNS QPS flood** | Muchas queries por segundo | Response rate limiting en el resolver |

## Fase 2 — Contención
1. Elevar mitigación al proveedor upstream — activar modo *Under Attack* (Cloudflare) / *AWS Shield Advanced auto-response* / *scrubbing center*.
2. Aplicar reglas WAF geo o rate limit temporales.
3. Escalar recursos si el servicio está en cloud (autoscaling) para absorber mientras la mitigación surte efecto.
4. Comunicación de estado a clientes / dirección (indicar tiempo estimado de restablecimiento).
5. Documentar la ventana del ataque (inicio, patrón, magnitud) para reporte + post-mortem.

## Fase 3 — Erradicación
DDoS no se "erradica" en el sentido tradicional. Es contención mantenida hasta que el atacante desiste. Enfoque:
1. Mantener mitigación hasta que el tráfico baje a niveles normales durante 30 min.
2. Documentar el rango del atacante (ASN) para blocklist ampliada.
3. Investigar si hay componente extorsiva (nota de rescate previa a DDoS = **ransom DDoS**) — si la hay, ver playbook 01 y no pagar por defecto.

## Fase 4 — Recuperación
1. Revertir mitigaciones extremas (geo-block, `Under Attack`) gradualmente para minimizar impacto usuarios legítimos.
2. Escalar hacia abajo los recursos añadidos.
3. Confirmar servicio operativo 100 % durante 60 min consecutivos antes de cerrar.
4. Comunicación a clientes de servicio restablecido + resumen del incidente si procede.

## Fase 5 — Actividad post-incidente
1. Informe con patrón del ataque, magnitud pico, coste (proveedor + horas + SLA breaches).
2. Refinar reglas WAF y ajustar autoscaling caps.
3. Revisar arquitectura de resiliencia: multi-región, anycast, cache edge.
4. Feedback a PPS sobre capacity planning y contratos.
5. Publicar IoCs (ASN, patrones) en MISP con TLP:AMBER.

## Notificaciones regulatorias
DDoS por sí solo no dispara RGPD (no hay violación de confidencialidad ni integridad). Sí puede disparar:

| Marco | Cuándo aplica |
|---|---|
| NIS2 | Si es entidad esencial o importante y el servicio afectado es crítico → 24 h / 72 h / 1 mes |
| DORA | Sector financiero → 4 h / 72 h / 1 mes |
| ENS RD 311/2022 | Sector público y afecta disponibilidad de sistema categorizado → CCN-CERT |
| Código Penal | Denuncia si se cuantifica daño (art. 264 bis) |

## Herramientas SOC involucradas
- **Suricata** — tipificación del ataque (SYN, UDP amp, HTTP, DNS).
- **Wazuh** — correlación con logs WAF/LB/web.
- **TheHive** — caso con timeline de la ventana.
- **Cortex** — analyzers de reputación IP + ASN (BGPview, AbuseIPDB, Shodan).
- **MISP** — publicación IoCs para federados.
- **Proveedor upstream** — el elemento más crítico, el SOC solo coordina y valida.

## Criterios de cierre
- Servicio operativo 100 % durante ≥ 60 min.
- Mitigaciones extremas revertidas.
- Informe entregado a dirección + partes interesadas.
- IoCs publicados.
- Contratos de mitigación validados (SLA cumplido por el proveedor).

## Métricas específicas
| Métrica | Objetivo |
|---|---|
| Tiempo hasta activación de mitigación upstream | ≤ 15 min |
| Tiempo hasta restablecimiento de servicio | ≤ 30 min (con proveedor DDoS) |
| Disponibilidad del mes (sla) | ≥ contratada |
| Duración total del ataque | Documentada |
| Pico bps / pps | Documentado |
