---
id: b2-m3-extraer
bloque: 2
titulo: "Verbo 2: extraer"
tipo: ejercicio
duracion_min: 45
requisitos: [b2-m2-clasificar]
desbloquea: [b2-m4-transformar]
caduca: bajo
objetivos:
  - "Extraer seis campos fijos de 25 correos desordenados a una tabla"
  - "Aplicar la columna «no consta» y contar cuántas veces aparece"
  - "Verificar cinco filas contra el correo original y marcar lo que no estaba escrito"
conceptos: [extraer, dato-estructurado, verificacion, verbo]
dataset: [dataset/ficheros/correos/]
profundizar:
  - id: b2-p2-limites-de-la-extraccion
    titulo: "Dónde se rompe la extracción"
---

Extraer es el verbo con mejor relación entre esfuerzo y ahorro en una empresa pequeña.
Es también el que se rompe de la forma más silenciosa: cuando el dato no está en el
texto, aparece igualmente en la tabla, bien escrito y con el formato correcto. Este nodo
te deja una técnica de defensa que vale para el resto del curso y se aplica en dos
minutos.

## Qué es

Sacar datos concretos de un texto desordenado y ponerlos en campos con nombre. Es lo
que convierte 200 correos en una tabla sobre la que se puede pensar.

La diferencia con leer es de resultado. Leer 200 correos te deja una impresión —«hay
mucha queja de entregas»— que no se puede contar, ni ordenar, ni enseñar a nadie.
Extraerlos te deja una tabla que se cuenta, se ordena y se cruza con otro fichero.
Todos los verbos siguientes necesitan que alguien haya hecho antes este.

## Cuándo brilla

- **Volumen con campos fijos.** 200 correos a minuto y medio de leer y copiar a mano
  son cinco horas. Y hay que repetirlo el mes que viene.
- **Cuando la salida es una tabla.** Una tabla se cuenta, y contar es la forma más
  barata de verificar. Un texto no te avisa de nada; una columna con veinte huecos, sí.
- **Cuando el texto es un desastre pero el dato, cuando está, está escrito.** Correos
  con el asunto en blanco y la incidencia en la tercera línea, hilos que empiezan por
  `RE:` sin que exista el original, reenvíos con tres niveles de `>` y el dato útil al
  final. Todo eso lo aguanta bien.

Lo que no arregla: que el dato no exista. Ahí es donde falla.

## Cuándo esto falla

- **El dato no está y se rellena igual.** Es el fallo grave del verbo, y no se parece
  a un error: se parece a un acierto. La casilla sale con formato de número de pedido,
  con el aspecto de los demás, y es inventada. Nadie lo nota mirando la tabla, porque
  en la tabla no queda ninguna marca.
- **El dato está dos veces y no coincide.** El asunto dice «pedido del martes» y el
  cuerpo dice el jueves. Si no has escrito antes qué manda, gana lo que aparezca
  primero, y esa decisión la ha tomado el orden del texto, no tú.
- **Unidades y formatos.** Fechas escritas de tres maneras, importes con coma y con
  punto, teléfonos en cuatro formatos, códigos postales que pierden el cero de delante.
  Un campo mal formateado no se suma y no se cruza: la tabla parece completa y no sirve.
- **Dos incidencias en un solo correo.** ¿Una fila o dos? Las dos respuestas son
  válidas; lo que no vale es no haberlo decidido, porque entonces unas veces será una y
  otras dos y el recuento final no significa nada.
- **La extracción «casi bien» que nadie comprueba.** Un 95% de acierto sobre 200
  correos son diez filas mal, y ninguna lleva marca.

### La defensa: la columna «no consta»

Se pide desde el principio, antes de extraer nada: **cuando un dato no esté escrito en
el texto, se escribe literalmente `no consta`. No se deduce, no se completa, no se
mira en otro sitio.**

Y después se cuenta cuántas veces aparece. Ése es el número que de verdad importa de
esta tabla, más que cualquier otro.

> [!WARNING]
> Si en un montón de correos escritos con prisa la columna «no consta» sale vacía o
> casi vacía, la primera hipótesis no es que los correos vinieran estupendos. Es que
> alguien ha rellenado los huecos. Sospecha, y ve a comprobar tres filas.

Un «no consta» no es un fallo de la extracción: es información. Te dice qué le falta a
tu material antes de que construyas nada encima. Si la referencia de pedido
falta en la mayoría de los correos, eso no se arregla extrayendo mejor: se arregla
pidiéndosela al cliente cuando escribe, y eso ya es un cambio de proceso.

## Las tres instancias

| Dónde | Qué se extrae | Dónde aparece el «no consta» |
|---|---|---|
| **Tu sector (CX)** | De un correo de cliente: quién escribe, referencia de pedido, qué pide y para cuándo | La referencia de pedido. Es el campo que más falta y el que más se inventa, porque tiene una forma muy reconocible y es fácil de imitar. |
| **Otro trabajo** | En una gestoría, de una factura recibida: NIF, fecha, base imponible, tipo de IVA | El tipo de IVA cuando la factura solo trae el total. Deducirlo es una cuenta, no una extracción, y si nadie lo declara ya no sabes qué casillas son dato y cuáles son estimación. |
| **Tu casa** | De una receta: ingredientes y cantidades para la lista de la compra | «Un chorro de aceite», «sal al gusto». Cantidad: no consta. Si en tu lista pone «100 ml», ese número lo has puesto tú. |

## Ejercicio

**Material:** `dataset/ficheros/correos/` (200 ficheros `.eml`) o el mismo contenido
junto en `dataset/ficheros/bandeja.mbox`. Trabaja con **25 correos**.

**1. Escribe las reglas antes de extraer nada (5 min).** Tres decisiones, por escrito:

- Si el asunto y el cuerpo se contradicen, ¿cuál manda?
- Si un correo trae dos incidencias, ¿es una fila o dos?
- Formato único de fecha: `AAAA-MM-DD`.

**2. Extrae a la tabla (15 min).** Seis columnas, ni una más:

| Columna | Qué va |
|---|---|
| `fichero` | Nombre del correo, para poder volver a él |
| `cliente` | Quién escribe, tal y como aparece |
| `fecha_de_los_hechos` | Cuándo pasó lo que cuenta, no cuándo se envió el correo |
| `referencia` | Número de pedido o de factura |
| `que_pide` | En menos de diez palabras |
| `adjunto_mencionado` | Sí o no |

**Regla que gobierna toda la tabla:** cualquier casilla cuyo dato no esté escrito en el
texto se rellena con `no consta`. Nada de deducir por contexto.

**3. Cuenta (7 min).** Cuántos `no consta` hay en cada columna. Cuántas filas te han
salido y por qué no son 25 si no son 25. Cuántos correos dicen que adjuntan algo.

**4. Verifica cinco filas (8 min).** Elige cinco al azar, abre su correo original y
comprueba casilla por casilla. Marca cada dato que no esté **literalmente** escrito en
el texto. Una sola marca en cinco filas ya te dice que las otras veinte hay que
mirarlas.

**Entregable:** `extraccion-correos.md` o una hoja con la tabla, las tres reglas del
paso 1, el recuento de `no consta` por columna y las marcas de la verificación. Cierra
con una línea: qué columna tiene más huecos y qué significa eso para quien tenga que
usar esa tabla para algo.

**Regla de parada:** no extraigas los 200. Con 25 ya sabes si tu método es fiable, y si
no lo es, extraer 200 solo multiplica el problema por ocho.

## Antes de pasar al siguiente

Los correos con los que has trabajado son de una empresa inventada. Con correos de
verdad hay una pregunta previa —qué se puede pegar y dónde— y tiene respuesta larga:
`b3-m7-datos-y-rgpd`, «Datos y RGPD: qué no se pega jamás». No la improvises ahora.

Y si te has topado con un PDF escaneado, una tabla partida en dos columnas o un dato
que aparece con dos valores distintos, esos son los casos duros del verbo:
`b2-p2-limites-de-la-extraccion`, «Dónde se rompe la extracción».

## Escribe tú la regla

En la bitácora, con tus palabras:

- «Una tabla extraída de un texto no me la creo hasta que \_\_\_.»
- «Cuando una casilla se queda vacía, lo que hago es \_\_\_, y lo que no hago nunca es
  \_\_\_.»

## Para la bitácora

- ¿Cuántos `no consta` te han salido, y en qué columna se concentran?
- ¿Cuántas marcas hiciste en la verificación de las cinco filas? ¿Qué tipo de dato
  fallaba: nombres, fechas o referencias?
- ¿Qué tarea tuya se parece a esto? Apunta cuántos minutos te lleva al mes copiar datos
  de un texto a una hoja.
