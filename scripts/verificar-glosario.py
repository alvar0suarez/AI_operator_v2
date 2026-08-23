#!/usr/bin/env python3
"""Verifica el contrato del glosario contra el registro de nodos.

Contrato (docs-internos/esquema-frontmatter.md, campo `conceptos`):
"Todo slug debe existir en contenido/glosario/glosario.yml".

Comprueba:
  1. Cobertura: todo slug del registro tiene entrada en el glosario.
  2. Sin sobrantes: toda entrada del glosario la usa algún nodo del registro.
  3. Integridad de `ver_tambien`: todos los destinos existen, entre 1 y 4,
     sin duplicados y sin apuntarse a sí mismo.
  4. `bloque_origen` es el bloque más bajo del registro que usa el concepto.
  5. Campos obligatorios presentes, slugs únicos y en kebab-case sin acentos.
  6. Higiene de redacción: la definición no empieza por "Es cuando" y el
     ejemplo no está vacío.

Uso:  python3 scripts/verificar-glosario.py     (código de salida 1 si falla)
"""

from __future__ import annotations

import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
RUTA_GLOSARIO = RAIZ / "contenido" / "glosario" / "glosario.yml"
RUTA_REGISTRO = RAIZ / "docs-internos" / "registro-de-nodos.yml"

CAMPOS_OBLIGATORIOS = ("slug", "termino", "definicion", "ejemplo", "ver_tambien", "bloque_origen")
PATRON_SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ARRANQUES_PROHIBIDOS = ("es cuando", "se trata de cuando", "es aquello que")


def cargar_yaml(ruta: Path) -> dict:
    with ruta.open(encoding="utf-8") as fichero:
        return yaml.safe_load(fichero)


def normalizar(texto: str) -> str:
    return " ".join(str(texto).split())


def sin_acentos(texto: str) -> str:
    descompuesto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in descompuesto if unicodedata.category(c) != "Mn")


def main() -> int:
    glosario = cargar_yaml(RUTA_GLOSARIO)
    registro = cargar_yaml(RUTA_REGISTRO)

    terminos = glosario["terminos"]
    errores: list[str] = []

    # ── Slugs del registro y bloque más bajo que usa cada uno ──────────────────
    bloque_minimo: dict[str, int] = {}
    usos: dict[str, list[str]] = defaultdict(list)
    for nodo in registro["nodos"]:
        for slug in nodo.get("conceptos") or []:
            usos[slug].append(nodo["id"])
            bloque_minimo[slug] = min(bloque_minimo.get(slug, 99), nodo["bloque"])

    slugs_registro = set(bloque_minimo)
    slugs_glosario = [t.get("slug") for t in terminos]

    # ── 5. Estructura de cada entrada ─────────────────────────────────────────
    vistos: set[str] = set()
    for indice, termino in enumerate(terminos, start=1):
        slug = termino.get("slug", f"<entrada {indice} sin slug>")
        for campo in CAMPOS_OBLIGATORIOS:
            if not termino.get(campo) and termino.get(campo) != 0:
                errores.append(f"[{slug}] falta el campo obligatorio '{campo}'")
        if isinstance(slug, str) and not PATRON_SLUG.match(slug):
            errores.append(f"[{slug}] el slug no es kebab-case sin acentos")
        if slug in vistos:
            errores.append(f"[{slug}] slug duplicado en el glosario")
        vistos.add(slug)

    # ── 1 y 2. Cobertura y sobrantes ──────────────────────────────────────────
    faltan = sorted(slugs_registro - vistos)
    sobran = sorted(vistos - slugs_registro)
    for slug in faltan:
        errores.append(f"FALTA: '{slug}' se usa en {usos[slug]} y no está en el glosario")
    for slug in sobran:
        errores.append(f"SOBRA: '{slug}' está en el glosario y no lo usa ningún nodo")

    # ── 3, 4 y 6. Reglas por entrada ──────────────────────────────────────────
    for termino in terminos:
        slug = termino.get("slug")
        relacionados = termino.get("ver_tambien") or []

        if not 1 <= len(relacionados) <= 4:
            errores.append(
                f"[{slug}] 'ver_tambien' tiene {len(relacionados)} entradas (mínimo 1, máximo 4)"
            )
        if len(set(relacionados)) != len(relacionados):
            errores.append(f"[{slug}] 'ver_tambien' tiene slugs repetidos")
        for destino in relacionados:
            if destino == slug:
                errores.append(f"[{slug}] 'ver_tambien' se apunta a sí mismo")
            elif destino not in vistos:
                errores.append(f"[{slug}] 'ver_tambien' apunta a '{destino}', que no existe")

        esperado = bloque_minimo.get(slug)
        if esperado is not None and termino.get("bloque_origen") != esperado:
            errores.append(
                f"[{slug}] 'bloque_origen' es {termino.get('bloque_origen')} "
                f"y el bloque más bajo que lo usa es {esperado}"
            )

        definicion = sin_acentos(normalizar(termino.get("definicion", "")))
        for arranque in ARRANQUES_PROHIBIDOS:
            if definicion.startswith(arranque):
                errores.append(f"[{slug}] la definición empieza por '{arranque}'")
        if len(normalizar(termino.get("ejemplo", ""))) < 40:
            errores.append(f"[{slug}] el ejemplo es demasiado corto para ser concreto")

    # ── Informe ───────────────────────────────────────────────────────────────
    print(f"Slugs distintos en el registro : {len(slugs_registro)}")
    print(f"Términos en el glosario        : {len(slugs_glosario)}")
    print(f"Cobertura                      : {len(slugs_registro & vistos)}/{len(slugs_registro)}")
    print(f"Sobrantes                      : {len(sobran)}")
    total_referencias = sum(len(t.get('ver_tambien') or []) for t in terminos)
    print(f"Referencias 'ver_tambien'      : {total_referencias}, todas resueltas"
          if not any("ver_tambien" in e for e in errores)
          else f"Referencias 'ver_tambien'      : {total_referencias}, CON ERRORES")

    if errores:
        print(f"\n{len(errores)} problema(s):")
        for error in errores:
            print(f"  - {error}")
        return 1

    print("\nOK: cobertura completa, sin sobrantes y todas las referencias resuelven.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
