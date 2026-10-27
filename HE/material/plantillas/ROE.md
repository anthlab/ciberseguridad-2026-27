# Reglas de enfrentamiento (ROE) — Test de intrusión

Plantilla del entregable `HE-E1`. Documento previo e imprescindible: **sin firma de
ambas partes no se ejecuta ninguna acción activa**. En el contexto del curso, la
contraparte que autoriza es el rol docente y el objetivo es el servicio de laboratorio
del proyecto.

---

## 1. Partes

| Rol | Nombre | Organización | Firma | Fecha |
|---|---|---|---|---|
| Propietario del activo (autoriza) | | | | |
| Responsable del test | | | | |

## 2. Objeto y objetivos

Descripción del ejercicio y qué se pretende demostrar (p. ej. validar el bastionado del portal del SOC de xest tras las UT de PPS).

## 3. Alcance (perímetro)

### En alcance
- IPs / rangos:
- Dominios / subdominios:
- Aplicaciones / APIs:
- Cuentas de prueba proporcionadas:

### Fuera de alcance (explícito)
- Sistemas de terceros, servicios en producción no listados, infraestructura del proveedor de nube, etc.

## 4. Ventana de ejecución

- Fechas: del ____ al ____
- Franja horaria permitida:
- Zona horaria:

## 5. Técnicas

### Permitidas
- Reconocimiento, enumeración, explotación en laboratorio, post-explotación con reversión.

### Prohibidas
- Denegación de servicio real.
- Ingeniería social sobre personas no informadas.
- Modificación destructiva de datos.
- Cualquier acción sobre sistemas fuera de alcance.

## 6. Regla de parada (`stop-the-test`)

- Condiciones que obligan a parar: indisponibilidad del servicio, hallazgo de dato personal masivo, indicio de compromiso previo por un tercero real.
- Quién puede invocarla: ____________________
- Cómo se comunica: ____________________

## 7. Comunicación

- Persona de contacto (24×7 durante la ventana):
- Canal primario / secundario:
- Procedimiento ante incidente colateral:

## 8. Manejo de datos capturados

- Cifrado en tránsito y en reposo de toda evidencia.
- No exfiltración de datos personales más allá de lo necesario para probar el hallazgo.
- Destrucción de los datos capturados tras la entrega del informe: fecha límite ____.

## 9. Entregables y plazos

- Informe de auditoría: fecha ____.
- Reunión de cierre y retest: fecha ____.

## 10. Marco legal

Este ejercicio se ampara en la autorización expresa del propietario del activo. Fuera
de este alcance, las técnicas empleadas pueden constituir delito conforme a los
artículos 197 bis, 197 ter, 264 y 264 bis del Código Penal español. Todo dato personal
que pudiera capturarse queda sujeto al RGPD (arts. 5, 6 y 32).

---

**Firmas** (ambas obligatorias antes de iniciar):

Propietario del activo: __________________________  Fecha: __________

Responsable del test: ____________________________  Fecha: __________
