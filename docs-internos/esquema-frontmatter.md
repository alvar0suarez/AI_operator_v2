# Esquema de frontmatter — contrato de nodo

Fuente normativa: `ESPECIFICACION.md` §6. Este fichero es la versión ejecutable de
ese contrato: `scripts/validar-grafo.py` lo aplica literalmente y falla el build si
un nodo no lo cumple.

## Ejemplo canónico

```yaml
---
id: b3-m4-sabotaje
bloque: 3
titulo: "Ejercicios de sabotaje"
tipo: ejercicio          # concepto | ejercicio | caso | artefacto | profundizacion
duracion_min: 45
requisitos: [b3-m1-anatomia-encargo, b2-m1-clasificar]
desbloquea: [b3-m6-verificacion-proporcional]
caduca: bajo             # bajo | medio | alto  (visible para la alumna)
objetivos:
  - "Detectar dato inventado en un output plausible"
  - "Distinguir error de contenido de error de tono"
conceptos: [verificacion, alucinacion, riesgo]
profundizar:
  - id: b3-p1-por-que-alucinan
    titulo: "Por qué los modelos inventan datos"
---
```

## Campos

| Campo | Obligatorio | Tipo | Regla |
|---|---|---|---|
| `id` | sí | string | Único en todo el repo. Patrón `b<bloque>-(m\|p)<n>-<slug>`. `m` = tronco, `p` = profundización. El slug es kebab-case sin acentos. |
| `bloque` | sí | int 0–6 | Debe coincidir con el prefijo de `id` y con el directorio del fichero. |
| `titulo` | sí | string | Entre comillas. Es el H1 renderado; **el cuerpo del nodo no repite el H1**. |
| `tipo` | sí | enum | `concepto` \| `ejercicio` \| `caso` \| `artefacto` \| `profundizacion` |
| `duracion_min` | sí | int 5–90 | Sesión real de 45–60 min (§1). Un nodo que pase de 60 se parte en dos. |
| `requisitos` | sí | lista de `id` | Aristas entrantes. Pueden estar vacías solo en `b0-m1`. Deben existir y no crear ciclos. |
| `desbloquea` | sí | lista de `id` | Aristas salientes. **Debe ser recíproco**: si A declara `desbloquea: [B]`, B declara `requisitos: [... A ...]`. El validador lo exige. |
| `caduca` | sí | enum | `bajo` \| `medio` \| `alto`. Visible para la alumna (§6). |
| `objetivos` | sí | lista de string | 1–4. Verbo observable en infinitivo ("detectar", "escribir"), nunca "conocer" o "entender". |
| `conceptos` | sí | lista de slugs | Alimentan el glosario autogenerado. Todo slug debe existir en `contenido/glosario/glosario.yml`. |
| `profundizar` | no | lista de `{id, titulo}` | Solo puede apuntar a nodos `tipo: profundizacion`. |
| `artefacto` | solo si `tipo: artefacto` | string | Ruta relativa a la plantilla en `/plantillas`. |
| `bloqueante` | no | bool | `true` marca un nodo que el grafo no deja saltar (§6: el diario del bloque 1). Por defecto `false`. |
| `dataset` | no | lista de rutas | Ficheros de `/dataset/ficheros` que el nodo usa. El validador comprueba que existan. |
| `solucion` | no | ruta | Fichero de solución. **Nunca se sirve al tutor** (§7.2) ni se publica (§8). |

## Reglas del grafo (§6)

1. **Tronco lineal**: los bloques 0→6 en orden. Un nodo tronco no puede requerir un
   nodo de un bloque posterior.
2. **Sin ciclos**. El validador hace orden topológico y falla si no lo consigue.
3. **Todo nodo alcanzable** desde `b0-m1-que-es-este-curso`.
4. **Reciprocidad** `requisitos` ↔ `desbloquea` entre nodos tronco (ver excepción en 5).
5. Un nodo `profundizacion` cuelga de exactamente un nodo tronco. Se enlaza así:
   el padre lo lista en `profundizar`, y el hijo declara `requisitos: [<id-del-padre>]`
   y `desbloquea: []`. **El padre NO lo lista en `desbloquea`**: la rama es opcional y
   no debe aparecer como paso siguiente del tronco. La regla de reciprocidad (4) no
   aplica a este par; el validador la exceptúa. Un nodo `profundizacion` **nunca** es
   requisito de un nodo tronco.
6. `caduca: alto` implica contenido aislado y sustituible sin tocar el resto (§9).

## Cuerpo del nodo

Después del frontmatter, en este orden:

1. Párrafo de entrada (2–4 frases). Sin encabezado. Dice qué se lleva del nodo.
2. Secciones `##` del contenido.
3. `## Las tres instancias` — obligatorio en nodos `concepto` de los bloques 2–4:
   su sector (CX), otro dominio profesional, vida personal (§2.3).
4. `## Cuándo esto falla` — obligatorio en todo nodo `concepto`.
5. `## Ejercicio` — si el nodo lo lleva.
6. `## Escribe tú la regla` — cierre de módulo donde ella redacta la generalización (§2.2).
7. `## Para la bitácora` — 2–3 preguntas concretas.

Un nodo `artefacto` sustituye 3–7 por `## Cómo se rellena` + `## Rúbrica` + `## Para la bitácora`.
