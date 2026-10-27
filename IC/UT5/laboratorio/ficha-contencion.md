# Ficha del alumnado — Contención inicial sin destruir evidencia (IC-E9, parte 2)

**Objetivo**: aplicar las primeras medidas que **limitan el daño** del incidente **preservando
la evidencia** para el forense de la UT6. Rúbrica R3. Todo en la **VLAN aislada**.

**Regla de oro**: **aislar ≠ apagar/reinstalar**. Apagar o reinstalar un equipo comprometido
borra la memoria RAM y artefactos volátiles que necesita el análisis. Contienes, no destruyes.

---

## Orden de la contención (de más a menos urgente)

1. **Cortar la exfiltración y el C2** (para de sangrar).
2. **Aislar los endpoints comprometidos** por red, sin apagarlos.
3. **Revocar la cuenta comprometida** y matar sus sesiones.
4. **Preservar** (snapshot) antes de cualquier limpieza. La limpieza es UT7.

## Paso 1 — Bloquear el indicador C2 (en el router/cortafuegos del lab)

Bloquea la IP `185.220.101.47` y el dominio `update-cdn-xest.link` para toda la VLAN. En una
plataforma con Wazuh, puedes usar la **respuesta activa** `firewall-drop` disparada por la
regla del C2. Documenta la hora exacta del bloqueo.

## Paso 2 — Aislar el endpoint (Wazuh active response), NO apagarlo

Aísla `portal-soc` (10.10.10.10) y `ws-admin` (10.10.10.31): que solo puedan hablar con el
agente Wazuh/SOC (10.10.10.20), nada más. **No** los apagues. Ver el snippet de respuesta
activa que te da el profesor (`active-response-aislar.md`).

## Paso 3 — Revocar la cuenta comprometida

`jadmin` está comprometida y el atacante creó `svc-update` (admin). Deshabilita ambas y **mata
sus sesiones activas** (no basta con cambiar la contraseña si la sesión sigue viva).

## Paso 4 — Preservar antes de tocar

Haz un **snapshot** de las VMs `portal-soc` y `ws-admin` **antes** de cualquier otra acción, y
anota su hash/etiqueta. Ese snapshot es la materia prima del forense (IC-E10). Registra cada
acción con hora en la tarea "Contención" del caso de TheHive.

## Lo que NO debes hacer (y por qué)

| Tentación | Por qué está mal |
|---|---|
| Apagar `ws-admin` | Pierdes la RAM: procesos, conexiones, claves en memoria. |
| Borrar la webshell "para limpiar" | Destruyes evidencia y avisas al atacante. Aíslas, no borras. |
| Reinstalar ya | Es **erradicación/recuperación** (UT7), después del forense (UT6). |
| Solo cambiar la contraseña de `jadmin` | La sesión activa sigue viva; hay que terminarla. |

**Entrega (parte 2)**: en `NN-IC-E9-caso.md`, la **contención documentada** (qué, a qué hora,
con qué comando) + prueba de que la **evidencia se preservó** (etiqueta/hash del snapshot) para
el handoff a UT6.
