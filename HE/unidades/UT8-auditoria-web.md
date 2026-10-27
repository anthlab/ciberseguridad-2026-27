# HE · UT8 — Auditoría de aplicaciones web

**8 horas** · RA5 (a, b, c, d, e, f) · Servicio SOC: Protección — validación de la aplicación en producción · Evidencias `HE-E15`, `HE-E16`

---

## 1. Objetivo de la unidad

Auditar una aplicación web completa siguiendo la metodología OWASP WSTG. El objetivo es el portal del SOC de xest, el mismo servicio que el módulo PPS ha construido y endurecido: aquí se comprueba empíricamente si ese endurecimiento resiste. **Requiere que PPS haya cerrado sus UT4 y UT5.**

## 2. Contenido

### 2.1 Autenticación web (RA5.a)

Formulario y sesión, tokens, **OAuth 2.0**, **OpenID Connect**, **SAML**. Debilidades y fortalezas de cada uno: dónde está el token, cómo se valida, qué pasa si expira mal.

### 2.2 Inventario del servicio (RA5.b)

Equipos, protocolos, servicios y sistemas operativos que sostienen la aplicación. Reutiliza el inventario de la UT5.

### 2.3 Análisis del flujo (RA5.c)

Interacción navegador–aplicación con **proxy de interceptación** (Burp/ZAP): entender el uso normal antes de atacar.

### 2.4 Examen manual (RA5.d)

Conforme a **OWASP WSTG**: lógica de negocio, autorización, gestión de sesión, validación de entrada. El examen manual encuentra lo que el escáner no ve (fallos de lógica y de autorización).

### 2.5 Automatización con verificación (RA5.e, RA5.f)

- Escáneres y plantillas (nuclei, ZAP activo), explotación asistida (sqlmap).
- **Verificación manual obligatoria** de cada hallazgo automático.
- Automatización de flujos autenticados con **Selenium**.

## 3. Laboratorio guiado

### Parte A — Análisis del flujo con proxy (RA5.a, RA5.c)

```bash
# ZAP en modo proxy; configurar el navegador para pasar por 127.0.0.1:8080
zaproxy &
# Recorrer la aplicación autenticado y revisar el árbol de peticiones
```

1. Mapea la autenticación y la gestión de sesión del portal. Identifica el mecanismo (cookie de sesión, token) y sus debilidades.

### Parte B — Examen manual WSTG (RA5.b, RA5.d)

2. Recorre las secciones aplicables de WSTG: control de acceso (IDOR), lógica de negocio, sesión, validación. Documenta cada hallazgo con evidencia.

### Parte C — Automatización con verificación (RA5.e, RA5.f)

```bash
# Escaneo activo dirigido
nuclei -u https://portal-soc.xest.local -severity critical,high,medium
sqlmap -u "https://portal-soc.xest.local/buscar?q=1" --batch --level 2

# Flujo autenticado automatizado
python3 selenium_flujo_login.py
```

3. Compara los hallazgos automáticos con los manuales y **explica las diferencias**: qué encontró solo el humano, qué solo la herramienta, qué fue falso positivo.

## 4. Entregables

- **`HE-E15`** (informe, rúbrica R2): informe de auditoría web completo — resumen ejecutivo, metodología, hallazgos con evidencia, riesgo y remediación.
- **`HE-E16`** (defensa oral, rúbrica R4): defensa de un hallazgo crítico ante tribunal simulado.

## 5. Criterios de superación

- El examen manual aporta hallazgos que el escáner no encontró (lógica/autorización).
- Todo hallazgo automático está verificado a mano; los falsos positivos, descartados.
- El informe convierte los hallazgos en riesgo priorizado y remediable.

## 6. Errores frecuentes

- Entregar la salida cruda de un escáner como si fuera un informe de auditoría.
- No verificar los hallazgos automáticos: se reporta ruido y se pierde credibilidad.
- Olvidar el resumen ejecutivo: el hallazgo técnico sin traducción de negocio no llega a quien decide.

## 7. Referencias

- OWASP **WSTG 4.2** — guía de referencia del examen.
- Burp Suite / OWASP ZAP, nuclei, sqlmap, Selenium.
- OAuth 2.0 (RFC 6749), OpenID Connect, SAML 2.0.
- MITRE ATT&CK — Exploitation of Public-Facing Application (T1190).
