# Ficha PPS-E11 · Tráfico móvil y validación de compras

**UT6 · RA4 c,d · Instrumento I2 · Rúbrica R2 · Semana 13**
Entorno: VLAN de laboratorio. Backend `NotasXest` (`trafico/`), mitmproxy, servidores de
compras (`compras/`).

> Regla de aula: la interceptación se hace **solo** contra el backend de laboratorio, en la
> VLAN aislada. Nada de interceptar tráfico ajeno.

## Objetivo

1. **Interceptar** el tráfico de la app y **demostrar** un protocolo inseguro: contraseña y
   clave de API viajando en **HTTP en claro**.
2. **Fijación de certificado (pinning)**: demostrar que una app que pinnea el certificado
   **no** se puede interceptar aunque se instale el CA de mitmproxy (documenta el bloqueo).
3. **Validación de compras**: argumentar, con una demostración, por qué la validación de una
   compra integrada **va en el servidor** y nunca solo en el cliente.

## Pasos

### A · HTTP en claro (RA4.d)
```bash
# terminal 1: backend en claro
python3 trafico/backend_inseguro.py --host 127.0.0.1 --port 8090
# terminal 2: mitmproxy con el addon que resalta secretos
mitmdump -q -s trafico/mitm_addon.py --mode regular --listen-port 8080
# terminal 3: la "app" hace login + sync a través del proxy
python3 trafico/app_cliente.py --base http://127.0.0.1:8090 --proxy http://127.0.0.1:8080
```
Captura la petición `/login`: se ve la **contraseña** en el cuerpo y la **X-Api-Key** en la
cabecera, en claro. Esa captura es tu evidencia.

### B · Pinning (RA4.d, parte defensiva)
```bash
# genera cert de laboratorio y arranca el backend en TLS (ver README del lab)
python3 trafico/backend_inseguro.py --tls        # 127.0.0.1:8443
python3 trafico/app_cliente_pinning.py --calcular-pin        # copia el pin
# conexión directa: pin coincide -> OK
python3 trafico/app_cliente_pinning.py --pin <PIN>
# a través de mitmproxy: pin distinto -> BLOQUEADO
python3 trafico/app_cliente_pinning.py --pin <PIN> --proxy 127.0.0.1:8080
```
Documenta el intento y el bloqueo: eso también es un resultado válido.

### C · Validación de compras (RA4.c)
Compara los dos servidores y **razona** la diferencia:
```bash
cd compras && python3 -m pytest -v
```
El servidor **vulnerable** activa premium con `{"purchase_valid": true}` enviado por el
cliente; el **seguro** lo rechaza y exige un recibo firmado verificado en el servidor.

## Entregable

`NN-PPS-E11-trafico.md`:
- **Captura y análisis** del tráfico (HTTP en claro): qué dato se filtra y por qué.
- **Pinning**: evidencia del bloqueo o del intento.
- **Compras**: diseño del flujo correcto (recibo firmado → verificación en servidor) y
  argumento de por qué la validación solo en cliente es insuficiente. Referencia a la salida
  del `pytest` como evidencia.

## Se evalúa (R2)

Corrección técnica, estructura y **trazabilidad** (hallazgo → evidencia → remediación),
fundamento metodológico (MASTG/MASVS), priorización del riesgo y redacción.
