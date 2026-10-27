# Plataforma web del curso

La web se genera a partir del propio repositorio: cada vez que subo material a `main`, GitHub Actions la reconstruye y la publica en GitHub Pages.

- `build.py`: copia el material a `_build/docs`, crea un índice en cada carpeta, empaqueta cada laboratorio y práctica en un `.zip` y genera la navegación.
- `inicio.md`: portada.
- `mkdocs.base.yml`: tema y opciones (la navegación la añade `build.py`).
- `assets/`: estilos y el progreso por unidad (se guarda en el navegador del alumno).
- `servir-aula.sh`: sirve la web en la red del aula sin Internet.

## Generarla en local

```
uv run --with-requirements plataforma/requirements.txt python3 plataforma/build.py
open _build/site/index.html
```

## En el aula sin Internet

1. En casa: genera la web, o descarga `curso-web-offline.zip` de la última ejecución de Actions.
2. En el equipo del profesor: `./plataforma/servir-aula.sh` y da a los alumnos la dirección que muestra.

La web también funciona abriendo `index.html` directamente, sin servidor (búsqueda incluida).

## Qué no va en la web

Nada del profesor: ni soluciones, ni claves de Kahoot, ni guiones docentes. Antes de subir material nuevo:

```
grep -rliE 'SOLUCION|solucion/|clave|kahoot' PPS HE IC comun SOC docs
```
