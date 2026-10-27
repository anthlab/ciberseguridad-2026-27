# Ficha de laboratorio · PPS-E8 — Migración del almacén de contraseñas a Argon2id

**UT5 · RA3.e · Rúbrica R1 (práctica de laboratorio) · Instrumento I1**

> Entorno: tu equipo del aula (Python 3). No necesita la VLAN de objetivos.
> Requisito: `pip install argon2-cffi pytest`.

## Contexto

El portal SOC de xest guarda las contraseñas de sus usuarios con **SHA-256 sin
sal** (`store.py`, `usuarios.json`). Es indefendible: SHA-256 es un hash rápido,
sin sal las claves iguales colisionan y sirven las tablas precalculadas. Tu
trabajo es migrar el almacén a **Argon2id** sin obligar a nadie a cambiar su
contraseña.

## Material que se te entrega

| Fichero | Qué es |
|---|---|
| `store.py` | Almacén de partida (SHA-256). El código que vas a mejorar. |
| `usuarios.json` | 10 usuarios con su hash SHA-256. Tu lote de datos. |
| `crack_demo.py` | Demo del coste: rompe un PIN contra SHA-256 y contra Argon2id. |

## Tareas

1. **Mide el problema.** Ejecuta `python3 crack_demo.py` y anota cuánto tarda el
   ataque contra cada esquema. Esa diferencia es tu justificación técnica.
2. **Migra el alta.** Cambia `crear_usuario` para que use Argon2id con parámetros
   justificados (`time_cost`, `memory_cost`, `parallelism`). Justifica la elección
   midiendo cuánto tarda un `hash()` en tu equipo (objetivo: 0,3–0,5 s).
3. **Migración transparente.** Cambia `verificar` para que:
   - si el hash guardado ya es Argon2id, valide con Argon2id;
   - si es el hash antiguo (SHA-256) y la clave es correcta, **re-hashee al vuelo**
     con Argon2id y actualice `usuarios.json`. El usuario no debe notar nada.
   - Añade `check_needs_rehash` para re-hashear si suben los parámetros.
4. **Prueba de regresión.** Escribe una suite `pytest` que incluya, como mínimo,
   un test que **fallaría si alguien reintrodujera el hash débil** (que un alta
   nunca vuelva a escribir un SHA-256 de 64 hex).
5. **Verifica la migración.** Demuestra con una ejecución que un usuario legacy,
   tras un login correcto, queda guardado como `argon2id` en el fichero.

## Qué entregar (`NN-PPS-E8.md` + PR)

- El diff / PR de `store.py` migrado.
- La suite de pruebas y su salida (`pytest -v`) en verde.
- Tabla con los **parámetros elegidos y su justificación** (tiempo medido).
- Evidencia de la migración transparente: `usuarios.json` de un usuario antes
  (`sha256`) y después (`argon2id`) de un login.

## Criterio de superación

Las contraseñas se almacenan con Argon2id y parámetros justificados **medidos, no
a ojo**; existe migración transparente; existe una prueba de regresión que caza la
reintroducción del hash débil. Sin esa prueba, el trabajo **no** está cerrado.
