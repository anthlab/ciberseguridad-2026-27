# Portal SOC de xest — código de partida (PPS · UT4)

Este es el **portal que vais a corregir** durante la UT4. Trae, a propósito, cuatro
vulnerabilidades reales que primero explotaréis en Juice Shop/DVWA (E6) y luego
cerraréis aquí, en el código, con su prueba de regresión (E7).

> Regla del módulo: una vulnerabilidad **no está cerrada** hasta que existe una prueba
> de regresión que **falla** contra el código vulnerable y **pasa** contra el corregido.

## Puesta en marcha (VLAN de aula aislada)

```bash
python3 -m pip install -r requirements.txt
flask --app app run          # http://127.0.0.1:5000
```

Usuarios de laboratorio (sintéticos): `ana/ana123`, `bruno/bruno123`, `admin/admin123`.
Recursos: `101` es de Ana, `102` de Bruno, `103` de administración.

## Mapa de las cuatro familias en este código

| Familia | Endpoint | Dónde vive el fallo |
|---|---|---|
| **SQLi** | `POST /login` | la consulta se construye concatenando `usuario`/`password` |
| **XSS** | `GET /buscar`, `/comentarios` | la entrada se refleja/almacena sin codificar |
| **Sesión** | `POST /login` | cookie `sid` sin `HttpOnly/Secure/SameSite` y sin rotación |
| **IDOR** | `GET /recurso/<id>` | no comprueba que el recurso sea del usuario |

## Qué tenéis que entregar

- **E6** (`ficha-PPS-E6-explotacion.md`): las cuatro familias explotadas en el laboratorio,
  con petición y captura.
- **E7** (`ficha-PPS-E7-correccion.md`): las cuatro corregidas **en este `app.py`** de forma
  estructural + una prueba de regresión por familia en `tests/test_seguridad.py`.

No despleguéis este portal fuera de la VLAN de aula. Es deliberadamente vulnerable.
