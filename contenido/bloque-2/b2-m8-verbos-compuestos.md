---
id: b2-m8-verbos-compuestos
bloque: 2
titulo: "Verbos compuestos: encadenar sin perder el hilo"
tipo: ejercicio
duracion_min: 50
requisitos: [b2-m7-detectar-anomalias]
desbloquea: [b2-m9-que-no-es-ninguno]
caduca: bajo
objetivos:
  - "Descomponer una tarea propia en la cadena de verbos que la forma"
  - "Calcular el acierto esperado de una cadena de tres pasos"
  - "Colocar un punto de control donde cada eslabón produzca algo revisable en 30 segundos"
conceptos: [verbo, cadena, punto-de-control, verificacion]
dataset: [dataset/ficheros/correos/, dataset/ficheros/tickets.xlsx]
---

Casi ninguna tarea real es un verbo suelto. «Pásame los correos de esta semana a una
tabla y dime cuáles pintan mal» son tres: extraer, clasificar y detectar anomalías. La
mala noticia de encadenar es aritmética y no se arregla con mejores instrucciones. La
buena es que se contrarresta con una cosa muy barata: mirar entre eslabón y eslabón.

## La aritmética que nadie hace

Si cada paso acierta el 90 %, tres pasos encadenados no aciertan el 90 %. Aciertan
0,9 × 0,9 × 0,9 = **73 %**. Sobre 20 correos, cinco o seis mal al final.

| Acierto por paso | 2 pasos | 3 pasos | 5 pasos |
|---|---|---|---|
| 99 % | 98 % | 97 % | 95 % |
| 95 % | 90 % | 86 % | 77 % |
| 90 % | 81 % | 73 % | 59 % |
| 80 % | 64 % | 51 % | 33 % |

Mira la última fila. Un 80 % por paso suena aceptable en una conversación y a los cinco
pasos has tirado dos tercios del trabajo.

No es exacto: a veces un fallo del paso 1 se corrige solo en el paso 3, y a veces el
paso 2 lo amplifica. Pero el orden de magnitud es ése, y el orden de magnitud es lo que
necesitas para decidir cuántos eslabones te puedes permitir. La respuesta casi siempre
es: menos de los que pensabas.

## El error no se queda quieto: cambia de forma

Esto es peor que la aritmética y es lo que de verdad hay que entender.

Supón que al extraer se te cuela el cliente equivocado en 2 de 20 filas. En el paso 2
esas dos filas se clasifican **perfectamente**: la categoría que les corresponde por lo
que pone en la fila. En el paso 3, el detector de rarezas las mira y no ve nada:
parecen normales, porque lo son. Sales con una tabla limpia, ordenada y con dos filas
falsas dentro.

Un error que sobrevive a la cadena sale disfrazado de resultado. Al final ya no se ve,
y si lo ves no sabes en qué paso ocurrió. Por eso el sitio donde se mira no es el final.

## Puntos de control: la regla de los 30 segundos

**Cada eslabón tiene que producir algo que puedas revisar en treinta segundos.** No
«léete las 20 extracciones»: un recuento.

| Después de | El control de 30 segundos | Qué te dice |
|---|---|---|
| Extraer | Cuántas casillas han quedado en «no consta», por columna | Si en un origen sucio salen cero, algo se ha rellenado solo |
| Clasificar | El reparto por categoría y cuántos en «otros» | Una categoría con 0 casos o un «otros» del 30 % significa que la lista está mal, no la clasificación |
| Detectar anomalías | Cuántas marcas, y tres de ellas abiertas al azar | Si no puedes ir a la fila concreta, la marca no existe |

Y una regla de diseño que sale de ahí: **si un eslabón no produce nada mirable, o lo
juntas con el siguiente o partes la tarea de otra manera.** Un paso cuyo resultado no
se puede comprobar no es un paso, es un salto de fe.

¿Dónde se pone el control si solo puedes poner uno? Después del primer paso. Todo lo
demás se construye encima, y un fallo ahí no se nota nunca más.

## Cuándo esto falla

- **Encadenar porque se puede.** Una tarea de seis minutos que haces tres veces al mes
  no necesita cadena. Montarla cuesta más que hacerla a mano el resto de tu vida
  laboral.
- **Cadena sin control intermedio.** Sale algo raro al final, no sabes de qué eslabón
  viene, y arreglas el que más se ve. Normalmente el que menos culpa tenía.
- **Un control que cuesta lo mismo que el trabajo.** Si comprobar el paso 2 te lleva lo
  que te llevaría hacer el paso 2 a mano, no encadenes: hazlo a mano y ahórrate el
  montaje.
- **Encadenar sobre una lista de categorías que no está cerrada.** El paso 2 arrastra
  al 3 y al 4. Si la taxonomía está mal, la cadena entera produce basura ordenada.
- **Creer que el eslabón débil es el último.** Casi siempre es el primero.
- **Que el resultado final no se pueda comprobar contra nada.** Si al terminar no puedes
  coger seis filas y contrastarlas con el origen, la cadena no vale por bien que suene
  lo que devuelve.

## Las tres instancias

| Dónde | La cadena | Dónde se mira |
|---|---|---|
| **Tu sector (CX)** | Correos → tabla → categoría → marcar lo raro | Después de la tabla: cuántos campos vacíos |
| **Otro trabajo** | En una gestoría: extraer los datos de 40 facturas → clasificar por régimen → señalar las que no cuadran con el trimestre anterior | Después de extraer, mirando solo los importes y el CIF. Un CIF mal leído convierte todo lo demás en decorado |
| **Tu casa** | Fotos de los tíquets del súper → tabla de gastos → clasificar por tipo → ver en qué se te va el mes | Después de la tabla: que los totales de cada tíquet cuadren con lo que pone abajo del papel. Si no cuadran, el resto de la cadena es una novela |

En los tres, el control barato está justo detrás del primer paso y consiste en contar
algo, no en releerlo todo.

## Ejercicio

Material: tu `extraccion-correos.md` del verbo 2 y tu `taxonomia-tickets.md` del verbo
1. Hoy no se extrae nada nuevo: se encadena lo que ya tienes.

1. **Paso 1 — la tabla que ya hiciste** (5 min). Quédate con 20 filas de tu extracción.
   Si no la conservaste, extrae 20 correos de `dataset/ficheros/correos/` con las mismas
   seis columnas.
2. **Control 1** (30 s). El recuento de `no consta` por columna. Ya lo tienes del verbo
   2: entonces era el final de una tarea, hoy es el primer control de una cadena. Si sale
   cero, no sigas.
3. **Paso 2 — clasificar** (12 min). Añade una columna `categoria` y asigna a cada fila
   una categoría de tu taxonomía, sin inventar ninguna nueva. Tu lista salió de los
   tickets y ahora la aplicas a correos: anota **cuántas filas no encajan y por qué**.
   Eso dice algo de la lista, no de los correos.
4. **Control 2** (30 s). Reparto por categoría y cuántos en «otros». Anótalo.
5. **Paso 3 — detectar** (10 min). Escribe en tres líneas qué es una fila normal de tu
   tabla y marca las que se salgan. Hay al menos tres formas de salirse: dos incidencias
   en un mismo correo, cliente no identificable y fecha que no encaja.
6. **Control final** (10 min). Coge tres filas marcadas y tres sin marcar y compáralas
   con su correo original. Cuenta los errores: ese número sobre seis es el acierto de tu
   cadena **medido**, no supuesto. Y por cada error, anota **en qué paso nació**. Casi
   ninguno nace en el último.
7. **Tu cadena** (5 min). Coge una tarea tuya del inventario del bloque 1 que resultara
   ser más de un paso y escríbela con flechas: verbo → verbo → verbo. Marca dónde
   pondrías tú el control y por qué ahí. Va a la tabla «Mis cadenas» de tu catálogo.

**Entregable:** la tabla con sus dos columnas nuevas, los tres controles con su número,
tu cadena escrita con flechas, y una frase: «el eslabón débil de mi cadena fue \_\_\_, y lo sé porque \_\_\_.»

**Regla de parada:** hoy montas los eslabones y miras entre uno y otro, a mano. Dejar
esto corriendo de un tirón se ve en `b5-m4-encadenar-y-controles`, «Encadenar pasos y
poner los controles humanos». El orden tiene razón de ser: no se deja sola una cadena de
la que aún no sabes por dónde se rompe.

## Escribe tú la regla

En tu catálogo, en la tabla «Mis cadenas», y en la bitácora:

- «Parto una tarea en cadena cuando \_\_\_, y no la parto cuando \_\_\_.»
- «Pongo el punto de control después de \_\_\_, porque \_\_\_.»

## Para la bitácora

- ¿Cuántos «no consta» te salieron, y qué columna se llevó la mayoría?
- De los seis contrastes del control final, ¿cuántos fallaron y en qué paso nacieron?
- ¿Qué tarea tuya llevas tratando como un paso y en realidad son tres?
