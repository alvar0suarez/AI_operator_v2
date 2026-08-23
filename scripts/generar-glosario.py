#!/usr/bin/env python3
"""Genera contenido/glosario/README.md a partir de contenido/glosario/glosario.yml.

ESPECIFICACION.md §6: "Los conceptos alimentan un glosario global autogenerado y la
navegación lateral". Este script es el generador de ese glosario.

Entradas:
  contenido/glosario/glosario.yml      definiciones (fuente escrita a mano)
  docs-internos/registro-de-nodos.yml  quién usa cada concepto

Salida:
  contenido/glosario/README.md         glosario navegable, orden alfabético,
                                       ancla por slug y nodos que usan el término

Uso:  python3 scripts/generar-glosario.py
"""

from __future__ import annotations

import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
RUTA_GLOSARIO = RAIZ / "contenido" / "glosario" / "glosario.yml"
RUTA_REGISTRO = RAIZ / "docs-internos" / "registro-de-nodos.yml"
RUTA_SALIDA = RAIZ / "contenido" / "glosario" / "README.md"

AVISO = (
    "<!-- FICHERO GENERADO. No lo edites a mano: se sobreescribe.\n"
    "     Fuente: contenido/glosario/glosario.yml\n"
    "     Generador: scripts/generar-glosario.py -->"
)


def sin_acentos(texto: str) -> str:
    """Devuelve el texto en minúsculas y sin diacríticos, para ordenar."""
    descompuesto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in descompuesto if unicodedata.category(c) != "Mn")


def cargar_yaml(ruta: Path) -> dict:
    with ruta.open(encoding="utf-8") as fichero:
        return yaml.safe_load(fichero)


def limpiar(texto: str) -> str:
    """Aplana un bloque plegado de YAML a una sola línea de markdown."""
    return " ".join(str(texto).split())


def usos_por_concepto(registro: dict) -> dict[str, list[dict]]:
    """slug -> lista de nodos que lo declaran, en orden de bloque e id."""
    usos: dict[str, list[dict]] = defaultdict(list)
    for nodo in registro["nodos"]:
        for slug in nodo.get("conceptos") or []:
            usos[slug].append(nodo)
    for slug in usos:
        usos[slug].sort(key=lambda n: (n["bloque"], n["id"]))
    return usos


def ruta_del_nodo(nodo: dict) -> str:
    """Ruta relativa del .md del nodo dentro de /contenido, según su tipo."""
    if nodo["tipo"] == "profundizacion":
        return f"../bloque-{nodo['bloque']}/profundizacion/{nodo['id']}.md"
    return f"../bloque-{nodo['bloque']}/{nodo['id']}.md"


def construir_indice(terminos: list[dict]) -> list[str]:
    """Índice alfabético agrupado por inicial."""
    por_inicial: dict[str, list[dict]] = defaultdict(list)
    for termino in terminos:
        por_inicial[sin_acentos(termino["termino"])[0].upper()].append(termino)

    lineas = ["## Índice", ""]
    for inicial in sorted(por_inicial):
        entradas = ", ".join(
            f"[{t['termino']}](#{t['slug']})" for t in por_inicial[inicial]
        )
        lineas.append(f"**{inicial}** · {entradas}")
        lineas.append("")
    return lineas


def construir_entrada(
    termino: dict, indice_terminos: dict[str, dict], usos: dict[str, list[dict]]
) -> list[str]:
    slug = termino["slug"]
    lineas = [
        f'<a id="{slug}"></a>',
        "",
        f"### {termino['termino']}",
        "",
        limpiar(termino["definicion"]),
        "",
        f"**Ejemplo.** {limpiar(termino['ejemplo'])}",
        "",
    ]

    relacionados = ", ".join(
        f"[{indice_terminos[otro]['termino']}](#{otro})"
        for otro in termino["ver_tambien"]
    )
    lineas.append(f"**Ver también:** {relacionados}")
    lineas.append("")

    nodos = usos.get(slug, [])
    lineas.append(f"**Aparece en** (bloque de origen: {termino['bloque_origen']}):")
    lineas.append("")
    if nodos:
        for nodo in nodos:
            marca = " *(profundización)*" if nodo["tipo"] == "profundizacion" else ""
            lineas.append(
                f"- Bloque {nodo['bloque']} — "
                f"[{nodo['titulo']}]({ruta_del_nodo(nodo)}){marca}"
            )
    else:
        lineas.append("- Ningún nodo del registro lo declara todavía.")
    lineas.append("")
    return lineas


def main() -> int:
    glosario = cargar_yaml(RUTA_GLOSARIO)
    registro = cargar_yaml(RUTA_REGISTRO)

    terminos = sorted(glosario["terminos"], key=lambda t: sin_acentos(t["termino"]))
    indice_terminos = {t["slug"]: t for t in glosario["terminos"]}
    usos = usos_por_concepto(registro)

    lineas: list[str] = [
        AVISO,
        "",
        "# Glosario",
        "",
        f"Las {len(terminos)} palabras que usa este curso, con un ejemplo cada una y "
        "los nodos donde aparecen. Está ordenado alfabéticamente, así que se puede "
        "leer de golpe o consultar suelto.",
        "",
        "Cada entrada dice también en qué bloque aparece por primera vez. Si un "
        "término te suena a chino y su bloque de origen es posterior al que estás "
        "haciendo, déjalo: te lo vas a encontrar explicado a su debido tiempo.",
        "",
    ]
    lineas += construir_indice(terminos)
    lineas.append("---")
    lineas.append("")

    for termino in terminos:
        lineas += construir_entrada(termino, indice_terminos, usos)
        lineas.append("---")
        lineas.append("")

    if lineas[-2:] == ["---", ""]:
        lineas = lineas[:-2]

    RUTA_SALIDA.parent.mkdir(parents=True, exist_ok=True)
    RUTA_SALIDA.write_text("\n".join(lineas).rstrip() + "\n", encoding="utf-8")

    print(f"Escrito {RUTA_SALIDA.relative_to(RAIZ)}: {len(terminos)} términos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
