#!/usr/bin/env python3
"""Genera la web del curso a partir del repositorio.

    uv run --with-requirements plataforma/requirements.txt python3 plataforma/build.py
    → _build/site/  (abrir index.html, servir con servir-aula.sh o publicar en Pages)

Pasos: copia el material a _build/docs, crea un índice en cada carpeta que no
lo tenga, empaqueta en .zip cada laboratorio y práctica, corrige los enlaces a
carpetas para que funcionen sin servidor y escribe mkdocs.yml con la navegación.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import urllib.parse
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PLAT = RAIZ / "plataforma"
BUILD = RAIZ / "_build"
DOCS = BUILD / "docs"

CONTENIDO = ["PPS", "HE", "IC", "comun", "SOC", "docs", "INICIO.md"]
GENERADOS: set[Path] = set()
IGNORAR = {".DS_Store", "__pycache__", ".pytest_cache", ".venv", ".coverage"}

MODULOS = {
    "PPS": ("Puesta en Producción Segura", "5023", "Martes", list(range(1, 9))),
    "IC": ("Incidentes de Ciberseguridad", "5021", "Miércoles", list(range(1, 9))),
    "HE": ("Hacking Ético", "5025", "Jueves", [1, 5, 2, 3, 4, 6, 7, 8]),
}

ICONOS = {
    ".pdf": "📕", ".md": "📝", ".py": "🐍", ".sh": "⚙️", ".java": "☕", ".c": "🔧",
    ".yml": "🧩", ".yaml": "🧩", ".json": "🧾", ".csv": "📊", ".txt": "📄",
    ".html": "🌐", ".docx": "📘", ".xml": "🧾", ".conf": "🧩", ".svg": "🖼️",
}


def copiar() -> None:
    if BUILD.exists():
        shutil.rmtree(BUILD)
    DOCS.mkdir(parents=True)
    for nombre in CONTENIDO:
        src = RAIZ / nombre
        if src.is_dir():
            shutil.copytree(src, DOCS / nombre, ignore=shutil.ignore_patterns(*IGNORAR))
        else:
            shutil.copy2(src, DOCS / nombre)
    shutil.copytree(PLAT / "assets", DOCS / "assets")
    shutil.copy2(PLAT / "inicio.md", DOCS / "index.md")
    for clave in MODULOS:
        readme = DOCS / clave / "README.md"
        lineas = readme.read_text(encoding="utf-8").splitlines()
        lineas.insert(1, f'\n<div class="progreso-modulo" data-modulo="{clave}"></div>')
        readme.write_text("\n".join(lineas) + "\n", encoding="utf-8")


def titulo_md(p: Path) -> str | None:
    for linea in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        if linea.startswith("# "):
            return linea[2:].strip()
    return None


def indice_de(d: Path) -> Path | None:
    for n in ("index.md", "README.md"):
        if (d / n).exists():
            return d / n
    return None


def tam(n: int) -> str:
    if n < 1024:
        return f"{n} B"
    return f"{n / 1024:.0f} KB" if n < 1024 * 1024 else f"{n / 1024 / 1024:.1f} MB"


def es_paquete(d: Path) -> bool:
    """Carpetas que se pueden descargar enteras: laboratorios y prácticas."""
    partes = d.relative_to(DOCS).parts
    return len(partes) >= 3 and ("laboratorio" in partes or "practicas" in partes)


def zip_de(d: Path) -> Path:
    destino = d / f"{d.name}.zip"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(d.rglob("*")):
            if f.is_file() and f != destino and f.suffix != ".zip" and f not in GENERADOS:
                z.write(f, Path(d.name) / f.relative_to(d))
    return destino


def enlace(nombre: str) -> str:
    return urllib.parse.quote(nombre)


def generar_indices() -> None:
    # De dentro afuera, para que los .zip de las subcarpetas no entren en el padre.
    carpetas = sorted((p for p in DOCS.rglob("*") if p.is_dir()), key=lambda p: -len(p.parts))
    for d in carpetas:
        rel = d.relative_to(DOCS)
        if rel.parts[0] == "assets":
            continue
        descarga = ""
        if es_paquete(d):
            z = zip_de(d)
            descarga = (
                f'\n[:material-download: Descargar la carpeta completa ({tam(z.stat().st_size)})]'
                f'({enlace(z.name)}){{ .md-button .md-button--primary }}\n'
            )
        existente = indice_de(d)
        if existente:
            if descarga:
                with existente.open("a", encoding="utf-8") as f:
                    f.write("\n" + descarga)
            continue
        subdirs = sorted(p for p in d.iterdir() if p.is_dir())
        ficheros = sorted(p for p in d.iterdir() if p.is_file() and p.suffix != ".zip")
        lineas = [f"# {d.name}", "", descarga]
        if subdirs:
            lineas += ["## Carpetas", ""]
            for s in subdirs:
                lineas.append(f"- 📁 [{s.name}]({enlace(s.name)}/)")
            lineas.append("")
        if ficheros:
            lineas += ["## Ficheros", "", "| | Fichero | Tamaño |", "|---|---|---|"]
            for f in ficheros:
                nombre = titulo_md(f) if f.suffix == ".md" else None
                texto = f"{nombre} (`{f.name}`)" if nombre else f"`{f.name}`"
                lineas.append(
                    f"| {ICONOS.get(f.suffix.lower(), '📄')} | [{texto}]({enlace(f.name)}) | {tam(f.stat().st_size)} |"
                )
        (d / "index.md").write_text("\n".join(lineas) + "\n", encoding="utf-8")
        GENERADOS.add(d / "index.md")


ENLACE_MD = re.compile(r"(\]\()([^)\s#]+)(#[^)\s]*)?(\))")


def corregir_enlaces() -> None:
    """Enlaces a carpetas → a su índice (sin servidor el navegador no lo resuelve)."""
    for md in DOCS.rglob("*.md"):
        texto = md.read_text(encoding="utf-8", errors="ignore")

        def sub(m: re.Match) -> str:
            url = m.group(2)
            if re.match(r"^[a-z]+:", url) or url.startswith("/"):
                return m.group(0)
            destino = (md.parent / urllib.parse.unquote(url)).resolve()
            if destino.is_dir():
                idx = indice_de(destino)
                if idx:
                    url = url.rstrip("/") + "/" + idx.name
            return f"{m.group(1)}{url}{m.group(3) or ''}{m.group(4)}"

        nuevo = ENLACE_MD.sub(sub, texto)
        if nuevo != texto:
            md.write_text(nuevo, encoding="utf-8")


def q(s: str) -> str:
    return '"' + s.replace('"', '\\"') + '"'


def nav_modulo(clave: str) -> list[str]:
    nombre, codigo, dia, orden = MODULOS[clave]
    m = DOCS / clave
    nav = [f"  - {q(clave)}:", f"    - Presentación: {clave}/README.md",
           f"    - Prácticas de clase: {clave}/practicas/index.md"]
    for n in orden:
        ut = m / f"UT{n}"
        teoria = sorted((m / "unidades").glob(f"UT{n}-*.md"))
        titulo = titulo_md(teoria[0]) if teoria else f"UT{n}"
        titulo = re.sub(r"^(?:(?:PPS|HE|IC)\s*·\s*)?UT\s*\d+\s*[·:—-]\s*", "", titulo or f"UT{n}")
        nav.append(f"    - {q(f'UT{n} · {titulo}')}:")
        nav.append(f"      - Guía: {clave}/UT{n}/GUIA-ALUMNADO.md")
        if teoria:
            nav.append(f"      - Teoría: {clave}/unidades/{teoria[0].name}")
        lab = ut / "laboratorio"
        if lab.is_dir() and indice_de(lab):
            nav.append(f"      - Laboratorio: {clave}/UT{n}/laboratorio/{indice_de(lab).name}")
    nav.append(f"    - Entregables: {clave}/evaluacion/entregables.md")
    if (m / "recursos").is_dir():
        nav.append("    - Herramientas:")
        for r in sorted((m / "recursos").glob("*.md")):
            nav.append(f"      - {q(titulo_md(r) or r.stem)}: {clave}/recursos/{r.name}")
    if (m / "material").is_dir():
        nav.append(f"    - Material de apoyo: {clave}/material/index.md")
    if clave == "IC":
        nav.append("    - SOC (Sigma y playbooks): SOC/plataforma/index.md")
    return nav


def escribir_config() -> None:
    comun = DOCS / "comun"
    paginas_comun = [
        ("Primera sesión", "PRIMERA-SESION.md"), ("Instalar el puesto", "GUIA-INSTALACION.md"),
        ("Herramientas", "GUIA-HERRAMIENTAS.md"), ("Precisiones del curso", "PRECISIONES-DEL-CURSO.md"),
        ("Plantilla de informe", "PLANTILLA-INFORME.md"), ("Laboratorios", "entornos/README.md"),
        ("OSINT: política", "legal/osint-aula-politica.md"),
        ("OSINT: consentimiento", "legal/consentimiento-autoosint.md"),
        ("Cursos gratuitos", "CURSOS-ONLINE.md"),
    ]
    nav = ["nav:", "  - Inicio: index.md", "  - Empieza aquí:"]
    nav += [f"    - {q(t)}: comun/{f}" for t, f in paginas_comun if (comun / f).exists()]
    for clave in ("PPS", "IC", "HE"):
        nav += nav_modulo(clave)
    nav += ["  - Índice completo: INICIO.md", "  - Evaluación (rúbricas): docs/planificacion/rubricas.md"]
    plantilla = (PLAT / "mkdocs.base.yml").read_text(encoding="utf-8")
    (BUILD / "mkdocs.yml").write_text(plantilla + "\n" + "\n".join(nav) + "\n", encoding="utf-8")


def main() -> int:
    copiar()
    generar_indices()
    corregir_enlaces()
    escribir_config()
    args = [sys.executable, "-m", "mkdocs", "build", "-q", "-f", str(BUILD / "mkdocs.yml")]
    if "--strict" in sys.argv:
        args.append("--strict")
    r = subprocess.run(args)
    if r.returncode == 0:
        print(f"Web generada en {os.path.relpath(BUILD / 'site')}/index.html")
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
