#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
centinelas.py — las cinco verdades escondidas, escritas como patrones que no
pueden aparecer en nada que ella lea antes de intentarlo.

## Por qué existe

`scripts/comprobar-build.py` comprobaba **rutas y nombres de fichero**: que no se
publicara nada de `dataset/SOLUCIONES/`. Pasaba en verde y tenía razón: ningún
fichero de SOLUCIONES estaba publicado. Y aun así el sitio publicaba las
respuestas del ejercicio central del bloque 4, escritas a mano, en el glosario,
en el campo `brief` de los nodos pendientes y en un ejercicio de sabotaje
(`docs-internos/FUGA-BLOQUE-4.md`).

La suposición implícita era «si las soluciones no están en el build, las
respuestas no están en el build», y es falsa. Las respuestas se pueden escribir
en cualquier sitio. Este módulo comprueba **el contenido**, no la procedencia.

## Dónde está la raya

Lo que sí se puede decir: que los datos están sucios y de qué clase de suciedad
se trata. Ella tiene que esperarla, la especificación la declara deliberada (§4)
y el bloque 2 entero se apoya en ella. «Hay clientes duplicados» es un aviso.

Lo que no se puede decir: **cuántos, cuáles, cómo se encuentran, qué cuestan y
qué los causa.** Eso es la respuesta, y llegar a ella sola es el ejercicio
(§5.3). Los centinelas de aquí abajo persiguen esa segunda lista.

## Cómo se usa

    python3 scripts/centinelas.py            # barre las fuentes y el build
    python3 scripts/centinelas.py RUTA...    # barre lo que se le diga

Como biblioteca, para `comprobar-build.py` y `empaquetar-tutor.py`:

    import centinelas
    hallazgos = centinelas.buscar(texto)

Sale 0 si no hay hallazgos, 1 si los hay.

> **Este fichero nombra las verdades escondidas.** Vive en `scripts/`, que no se
> publica ni viaja al tutor. Si algún día se publica `scripts/`, esto es una
> filtración por sí solo.
"""
from __future__ import annotations

import argparse
import bisect
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Lo que se barre cuando no se dice otra cosa: todo lo que ella puede llegar a
# leer. El dataset en sí no se barre —los datos contienen las verdades, ése es
# el sentido del gemelo— pero su LEEME sí, porque es prosa que se lee antes.
RUTAS_POR_DEFECTO = [
    Path("contenido"),
    Path("ejercicios"),
    Path("plantillas"),
    Path("sitio/index-fuente.md"),
    Path("sitio/build"),
    Path("dataset/ficheros/LEEME.md"),
    Path("tutor/prompts"),
    Path("tutor/guardarrailes"),
    Path("tutor/serverless/curso.json"),
    Path("README.md"),
]

EXTENSIONES = {".md", ".html", ".yml", ".yaml", ".json", ".txt", ".js", ".css"}

# Directorios que nunca se barren: o son la clave de corrección, o son ruido.
EXCLUIDOS = {"SOLUCIONES", "docs-internos", "node_modules", "__pycache__",
             ".git", "_auditoria"}

# Bundles de terceros que MkDocs Material copia al build. No los escribimos
# nosotros y no pueden filtrar nada: lo que sí hacen es disparar los centinelas
# numéricos, porque llevan tablas de pesos dentro (el segmentador japonés de
# lunr tiene un 6620 que no son las ventas fantasma de V3).
DE_TERCEROS = {"javascripts", "stylesheets", "webfonts", "fonts"}


def es_de_terceros(ruta: Path) -> bool:
    return bool(DE_TERCEROS & set(ruta.parts))


# ─────────────────────────────── Modelo ───────────────────────────────────────

@dataclass(frozen=True)
class Centinela:
    """Un patrón que delata una verdad escondida.

    `patron` es la señal. Si además lleva `contexto`, sólo cuenta como hallazgo
    cuando el contexto aparece a menos de `ventana` caracteres: así «12» sólo
    salta cuando va con «duplicados», y no cada vez que alguien escribe una hora.
    `contexto2` añade una segunda condición que también tiene que cumplirse, para
    las señales que sólo delatan cuando concurren dos cosas: un porcentaje, cerca
    de «tickets», cerca de «factura».
    """
    codigo: str
    verdad: str
    delata: str
    patron: str
    contexto: str = ""
    ventana: int = 260
    contexto2: str = ""
    # Casi todos los centinelas se comprueban contra verdades-escondidas.md
    # (ver `autoprueba`). Los que protegen respuestas de ejercicios anteriores
    # al bloque 4 no salen en esa clave, y se marcan para no exigírselo.
    en_la_clave: bool = True

    def compilado(self) -> re.Pattern:
        return re.compile(self.patron)

    def contextos_compilados(self) -> list[re.Pattern]:
        return [re.compile(c) for c in (self.contexto, self.contexto2) if c]


@dataclass(frozen=True)
class Hallazgo:
    ruta: str
    linea: int          # 0 si no se puede situar
    centinela: Centinela
    fragmento: str

    def __str__(self) -> str:
        donde = f"{self.ruta}:{self.linea}" if self.linea else self.ruta
        return (f"{donde}: [{self.centinela.verdad}/{self.centinela.codigo}] "
                f"{self.centinela.delata}\n      …{self.fragmento}…")


# ────────────────────────── Los centinelas ────────────────────────────────────
# Los patrones se aplican sobre texto normalizado: minúsculas, sin tildes y con
# los espacios colapsados. Por eso aquí se escribe `factur`, no `facturación`.
# Los miles admiten punto o espacio (`3.344`, `3 344`) y los decimales, coma.

_TICKETS = r"ticket|incidencia|queja|llamada|contacto|caso|reclamacion"

# Un número suelto sólo delata si no lleva pegada una unidad que lo explique.
# Sin esto, «67 min → 72 min» del bloque 3 se confunde con los 72 tickets de V5.
_SIN_UNIDAD = (r"(?! ?(?:min\b|minutos|h\b|horas|s\b|segundos|dias|semanas|"
               r"meses|anos|€|euros|%|km|kg|l\b|litros|filas|columnas))")

# V5 está en la universalidad, no en la negación. Que a *este* bar no le avisaran
# lo cuenta el propio cliente en su correo, y el sabotaje de nivel 2 se sostiene
# sobre ello. Lo que no puede aparecer en ningún sitio es que no se avise a nadie:
# eso es V5 enunciada, y el bloque 3 va antes del 4.
_UNIVERSAL = (r"nadie|nunca|jamas|ningun|ni una vez|ni una sola|cero veces|"
              r"en toda la empresa|sin aplicar|solo en papel|"
              r"no existe en la operacion|incumpl")

CENTINELAS: list[Centinela] = [

    # ── V1 · el fallo de redondeo en los pedidos con descuento ────────────────
    Centinela("v1-mecanismo", "V1", "el mecanismo del fallo de facturación",
              r"redonde\w*[^.;:]{0,45}(?:al alza|hacia arriba|para arriba)",
              r"precio|importe|factur|centimo|descuento|dto\b|€|euros",
              ventana=70),
    Centinela("v1-mecanismo-descuento", "V1", "el redondeo, atado al descuento",
              r"redonde\w*[^.;:]{0,45}al alza|redonde\w*[^.;:]{0,30}(?:precio|importe)",
              r"descuento|dto\b", ventana=400),
    # No hace falta describir el mecanismo para delatarlo: basta con llamarlo por
    # su nombre al lado de una factura. «Arreglar el redondeo y quedarte sin las
    # quejas» era el ejemplo de `coste-de-oportunidad`, y decía V1 entera.
    Centinela("v1-nombre-del-fallo", "V1", "el fallo, llamado por su nombre",
              r"redondeo",
              r"factur|descuento|dto\b|precio unitario|importe|cobr|queja",
              ventana=90),
    Centinela("v1-mecanismo-inverso", "V1", "el mecanismo, dicho del revés",
              r"(?:descuento|dto)\w* (?:sobre|al|a|en) (?:el |cada )?precio unitario"),
    Centinela("v1-volumen", "V1", "cuántos tickets salen del fallo",
              r"\b304\b" + _SIN_UNIDAD, _TICKETS + r"|factur|origen"),
    Centinela("v1-porcentaje", "V1", "cuánto pesa el fallo sobre el total",
              r"\b38(?:[,.]\d+)? ?%", _TICKETS + r"|factur"),
    Centinela("v1-sobrefacturacion", "V1", "la sobrefacturación acumulada",
              r"\b623[,.]\d\d\b|\b1[. ]?247[,.]48\b"),
    Centinela("v1-coste", "V1", "lo que cuesta atender los tickets del fallo",
              r"\b3[. ]?344\b"),
    Centinela("v1-lineas", "V1", "las líneas y pedidos afectados",
              r"\b3[. ]?(?:259|422)\b|\b1[. ]?155\b",
              r"linea|pedido|descuento|dto"),
    Centinela("v1-cobertura", "V1", "qué proporción de las líneas con descuento falla",
              r"\b95[,.]\d+ ?%", r"descuento|dto|linea"),
    Centinela("v1-pr06", "V1", "PR-06 como el procedimiento que el sistema incumple",
              r"pr-06",
              r"redonde|al alza|no (?:se )?(?:cumple|aplica|sigue|hace)|nadie|incumpl"),
    Centinela("v1-trampa-categoria", "V1", "el error de fiarse de la columna «categoria»",
              r"\b24[,.]\d+ ?%|\b194 (?:" + _TICKETS + r")|\b13[,.]8 puntos",
              r"categoria|factur|" + _TICKETS),

    # ── V0 · la taxonomía real, que es la puerta de todo lo demás ─────────────
    # No es una de las cinco, pero es lo primero que hay que reconstruir para
    # llegar a V1 y a V5: cuántas categorías de verdad hay debajo de las catorce
    # etiquetas de `tickets.xlsx`. Decir el número le ahorra el ejercicio entero
    # de `b4-m1-taxonomias`.
    Centinela("v0-tamano", "V0", "cuántas categorías reales hay debajo de las etiquetas",
              r"(?:8|ocho) categorias|(?:14|catorce) (?:etiquetas|formas|categorias)|"
              r"para decir (?:8|ocho)",
              r"categoria|etiqueta|ticket|taxonomia|incidencia|clasific"),
    Centinela("v0-devoluciones", "V0", "cuántas líneas en negativo hay que contar",
              r"\b45\b" + _SIN_UNIDAD, r"negativ|devoluci|linea", ventana=120,
              en_la_clave=False),
    # ── Las concentraciones, dichas con cualquier redondeo ────────────────────
    # La cifra de una verdad no se filtra sólo escribiéndola clavada. «El 40 % de
    # los correos dicen lo mismo: la factura no cuadra» es V1 entera, redondeada.
    # Por eso estos tres centinelas van por franja y exigen dos contextos: el
    # porcentaje, el conjunto sobre el que se calcula, y de qué habla.
    Centinela("v1-concentracion", "V1", "la concentración de contactos de facturación",
              r"\b(?:3[0-9]|4[0-5])(?:[,.]\d+)? ?%|una de cada (?:dos|tres)",
              _TICKETS + r"|correo",
              ventana=220,
              contexto2=r"factur|no cuadra|descuadre|albaran|importe|cobr"),
    Centinela("v4-concentracion", "V4", "la concentración de incidencias en tres clientes",
              r"\b(?:1[89]|2[0-5])(?:[,.]\d+)? ?%",
              _TICKETS,
              ventana=220,
              contexto2=r"tres clientes|3 clientes|hosteleria|deficitari"),
    Centinela("v5-concentracion", "V5", "la concentración de contactos por falta de aviso",
              r"\b(?:[89]|10)(?:[,.]\d+)? ?%",
              _TICKETS,
              ventana=220,
              contexto2=r"avis|sin avisar|cerrad|vispera|dia antes"),

    # ── V2 · los doce clientes duplicados ─────────────────────────────────────
    Centinela("v2-recuento", "V2", "cuántos duplicados hay",
              r"\b(?:12|doce)\b" + _SIN_UNIDAD,
              r"duplicad|fichas repetidas|pares? de fichas", ventana=140),
    Centinela("v2-clientes-reales", "V2", "el recuento real de clientes",
              r"\b288\b" + _SIN_UNIDAD, r"client|ficha|maestro", ventana=120),
    Centinela("v2-metodo", "V2", "cómo se encuentran los duplicados",
              r"duplicad|dos fichas|ficha repetida",
              r"normaliz|cotej|mismo telefono|misma direccion|"
              r"telefono (?:y|\+) (?:la )?direccion|direccion (?:y|\+) (?:el )?telefono",
              ventana=140),
    Centinela("v2-dano", "V2", "el daño real: dos condiciones para un mismo cliente",
              r"dos fichas|ficha (?:nueva|repetida|duplicada)|"
              r"(?:factur\w+|cobra\w+|dad\w+ de alta) dos veces|"
              r"dos veces al mismo cliente|dos condiciones distintas",
              r"client|ficha|alta|maestro|descuento", ventana=160),
    Centinela("v2-procedimientos", "V2", "PR-01 y PR-09 como los que no se cumplen",
              r"pr-01|pr-09", r"duplicad|alta|telefono|titular|ficha"),
    Centinela("v2-pares", "V2", "los pares concretos del maestro",
              r"cli-0(?:001|013|023|031|033|036|046|081|094|095|101|120|"
              r"155|169|178|185|238|249|258|265|277|294|296|300)\b",
              r"duplicad|ficha|par\b|mismo cliente|repetid"),

    # ── V3 · el pico de diciembre que no es demanda ───────────────────────────
    Centinela("v3-fantasma", "V3", "los pedidos fantasma",
              r"fantasma", r"pedido|linea|venta|diciembre|import"),
    Centinela("v3-bloque-de-ids", "V3", "el bloque de ids de la segunda carga",
              r"ped-9[\dx]"),
    Centinela("v3-doble-importacion", "V3", "la causa del pico",
              r"doble (?:importaci|carga)|import\w* dos veces|"
              r"(?:carga|importaci\w+) duplicada|se (?:importo|cargo) dos veces"),
    Centinela("v3-recuento", "V3", "cuántos pedidos o líneas sobran",
              r"(?:\b62\b|\b244\b|\b1[. ]?188\b)" + _SIN_UNIDAD,
              r"pedido|linea|fantasma|diciembre|duplicad", ventana=160),
    Centinela("v3-porcentajes", "V3", "el pico real frente al registrado",
              r"\b(?:41[,.]0\d|12[,.]0[0-9]|32[,.]84|11[,.]94) ?%", r"diciembre|pico|mes"),
    Centinela("v3-importe", "V3", "las ventas que nunca existieron",
              r"\b6[. ]?620\b"),
    Centinela("v3-ventana", "V3", "la ventana de la doble importación",
              r"del 9 al 13 de diciembre|9 (?:al|-) 13 de diciembre|"
              r"semana del 9 de diciembre"),

    # ── V4 · los tres clientes que cuestan dinero ─────────────────────────────
    Centinela("v4-clientes", "V4", "los tres clientes deficitarios, por su id",
              r"cli-0(?:042|118|233)\b"),
    Centinela("v4-nombres", "V4", "los tres clientes deficitarios, por su nombre",
              r"el cantabrico|la ria\b|casa ramon",
              _TICKETS + r"|margen|deficit|coste|cuesta|rentab"),
    Centinela("v4-volumen", "V4", "cuántas incidencias concentran",
              r"\b176\b" + _SIN_UNIDAD, _TICKETS, ventana=160),
    Centinela("v4-porcentaje", "V4", "qué parte del total concentran",
              r"\b22(?:[,.]\d+)? ?%", _TICKETS),
    Centinela("v4-resultado", "V4", "lo que cuestan de más de lo que dejan",
              r"\b1[. ]?(?:653|936)\b|\b282[,.]27\b|\b591[,.]28\b|"
              r"\b510[,.]95\b|\b551[,.]50\b"),
    Centinela("v4-coste-contacto", "V4", "el coste unitario de un contacto, ya derivado",
              r"\b11(?:[,.]00)? ?(?:€|euros)", r"contacto|ticket|atender|llamada",
              ventana=160),

    # ── V5 · PR-07, el procedimiento que nadie sigue ──────────────────────────
    Centinela("v5-incumplimiento", "V5", "que PR-07 no se aplica con nadie",
              r"pr-07", _UNIVERSAL, ventana=200),
    Centinela("v5-nadie-avisa", "V5", "que el aviso previo no se da nunca",
              r"aviso previo|avisar (?:el dia antes|la vispera)",
              _UNIVERSAL, ventana=200),
    Centinela("v5-volumen", "V5", "cuántos tickets causa la omisión",
              r"\b72\b" + _SIN_UNIDAD, _TICKETS + r"|aviso|entrega",
              ventana=120),
    Centinela("v5-porcentaje", "V5", "qué parte del total causa la omisión",
              r"\b9(?:[,.]0+)? ?%", _TICKETS + r"|aviso|entrega"),
    Centinela("v5-coste", "V5", "lo que cuestan esos contactos",
              r"\b792\b", r"€|euros|coste|contacto"),
]


# ───────────────────────── Normalización del texto ────────────────────────────

def normalizar(texto: str) -> tuple[str, list[int]]:
    """Devuelve el texto en minúsculas, sin tildes y con espacios colapsados,
    junto al índice original de cada carácter, para poder situar el hallazgo."""
    salida: list[str] = []
    indices: list[int] = []
    espacio = False
    for posicion, caracter in enumerate(texto):
        if caracter.isspace() or caracter in "   ​":
            espacio = True
            continue
        if caracter in "*`_":      # énfasis de markdown: no parte una frase
            continue
        if espacio and salida:
            salida.append(" ")
            indices.append(posicion)
        espacio = False
        descompuesto = unicodedata.normalize("NFKD", caracter)
        base = "".join(c for c in descompuesto if not unicodedata.combining(c))
        base = base.lower() if base else caracter.lower()
        for c in base:
            salida.append(c)
            indices.append(posicion)
    return "".join(salida), indices


_ETIQUETA = re.compile(r"<(script|style)\b.*?</\1>|<[^>]*>", re.S | re.I)
_ENTIDAD = re.compile(r"&(?:#\d+|#x[0-9a-fA-F]+|[a-zA-Z]+);")


def texto_visible(html: str) -> str:
    """Quita marcado dejando los huecos: las posiciones no se mueven, así que
    las líneas que se reporten siguen siendo las del fichero."""
    sin_etiquetas = _ETIQUETA.sub(lambda m: " " * len(m.group(0)), html)
    return _ENTIDAD.sub(lambda m: " " * len(m.group(0)), sin_etiquetas)


# ───────────────────────────── Búsqueda ───────────────────────────────────────

def buscar(texto: str, ruta: str = "", es_html: bool = False) -> list[Hallazgo]:
    """Todos los centinelas que saltan en `texto`, en orden de aparición."""
    if es_html:
        texto = texto_visible(texto)
    plano, indices = normalizar(texto)
    saltos = [i for i, c in enumerate(texto) if c == "\n"]

    def linea_de(posicion_plana: int) -> int:
        if posicion_plana >= len(indices):
            return 0
        return bisect.bisect_right(saltos, indices[posicion_plana]) + 1

    hallazgos: list[Hallazgo] = []
    for centinela in CENTINELAS:
        contextos = centinela.contextos_compilados()
        for encaje in centinela.compilado().finditer(plano):
            if contextos:
                desde = max(0, encaje.start() - centinela.ventana)
                hasta = min(len(plano), encaje.end() + centinela.ventana)
                if not all(c.search(plano, desde, hasta) for c in contextos):
                    continue
            recorte = plano[max(0, encaje.start() - 55):encaje.end() + 55]
            hallazgos.append(Hallazgo(ruta, linea_de(encaje.start()),
                                      centinela, recorte.strip()))
    hallazgos.sort(key=lambda h: (h.linea, h.centinela.codigo))
    return hallazgos


def ficheros_de(rutas: list[Path], raiz: Path = RAIZ):
    """Los ficheros de texto que hay bajo `rutas`, sin lo excluido."""
    for ruta in rutas:
        absoluta = ruta if ruta.is_absolute() else raiz / ruta
        if not absoluta.exists():
            continue
        candidatos = [absoluta] if absoluta.is_file() else sorted(absoluta.rglob("*"))
        for fichero in candidatos:
            if not fichero.is_file() or fichero.suffix.lower() not in EXTENSIONES:
                continue
            if EXCLUIDOS & set(fichero.parts) or es_de_terceros(fichero):
                continue
            yield fichero


def barrer(rutas: list[Path], raiz: Path = RAIZ) -> list[Hallazgo]:
    hallazgos: list[Hallazgo] = []
    for fichero in ficheros_de(rutas, raiz):
        try:
            texto = fichero.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        try:
            relativa = str(fichero.relative_to(raiz))
        except ValueError:
            relativa = str(fichero)
        hallazgos += buscar(texto, relativa, es_html=fichero.suffix.lower() == ".html")
    return hallazgos


# ───────────────────────────── Autoprueba ─────────────────────────────────────

CLAVE = Path("dataset/SOLUCIONES/verdades-escondidas.md")


def autoprueba(raiz: Path = RAIZ) -> list[str]:
    """Un centinela que no salta con la clave de corrección delante no sirve.

    Se ejecuta contra `verdades-escondidas.md`, que es el peor caso posible: si
    algún patrón no reconoce ahí su propia verdad, es que está mal escrito y no
    protege nada. Devuelve los códigos que no saltaron.
    """
    fichero = raiz / CLAVE
    if not fichero.exists():
        return [f"no existe {CLAVE}: ejecuta antes `make dataset`"]
    encontrados = {h.centinela.codigo
                   for h in buscar(fichero.read_text(encoding="utf-8"))}
    return sorted(c.codigo for c in CENTINELAS
                  if c.en_la_clave and c.codigo not in encontrados)


# ─────────────────────────────── CLI ──────────────────────────────────────────

def main(argumentos=None) -> int:
    analizador = argparse.ArgumentParser(
        description="Busca las cinco verdades escondidas en lo que ella puede leer.")
    analizador.add_argument("rutas", nargs="*", type=Path,
                            help="qué barrer (por defecto: contenido, ejercicios, "
                                 "plantillas, el build y el paquete del tutor)")
    analizador.add_argument("--sin-autoprueba", action="store_true",
                            help="no comprobar los centinelas contra la clave")
    opciones = analizador.parse_args(argumentos)

    if not opciones.sin_autoprueba:
        mudos = autoprueba()
        if mudos:
            print("CENTINELAS QUE NO DETECTAN SU PROPIA VERDAD:", file=sys.stderr)
            for codigo in mudos:
                print(f"  - {codigo}", file=sys.stderr)
            print("\nUn centinela mudo da vía libre a la filtración que vigila.",
                  file=sys.stderr)
            return 2

    rutas = opciones.rutas or RUTAS_POR_DEFECTO
    hallazgos = barrer(rutas)

    if hallazgos:
        print("LAS RESPUESTAS ESTÁN A LA VISTA:", file=sys.stderr)
        for hallazgo in hallazgos:
            print(f"  - {hallazgo}", file=sys.stderr)
        verdades = sorted({h.centinela.verdad for h in hallazgos})
        print(f"\n{len(hallazgos)} filtraciones ({', '.join(verdades)}). "
              f"El ejercicio central del bloque 4 se resuelve leyendo.", file=sys.stderr)
        return 1

    revisados = sum(1 for _ in ficheros_de(rutas))
    print(f"Sin filtraciones: {revisados} ficheros revisados contra "
          f"{len(CENTINELAS)} centinelas de las verdades escondidas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
