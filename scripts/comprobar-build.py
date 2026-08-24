#!/usr/bin/env python3
"""Comprueba que el sitio construido no publica nada que no deba publicarse.

Es la última red de seguridad de ESPECIFICACION.md §8 ("/SOLUCIONES excluido del
build público") y de §7.2. Se ejecuta después de `mkdocs build` y falla el proceso
si encuentra una filtración, en vez de dejarla pasar en silencio.

Comprueba dos cosas distintas, y hacen falta las dos:

1. **Procedencia.** Que no se publique ningún fichero de `dataset/SOLUCIONES/`,
   ni su nombre, ni una ruta de `docs-internos/`.
2. **Contenido.** Que no aparezcan las respuestas del ejercicio central del
   bloque 4, vengan de donde vengan (`scripts/centinelas.py`).

La comprobación 1 sola no basta y el proyecto lo aprendió por las malas: pasaba
en verde mientras el sitio publicaba las cinco verdades escondidas escritas a
mano en el glosario, en el `brief` de los nodos pendientes y en un sabotaje.
`docs-internos/FUGA-BLOQUE-4.md` cuenta el episodio entero.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import centinelas  # noqa: E402  (el sys.path de arriba es lo que lo hace posible)

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

EXTENSIONES = {".html", ".js", ".json", ".md", ".txt"}


def main() -> int:
    if not BUILD.exists():
        print(f"No existe {BUILD}. Ejecuta antes: mkdocs build -f sitio/mkdocs.yml", file=sys.stderr)
        return 2

    mudos = centinelas.autoprueba(RAIZ)
    if mudos:
        print("CENTINELAS QUE NO DETECTAN SU PROPIA VERDAD: "
              + ", ".join(mudos), file=sys.stderr)
        print("Arréglalos antes de fiarte de este comprobador.", file=sys.stderr)
        return 2

    fallos: list[str] = []
    filtraciones: list[centinelas.Hallazgo] = []

    for fichero in BUILD.rglob("*"):
        if not fichero.is_file() or fichero.suffix not in EXTENSIONES:
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
        if not centinelas.es_de_terceros(rel):
            filtraciones += centinelas.buscar(texto, str(rel),
                                              es_html=fichero.suffix == ".html")

    # Ningún fichero de SOLUCIONES/ puede existir dentro del build, por nombre.
    if SOLUCIONES.exists():
        nombres = {f.name for f in SOLUCIONES.rglob("*") if f.is_file()}
        for f in BUILD.rglob("*"):
            if f.is_file() and f.name in nombres:
                fallos.append(f"{f.relative_to(BUILD)}: es un fichero de SOLUCIONES/ publicado")

    if filtraciones:
        print("EL SITIO PUBLICA LAS RESPUESTAS DEL BLOQUE 4:", file=sys.stderr)
        for hallazgo in filtraciones:
            print(f"  - {hallazgo}", file=sys.stderr)
        verdades = ", ".join(sorted({h.centinela.verdad for h in filtraciones}))
        print(f"\n{len(filtraciones)} filtraciones ({verdades}). Con esto en el "
              f"sitio, el ejercicio central del bloque 4 se resuelve leyendo.",
              file=sys.stderr)

    if fallos:
        print("FILTRACIÓN EN EL BUILD:", file=sys.stderr)
        for f in fallos:
            print(f"  - {f}", file=sys.stderr)
        print(f"\n{len(fallos)} problemas. El sitio NO se publica así.", file=sys.stderr)

    if fallos or filtraciones:
        return 1

    n = sum(1 for f in BUILD.rglob("*.html"))
    print(f"Build limpio: {n} páginas. Ni SOLUCIONES/, ni docs-internos/, ni "
          f"ninguna verdad escondida ({len(centinelas.CENTINELAS)} centinelas).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
