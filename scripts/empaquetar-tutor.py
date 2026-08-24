#!/usr/bin/env python3
"""Construye tutor/serverless/curso.json: lo único que el tutor llega a ver.

Este script es el guardarraíl 1 y el 3 implementados como arquitectura en vez de
como instrucción. La función serverless no tiene acceso al repositorio: solo carga
este paquete. Por tanto:

- Las soluciones de los ejercicios NO se le pueden escapar, porque no están dentro.
- `dataset/SOLUCIONES/` no se le puede escapar, porque no está dentro.
- No puede inventarse nodos que no existen, porque lleva el índice completo.

Lo que no se empaqueta no se puede filtrar. Es más barato de garantizar que
pedirle al modelo que se porte bien.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import centinelas  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
REGISTRO = RAIZ / "docs-internos" / "registro-de-nodos.yml"
CONTENIDO = RAIZ / "contenido"
GLOSARIO = CONTENIDO / "glosario" / "glosario.yml"
SALIDA = RAIZ / "tutor" / "serverless" / "curso.json"

# Si alguna de estas cadenas aparece en el paquete, el empaquetado falla.
# Es una comprobación de último recurso: la garantía real es no leer esos ficheros.
# Van por procedencia; las respuestas escritas a mano las caza `centinelas.py`.
CENTINELAS = ["dataset/SOLUCIONES", "verdades-escondidas", "taxonomia-real",
              "pedidos-fantasma", "cuentas-v4", "mapa-duplicados"]

# Campos del frontmatter que NO viajan al tutor.
CAMPOS_EXCLUIDOS = {"solucion", "brief", "fuente_spec"}


def separar_frontmatter(texto: str) -> tuple[dict, str]:
    if not texto.startswith("---"):
        return {}, texto
    fin = texto.find("\n---", 3)
    if fin == -1:
        return {}, texto
    return yaml.safe_load(texto[3:fin]) or {}, texto[fin + 4 :].lstrip("\n")


def main() -> int:
    registro = yaml.safe_load(REGISTRO.read_text(encoding="utf-8"))

    indice = []
    cuerpos = {}

    for nodo in registro["nodos"]:
        entrada = {
            "id": nodo["id"],
            "titulo": nodo["titulo"],
            "bloque": nodo["bloque"],
            "tipo": nodo["tipo"],
            "estado": nodo["estado"],
            "duracion_min": nodo["duracion_min"],
            "caduca": nodo["caduca"],
            "requisitos": nodo.get("requisitos", []),
            "desbloquea": nodo.get("desbloquea", []),
            "conceptos": nodo.get("conceptos", []),
            "tiene_solucion": bool(nodo.get("solucion")),
        }
        indice.append(entrada)

        sub = "profundizacion/" if nodo["tipo"] == "profundizacion" else ""
        fichero = CONTENIDO / f"bloque-{nodo['bloque']}" / sub / f"{nodo['id']}.md"
        if fichero.exists():
            meta, cuerpo = separar_frontmatter(fichero.read_text(encoding="utf-8"))
            cuerpos[nodo["id"]] = {
                "objetivos": meta.get("objetivos", []),
                "texto": cuerpo,
            }

    glosario = []
    if GLOSARIO.exists():
        g = yaml.safe_load(GLOSARIO.read_text(encoding="utf-8"))
        glosario = [
            {"slug": t["slug"], "termino": t["termino"],
             "definicion": " ".join(t["definicion"].split())}
            for t in g["terminos"]
        ]

    prompts = {}
    for p in sorted((RAIZ / "tutor" / "prompts").glob("*.md")):
        # Se quitan el H1 y las reglas horizontales de separación, y nada más.
        #
        # Cuidado aquí: la cita en bloque de la cabecera NO es documentación nuestra,
        # es la restricción dura del modo ("nunca da la solución de un ejercicio",
        # "señala, no reescribe"). Recortarla deja al modelo sin la única línea que
        # de verdad lo limita. Una versión anterior de este script la descartaba;
        # lo cazó tutor/serverless/pruebas/guardarrailes.test.mjs.
        lineas = []
        for linea in p.read_text(encoding="utf-8").splitlines():
            if linea.startswith("# ") or linea.strip() in {"---", "***", "___"}:
                continue
            lineas.append(linea)
        prompts[p.stem] = "\n".join(lineas).strip()

    paquete = {
        "curso": registro["meta"]["curso"],
        "bloques": registro["meta"]["bloques"],
        "raiz": registro["meta"]["raiz"],
        "indice": indice,
        "cuerpos": cuerpos,
        "glosario": glosario,
        "prompts": prompts,
        "modos": ["explicar-de-otra-forma", "socratico", "revisar-artefacto",
                  "mas-practica", "aplicar-a-mi-caso"],
        "modo_por_defecto": "socratico",
    }

    serializado = json.dumps(paquete, ensure_ascii=False, indent=1)

    fallos = [c for c in CENTINELAS if c in serializado]
    if fallos:
        print(f"ABORTADO: el paquete del tutor contiene {fallos}. "
              "Algo está filtrando soluciones al contexto del tutor.", file=sys.stderr)
        return 1

    # El tutor da tracción, no respuestas (§7). Si las respuestas están en su
    # contexto, tarde o temprano las suelta: la única defensa barata es que no
    # viajen dentro.
    filtraciones = centinelas.buscar(serializado, "curso.json")
    if filtraciones:
        print("ABORTADO: el paquete del tutor lleva dentro las verdades escondidas:",
              file=sys.stderr)
        for hallazgo in filtraciones:
            print(f"  - [{hallazgo.centinela.verdad}/{hallazgo.centinela.codigo}] "
                  f"{hallazgo.centinela.delata}: …{hallazgo.fragmento}…", file=sys.stderr)
        return 1

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(serializado, encoding="utf-8")

    escritos = len(cuerpos)
    print(f"tutor/serverless/curso.json: {len(indice)} nodos en el índice, "
          f"{escritos} con contenido, {len(glosario)} términos, {len(prompts)} prompts. "
          f"Sin soluciones.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
