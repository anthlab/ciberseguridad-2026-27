# Informe de vulnerabilidad → corrección → prueba (PPS · UT4/UT5)

Plantilla del entregable `PPS-E6`. Una ficha por vulnerabilidad. El informe no está
completo hasta que la columna «Prueba de regresión» apunta a una prueba que falla
contra el código vulnerable y pasa contra el corregido.

---

## Resumen

| Id | Familia (OWASP) | Componente | Riesgo | Estado |
|---|---|---|---|---|
| V-01 | | | Crítico/Alto/Medio/Bajo | Cerrada/Abierta |
| V-02 | | | | |

---

## Ficha V-01 — <título breve>

**Familia:** (p. ej. A03:2021 Inyección) · **Componente:** `ruta/fichero:línea`
**Nivel de riesgo:** Alto · **Requisito ASVS relacionado:** V5.3.4

### Descripción
Qué es y por qué es explotable en este componente concreto.

### Evidencia de explotación
Petición y respuesta que demuestran la vulnerabilidad. Captura o `curl` reproducible.

```
POST /buscar HTTP/1.1
Host: portal-soc.xest.local
Content-Type: application/x-www-form-urlencoded

q=' OR '1'='1
```

### Impacto
Qué consigue un atacante: lectura de datos ajenos, ejecución, escalada, etc.

### Corrección aplicada
Descripción del cambio y confirmación (hash del commit). El patrón correcto, no un parche cosmético.

```python
# Antes (vulnerable)
cursor.execute("SELECT * FROM items WHERE nombre = '" + q + "'")
# Después (parametrizado)
cursor.execute("SELECT * FROM items WHERE nombre = %s", (q,))
```

### Prueba de regresión
Ruta de la prueba y qué comprueba. Debe fallar contra el código anterior.

```
tests/test_seguridad.py::test_busqueda_no_es_inyectable
```

### Verificación
Cómo se confirmó el cierre (re-explotación fallida, prueba en verde, escaneo limpio).

---

## Ficha V-02 — <título breve>

*(repetir la estructura)*
