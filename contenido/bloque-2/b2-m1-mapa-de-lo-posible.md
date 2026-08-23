---
id: b2-m1-mapa-de-lo-posible
bloque: 2
titulo: "El mapa de lo posible"
tipo: concepto
duracion_min: 30
requisitos: [b1-m8-inventario-de-procesos]
desbloquea: [b2-m2-clasificar]
caduca: bajo
objetivos:
  - "Nombrar con un verbo o una cadena cada tarea de tu inventario"
  - "Distinguir un patrón de un producto y decir por qué uno dura más que el otro"
  - "Separar «esto se puede delegar» de «esto se debe delegar»"
conceptos: [patron, imaginacion-informada, verbo]
---

Tienes un inventario de tareas puntuadas y ordenadas. Sabes cuáles pesan, cuáles no
sabrías explicar y cuáles quizá no deberían existir. Falta la otra mitad de la
decisión: qué se le puede encargar a una máquina. Eso no es una pregunta de criterio.
Es una pregunta de vocabulario, y este bloque son seis palabras.

## El agujero no está en tu criterio

Una administrativa lleva tres años copiando a mano el número de pedido de los correos
de clientes a una hoja de cálculo. Cuarenta correos al mes, tres minutos cada uno: 120
minutos al mes, tres jornadas al año. No lo hace por gusto ni porque haya
decidido que no se puede delegar. Lo hace porque nunca se le ha ocurrido que esa
operación tenga nombre.

Ése es el problema que resuelve este bloque. **La gente no automatiza lo que no sabe
que es automatizable.** No es un fallo de pensamiento crítico: pregúntale a esa mujer
si se fiaría de una máquina para contestar a un cliente enfadado y te dará una
respuesta perfectamente prudente. Le falta imaginación informada, que es otra cosa: no
tiene la lista de lo que existe.

El agujero se nota en las dos direcciones a la vez: se dejan sin tocar durante años
cosas mecánicas y a la vez se piden imposibles —«que me lleve la relación con los
clientes»—. El bloque 1 te dio el criterio; lo que faltaba eran las opciones sobre las
que aplicarlo.

## Patrones, no productos

Un mapa de productos caduca en seis meses: cambian los nombres, los precios y quién
compra a quién. Un mapa de patrones no. Clasificar documentos, sacar datos de un texto
o comprobar algo contra una norma se llevan haciendo décadas: primero a mano, después
con reglas, ahora de otra forma. Cambia el instrumento, no la operación.

Y hay una razón práctica. Con los verbos en la cabeza, una herramienta nueva se
evalúa en diez minutos con tres preguntas:

1. ¿Cuál de los seis verbos hace?
2. ¿Cómo compruebo lo que devuelve, y en cuánto tiempo?
3. ¿Qué pasa si falla una de cada veinte veces?

Sin ellos, evaluar una herramienta consiste en leerte su página web y creértela.

Por eso aquí no vas a ver un nombre de producto hasta el último nodo del bloque,
`b2-p5-herramientas-hoy`, «Apéndice desechable: cómo está el panorama ahora mismo»,
marcado con caducidad alta y con fecha de revisión en la cabecera. Está al final a
propósito: el día que se quede viejo se sustituye entero sin tocar nada más.

## Los seis verbos

| Verbo | Qué hace | Un ejemplo mínimo |
|---|---|---|
| **Clasificar** | Mete cada cosa en una categoría de una lista cerrada | 800 tickets, cada uno con su tipo de incidencia |
| **Extraer** | Saca datos concretos de un texto desordenado y los pone en campos | De un correo: cliente, fecha, referencia de pedido |
| **Transformar** | Cambia de formato conservando el contenido | Un hilo de cuatro correos convertido en un parte de cinco líneas |
| **Redactar borrador** | Produce un primer texto que tú corriges | Una respuesta a una reclamación que reescribes a medias |
| **Comparar contra criterio** | Evalúa algo frente a una norma escrita | Una respuesta enviada, contra lo que dice el procedimiento |
| **Detectar anomalías** | Encuentra lo que se sale de una normalidad definida antes | Líneas de pedido con cantidad negativa |

Seis, y no es una lista corta por resumir. No describen todo lo que existe: describen
lo que se puede encargar **y verificar** desde una oficina pequeña sin montar nada.
Esa segunda mitad es la que deja la lista en seis.

## Casi ninguna tarea es un solo verbo

Coge el informe semanal para gerencia de la semana inventada del bloque 1: cuatro
veces al mes, 35 minutos de mediana, 140 al mes. De lejos es «hacer el informe» y no
se puede delegar. De cerca son cuatro eslabones:

`extraer` (qué ha pasado, sacado de tickets y correos) → `clasificar` (agrupado por
tipo) → `detectar anomalías` (qué se sale de lo normal esta semana) → `transformar` (a
una página que se lea en dos minutos).

Tres de los cuatro son mecánicos. El cuarto —decidir qué se le cuenta a gerencia— no
es ninguno de los seis: es criterio tuyo y se queda contigo.

Esto pasa casi siempre. Cuando alguien dice «esta tarea no se puede automatizar», suele
estar hablando de la cadena entera y tiene razón sobre un eslabón. La ganancia está en
los otros tres. Encadenar tiene su precio —los errores no se quedan quietos, se
arrastran— y eso se trabaja en `b2-m8-verbos-compuestos`, «Verbos compuestos:
encadenar sin perder el hilo».

## Cómo va este bloque

Seis nodos, uno por verbo, todos con la misma forma: qué es, cuándo brilla, cuándo
falla y por qué, tres instancias y un ejercicio sobre el dataset. La repetición es
deliberada: un patrón no transfiere por entenderlo una vez, transfiere por reconocerlo
seis veces en sitios que no se parecen.

El dataset es una distribuidora de agua y bebidas inventada, Aguas del Norte: 300
clientes, 800 tickets, unos 1.900 pedidos, 200 correos y un manual interno. Sucio a
propósito, como el material real. Aquí tampoco vas a subir ni un dato tuyo. Después de
los seis verbos van las cadenas, lo que no es ninguno de los seis, y tu catálogo de
patrones: el artefacto 2 de 6.

## Cuándo esto falla

- **Forzar la tarea al verbo.** Si para que encaje tienes que retorcerla, o es una
  cadena o no es ninguno. Ninguna de las dos cosas es un fracaso: son dos diagnósticos
  distintos.
- **Confundir «se puede» con «se debe».** El verbo dice que la operación existe; si
  merece la pena lo dice el filtro del bloque 1. Una tarea de 40 minutos al mes se
  sigue aparcando aunque sea un clasificar de manual.
- **Nombrar el verbo y darlo por hecho.** Reconocer no es especificar. Entre «esto es
  un extraer» y que salga bien hay un encargo escrito: el bloque 3 entero.
- **Ponerle un verbo a una tarea que no debería existir.** Delegarla la deja instalada
  para siempre, y encima documentada. Si esa fila lleva un «no» en la columna de si
  debería existir, el verbo no es la respuesta.
- **Creer que la lista describe el universo.** El juicio con consecuencias, la
  responsabilidad legal y la relación humana no están en los seis, y no es un olvido:
  `b2-m9-que-no-es-ninguno`, «Lo que no es ninguno de los seis».

## Las tres instancias

| Dónde | La tarea | La cadena |
|---|---|---|
| **Tu sector (CX)** | Cuadrar albaranes con pedidos, 180 min/mes | extraer (los datos del albarán) → comparar contra criterio (contra el pedido) → detectar anomalías (lo que no cuadra) |
| **Otro trabajo** | En una gestoría, las 60 facturas de clientes que llegan por correo cada mes | extraer (fecha, base, IVA, NIF) → clasificar (por régimen) → comparar contra criterio (que no falte ningún dato obligatorio) |
| **Tu casa** | El correo de papel: banco, comunidad, seguro | clasificar (hay que hacer algo / archivar / tirar) → extraer (fecha límite e importe) → transformar (una línea en el calendario) |

Fíjate en el tercero: no hay ninguna herramienta de por medio y el patrón es idéntico.
Si un verbo solo funcionara en tu oficina, no sería un patrón: sería una costumbre.

## Ejercicio

**Qué:** ponerle nombre a lo que ya tienes escrito. Diez minutos.

Abre tu inventario del bloque 1 y añade una columna: **verbo o cadena**.

1. Para cada una de las diez tareas, escribe el verbo. Si son varios, con flechas y en
   el orden en que ocurren: `extraer → clasificar → transformar`.
2. Si no encaja ninguno, escribe `ninguno` y una línea de por qué. Esas filas son las
   más valiosas del inventario y las vas a volver a abrir en `b2-m9-que-no-es-ninguno`.
3. No toques ninguna puntuación. Hoy no se decide nada: se nombra.

**Entregable:** tu inventario con la columna nueva, guardado donde estaba.

**Regla de parada:** no elijas herramienta y no pruebes nada. El primer ejercicio con
el dataset es el nodo siguiente.

## Escribe tú la regla

En la bitácora, con tus palabras:

- «Cuando me cae una tarea nueva, antes de decidir si se puede delegar, me pregunto
  \_\_\_.»
- «Un patrón y un producto se distinguen en que \_\_\_.»

## Para la bitácora

- ¿Cuántas de tus diez tareas han resultado ser una cadena y no un verbo suelto?
- ¿Qué tarea llevabas años haciendo a mano sin saber que tenía nombre? Apunta sus
  minutos al mes: es el número contra el que vas a medir dentro de tres bloques.
- ¿Alguna se ha quedado en `ninguno`? Escribe qué la separa de las otras nueve.
