# Programa "CX + IA"

Curso autodidacta, autocontenido y profundo para una profesional de atención al
cliente en una PyME. No enseña herramientas de IA: enseña a **ver el trabajo como
procesos, decidir qué delegar a una máquina, verificar lo que la máquina produce y
rediseñar cómo se trabaja.**

La fuente de verdad conceptual es [`ESPECIFICACION.md`](ESPECIFICACION.md). Este
repositorio la implementa. **Si el código contradice ese documento, gana el
documento** hasta que se actualice explícitamente.

---

## Qué hay aquí

```
contenido/          Los nodos del curso. Markdown con frontmatter (§6).
  bloque-0 … 6/       Tronco lineal, un directorio por bloque.
    profundizacion/   Ramas opcionales: "esto me interesa, quiero más".
  glosario/           glosario.yml → glosario global autogenerado.
dataset/            El gemelo sintético: Aguas del Norte, S.L. (§4).
  generador/          Notas del generador.
  ficheros/           Lo que ve la alumna. Sucio a propósito.
  SOLUCIONES/         Las verdades escondidas. Excluido del sitio publicado.
ejercicios/
  sabotaje/           Seis niveles de dificultad (§5.1).
  rubricas/           Corrección de tres niveles (§5.3).
plantillas/         Los artefactos en blanco que ella rellena.
tutor/              Prompts por modo y guardarraíles (§7).
sitio/              MkDocs Material.
scripts/            Generador del dataset, validador del grafo, verificador.
docs-internos/      Contratos de construcción. No se publican.
```

## Estado

| Fase (§8) | Estado |
|---|---|
| 0 — Esqueleto, frontmatter, validador del grafo | hecha |
| 1 — Generador del dataset con las verdades escondidas | hecha |
| 2 — Bloques 1–3 completos (más el bloque 0 de entrada) | hecha |
| 3 — Sitio estático navegable en móvil | hecha |
| 4 — Tutor con los 5 modos y guardarraíles | hecha |
| **— PILOTO CON ELLA —** | **pendiente** |
| 5 — Bloque 4 (CX), diseñado con lo aprendido en el piloto | esqueleto |
| 6 — Bloques 5–6 | esqueleto |

En números: **45 nodos escritos** de 71 (los otros 26 son los bloques 4–6, a propósito),
**106 conceptos** en el glosario, **9 plantillas** de artefacto, **6 ejercicios de
sabotaje** (uno por nivel de §5.1), y un dataset de 300 clientes, 5.400 líneas de pedido,
800 tickets y 200 correos con sus cinco verdades escondidas verificables.

Los bloques 4–6 existen en el grafo con su temario y `estado: pendiente-piloto`,
sin contenido escrito. Es deliberado: §3 dice que el bloque 4 *"se diseña mucho
mejor sabiendo dónde se atascó de verdad"*. Ver `docs-internos/decisiones.md` (D1 y D11).

Los bloques 1+2+3 ya son un curso completo por sí solos (§9).

## Cómo llega esto a ella

El entregable **no es este repositorio**: es una dirección web que abre en el móvil, sin
instalar nada y sin cuenta.

| | Sitio | Tutor | Con el repo privado |
|---|---|---|---|
| **Cloudflare Pages** — recomendado | sí | sí | gratis |
| **GitHub Pages** — ya configurado en `.github/workflows/sitio.yml` | sí | no | requiere plan de pago o hacer público el repo |

El tutor necesita ejecutar código en servidor para que la clave de API no esté en el
navegador (§7.5), y GitHub Pages no ejecuta nada. Todo lo demás —nodos, ejercicios,
sabotajes, dataset, plantillas y la página **Dónde vas**— funciona igual en los dos.

Para el piloto, GitHub Pages basta: el tutor se puede encender después, y mientras tanto
el widget dice que no está activo en vez de fingir un error.

Los pasos concretos están en [`docs-internos/despliegue.md`](docs-internos/despliegue.md).

### Lo que ella ve

1. **La portada** le dice qué se lleva y qué el curso no hace.
2. **La navegación lateral** son los seis bloques en orden, con las ramas de
   profundización colgando de su nodo.
3. **Cada nodo** lleva arriba su tipo, su duración y su etiqueta de caducidad, y abajo
   dos casillas —«ya lo he intentado» y «nodo terminado»— más el tutor.
4. **Dónde vas** reúne lo que ha marcado, cuál es el siguiente nodo desbloqueado y cómo
   va su portfolio de artefactos.
5. **Sus artefactos y su bitácora son ficheros suyos**, en su ordenador. El curso le da
   la plantilla y la rúbrica; el documento no pasa por ningún servidor.

## Puesta en marcha

```bash
pip install -r requirements.txt

make dataset     # genera el gemelo sintético (semilla fija, reproducible)
make verificar   # comprueba que las 5 verdades escondidas siguen siendo derivables
make validar     # valida el grafo de nodos: ciclos, referencias, alcanzabilidad
make sitio       # levanta el sitio en local
make todo        # las cuatro cosas
```

El tutor necesita además una clave de API en la función serverless. Ver
[`tutor/README.md`](tutor/README.md). **La clave nunca va en el cliente** (§7.5).

## Cómo se añade contenido

1. Da de alta el nodo en `docs-internos/registro-de-nodos.yml`. Es el contrato.
2. Escribe el `.md` en el directorio de su bloque, respetando
   `docs-internos/esquema-frontmatter.md` y `docs-internos/guia-de-estilo.md`.
3. `make validar`. Si el grafo no valida, no entra.

## Principios que no se negocian

Están en `ESPECIFICACION.md` §2 y se aplican en cada nodo:

1. **Artefacto sobre lección.** Ningún módulo termina en "has leído".
2. **Concreto → patrón → generalización escrita por ella.**
3. **Tres instancias por patrón:** su sector, otro dominio profesional, vida personal.
4. **La verificación es la asignatura troncal.**
5. **Fallar es diagnóstico, no fracaso.**
6. **Regla de parada explícita.** El nivel 3 de la escalera es un éxito, no un techo.
7. **Sin gamificación.** Minutos ahorrados y portfolio; ni una insignia.

Y uno que atraviesa el repositorio entero: **el curso funciona al 100% sin un solo
dato real de su empresa.** Nunca se le pide que suba nada.
