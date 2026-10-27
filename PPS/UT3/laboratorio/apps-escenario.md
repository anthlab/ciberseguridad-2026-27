# Laboratorio UT3 · Parte A — Tres aplicaciones, tres niveles ASVS (alumnado)

> Material de manos para la asignación de nivel ASVS (evidencia **PPS-E4**).
> Hoja de requisitos: `PPS/material/plantillas/checklist_asvs.md` (ASVS 4.0.3, nivel 2).
> Referencia de la unidad: `PPS/unidades/UT3-asvs-superficie-riesgo.md`.

Se te presentan tres aplicaciones reales del ecosistema de xest. Para **cada una**:

1. Asigna un **nivel de verificación ASVS** (L1, L2 o L3).
2. **Justifícalo** con dos argumentos: qué **datos** trata y cuál es el **impacto** de un
   compromiso. No vale "por si acaso": el nivel debe ser **proporcional al riesgo**.
3. Solo para la **App B** (portal SOC, tu objetivo del módulo): extrae de la hoja ASVS la
   **lista de requisitos aplicables** y traza cada uno a la **prueba** que lo verificará
   (una prueba automática, una captura de auditoría o un entregable posterior PPS-E4…E9).

Entrega: `NN-PPS-E4-asvs.md` (dictamen + tabla de requisitos trazados).

---

## App A — `xest.edu` · Web institucional del centro

- **Qué es**: sitio informativo público del CIPFP: noticias, oferta formativa, calendario,
  formularios de contacto que envían un correo. Sin cuentas de usuario, sin panel privado.
- **Datos que trata**: contenido público + el nombre y correo de quien rellena el formulario
  de contacto (dato personal básico, no categoría especial).
- **Autenticación**: ninguna de cara al visitante. Solo el gestor de contenidos interno.
- **Impacto de un compromiso**: desfiguración de la portada, spam desde el formulario.
  No hay datos sensibles que exfiltrar ni dinero en juego.
- **Exposición**: publicada en Internet.

## App B — `portal-soc.xest.local` · Portal del SOC de xest  *(tu objetivo del módulo)*

- **Qué es**: portal con **cuentas de usuario** (analistas del SOC) que da acceso a paneles
  de incidentes, alertas de Wazuh y casos de TheHive. Es el servicio que construyes y
  bastionas a lo largo de PPS y que HE audita e IC vigila.
- **Datos que trata**: credenciales de analistas, tokens de sesión, y **datos operativos de
  seguridad** (alertas, IOC, incidentes) — información sensible de negocio, aunque no
  categoría especial del art. 9 RGPD.
- **Autenticación**: login usuario/contraseña; distintos roles (analista, responsable).
- **Impacto de un compromiso**: un atacante que entra ve la telemetría de seguridad de la
  organización, puede borrar evidencias o suplantar a un analista. Compromete el propio
  órgano que debería detectar el ataque.
- **Exposición**: interno + accesible por VPN.

## App C — `pagos.xest.local` · Pasarela de pago de matrículas y tasas

- **Qué es**: componente que cobra matrículas y tasas del alumnado. Procesa tarjetas a través
  de un proveedor (TPV virtual) y guarda el histórico de transacciones.
- **Datos que trata**: importe, referencia de pago, datos de titular, tokens de tarjeta.
  Ámbito **PCI-DSS**; dinero real; impacto económico y legal directo.
- **Autenticación**: cuenta del pagador + doble factor en operaciones sensibles.
- **Impacto de un compromiso**: fraude, robo de datos de tarjeta, sanción regulatoria,
  pérdida de confianza. Un fallo aquí tiene consecuencias financieras y jurídicas.
- **Exposición**: publicada en Internet, integrada con un proveedor de pago externo.

---

## Rejilla para tu dictamen (rellénala)

| App | Nivel ASVS | Dato que lo justifica | Impacto que lo justifica |
|---|:--:|---|---|
| A · Web institucional | | | |
| B · Portal SOC | | | |
| C · Pasarela de pago | | | |

## Requisitos aplicables al portal SOC (App B, nivel 2) — traza cada uno a su prueba

Toma las familias de la hoja `checklist_asvs.md` (V2 auth, V3 sesión, V4 acceso, V5
validación, V7 errores, V9 comunicaciones, V14 configuración) y completa:

| Req. ASVS | Qué verifica | Prueba / evidencia que lo comprobará | ¿Cuándo (UT)? |
|---|---|---|---|
| 5.3.4 | Consultas parametrizadas | `tests/test_seguridad.py::test_login_no_inyectable` | UT4 (PPS-E7) |
| 14.4.1 | Cabeceras de seguridad | `verifica_asvs.py` (sonda externa) | UT3 hoy / UT5 (PPS-E9) |
| … | … | … | … |

> Pista: una parte de los requisitos de **V9/V14** los puedes comprobar **hoy mismo** desde
> fuera con `verifica_asvs.py` contra el portal. Los de **V2/V3/V4/V5** exigen la lógica de
> login que construirás en UT4-UT5: se trazan a las pruebas de regresión de esos entregables.
