# Instrucciones para Claude en este repositorio

## Lo primero

`ESPECIFICACION.md` es la fuente de verdad conceptual. Si algo en el código o en el
contenido la contradice, **gana la especificación** hasta que alguien la actualice
explícitamente. Antes de cualquier cambio de fondo, léela.

Después, según lo que vayas a tocar:

| Vas a tocar | Lee antes |
|---|---|
| Un nodo de contenido | `docs-internos/guia-de-estilo.md` y `esquema-frontmatter.md` |
| El grafo, ids, requisitos | `docs-internos/registro-de-nodos.yml` |
| El dataset | `dataset/ESPECIFICACION-DATASET.md` |
| Por qué algo está como está | `docs-internos/decisiones.md` |

## Reglas duras

- **Nunca pidas datos reales de la empresa de la alumna**, ni en un ejercicio, ni en
  un ejemplo, ni en el tutor. Todo corre sobre `dataset/ficheros/`.
- **`dataset/SOLUCIONES/` no se publica ni se le sirve al tutor** (§7.2). Si escribes
  algo que lo lea, comprueba que no acaba en el build ni en el contexto del tutor.
- **El dataset no se edita a mano.** Se cambia `scripts/generar-dataset.py`, se
  regenera y se pasa `scripts/verificar-verdades.py`.
- **La clave de API nunca en el cliente** (§7.5). La llamada va siempre por la
  función serverless.
- **Sin gamificación** (§2.7). Ni insignias, ni rachas, ni puntos.
- **El tutor no da respuestas, da tracción** (§7). Si un cambio hace que el tutor
  resuelva un ejercicio, el cambio está mal.

## Contenido

Se escribe en español de España, tuteando, en femenino. Frases cortas. Sin
entusiasmo de folleto, sin emojis, sin "¡vamos allá!". La lectora es competente en
su trabajo y ajena a éste: la distancia entre "principiante" y "tonta" es el error
de tono más caro del proyecto.

Todo nodo de concepto lleva sus **tres instancias** (CX / otro dominio profesional /
vida personal) y su sección **"Cuándo esto falla"**. Todo módulo cierra con
**"Escribe tú la regla"**: la generalización la redacta ella, no nosotros (§2.2).

## Antes de dar nada por terminado

```bash
make todo        # las cinco de abajo, en orden
```

```bash
make validar     # grafo: ciclos, referencias rotas, alcanzabilidad, reciprocidad
make verificar   # las 5 verdades escondidas siguen siendo derivables del dataset
make sitio-build # el sitio construye y SOLUCIONES/ no está dentro
make centinelas  # y las 5 verdades no están escritas a mano en ningún sitio
```

Si `validar` o `verificar` fallan, no está terminado. `verificar` fallando significa
que el ejercicio central del bloque 4 ha dejado de tener solución.

`centinelas` fallando significa lo contrario y es igual de grave: la solución está
publicada. Pasó (`docs-internos/FUGA-BLOQUE-4.md`), y pasó con las comprobaciones en
verde, porque miraban de dónde venía cada fichero y no qué decía. **Que algo no salga
de `SOLUCIONES/` no quiere decir que no sea la respuesta.**

## Bloques 4–6

Están en el grafo con `estado: pendiente-piloto` y **sin contenido a propósito**.
§3 y §8 de la especificación son explícitas: se pilotan los bloques 1–3 con ella
antes de escribir el 4, porque el 4 se diseña mucho mejor sabiendo dónde se atascó
de verdad. No los rellenes sin que el piloto haya ocurrido; el input para escribirlos
es el registro de preguntas del tutor (§7.4).

## Git

Rama de trabajo: `claude/revisar-especificacion-ukp7rd`. Mensajes de commit en
español, en imperativo, describiendo el porqué cuando no sea obvio.
