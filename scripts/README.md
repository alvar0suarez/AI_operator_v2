# scripts/

Utilidades de mantenimiento del repositorio. Ninguna es contenido para la alumna:
son herramientas de quien construye el curso. Todas se ejecutan desde la raíz del
repositorio, con Python 3.11 y sin más dependencias que PyYAML, `openpyxl` y
`python-docx` (nada de pandas ni numpy).

Este índice crece con el directorio: cada script nuevo se documenta aquí.

| Script | Qué hace | Sale con 1 si… |
|---|---|---|
| `validar-grafo.py` | Valida el grafo de nodos y el frontmatter contra el esquema | hay errores |
| `verificar-glosario.py` | Valida el contrato del glosario contra el registro de nodos | hay errores |
| `generar-glosario.py` | Regenera `contenido/glosario/README.md` desde `glosario.yml` | falla la generación |

Orden razonable antes de dar por bueno un cambio de contenido:

```bash
python3 scripts/validar-grafo.py
python3 scripts/verificar-glosario.py
python3 scripts/generar-glosario.py     # solo si has tocado el glosario
```

---

## `validar-grafo.py`

El validador que exige `ESPECIFICACION.md` §8: *"script que verifica el grafo de
requisitos (sin ciclos, sin referencias rotas, todo nodo alcanzable)"*. Aplica
literalmente `docs-internos/esquema-frontmatter.md`.

```bash
python3 scripts/validar-grafo.py [--json] [--estricto] [--repo RUTA]
```

| Bandera | Efecto |
|---|---|
| `--json` | Informe en JSON (`ok`, `resumen`, `errores`, `avisos`) para CI o para otro script |
| `--estricto` | Los avisos cuentan como errores: útil cuando los bloques 4–6 dejen de estar pendientes |
| `--repo RUTA` | Valida otro árbol (se usa para los bancos de prueba); por defecto, el repositorio que contiene el script |

Código de salida: `0` si no hay errores, `1` si los hay.

### Qué lee

1. `docs-internos/registro-de-nodos.yml` — **registro canónico**. Es la fuente de
   verdad: primero se apunta el nodo aquí y después se escribe su `.md`.
2. Todos los `.md` de `contenido/` que traen frontmatter YAML. Los que no lo
   traen se ignoran con un aviso (salvo `README.md` e `index.md`).
3. `contenido/glosario/glosario.yml` para los slugs de `conceptos`.

### Qué comprueba

**Esquema, campo a campo** (sobre las dos fuentes, cada una con su ruta y línea):
campos obligatorios, campos no previstos, patrón del `id`
(`b<bloque>-(m|p)<n>-<slug-kebab-sin-acentos>`), coherencia `id` ↔ `bloque` ↔
directorio del fichero, enums de `tipo` y `caduca`, rango de `duracion_min`
(5–90), `estado` del registro, listas sin repetidos ni autorreferencia,
`objetivos` (1–4, verbo observable en infinitivo), `conceptos` en kebab-case,
`bloqueante` booleano, `artefacto` obligatorio en los nodos `tipo: artefacto`, y
formas de `dataset`, `solucion` y `profundizar`.

**Grafo:**

- Sin ciclos: orden topológico sobre `requisitos` + `desbloquea` + las ramas
  derivadas. Si no cierra, **imprime el ciclo concreto** (`a → b → c → a`).
- Sin referencias rotas en `requisitos`, `desbloquea` y `profundizar`.
- Todo nodo alcanzable desde `meta.raiz` siguiendo `desbloquea` + `profundizar`.
- Reciprocidad `requisitos` ↔ `desbloquea` (ver las excepciones más abajo).
- Un nodo tronco no puede exigir un nodo de un bloque posterior, y `desbloquea`
  no va hacia atrás.
- Una `profundizacion` cuelga de exactamente un padre tronco, con
  `desbloquea: []`, y nunca es requisito de un nodo tronco.

**Registro ↔ ficheros:** mismo conjunto de ids y, para cada nodo presente en los
dos, mismos `titulo`, `tipo`, `bloque`, `duracion_min`, `caduca`, `requisitos`,
`desbloquea` y `conceptos`. Un nodo del registro con `estado: escrito` y sin
`.md` es **error**; con `estado: pendiente-piloto` y sin `.md` es **aviso** (los
bloques 4–6 se escriben después del piloto, `ESPECIFICACION.md` §3). Un `.md` que
no está en el registro es error. Si las listas coinciden como conjunto pero no en
orden, es aviso.

**`profundizar` derivado:** la lista de ramas de cada padre se calcula a partir
del requisito único de cada nodo `profundizacion`, y el `.md` del padre tiene que
declararla exactamente igual, títulos incluidos.

**Glosario:** todo slug de `conceptos` existe en `contenido/glosario/glosario.yml`.
Si el fichero aún no existe, es aviso y no error. Los términos del glosario que no
usa ningún nodo salen como aviso.

**Fugas de soluciones:** ningún nodo publicado —ni frontmatter ni cuerpo— puede
referenciar rutas de `dataset/SOLUCIONES/`. Solo el campo `solucion` puede, porque
no se sirve al tutor ni se publica (`ESPECIFICACION.md` §7.2 y §8).

### Decisiones que conviene conocer

- **La reciprocidad se exige en la dirección que fija el esquema**: si A declara
  `desbloquea: [B]`, B tiene que declarar A en `requisitos`. Al revés solo se
  exige dentro del mismo bloque. Un requisito hacia un bloque anterior es un
  *requisito cruzado* legítimo (`ESPECIFICACION.md` §6: `b3-m4-sabotaje` exige
  `b2-m2-clasificar` y el nodo del bloque 2 no lo lista como paso siguiente). El
  resumen los cuenta para que se vean.
- **Las ramas de profundización están exceptuadas de la reciprocidad**: el padre
  las lista en `profundizar`, nunca en `desbloquea`; la rama declara
  `requisitos: [padre]` y `desbloquea: []`.
- **Las rutas de `artefacto`, `dataset` y `solucion` solo se comprueban en nodos
  que ya tienen `.md`.** Un nodo todavía sin escribir puede apuntar a una
  plantilla o a un fichero del dataset que generan fases posteriores
  (`ESPECIFICACION.md` §8, fases de construcción).
- Un nodo `tipo: artefacto` **debe** declarar `artefacto`; otros tipos pueden
  declararlo si entregan plantilla (el diario del bloque 1 es `ejercicio` y la
  entrega).

### Estado actual (fase 0)

Con el registro completo y sin ningún `.md` escrito, la ejecución da 45 errores
(los nodos `escrito` de los bloques 0–3 que aún no tienen fichero) y 26 avisos
(los nodos `pendiente-piloto` de los bloques 4–6). El grafo en sí está limpio:
sin ciclos, sin referencias rotas y 71/71 nodos alcanzables desde
`b0-m1-que-es-este-curso`.

---

## `verificar-glosario.py`

Verifica el contrato del glosario contra el registro de nodos: cobertura (todo
slug del registro tiene entrada), ausencia de sobrantes, integridad de
`ver_tambien`, coherencia de `bloque_origen` con el bloque más bajo que usa el
concepto, campos obligatorios, slugs únicos en kebab-case sin acentos, e higiene
de redacción de las definiciones.

```bash
python3 scripts/verificar-glosario.py
```

Código de salida `1` si falla algo. Complementa a `validar-grafo.py`, que solo
comprueba que los slugs existan.

## `generar-glosario.py`

Regenera `contenido/glosario/README.md` —el glosario navegable, en orden
alfabético, con ancla por slug y los nodos que usan cada término— a partir de
`contenido/glosario/glosario.yml` y del registro de nodos.

```bash
python3 scripts/generar-glosario.py
```

El `.md` es artefacto generado: se edita `glosario.yml`, nunca el README.

---

## Pendiente

`generar-dataset.py` — el generador del gemelo sintético con semilla fija
(`ESPECIFICACION.md` §4 y §8, fase 1). Todavía no existe; cuando se escriba, se
documenta aquí.
