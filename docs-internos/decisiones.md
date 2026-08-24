# Registro de decisiones

Decisiones tomadas al implementar `ESPECIFICACION.md`, con su justificación. La
especificación manda; esto documenta dónde se ha concretado algo que ella dejaba
abierto y dónde se ha añadido algo que no estaba.

---

### D1 — Alcance de esta entrega: fases 0 a 4

`ESPECIFICACION.md` §8 fija el orden de construcción y coloca un hito explícito:
**"— PILOTO CON ELLA —"** entre la fase 4 (tutor) y la fase 5 (bloque 4). §3 lo
refuerza: *"los bloques 1–3 se escriben, se publican y se pilotan ANTES de escribir
el 4. El bloque 4 se diseña mucho mejor sabiendo dónde se atascó de verdad."*

Se implementan por tanto las fases 0–4 completas. Los bloques 4, 5 y 6 quedan como
nodos de esqueleto con `estado: pendiente-piloto`: tienen frontmatter válido, están
en el grafo, se validan y se publican como índice con su temario, pero no llevan
contenido escrito. Escribirlos ahora sería contradecir la especificación.

El input para escribirlos ya está previsto: el registro de preguntas del tutor
(§7.4, uso 2: *"Tú ves dónde se atasca la gente → es el input directo para escribir
el bloque 4"*).

### D2 — Bloque 0 "Antes de empezar"

La especificación describe seis bloques y no menciona una entrada al curso. Pero
§2.5 exige que "fallar es diagnóstico" se le diga **antes del primer ejercicio**, §5.5
necesita que la bitácora exista desde la primera sesión, y §9 pide "expectativas
honestas desde la primera página".

Eso no cabe dentro del bloque 1 sin desvirtuarlo: el bloque 1 empieza sin IA y con
el diario. Se añaden cuatro nodos cortos (`b0-m1`…`b0-m4`, ~70 min en total) que
cubren esas tres obligaciones. No es un séptimo bloque de materia: es el umbral.

### D3 — `b1-m9-primera-victoria`

§9 identifica el riesgo de abandono en el bloque 1 y su mitigación: *"una victoria
pequeña con IA al final de la semana 1 como anticipo"*. Se materializa como nodo
propio en lugar de como párrafo, para que sea ejecutable y medible, y cuelga de
`b1-m2` (el diario) porque necesita la línea base para poder medirse.

El nodo dice de forma explícita que es un anticipo y que el método llega en el
bloque 3, para que no confunda la victoria con el método.

### D4 — `b2-m1-mapa-de-lo-posible`

El bloque 2 de la especificación empieza directamente por el verbo 1, pero su
párrafo de apertura contiene una tesis que merece nodo: *"la gente no automatiza lo
que no sabe que es automatizable... es falta de imaginación informada"*. Se convierte
en nodo de entrada del bloque. No añade materia nueva; da el marco antes de los seis
verbos.

### D5 — Aristas del bloque 3

El frontmatter de ejemplo de §6 declara `b3-m4-sabotaje` con
`desbloquea: [b3-m6-verificacion-proporcional]`. Pero el orden de contenidos de §3
(3.4 sabotaje → 3.5 modos de fallo → 3.6 verificación proporcional) es
pedagógicamente deliberado: **primero falla, después la taxonomía del fallo**.

Se respetan ambas cosas: `b3-m4` declara `desbloquea: [b3-m5, b3-m6]` y `b3-m6`
declara `requisitos: [b3-m4, b3-m5]`. La arista literal del ejemplo existe y la
cadena pedagógica también.

### D6 — Enlace de los nodos de profundización

§6 dice que las ramas de profundización son opcionales. Si el padre las listara en
`desbloquea`, aparecerían como paso siguiente del tronco y dejarían de ser
opcionales. Regla adoptada: el padre las lista en `profundizar`, el hijo declara
`requisitos: [padre]` y `desbloquea: []`, y el validador exceptúa a este par de la
regla de reciprocidad. Documentado en `esquema-frontmatter.md`.

### D7 — Siete plantillas de artefacto, no seis

§5.4 habla de "6 artefactos reales", uno por bloque. Pero el bloque 3 produce dos
(§3: *"`plantilla-de-verificacion.md`... Y su primer `contexto-trabajo.md`"*) y la
bitácora (§5.5) es un fichero propio suyo que también necesita plantilla. El
portfolio de cara a ella sigue siendo de 6 artefactos; las plantillas en blanco son
más porque hay piezas de apoyo.

### D8 — MkDocs Material

§8 ofrece la elección: *"MkDocs Material es la opción de menor fricción; Astro si se
quiere más control sobre el tutor"*. Se elige MkDocs Material.

Razones: la lectura en móvil y la búsqueda ya vienen resueltas y son requisito
explícito de §8; el contenido es markdown con frontmatter y no necesita capa de
componentes; el tutor es un widget de ~300 líneas de JavaScript contra una función
serverless, y eso funciona igual embebido en MkDocs. Astro añadiría un sistema de
build entero para una ganancia que aquí no se cobra.

Si en el futuro el tutor creciera hasta necesitar estado de aplicación de verdad,
migrar el sitio no obliga a tocar el contenido: los nodos son markdown y el
frontmatter es agnóstico. La decisión es reversible y está aislada en `/sitio`.

### D9 — El dataset se genera, no se versiona a mano

§4 exige reproducibilidad desde script con semilla fija. Los ficheros generados se
versionan igualmente (para que ella pueda clonar y trabajar sin ejecutar nada), pero
la fuente de verdad es `scripts/generar-dataset.py` y **nunca se editan a mano**.
`dataset/SOLUCIONES/` sí se versiona: es lo que hace posible la corrección objetiva
de §5.3. Lo que no se hace es publicarlo en el sitio.

### D10 — Verificación del dataset como test de regresión

Añadido no pedido explícitamente, pero implícito en §4 (*"como los datos los
generamos nosotros, existe respuesta correcta"*): `scripts/verificar-verdades.py`
reconstruye las cinco verdades escondidas **sin leer `SOLUCIONES/`**. Si una verdad
deja de ser derivable desde los ficheros publicados, el ejercicio central del bloque
4 sería irresoluble y el script falla. Es la garantía de que el corrector automático
del curso sigue teniendo respuesta correcta.

### D11 — Los bloques 4–6 no tienen fichero `.md`, y es deliberado

Podría haberse creado un `.md` de esqueleto por cada nodo de los bloques 4, 5 y 6. No
se ha hecho, por dos razones:

1. **Un fichero vacío miente.** Un `.md` con frontmatter y sin cuerpo pasa el validador
   y aparenta que el nodo existe. Al mes siguiente nadie recuerda cuáles estaban de
   verdad escritos.
2. **El registro ya es la fuente de verdad.** `scripts/construir-sitio.py` genera la
   página de un nodo `pendiente-piloto` a partir de su entrada del registro: título,
   duración prevista y **por qué todavía no está escrito**. Es una página útil para la
   alumna, no un hueco.

   Durante un tiempo esa página imprimía además el `brief`, que es el encargo interno
   y en cuatro casos nombra la verdad escondida del nodo. Ya no: ver D12 y
   `FUGA-BLOQUE-4.md`. Un campo que el contrato declara no publicable no se publica
   «porque queda bien en la página».

Consecuencia en las herramientas: `validar-grafo.py` trata "nodo `escrito` sin fichero"
como **error** y "nodo `pendiente-piloto` sin fichero" como **aviso**. Escribir uno de
esos nodos consiste en crear su `.md` y cambiar su `estado` en el registro; el
validador empieza a exigirlo automáticamente.

### D12 — Las comprobaciones de fuga van por contenido, no por procedencia

Durante semanas el sitio publicó las respuestas del ejercicio central del bloque 4
con `scripts/comprobar-build.py` en verde. El comprobador miraba de dónde venía cada
fichero —que nada saliera de `dataset/SOLUCIONES/`— y tenía razón: no salía. Lo que
no miraba es qué decían los ficheros, y las respuestas estaban escritas a mano en el
glosario, en el `brief` de los nodos pendientes, en un sabotaje y en tres sitios más
(`FUGA-BLOQUE-4.md`).

De ahí `scripts/centinelas.py`: las cinco verdades escritas como patrones, y las tres
comprobaciones que sirven algo aplicándolos —el build, el paquete del tutor y el
barrido de las fuentes—. Tres decisiones de diseño que no son obvias:

1. **Por franja, no por cifra clavada.** «El 40 % de los correos hablan de facturas»
   es V1 igual de bien que «el 38,00 %». Un centinela que sólo busque la cifra exacta
   protege del copiar y pegar, que es el caso que menos pasa.
2. **Conjuntivos.** Un porcentaje sólo delata si cerca hay además un conjunto y un
   tema. Sin eso el bloque 2 no podría enseñar que un «Otros» por encima del 10 % es
   señal de taxonomía mala, porque esa regla y el dato real se escriben igual.
3. **Con autoprueba.** Los centinelas se ejecutan contra la clave de corrección antes
   de barrer nada, y si alguno no reconoce ahí su propia verdad, el proceso falla. Un
   centinela mudo es peor que no tenerlo: da por limpio lo que no ha mirado.

La raya que aplican está escrita en la cabecera del módulo y en `FUGA-BLOQUE-4.md`:
**la suciedad se anuncia, la respuesta no**. Decir «hay clientes duplicados» es un
aviso que ella necesita; decir cuántos, cuáles o cómo se encuentran es el ejercicio.

