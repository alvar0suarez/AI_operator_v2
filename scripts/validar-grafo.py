#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validar-grafo.py — validador del grafo de nodos del curso "CX + IA".

Implementa lo que exige ESPECIFICACION.md §8 ("script que verifica el grafo de
requisitos: sin ciclos, sin referencias rotas, todo nodo alcanzable") aplicando
literalmente el contrato de docs-internos/esquema-frontmatter.md.

Qué comprueba, en orden:

  1. Carga  docs-internos/registro-de-nodos.yml (registro canónico) y todos los
     .md de contenido/ que llevan frontmatter YAML.
  2. Esquema: campos obligatorios, tipos, enums, rangos, patrón del id y
     coherencia id ↔ bloque ↔ directorio.
  3. Grafo: sin ciclos (orden topológico; si falla imprime el ciclo concreto),
     sin referencias rotas, todo nodo alcanzable desde meta.raiz, reciprocidad
     requisitos ↔ desbloquea con la excepción de las ramas de profundización,
     orden de bloques y forma de las ramas.
  4. Divergencia registro ↔ ficheros .md.
  5. Lista `profundizar` derivada y exigida al fichero del padre.
  6. Slugs de `conceptos` contra contenido/glosario/glosario.yml.
  7. Fugas de dataset/SOLUCIONES/ fuera del campo `solucion`.

Uso:
    python3 scripts/validar-grafo.py [--json] [--estricto] [--repo RUTA]

Salida: 0 si no hay errores, 1 si los hay (con --estricto, los avisos también
cuentan como errores). Dependencias: PyYAML y biblioteca estándar. Python 3.11.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("Falta PyYAML: pip install PyYAML\n")
    raise SystemExit(2)


# ─────────────────────────────── Constantes del contrato ──────────────────────
# Fuente: docs-internos/esquema-frontmatter.md

TIPOS = {"concepto", "ejercicio", "caso", "artefacto", "profundizacion"}
CADUCIDADES = {"bajo", "medio", "alto"}
ESTADOS = {"escrito", "pendiente-piloto"}

DURACION_MIN = 5
DURACION_MAX = 90
OBJETIVOS_MIN = 1
OBJETIVOS_MAX = 4

PATRON_ID = re.compile(r"^b([0-6])-(m|p)(\d+)-([a-z0-9]+(?:-[a-z0-9]+)*)$")
PATRON_SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PATRON_SOLUCIONES = re.compile(r"SOLUCIONES/")

# Verbos prohibidos al abrir un objetivo: no son observables (guía de estilo).
VERBOS_NO_OBSERVABLES = {"conocer", "entender", "comprender", "saber", "aprender"}

# Campos admitidos según de dónde venga el nodo.
CAMPOS_COMUNES = {
    "id", "bloque", "titulo", "tipo", "duracion_min", "requisitos", "desbloquea",
    "caduca", "conceptos", "artefacto", "bloqueante", "dataset", "solucion",
}
CAMPOS_SOLO_FICHERO = {"objetivos", "profundizar"}
CAMPOS_SOLO_REGISTRO = {"estado", "brief", "fuente_spec"}

OBLIGATORIOS_FICHERO = {
    "id", "bloque", "titulo", "tipo", "duracion_min", "requisitos", "desbloquea",
    "caduca", "objetivos", "conceptos",
}
OBLIGATORIOS_REGISTRO = {
    "id", "bloque", "titulo", "tipo", "duracion_min", "requisitos", "desbloquea",
    "caduca", "conceptos", "estado",
}

# Campos del registro que no se publican y por tanto pueden nombrar SOLUCIONES.
CAMPOS_NO_PUBLICADOS = {"solucion", "brief", "fuente_spec", "estado"}

# Campos que se cruzan registro ↔ fichero .md (§ tarea 4).
CAMPOS_CRUZADOS = [
    "titulo", "tipo", "bloque", "duracion_min", "caduca",
    "requisitos", "desbloquea", "conceptos",
]

RUTA_REGISTRO = Path("docs-internos/registro-de-nodos.yml")
RUTA_CONTENIDO = Path("contenido")
RUTA_GLOSARIO = Path("contenido/glosario/glosario.yml")
RUTA_PLANTILLAS = Path("plantillas")
RUTA_DATASET = Path("dataset/ficheros")


# ─────────────────────────────── Modelo de datos ──────────────────────────────

class CargadorConLineas(yaml.SafeLoader):
    """SafeLoader que anota cada mapa con la línea (1-based) donde empieza."""


def _construir_mapa_con_linea(cargador, nodo_yaml, deep=False):
    mapa = yaml.SafeLoader.construct_mapping(cargador, nodo_yaml, deep=deep)
    mapa["__linea__"] = nodo_yaml.start_mark.line + 1
    return mapa


CargadorConLineas.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    lambda cargador, nodo_yaml: _construir_mapa_con_linea(cargador, nodo_yaml, deep=False),
)


def sin_marcas(valor):
    """Devuelve el valor sin las claves __linea__ que mete el cargador."""
    if isinstance(valor, dict):
        return {k: sin_marcas(v) for k, v in valor.items() if k != "__linea__"}
    if isinstance(valor, list):
        return [sin_marcas(v) for v in valor]
    return valor


@dataclass
class Nodo:
    """Un nodo tal y como lo declara una de las dos fuentes."""
    id: str
    datos: dict                      # frontmatter / entrada del registro, ya limpio
    origen: str                      # "registro" | "fichero"
    ruta: str                        # ruta relativa al repositorio
    linea: int                       # línea donde empieza el nodo
    lineas_campo: dict = field(default_factory=dict)
    cuerpo: list = field(default_factory=list)      # líneas del cuerpo (.md)
    linea_cuerpo: int = 0            # línea del fichero donde empieza el cuerpo

    def campo(self, nombre):
        return self.datos.get(nombre)

    def linea_de(self, nombre):
        """Línea del campo si se ha podido localizar; si no, la del nodo."""
        return self.lineas_campo.get(nombre, self.linea)

    @property
    def bloque(self):
        valor = self.datos.get("bloque")
        return valor if isinstance(valor, int) else -1

    @property
    def tipo(self):
        return self.datos.get("tipo")

    @property
    def es_profundizacion(self):
        return self.datos.get("tipo") == "profundizacion"

    def lista(self, nombre):
        """Lista de ids del campo, o [] si falta o no es lista."""
        valor = self.datos.get(nombre)
        return [v for v in valor if isinstance(v, str)] if isinstance(valor, list) else []


@dataclass
class Hallazgo:
    nivel: str                       # "error" | "aviso"
    codigo: str
    mensaje: str
    nodo: str = ""
    ruta: str = ""
    linea: int = 0

    def como_dict(self):
        d = {"nivel": self.nivel, "codigo": self.codigo, "mensaje": self.mensaje}
        if self.nodo:
            d["nodo"] = self.nodo
        if self.ruta:
            d["ruta"] = self.ruta
        if self.linea:
            d["linea"] = self.linea
        return d

    @property
    def ubicacion(self):
        if self.ruta and self.linea:
            return f"{self.ruta}:{self.linea}"
        return self.ruta or ""


class Informe:
    """Acumula hallazgos y los rinde para humanos o para máquina."""

    def __init__(self):
        self.hallazgos: list[Hallazgo] = []
        self.resumen: dict = {}

    def error(self, codigo, mensaje, nodo="", ruta="", linea=0):
        self.hallazgos.append(Hallazgo("error", codigo, mensaje, nodo, ruta, linea))

    def aviso(self, codigo, mensaje, nodo="", ruta="", linea=0):
        self.hallazgos.append(Hallazgo("aviso", codigo, mensaje, nodo, ruta, linea))

    @property
    def errores(self):
        return [h for h in self.hallazgos if h.nivel == "error"]

    @property
    def avisos(self):
        return [h for h in self.hallazgos if h.nivel == "aviso"]


# ─────────────────────────────── Carga de fuentes ─────────────────────────────

def localizar_lineas_de_campos(lineas, inicio, fin):
    """Mapea nombre_de_campo → línea, mirando el texto crudo del bloque del nodo.

    `inicio` y `fin` son líneas 1-based, `fin` incluido. Solo mira el primer
    nivel de indentación del nodo, para no confundirse con los campos anidados.
    """
    encontrados = {}
    patron = re.compile(r"^\s*-?\s*([a-z_][a-z0-9_]*)\s*:")
    sangria_base = None
    for numero in range(inicio, min(fin, len(lineas)) + 1):
        linea = lineas[numero - 1]
        if not linea.strip() or linea.lstrip().startswith("#"):
            continue
        coincidencia = patron.match(linea)
        if not coincidencia:
            continue
        sangria = len(linea) - len(linea.lstrip())
        if linea.lstrip().startswith("- "):
            sangria += 2
        if sangria_base is None:
            sangria_base = sangria
        if sangria == sangria_base:
            encontrados.setdefault(coincidencia.group(1), numero)
    return encontrados


def cargar_registro(raiz, informe):
    """Devuelve (meta, {id: Nodo}). Aborta con excepción si el YAML no parsea."""
    ruta_abs = raiz / RUTA_REGISTRO
    ruta_rel = str(RUTA_REGISTRO)
    if not ruta_abs.is_file():
        informe.error("registro-ausente", f"no existe {ruta_rel}", ruta=ruta_rel)
        return {}, {}

    texto = ruta_abs.read_text(encoding="utf-8")
    lineas = texto.splitlines()
    try:
        crudo = yaml.load(texto, Loader=CargadorConLineas)
    except yaml.YAMLError as exc:
        informe.error("registro-ilegible", f"YAML inválido: {exc}", ruta=ruta_rel)
        return {}, {}

    if not isinstance(crudo, dict):
        informe.error("registro-ilegible", "la raíz del registro no es un mapa", ruta=ruta_rel)
        return {}, {}

    meta = sin_marcas(crudo.get("meta") or {})
    entradas = crudo.get("nodos")
    if not isinstance(entradas, list):
        informe.error("registro-ilegible", "el registro no trae lista `nodos`", ruta=ruta_rel)
        return meta, {}

    # Rango de líneas de cada entrada, para poder señalar campo a campo.
    inicios = [e.get("__linea__", 0) if isinstance(e, dict) else 0 for e in entradas]
    nodos = {}
    for indice, entrada in enumerate(entradas):
        if not isinstance(entrada, dict):
            informe.error("registro-entrada-invalida",
                          f"la entrada {indice + 1} de `nodos` no es un mapa", ruta=ruta_rel)
            continue
        inicio = inicios[indice] or 1
        fin = (inicios[indice + 1] - 1) if indice + 1 < len(inicios) and inicios[indice + 1] else len(lineas)
        datos = sin_marcas(entrada)
        identificador = datos.get("id")
        if not isinstance(identificador, str) or not identificador:
            informe.error("nodo-sin-id",
                          f"entrada {indice + 1} del registro sin campo `id` utilizable",
                          ruta=ruta_rel, linea=inicio)
            continue
        if identificador in nodos:
            informe.error("id-duplicado",
                          f"`{identificador}` aparece dos veces en el registro "
                          f"(la primera en la línea {nodos[identificador].linea})",
                          nodo=identificador, ruta=ruta_rel, linea=inicio)
            continue
        nodos[identificador] = Nodo(
            id=identificador, datos=datos, origen="registro", ruta=ruta_rel,
            linea=inicio, lineas_campo=localizar_lineas_de_campos(lineas, inicio, fin),
        )
    return meta, nodos


def cargar_ficheros(raiz, informe):
    """Lee todos los .md de contenido/ con frontmatter. Devuelve {id: Nodo}."""
    directorio = raiz / RUTA_CONTENIDO
    nodos = {}
    if not directorio.is_dir():
        informe.error("contenido-ausente", f"no existe el directorio {RUTA_CONTENIDO}/",
                      ruta=str(RUTA_CONTENIDO))
        return nodos

    for ruta_abs in sorted(directorio.rglob("*.md")):
        ruta_rel = str(ruta_abs.relative_to(raiz))
        lineas = ruta_abs.read_text(encoding="utf-8").splitlines()
        if not lineas or lineas[0].strip() != "---":
            if ruta_abs.name.lower() not in {"readme.md", "index.md"}:
                informe.aviso("md-sin-frontmatter",
                              "fichero .md en contenido/ sin frontmatter: se ignora",
                              ruta=ruta_rel, linea=1)
            continue

        cierre = next((i for i in range(1, len(lineas))
                       if lineas[i].strip() in {"---", "..."}), None)
        if cierre is None:
            informe.error("frontmatter-sin-cierre",
                          "el frontmatter abre con --- y no cierra", ruta=ruta_rel, linea=1)
            continue

        try:
            datos = yaml.load("\n".join(lineas[1:cierre]), Loader=CargadorConLineas)
        except yaml.YAMLError as exc:
            linea = getattr(getattr(exc, "problem_mark", None), "line", 0) + 2
            informe.error("frontmatter-ilegible", f"YAML inválido: {exc}",
                          ruta=ruta_rel, linea=linea)
            continue

        if not isinstance(datos, dict):
            informe.error("frontmatter-ilegible", "el frontmatter no es un mapa",
                          ruta=ruta_rel, linea=1)
            continue

        datos = sin_marcas(datos)
        identificador = datos.get("id")
        if not isinstance(identificador, str) or not identificador:
            informe.error("nodo-sin-id", "frontmatter sin campo `id` utilizable",
                          ruta=ruta_rel, linea=2)
            continue
        if identificador in nodos:
            informe.error("id-duplicado",
                          f"`{identificador}` ya lo declara {nodos[identificador].ruta}",
                          nodo=identificador, ruta=ruta_rel, linea=2)
            continue

        nodos[identificador] = Nodo(
            id=identificador, datos=datos, origen="fichero", ruta=ruta_rel, linea=2,
            lineas_campo=localizar_lineas_de_campos(lineas, 2, cierre),
            cuerpo=lineas[cierre + 1:], linea_cuerpo=cierre + 2,
        )
    return nodos


def cargar_glosario(raiz, informe):
    """Devuelve el conjunto de slugs del glosario, o None si aún no existe."""
    ruta_abs = raiz / RUTA_GLOSARIO
    ruta_rel = str(RUTA_GLOSARIO)
    if not ruta_abs.is_file():
        return None
    try:
        crudo = yaml.safe_load(ruta_abs.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        informe.error("glosario-ilegible", f"YAML inválido: {exc}", ruta=ruta_rel)
        return set()

    # Se admiten tres formas: mapa slug→definición, mapa con `terminos`/`entradas`,
    # o lista de slugs / de mapas con clave `slug`, `id` o `termino`.
    if isinstance(crudo, dict):
        for clave in ("terminos", "entradas", "glosario"):
            if clave in crudo:
                crudo = crudo[clave]
                break
    slugs = set()
    if isinstance(crudo, dict):
        slugs = {k for k in crudo if isinstance(k, str)}
    elif isinstance(crudo, list):
        for elemento in crudo:
            if isinstance(elemento, str):
                slugs.add(elemento)
            elif isinstance(elemento, dict):
                for clave in ("slug", "id", "termino", "concepto"):
                    if isinstance(elemento.get(clave), str):
                        slugs.add(elemento[clave])
                        break
    else:
        informe.error("glosario-ilegible", "estructura no reconocida", ruta=ruta_rel)
    return slugs


# ─────────────────────────── 2. Validación del esquema ────────────────────────

def ruta_esperada(nodo_id, bloque, tipo):
    """Dónde debe vivir el .md de un nodo, según el árbol de ESPECIFICACION.md §8."""
    base = RUTA_CONTENIDO / f"bloque-{bloque}"
    if tipo == "profundizacion":
        base = base / "profundizacion"
    return str(base / f"{nodo_id}.md")


def validar_esquema(nodo, meta, informe):
    """Aplica docs-internos/esquema-frontmatter.md campo a campo a un nodo."""
    datos = nodo.datos
    ruta = nodo.ruta
    esperados = CAMPOS_COMUNES | (
        CAMPOS_SOLO_FICHERO if nodo.origen == "fichero" else CAMPOS_SOLO_REGISTRO)
    obligatorios = OBLIGATORIOS_FICHERO if nodo.origen == "fichero" else OBLIGATORIOS_REGISTRO

    def err(codigo, mensaje, campo=None):
        informe.error(codigo, mensaje, nodo=nodo.id, ruta=ruta,
                      linea=nodo.linea_de(campo) if campo else nodo.linea)

    def avi(codigo, mensaje, campo=None):
        informe.aviso(codigo, mensaje, nodo=nodo.id, ruta=ruta,
                      linea=nodo.linea_de(campo) if campo else nodo.linea)

    for campo in sorted(obligatorios - set(datos)):
        err("campo-obligatorio-ausente", f"falta el campo obligatorio `{campo}`")
    for campo in sorted(set(datos) - esperados):
        avi("campo-desconocido", f"campo `{campo}` no previsto en el esquema", campo)

    # id: patrón, y la letra m/p coherente con el tipo.
    coincidencia = PATRON_ID.match(nodo.id)
    if not coincidencia:
        err("id-mal-formado",
            f"`{nodo.id}` no cumple el patrón b<bloque>-(m|p)<n>-<slug-kebab-sin-acentos>", "id")
    bloque_del_id = int(coincidencia.group(1)) if coincidencia else None
    letra = coincidencia.group(2) if coincidencia else None

    # tipo
    tipo = datos.get("tipo")
    if "tipo" in datos and tipo not in TIPOS:
        err("tipo-invalido",
            f"tipo `{tipo}`; se admite {' | '.join(sorted(TIPOS))}", "tipo")
    if letra and tipo in TIPOS:
        if letra == "p" and tipo != "profundizacion":
            err("id-tipo-incoherente",
                f"el id usa `p` (rama de profundización) pero el tipo es `{tipo}`", "id")
        if letra == "m" and tipo == "profundizacion":
            err("id-tipo-incoherente",
                "el tipo es `profundizacion` pero el id usa `m` (tronco)", "id")

    # bloque
    bloque = datos.get("bloque")
    if "bloque" in datos:
        if not isinstance(bloque, int) or isinstance(bloque, bool) or not 0 <= bloque <= 6:
            err("bloque-invalido", f"bloque `{bloque}`; se espera un entero 0–6", "bloque")
        else:
            if bloque_del_id is not None and bloque != bloque_del_id:
                err("bloque-incoherente",
                    f"bloque {bloque} pero el id dice b{bloque_del_id}", "bloque")
            bloques_meta = meta.get("bloques") or {}
            if bloques_meta and bloque not in bloques_meta:
                err("bloque-desconocido",
                    f"el bloque {bloque} no está declarado en meta.bloques", "bloque")

    # titulo
    titulo = datos.get("titulo")
    if "titulo" in datos and (not isinstance(titulo, str) or not titulo.strip()):
        err("titulo-invalido", "`titulo` debe ser una cadena no vacía", "titulo")

    # duracion_min
    duracion = datos.get("duracion_min")
    if "duracion_min" in datos:
        if not isinstance(duracion, int) or isinstance(duracion, bool):
            err("duracion-invalida", f"`duracion_min` debe ser entero, no {type(duracion).__name__}",
                "duracion_min")
        elif not DURACION_MIN <= duracion <= DURACION_MAX:
            err("duracion-fuera-de-rango",
                f"duracion_min {duracion}; el rango del esquema es {DURACION_MIN}–{DURACION_MAX}",
                "duracion_min")

    # caduca
    caduca = datos.get("caduca")
    if "caduca" in datos and caduca not in CADUCIDADES:
        err("caduca-invalida", f"caduca `{caduca}`; se admite bajo | medio | alto", "caduca")

    # estado (solo registro)
    if nodo.origen == "registro":
        estado = datos.get("estado")
        if "estado" in datos and estado not in ESTADOS:
            err("estado-invalido",
                f"estado `{estado}`; se admite {' | '.join(sorted(ESTADOS))}", "estado")

    # requisitos y desbloquea: listas de ids, sin repetidos ni autorreferencia
    for campo in ("requisitos", "desbloquea"):
        valor = datos.get(campo)
        if campo not in datos:
            continue
        if not isinstance(valor, list) or not all(isinstance(v, str) for v in valor):
            err("lista-invalida", f"`{campo}` debe ser una lista de ids", campo)
            continue
        if len(set(valor)) != len(valor):
            err("lista-con-repetidos", f"`{campo}` repite ids", campo)
        if nodo.id in valor:
            err("autorreferencia", f"`{campo}` se apunta a sí mismo", campo)
    if datos.get("requisitos") == [] and nodo.id != (meta.get("raiz") or "b0-m1"):
        err("requisitos-vacios",
            "solo la raíz del curso puede tener `requisitos: []`", "requisitos")

    # conceptos: slugs kebab-case
    conceptos = datos.get("conceptos")
    if "conceptos" in datos:
        if not isinstance(conceptos, list) or not all(isinstance(c, str) for c in conceptos):
            err("lista-invalida", "`conceptos` debe ser una lista de slugs", "conceptos")
        else:
            if not conceptos:
                err("conceptos-vacios", "`conceptos` no puede estar vacío", "conceptos")
            if len(set(conceptos)) != len(conceptos):
                err("lista-con-repetidos", "`conceptos` repite slugs", "conceptos")
            for slug in conceptos:
                if not PATRON_SLUG.match(slug):
                    err("slug-mal-formado",
                        f"concepto `{slug}`: se espera kebab-case sin acentos", "conceptos")

    # objetivos (solo fichero): 1–4, verbo observable en infinitivo
    if nodo.origen == "fichero" and "objetivos" in datos:
        objetivos = datos.get("objetivos")
        if not isinstance(objetivos, list) or not all(isinstance(o, str) for o in objetivos):
            err("lista-invalida", "`objetivos` debe ser una lista de cadenas", "objetivos")
        else:
            if not OBJETIVOS_MIN <= len(objetivos) <= OBJETIVOS_MAX:
                err("objetivos-fuera-de-rango",
                    f"{len(objetivos)} objetivos; el esquema pide entre "
                    f"{OBJETIVOS_MIN} y {OBJETIVOS_MAX}", "objetivos")
            for objetivo in objetivos:
                primera = objetivo.strip().split(" ")[0].lower().strip('"“”')
                if primera in VERBOS_NO_OBSERVABLES:
                    err("objetivo-no-observable",
                        f"«{objetivo}»: `{primera}` no es un verbo observable", "objetivos")
                elif primera and not primera.endswith(("ar", "er", "ir", "se", "lo", "la", "las", "los")):
                    avi("objetivo-sin-infinitivo",
                        f"«{objetivo}»: se espera empezar por verbo en infinitivo", "objetivos")

    # bloqueante
    if "bloqueante" in datos and not isinstance(datos["bloqueante"], bool):
        err("bloqueante-invalido", "`bloqueante` debe ser booleano", "bloqueante")

    # artefacto: obligatorio si tipo == artefacto; puede aparecer en otros tipos
    # que entregan plantilla (p. ej. el diario del bloque 1), pero siempre bajo /plantillas.
    artefacto = datos.get("artefacto")
    if tipo == "artefacto" and "artefacto" not in datos:
        err("artefacto-ausente", "un nodo `tipo: artefacto` debe declarar `artefacto`")
    if "artefacto" in datos:
        if not isinstance(artefacto, str) or not artefacto.strip():
            err("artefacto-invalido", "`artefacto` debe ser una ruta", "artefacto")
        elif not artefacto.startswith(f"{RUTA_PLANTILLAS}/"):
            avi("artefacto-fuera-de-plantillas",
                f"`{artefacto}` debería colgar de {RUTA_PLANTILLAS}/", "artefacto")

    # dataset
    if "dataset" in datos:
        valor = datos["dataset"]
        if not isinstance(valor, list) or not all(isinstance(v, str) for v in valor):
            err("lista-invalida", "`dataset` debe ser una lista de rutas", "dataset")
        else:
            for referencia in valor:
                if not referencia.startswith(f"{RUTA_DATASET}/"):
                    avi("dataset-fuera-de-ficheros",
                        f"`{referencia}` debería colgar de {RUTA_DATASET}/", "dataset")

    # solucion
    if "solucion" in datos and not isinstance(datos["solucion"], str):
        err("solucion-invalida", "`solucion` debe ser una ruta", "solucion")

    # profundizar (solo fichero): lista de {id, titulo}
    if nodo.origen == "fichero" and "profundizar" in datos:
        valor = datos["profundizar"]
        if not isinstance(valor, list):
            err("profundizar-invalido", "`profundizar` debe ser una lista de {id, titulo}",
                "profundizar")
        else:
            for elemento in valor:
                if not isinstance(elemento, dict) or "id" not in elemento or "titulo" not in elemento:
                    err("profundizar-invalido",
                        f"entrada de `profundizar` sin `id` y `titulo`: {elemento!r}", "profundizar")

    # Coherencia id ↔ bloque ↔ directorio (solo tiene sentido en ficheros)
    if nodo.origen == "fichero" and isinstance(bloque, int) and tipo in TIPOS:
        esperada = ruta_esperada(nodo.id, bloque, tipo)
        directorio_esperado = str(Path(esperada).parent)
        directorio_real = str(Path(nodo.ruta).parent)
        if directorio_real != directorio_esperado:
            err("directorio-incoherente",
                f"el nodo vive en {directorio_real}/ y por bloque/tipo le toca "
                f"{directorio_esperado}/")
        elif nodo.ruta != esperada:
            avi("nombre-de-fichero",
                f"por convención el fichero debería llamarse {Path(esperada).name}")


# ─────────────────────────── 3. Validación del grafo ──────────────────────────

def derivar_profundizar(nodos):
    """padre → [ids de sus ramas], a partir del requisito único de cada rama."""
    ramas = {}
    for nodo in nodos.values():
        if not nodo.es_profundizacion:
            continue
        requisitos = nodo.lista("requisitos")
        if len(requisitos) == 1:
            ramas.setdefault(requisitos[0], []).append(nodo.id)
    return ramas


def buscar_ciclo(aristas, ids):
    """Devuelve un ciclo concreto [a, b, ..., a] o None."""
    estado = {}
    pila = []

    def visitar(actual):
        estado[actual] = 1
        pila.append(actual)
        for siguiente in aristas.get(actual, []):
            if estado.get(siguiente, 0) == 1:
                return pila[pila.index(siguiente):] + [siguiente]
            if estado.get(siguiente, 0) == 0:
                ciclo = visitar(siguiente)
                if ciclo:
                    return ciclo
        pila.pop()
        estado[actual] = 2
        return None

    for identificador in ids:
        if estado.get(identificador, 0) == 0:
            ciclo = visitar(identificador)
            if ciclo:
                return ciclo
    return None


def validar_grafo(nodos, meta, ramas, informe, resumen):
    """Referencias, ciclos, alcanzabilidad, reciprocidad y forma de las ramas."""
    ids = set(nodos)

    # 3.1 Referencias rotas en requisitos / desbloquea / profundizar.
    for nodo in nodos.values():
        for campo in ("requisitos", "desbloquea"):
            for referencia in nodo.lista(campo):
                if referencia not in ids:
                    informe.error("referencia-rota",
                                  f"`{campo}` apunta a `{referencia}`, que no existe",
                                  nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de(campo))
        for elemento in (nodo.datos.get("profundizar") or []):
            if isinstance(elemento, dict) and isinstance(elemento.get("id"), str):
                if elemento["id"] not in ids:
                    informe.error("referencia-rota",
                                  f"`profundizar` apunta a `{elemento['id']}`, que no existe",
                                  nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de("profundizar"))
                elif not nodos[elemento["id"]].es_profundizacion:
                    informe.error("profundizar-a-tronco",
                                  f"`profundizar` apunta a `{elemento['id']}`, que no es "
                                  f"tipo profundizacion",
                                  nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de("profundizar"))

    # 3.2 Ciclos: se topologiza el grafo con todas las aristas conocidas.
    aristas = {i: set() for i in ids}
    for nodo in nodos.values():
        for requisito in nodo.lista("requisitos"):
            if requisito in ids:
                aristas[requisito].add(nodo.id)
        for siguiente in nodo.lista("desbloquea"):
            if siguiente in ids:
                aristas[nodo.id].add(siguiente)
    for padre, hijos in ramas.items():
        if padre in ids:
            aristas[padre].update(h for h in hijos if h in ids)
    aristas = {k: sorted(v) for k, v in aristas.items()}
    resumen["aristas"] = sum(len(v) for v in aristas.values())

    grados = {i: 0 for i in ids}
    for origen, destinos in aristas.items():
        for destino in destinos:
            grados[destino] += 1
    cola = sorted(i for i in ids if grados[i] == 0)
    orden = []
    while cola:
        actual = cola.pop(0)
        orden.append(actual)
        for destino in aristas[actual]:
            grados[destino] -= 1
            if grados[destino] == 0:
                cola.append(destino)
                cola.sort()
    resumen["orden_topologico"] = len(orden) == len(ids)
    if len(orden) != len(ids):
        ciclo = buscar_ciclo(aristas, sorted(ids - set(orden)))
        if ciclo:
            informe.error("ciclo",
                          "ciclo en el grafo de requisitos: " + " → ".join(ciclo),
                          nodo=ciclo[0], ruta=nodos[ciclo[0]].ruta, linea=nodos[ciclo[0]].linea)
        else:
            informe.error("ciclo",
                          "el orden topológico no cierra; nodos implicados: "
                          + ", ".join(sorted(ids - set(orden))))

    # 3.3 Alcanzabilidad desde meta.raiz siguiendo desbloquea + profundizar.
    raiz = meta.get("raiz")
    if not raiz:
        informe.error("raiz-ausente", "meta.raiz no está declarada en el registro",
                      ruta=str(RUTA_REGISTRO))
    elif raiz not in ids:
        informe.error("raiz-inexistente", f"meta.raiz apunta a `{raiz}`, que no existe",
                      ruta=str(RUTA_REGISTRO))
    else:
        alcanzados = set()
        pendientes = [raiz]
        while pendientes:
            actual = pendientes.pop()
            if actual in alcanzados:
                continue
            alcanzados.add(actual)
            siguientes = [s for s in nodos[actual].lista("desbloquea") if s in ids]
            siguientes += [h for h in ramas.get(actual, []) if h in ids]
            pendientes.extend(siguientes)
        resumen["alcanzables"] = len(alcanzados)
        for identificador in sorted(ids - alcanzados):
            nodo = nodos[identificador]
            informe.error("nodo-inalcanzable",
                          f"no se llega a `{identificador}` desde `{raiz}` siguiendo "
                          f"desbloquea + profundizar",
                          nodo=identificador, ruta=nodo.ruta, linea=nodo.linea)

    # 3.4 Reciprocidad, orden de bloques y ramas de profundización.
    cruzados = 0
    for nodo in nodos.values():
        # Aristas salientes declaradas: A.desbloquea → B exige A ∈ B.requisitos.
        for destino in nodo.lista("desbloquea"):
            if destino not in ids:
                continue
            otro = nodos[destino]
            if otro.es_profundizacion:
                informe.error("desbloquea-a-profundizacion",
                              f"`{destino}` es una rama de profundización: el padre no la "
                              f"lista en `desbloquea`, la lista en `profundizar`",
                              nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de("desbloquea"))
                continue
            if nodo.id not in otro.lista("requisitos"):
                informe.error("reciprocidad-rota",
                              f"`{nodo.id}` declara desbloquea:[{destino}] pero `{destino}` "
                              f"no lo lista en `requisitos`",
                              nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de("desbloquea"))
            if otro.bloque >= 0 and nodo.bloque >= 0 and otro.bloque < nodo.bloque:
                informe.error("desbloquea-hacia-atras",
                              f"`{nodo.id}` (bloque {nodo.bloque}) desbloquea `{destino}` "
                              f"(bloque {otro.bloque}): el tronco no va hacia atrás",
                              nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de("desbloquea"))

        # Aristas entrantes declaradas: B.requisitos → A.
        if nodo.es_profundizacion:
            continue  # el par padre ↔ rama tiene su propia regla (3.5)
        for requisito in nodo.lista("requisitos"):
            if requisito not in ids:
                continue
            otro = nodos[requisito]
            if otro.es_profundizacion:
                informe.error("tronco-requiere-profundizacion",
                              f"`{nodo.id}` es tronco y exige la rama `{requisito}`: "
                              f"una profundización nunca bloquea el tronco",
                              nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de("requisitos"))
                continue
            if otro.bloque > nodo.bloque >= 0:
                informe.error("requisito-de-bloque-posterior",
                              f"`{nodo.id}` (bloque {nodo.bloque}) exige `{requisito}` "
                              f"(bloque {otro.bloque})",
                              nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de("requisitos"))
                continue
            if nodo.id in otro.lista("desbloquea"):
                continue
            if otro.bloque == nodo.bloque:
                informe.error("reciprocidad-rota",
                              f"`{nodo.id}` exige `{requisito}` (mismo bloque) pero "
                              f"`{requisito}` no lo lista en `desbloquea`",
                              nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de("requisitos"))
            else:
                # Requisito cruzado a un bloque anterior: legítimo (ESPECIFICACION.md §6,
                # ejemplo b3-m4-sabotaje ← b2-*-clasificar). `desbloquea` marca el paso
                # siguiente del tronco y no debe apuntar a otro bloque.
                cruzados += 1
    resumen["requisitos_cruzados"] = cruzados

    # 3.5 Forma de las ramas de profundización.
    for nodo in nodos.values():
        if not nodo.es_profundizacion:
            continue
        requisitos = nodo.lista("requisitos")
        if len(requisitos) != 1:
            informe.error("rama-sin-padre-unico",
                          f"una profundización cuelga de exactamente un padre; "
                          f"`{nodo.id}` declara {len(requisitos)} requisitos",
                          nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de("requisitos"))
        elif requisitos[0] in ids and nodos[requisitos[0]].es_profundizacion:
            informe.error("rama-cuelga-de-rama",
                          f"`{nodo.id}` cuelga de `{requisitos[0]}`, que también es una rama",
                          nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de("requisitos"))
        if nodo.lista("desbloquea"):
            informe.error("rama-con-desbloquea",
                          f"`{nodo.id}` es una rama opcional: `desbloquea` debe estar vacío",
                          nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de("desbloquea"))


# ───────────────── 4 y 5. Divergencia registro ↔ ficheros, profundizar ────────

def validar_divergencia(registro, ficheros, informe):
    """El registro es canónico: los .md no pueden decir otra cosa."""
    for identificador in sorted(set(registro) | set(ficheros)):
        en_registro = registro.get(identificador)
        en_fichero = ficheros.get(identificador)

        if en_registro and not en_fichero:
            estado = en_registro.datos.get("estado")
            destino = ruta_esperada(identificador, en_registro.bloque, en_registro.tipo)
            if estado == "pendiente-piloto":
                informe.aviso("nodo-pendiente-sin-fichero",
                              f"pendiente de piloto: aún no existe {destino}",
                              nodo=identificador, ruta=en_registro.ruta, linea=en_registro.linea)
            else:
                informe.error("nodo-sin-fichero",
                              f"estado `{estado}` pero no existe {destino}",
                              nodo=identificador, ruta=en_registro.ruta, linea=en_registro.linea)
            continue

        if en_fichero and not en_registro:
            informe.error("nodo-no-registrado",
                          "el nodo no está en docs-internos/registro-de-nodos.yml "
                          "(el registro es la fuente de verdad: primero ahí, después el fichero)",
                          nodo=identificador, ruta=en_fichero.ruta, linea=en_fichero.linea)
            continue

        for campo in CAMPOS_CRUZADOS:
            valor_registro = en_registro.datos.get(campo)
            valor_fichero = en_fichero.datos.get(campo)
            if valor_registro == valor_fichero:
                continue
            if (isinstance(valor_registro, list) and isinstance(valor_fichero, list)
                    and set(valor_registro) == set(valor_fichero)):
                informe.aviso("orden-divergente",
                              f"`{campo}` tiene los mismos elementos en distinto orden "
                              f"que el registro",
                              nodo=identificador, ruta=en_fichero.ruta,
                              linea=en_fichero.linea_de(campo))
                continue
            informe.error("divergencia",
                          f"`{campo}`: el fichero dice {valor_fichero!r} y el registro "
                          f"{valor_registro!r} ({en_registro.ruta}:{en_registro.linea_de(campo)})",
                          nodo=identificador, ruta=en_fichero.ruta,
                          linea=en_fichero.linea_de(campo))


def validar_profundizar_derivado(ficheros, ramas, nodos, informe):
    """El .md del padre debe declarar exactamente las ramas que le cuelgan."""
    for identificador, nodo in ficheros.items():
        esperadas = sorted(ramas.get(identificador, []))
        declaradas = []
        for elemento in (nodo.datos.get("profundizar") or []):
            if isinstance(elemento, dict) and isinstance(elemento.get("id"), str):
                declaradas.append(elemento["id"])

        for sobrante in sorted(set(declaradas) - set(esperadas)):
            informe.error("profundizar-sobrante",
                          f"`profundizar` lista `{sobrante}`, que no declara "
                          f"`requisitos: [{identificador}]`",
                          nodo=identificador, ruta=nodo.ruta, linea=nodo.linea_de("profundizar"))
        for ausente in sorted(set(esperadas) - set(declaradas)):
            informe.error("profundizar-ausente",
                          f"`{ausente}` cuelga de este nodo pero no aparece en `profundizar`",
                          nodo=identificador, ruta=nodo.ruta,
                          linea=nodo.linea_de("profundizar") if "profundizar" in nodo.datos else nodo.linea)
        if len(set(declaradas)) != len(declaradas):
            informe.error("profundizar-repetido", "`profundizar` repite ids",
                          nodo=identificador, ruta=nodo.ruta, linea=nodo.linea_de("profundizar"))

        # El título de cada rama debe ser el mismo que el de la rama.
        for elemento in (nodo.datos.get("profundizar") or []):
            if not isinstance(elemento, dict):
                continue
            rama = nodos.get(elemento.get("id"))
            if rama is None:
                continue
            if elemento.get("titulo") != rama.datos.get("titulo"):
                informe.error("profundizar-titulo-divergente",
                              f"`profundizar` llama a `{rama.id}` "
                              f"{elemento.get('titulo')!r} y su título es "
                              f"{rama.datos.get('titulo')!r}",
                              nodo=identificador, ruta=nodo.ruta,
                              linea=nodo.linea_de("profundizar"))


# ───────────────────── 6 y 7. Glosario y fugas de SOLUCIONES ──────────────────

def validar_conceptos(nodos, glosario, informe, resumen):
    usados = sorted({c for n in nodos.values() for c in (n.datos.get("conceptos") or [])
                     if isinstance(c, str)})
    resumen["conceptos_usados"] = len(usados)
    if glosario is None:
        informe.aviso("glosario-ausente",
                      f"no existe {RUTA_GLOSARIO}: no se han podido comprobar "
                      f"{len(usados)} slugs de `conceptos`",
                      ruta=str(RUTA_GLOSARIO))
        return
    resumen["conceptos_en_glosario"] = len(glosario)
    for nodo in nodos.values():
        for slug in (nodo.datos.get("conceptos") or []):
            if isinstance(slug, str) and slug not in glosario:
                informe.error("concepto-fuera-del-glosario",
                              f"el concepto `{slug}` no existe en {RUTA_GLOSARIO}",
                              nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de("conceptos"))
    huerfanos = sorted(glosario - set(usados))
    if huerfanos:
        informe.aviso("glosario-con-terminos-sin-uso",
                      f"{len(huerfanos)} términos del glosario no los usa ningún nodo: "
                      + ", ".join(huerfanos[:8]) + ("…" if len(huerfanos) > 8 else ""),
                      ruta=str(RUTA_GLOSARIO))


def validar_fugas_de_soluciones(nodos, informe):
    """Nada publicado puede apuntar a dataset/SOLUCIONES/ salvo el campo `solucion`."""
    def apunta(valor):
        if isinstance(valor, str):
            return bool(PATRON_SOLUCIONES.search(valor))
        if isinstance(valor, list):
            return any(apunta(v) for v in valor)
        if isinstance(valor, dict):
            return any(apunta(v) for v in valor.values())
        return False

    for nodo in nodos.values():
        for campo, valor in nodo.datos.items():
            if campo in CAMPOS_NO_PUBLICADOS:
                continue
            if apunta(valor):
                informe.error("fuga-de-soluciones",
                              f"el campo `{campo}` referencia SOLUCIONES/; solo el campo "
                              f"`solucion` puede hacerlo (nunca se publica)",
                              nodo=nodo.id, ruta=nodo.ruta, linea=nodo.linea_de(campo))
        for desplazamiento, linea in enumerate(nodo.cuerpo):
            if PATRON_SOLUCIONES.search(linea):
                informe.error("fuga-de-soluciones",
                              "el cuerpo del nodo referencia SOLUCIONES/: eso no se publica",
                              nodo=nodo.id, ruta=nodo.ruta,
                              linea=nodo.linea_cuerpo + desplazamiento)


def validar_rutas_referenciadas(registro, ficheros, raiz, informe):
    """Rutas de `artefacto`, `dataset` y `solucion` de los nodos ya publicados.

    Solo se comprueban los nodos que tienen .md: un nodo todavía sin escribir puede
    apuntar a una plantilla o a un fichero del dataset que generan fases posteriores
    (ESPECIFICACION.md §8, fases de construcción).
    """
    for identificador, nodo in ficheros.items():
        fuentes = [nodo]
        if identificador in registro:
            fuentes.append(registro[identificador])
        vistas = set()
        for fuente in fuentes:
            referencias = []
            if isinstance(fuente.datos.get("artefacto"), str):
                referencias.append(("artefacto", fuente.datos["artefacto"]))
            if isinstance(fuente.datos.get("solucion"), str):
                referencias.append(("solucion", fuente.datos["solucion"]))
            for elemento in (fuente.datos.get("dataset") or []):
                if isinstance(elemento, str):
                    referencias.append(("dataset", elemento))
            for campo, referencia in referencias:
                if referencia in vistas:
                    continue
                vistas.add(referencia)
                if not (raiz / referencia).exists():
                    informe.error("ruta-inexistente",
                                  f"`{campo}` apunta a `{referencia}`, que no existe en el repo",
                                  nodo=identificador, ruta=fuente.ruta,
                                  linea=fuente.linea_de(campo))


# ─────────────────────────────── Orquestación ─────────────────────────────────

def validar(raiz):
    informe = Informe()
    resumen = {}

    meta, registro = cargar_registro(raiz, informe)
    ficheros = cargar_ficheros(raiz, informe)
    glosario = cargar_glosario(raiz, informe)

    # Nodo efectivo: manda el registro (es canónico); si un nodo solo existe como
    # fichero, se usa el fichero para que el grafo se valide igual.
    nodos = dict(ficheros)
    nodos.update(registro)

    resumen["curso"] = meta.get("curso", "")
    resumen["raiz"] = meta.get("raiz", "")
    resumen["nodos_registro"] = len(registro)
    resumen["nodos_fichero"] = len(ficheros)
    resumen["nodos_totales"] = len(nodos)
    resumen["por_estado"] = {}
    for nodo in registro.values():
        clave = str(nodo.datos.get("estado"))
        resumen["por_estado"][clave] = resumen["por_estado"].get(clave, 0) + 1
    resumen["por_tipo"] = {}
    for nodo in nodos.values():
        clave = str(nodo.tipo)
        resumen["por_tipo"][clave] = resumen["por_tipo"].get(clave, 0) + 1

    for nodo in registro.values():
        validar_esquema(nodo, meta, informe)
    for nodo in ficheros.values():
        validar_esquema(nodo, meta, informe)

    ramas = derivar_profundizar(nodos)
    resumen["ramas_derivadas"] = sum(len(v) for v in ramas.values())

    validar_grafo(nodos, meta, ramas, informe, resumen)
    validar_divergencia(registro, ficheros, informe)
    validar_profundizar_derivado(ficheros, ramas, nodos, informe)
    validar_conceptos(nodos, glosario, informe, resumen)
    validar_fugas_de_soluciones(nodos, informe)
    validar_rutas_referenciadas(registro, ficheros, raiz, informe)

    resumen["errores"] = len(informe.errores)
    resumen["avisos"] = len(informe.avisos)
    informe.resumen = resumen
    return informe


# ─────────────────────────────── Presentación ─────────────────────────────────

def agrupar(hallazgos):
    """Agrupa por código (orden de primera aparición) y ordena por fichero y línea."""
    grupos = {}
    for hallazgo in hallazgos:
        grupos.setdefault(hallazgo.codigo, []).append(hallazgo)
    for grupo in grupos.values():
        grupo.sort(key=lambda h: (h.ruta, h.linea, h.nodo))
    return grupos


def rendir_texto(informe, raiz, estricto):
    resumen = informe.resumen
    lineas = []
    ancho = 78
    lineas.append("═" * ancho)
    lineas.append(f"Validador del grafo — {resumen.get('curso') or 'CX + IA'}")
    lineas.append(f"Repositorio: {raiz}")
    lineas.append("═" * ancho)
    lineas.append(
        f"Registro: {RUTA_REGISTRO} — {resumen.get('nodos_registro', 0)} nodos"
    )
    lineas.append(
        f"Contenido: {RUTA_CONTENIDO}/ — {resumen.get('nodos_fichero', 0)} nodos con frontmatter"
    )
    lineas.append("")

    for nivel, titulo in (("error", "ERRORES"), ("aviso", "AVISOS")):
        hallazgos = informe.errores if nivel == "error" else informe.avisos
        lineas.append(f"{titulo} ({len(hallazgos)})")
        lineas.append("─" * ancho)
        if not hallazgos:
            lineas.append("  ninguno")
            lineas.append("")
            continue
        for codigo, grupo in agrupar(hallazgos).items():
            lineas.append(f"  [{codigo}] ×{len(grupo)}")
            for hallazgo in grupo:
                ubicacion = hallazgo.ubicacion
                etiqueta = f"{hallazgo.nodo}: " if hallazgo.nodo else ""
                if ubicacion:
                    lineas.append(f"    {ubicacion}")
                    lineas.append(f"      {etiqueta}{hallazgo.mensaje}")
                else:
                    lineas.append(f"    {etiqueta}{hallazgo.mensaje}")
        lineas.append("")

    lineas.append("RESUMEN")
    lineas.append("─" * ancho)
    lineas.append(f"  nodos totales .............. {resumen.get('nodos_totales', 0)}"
                  f" (registro {resumen.get('nodos_registro', 0)},"
                  f" ficheros {resumen.get('nodos_fichero', 0)})")
    if resumen.get("por_estado"):
        estados = ", ".join(f"{k} {v}" for k, v in sorted(resumen["por_estado"].items()))
        lineas.append(f"  estados del registro ....... {estados}")
    if resumen.get("por_tipo"):
        tipos = ", ".join(f"{k} {v}" for k, v in sorted(resumen["por_tipo"].items()))
        lineas.append(f"  tipos ...................... {tipos}")
    lineas.append(f"  aristas del grafo .......... {resumen.get('aristas', 0)}")
    lineas.append(f"  orden topológico ........... "
                  f"{'sí, sin ciclos' if resumen.get('orden_topologico') else 'NO: hay ciclo'}")
    lineas.append(f"  alcanzables desde {resumen.get('raiz', '?')} ... "
                  f"{resumen.get('alcanzables', 0)}/{resumen.get('nodos_totales', 0)}")
    lineas.append(f"  ramas de profundización .... {resumen.get('ramas_derivadas', 0)}")
    lineas.append(f"  requisitos cruzados ........ {resumen.get('requisitos_cruzados', 0)}"
                  f"  (a bloque anterior, sin `desbloquea` recíproco: legítimo, §6)")
    if "conceptos_en_glosario" in resumen:
        lineas.append(f"  conceptos .................. {resumen.get('conceptos_usados', 0)} usados,"
                      f" {resumen['conceptos_en_glosario']} en el glosario")
    else:
        lineas.append(f"  conceptos .................. {resumen.get('conceptos_usados', 0)} usados,"
                      f" glosario aún sin crear")
    lineas.append("")
    veredicto = f"ERRORES {resumen.get('errores', 0)} · AVISOS {resumen.get('avisos', 0)}"
    if estricto:
        veredicto += "  (--estricto: los avisos cuentan como errores)"
    lineas.append(veredicto)
    hay_fallo = resumen.get("errores", 0) > 0 or (estricto and resumen.get("avisos", 0) > 0)
    lineas.append("Resultado: " + ("FALLA" if hay_fallo else "OK"))
    lineas.append("═" * ancho)
    return "\n".join(lineas)


def rendir_json(informe, estricto):
    hay_fallo = informe.resumen.get("errores", 0) > 0 or (
        estricto and informe.resumen.get("avisos", 0) > 0)
    return json.dumps({
        "ok": not hay_fallo,
        "estricto": estricto,
        "resumen": informe.resumen,
        "errores": [h.como_dict() for h in informe.errores],
        "avisos": [h.como_dict() for h in informe.avisos],
    }, ensure_ascii=False, indent=2)


def main(argumentos=None):
    analizador = argparse.ArgumentParser(
        description="Valida el grafo de nodos del curso CX + IA "
                    "(ESPECIFICACION.md §8).")
    analizador.add_argument("--json", action="store_true",
                            help="salida en JSON para consumo automático")
    analizador.add_argument("--estricto", action="store_true",
                            help="los avisos cuentan como errores")
    analizador.add_argument("--repo", default=None,
                            help="raíz del repositorio (por defecto, la que contiene "
                                 "este script)")
    opciones = analizador.parse_args(argumentos)

    raiz = Path(opciones.repo).resolve() if opciones.repo else Path(__file__).resolve().parent.parent
    informe = validar(raiz)

    if opciones.json:
        print(rendir_json(informe, opciones.estricto))
    else:
        print(rendir_texto(informe, raiz, opciones.estricto))

    hay_fallo = informe.resumen.get("errores", 0) > 0 or (
        opciones.estricto and informe.resumen.get("avisos", 0) > 0)
    return 1 if hay_fallo else 0


if __name__ == "__main__":
    raise SystemExit(main())
