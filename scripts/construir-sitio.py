#!/usr/bin/env python3
"""Ensambla sitio/docs/ a partir del contenido del repositorio.

Por qué existe este paso en vez de apuntar MkDocs directamente a contenido/:

1. El frontmatter de §6 lleva información que la alumna tiene que VER (duración,
   caducidad, requisitos, ramas de profundización). Aquí se convierte en cabecera
   renderizada en vez de quedarse como metadatos invisibles.
2. `dataset/SOLUCIONES/` y `docs-internos/` no pueden acabar publicados. La forma
   segura de garantizarlo no es excluirlos: es no copiarlos nunca. Lo que no entra
   en sitio/docs/ no se puede publicar por descuido.
3. La navegación sale del registro de nodos, que es la fuente de verdad del orden.
   Escribir el `nav` a mano en mkdocs.yml se desincroniza al segundo nodo nuevo.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
CONTENIDO = RAIZ / "contenido"
DESTINO = RAIZ / "sitio" / "docs"
REGISTRO = RAIZ / "docs-internos" / "registro-de-nodos.yml"

# Nada de esto se copia jamás al sitio. Es una lista de exclusión de último recurso:
# la garantía real es que solo se copia lo que se nombra explícitamente.
PROHIBIDO = ("SOLUCIONES", "docs-internos", "_auditoria", "solucion.md")

CADUCIDAD = {
    "bajo": ("Duradero", "Esto va a seguir siendo cierto dentro de tres años."),
    "medio": ("Revisable", "El fondo dura; los detalles concretos habrá que revisarlos."),
    "alto": ("Desechable", "Esto caduca. Está aislado a propósito: se sustituye entero sin tocar el resto."),
}

TIPOS = {
    "concepto": "Concepto",
    "ejercicio": "Ejercicio",
    "caso": "Caso",
    "artefacto": "Artefacto",
    "profundizacion": "Profundización",
}


def leer_frontmatter(ruta: Path) -> tuple[dict, str]:
    texto = ruta.read_text(encoding="utf-8")
    if not texto.startswith("---"):
        return {}, texto
    fin = texto.find("\n---", 3)
    if fin == -1:
        return {}, texto
    meta = yaml.safe_load(texto[3:fin]) or {}
    cuerpo = texto[fin + 4 :].lstrip("\n")
    return meta, cuerpo


def cabecera(meta: dict, indice: dict) -> str:
    """La ficha que ve la alumna encima de cada nodo."""
    etiqueta, explicacion = CADUCIDAD[meta["caduca"]]
    tipo = TIPOS.get(meta["tipo"], meta["tipo"])

    lineas = [f"# {meta['titulo']}", ""]
    lineas.append(
        f'<span class="ficha-nodo">{tipo} · {meta["duracion_min"]} min · '
        f'<span class="caduca caduca-{meta["caduca"]}" title="{explicacion}">{etiqueta}</span></span>'
    )
    lineas.append("")

    if meta.get("bloqueante"):
        lineas += [
            '!!! warning "Este nodo es bloqueante"',
            "",
            "    El resto del curso se apoya en lo que salga de aquí. Si te lo saltas,",
            "    los bloques 5 y 6 no van a poder demostrarte nada.",
            "",
        ]

    reqs = [r for r in meta.get("requisitos", []) if r in indice]
    if reqs:
        enlaces = ", ".join(f"[{indice[r]['titulo']}]({enlace(r, indice)})" for r in reqs)
        lineas += [f"**Antes de esto:** {enlaces}", ""]

    if meta.get("objetivos"):
        lineas += ["!!! abstract \"Al terminar sabrás\"", ""]
        lineas += [f"    - {o}" for o in meta["objetivos"]]
        lineas += [""]

    return "\n".join(lineas)


def pie(meta: dict, indice: dict) -> str:
    lineas = ["", "---", ""]

    if meta.get("profundizar"):
        lineas += ["## Si quieres más", "",
                   "Ramas opcionales. No hacen falta para seguir; están por si el tema te ha enganchado.", ""]
        for p in meta["profundizar"]:
            if p["id"] in indice:
                lineas.append(f"- [{p['titulo']}]({enlace(p['id'], indice)})")
        lineas.append("")

    sigs = [d for d in meta.get("desbloquea", []) if d in indice]
    if sigs:
        enlaces = " · ".join(f"[{indice[s]['titulo']}]({enlace(s, indice)})" for s in sigs)
        lineas += [f"**Siguiente:** {enlaces}", ""]

    if meta.get("conceptos"):
        cs = ", ".join(f"[{c}](../../glosario/README.md#{c})" for c in meta["conceptos"])
        lineas += [f'<span class="conceptos-nodo">Conceptos: {cs}</span>', ""]

    return "\n".join(lineas)


def enlace(nodo_id: str, indice: dict) -> str:
    """Ruta relativa entre nodos, desde un fichero de bloque-N/."""
    destino = indice[nodo_id]
    b = destino["bloque"]
    if destino["tipo"] == "profundizacion":
        return f"../bloque-{b}/profundizacion/{nodo_id}.md"
    return f"../bloque-{b}/{nodo_id}.md"


def marcador_pendiente(meta: dict) -> str:
    return "\n".join([
        f"# {meta['titulo']}", "",
        '!!! note "Todavía sin escribir, y es a propósito"', "",
        "    Este nodo está previsto y tiene su sitio en el curso, pero aún no tiene",
        "    contenido. La especificación del programa es explícita: los bloques 1 a 3",
        "    se escriben, se publican y **se pilotan** antes de escribir el 4, porque el",
        "    bloque 4 se diseña mucho mejor sabiendo dónde te atascaste de verdad.", "",
        "    Lo que se vaya viendo en el piloto es lo que va a escribir esto.", "",
        f"**Lo que va a cubrir:** {meta.get('brief', '—')}", "",
        f"*Duración prevista: {meta['duracion_min']} min.*", "",
    ])


def construir(verbose: bool = True) -> dict:
    registro = yaml.safe_load(REGISTRO.read_text(encoding="utf-8"))
    indice = {n["id"]: n for n in registro["nodos"]}

    if DESTINO.exists():
        shutil.rmtree(DESTINO)
    DESTINO.mkdir(parents=True)

    stats = {"escritos": 0, "pendientes": 0, "copiados": 0}

    for nodo in registro["nodos"]:
        b = nodo["bloque"]
        sub = "profundizacion/" if nodo["tipo"] == "profundizacion" else ""
        destino = DESTINO / f"bloque-{b}" / sub / f"{nodo['id']}.md"
        destino.parent.mkdir(parents=True, exist_ok=True)

        origen = CONTENIDO / f"bloque-{b}" / sub / f"{nodo['id']}.md"
        if origen.exists():
            meta, cuerpo = leer_frontmatter(origen)
            meta = {**nodo, **meta}
            destino.write_text(cabecera(meta, indice) + cuerpo + pie(meta, indice), encoding="utf-8")
            stats["escritos"] += 1
        else:
            destino.write_text(marcador_pendiente(nodo), encoding="utf-8")
            stats["pendientes"] += 1

    # Páginas sueltas que sí se publican, nombradas una a una.
    sueltas = [
        (CONTENIDO / "glosario" / "README.md", DESTINO / "glosario" / "README.md"),
        (RAIZ / "sitio" / "index-fuente.md", DESTINO / "index.md"),
    ]
    for plantilla in sorted((RAIZ / "plantillas").glob("*.md")):
        sueltas.append((plantilla, DESTINO / "plantillas" / plantilla.name))
    for ej in sorted((RAIZ / "ejercicios").rglob("*.md")):
        if "solucion" in ej.name.lower():
            continue  # las soluciones no se publican como página propia
        sueltas.append((ej, DESTINO / "ejercicios" / ej.relative_to(RAIZ / "ejercicios")))
    sueltas.append((RAIZ / "sitio" / "assets-fuente.css", DESTINO / "assets" / "curso.css"))
    tutor_js = RAIZ / "tutor" / "widget" / "tutor.js"
    if tutor_js.exists():
        sueltas.append((tutor_js, DESTINO / "assets" / "tutor.js"))

    for origen, destino in sueltas:
        if not origen.exists():
            continue
        if any(p in str(origen) for p in PROHIBIDO):
            raise SystemExit(f"ABORTADO: se intentaba publicar una ruta prohibida: {origen}")
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(origen, destino)
        stats["copiados"] += 1

    escribir_nav(registro, indice)

    if verbose:
        print(f"sitio/docs/ construido: {stats['escritos']} nodos escritos, "
              f"{stats['pendientes']} pendientes de piloto, {stats['copiados']} páginas sueltas")
    return stats


def escribir_nav(registro: dict, indice: dict) -> None:
    """El nav sale del registro, no de mkdocs.yml, para que no se desincronice."""
    nav = [{"Empezar aquí": "index.md"}]
    for bloque in sorted(registro["meta"]["bloques"]):
        info = registro["meta"]["bloques"][bloque]
        entradas = []
        for nodo in registro["nodos"]:
            if nodo["bloque"] != bloque or nodo["tipo"] == "profundizacion":
                continue
            entradas.append({nodo["titulo"]: f"bloque-{bloque}/{nodo['id']}.md"})
            hijos = [n for n in registro["nodos"]
                     if n["tipo"] == "profundizacion" and n.get("requisitos") == [nodo["id"]]]
            for h in hijos:
                entradas.append({f"↳ {h['titulo']}": f"bloque-{bloque}/profundizacion/{h['id']}.md"})
        if entradas:
            titulo = info["titulo"] if bloque == 0 else f"{bloque}. {info['titulo']}"
            nav.append({titulo: entradas})

    plantillas = sorted((RAIZ / "plantillas").glob("*.md"))
    if plantillas:
        nav.append({"Plantillas": [{p.stem.replace("-", " ").capitalize(): f"plantillas/{p.name}"} for p in plantillas]})
    nav.append({"Glosario": "glosario/README.md"})

    (RAIZ / "sitio" / "nav.yml").write_text(
        yaml.safe_dump({"nav": nav}, allow_unicode=True, sort_keys=False, width=120),
        encoding="utf-8",
    )


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Ensambla sitio/docs/ desde el contenido del repositorio.")
    p.add_argument("--json", action="store_true", help="salida en JSON")
    args = p.parse_args()
    stats = construir(verbose=not args.json)
    if args.json:
        print(json.dumps(stats, ensure_ascii=False))
