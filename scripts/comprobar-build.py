#!/usr/bin/env python3
"""Comprueba que el sitio construido no publica nada que no deba publicarse.

Es la última red de seguridad de ESPECIFICACION.md §8 ("/SOLUCIONES excluido del
build público") y de §7.2. Se ejecuta después de `mkdocs build` y falla el proceso
si encuentra una filtración, en vez de dejarla pasar en silencio.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BUILD = RAIZ / "sitio" / "build"
SOLUCIONES = RAIZ / "dataset" / "SOLUCIONES"

# Frases que solo existen en SOLUCIONES/ y en docs-internos/. Si alguna aparece en
# el sitio construido, algo se ha filtrado.
CENTINELAS = [
    "verdades-escondidas",
    "taxonomia-real",
    "pedidos-fantasma",
    "mapa-duplicados",
    "cuentas-v4",
    "categoria_real",
]

RUTAS_PROHIBIDAS = [
    re.compile(r"dataset/SOLUCIONES"),
    re.compile(r"docs-internos/"),
]


def main() -> int:
    if not BUILD.exists():
        print(f"No existe {BUILD}. Ejecuta antes: mkdocs build -f sitio/mkdocs.yml", file=sys.stderr)
        return 2

    fallos: list[str] = []

    for fichero in BUILD.rglob("*"):
        if not fichero.is_file() or fichero.suffix not in {".html", ".js", ".json", ".md", ".txt"}:
            continue
        try:
            texto = fichero.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        rel = fichero.relative_to(BUILD)
        for centinela in CENTINELAS:
            if centinela in texto:
                fallos.append(f"{rel}: contiene el centinela «{centinela}»")
        for patron in RUTAS_PROHIBIDAS:
            if patron.search(texto):
                fallos.append(f"{rel}: referencia una ruta prohibida ({patron.pattern})")

    # Ningún fichero de SOLUCIONES/ puede existir dentro del build, por nombre.
    if SOLUCIONES.exists():
        nombres = {f.name for f in SOLUCIONES.rglob("*") if f.is_file()}
        for f in BUILD.rglob("*"):
            if f.is_file() and f.name in nombres:
                fallos.append(f"{f.relative_to(BUILD)}: es un fichero de SOLUCIONES/ publicado")

    if fallos:
        print("FILTRACIÓN EN EL BUILD:", file=sys.stderr)
        for f in fallos:
            print(f"  - {f}", file=sys.stderr)
        print(f"\n{len(fallos)} problemas. El sitio NO se publica así.", file=sys.stderr)
        return 1

    n = sum(1 for f in BUILD.rglob("*.html"))
    print(f"Build limpio: {n} páginas, sin filtraciones de SOLUCIONES/ ni de docs-internos/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
