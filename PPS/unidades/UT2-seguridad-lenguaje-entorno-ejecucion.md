# PPS · UT2 — Seguridad del lenguaje y del entorno de ejecución

**5 horas** · RA1 (e) · Servicio SOC: Prevención — configuración segura · Evidencia `PPS-E3`

---

## 1. Objetivo de la unidad

Elegir lenguaje y entorno de ejecución es una decisión de seguridad, no solo de rendimiento o de gusto del equipo. Esta unidad enseña a **razonar esa elección** y a aislar un proceso para que, aunque el código falle, el daño quede contenido.

## 2. Contenido

### 2.1 Garantías que aporta (o no) el lenguaje

- **Seguridad de memoria**: Rust, Go, Java, C#, Python la garantizan; C y C++ no. Un servicio expuesto a Internet escrito en C carga con toda la familia de desbordamientos y uso-después-de-liberar salvo mitigación explícita.
- **Tipado**: el tipado fuerte y estático detecta en compilación clases enteras de error; el dinámico las traslada a tiempo de ejecución.
- **Gestión de excepciones**: un lenguaje que obliga a tratar el error (Go con valores de retorno, Rust con `Result`) reduce el fallo silencioso.
- **Cadena de suministro del propio lenguaje**: el intérprete, el compilador y el gestor de paquetes también son superficie (typosquatting en PyPI/npm, compilador troyanizado).

### 2.2 Entornos de ejecución aislados

| Mecanismo | Qué aísla | Uso típico |
|---|---|---|
| **Sandbox del navegador** | JavaScript del cliente respecto al SO | Aplicaciones web |
| **JVM / CLR** | Bytecode respecto al nativo | Java / .NET |
| **Contenedor** | Proceso respecto al host (namespaces, cgroups) | Despliegue en producción |
| **seccomp** | Llamadas al sistema permitidas al proceso | Endurecer contenedores |
| **AppArmor / SELinux** | Acceso del proceso a ficheros y capacidades | Bastionado del host |

Aislar es reducir lo que un proceso comprometido puede hacer. Un contenedor sin `seccomp` ni usuario no-root comparte demasiada superficie con el host.

## 3. Laboratorio guiado

### Parte A — Dictamen de elección de lenguaje (RA1.e)

1. Escenario: servicio HTTP expuesto a Internet que procesa ficheros subidos por el usuario.
2. Evalúa **tres lenguajes candidatos** (p. ej. Go, Python, C) con estos criterios: seguridad de memoria, madurez del ecosistema de seguridad, facilidad de despliegue aislado, superficie de la cadena de suministro.
3. Emite una recomendación **justificada con los criterios**, no con preferencias.

### Parte B — Aislar un proceso con seccomp (RA1.e, refuerzo)

```bash
# Ver las llamadas al sistema que hace un contenedor
docker run --rm --security-opt seccomp=unconfined alpine \
  sh -c 'strace -f -c whoami' 2>&1 | tail -20

# Aplicar un perfil seccomp restrictivo y comprobar que bloquea
docker run --rm --security-opt seccomp=./perfil-restrictivo.json alpine whoami

# Ejecutar como usuario no-root y sin capacidades extra
docker run --rm --user 1000:1000 --cap-drop ALL alpine id
```

4. Construye un perfil `seccomp` que permita solo las llamadas necesarias y demuestra empíricamente que una llamada prohibida (p. ej. `mount`) es rechazada.
5. Documenta la diferencia de superficie entre el contenedor por defecto y el endurecido.

## 4. Entregable

- **`PPS-E3`** (informe, rúbrica R2): dictamen técnico de elección de lenguaje y entorno de ejecución con criterios de seguridad explícitos, más la evidencia del aislamiento con `seccomp` (perfil aplicado y llamada bloqueada).

## 5. Criterios de superación

- La recomendación se sostiene sobre criterios de seguridad, no sobre familiaridad del equipo.
- El aislamiento se demuestra **empíricamente**: se ve la llamada bloqueada, no se afirma que lo estaría.

## 6. Errores frecuentes

- Elegir el lenguaje "que ya conoce el equipo" sin evaluar la superficie que introduce.
- Confiar en la ofuscación de bytecode como control de seguridad.
- Dar por aislado un contenedor que corre como root con todas las capacidades.

## 7. Referencias

- NIST SP 800-190 — Application Container Security Guide.
- OWASP Docker Security Cheat Sheet.
- Documentación de `seccomp`, AppArmor y las opciones `--security-opt` de Docker.
