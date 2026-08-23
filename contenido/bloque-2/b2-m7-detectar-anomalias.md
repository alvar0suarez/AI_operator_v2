---
id: b2-m7-detectar-anomalias
bloque: 2
titulo: "Verbo 6: detectar anomalías"
tipo: ejercicio
duracion_min: 45
requisitos: [b2-m6-comparar-contra-criterio]
desbloquea: [b2-m8-verbos-compuestos]
caduca: bajo
objetivos:
  - "Escribir la definición de normalidad de un conjunto antes de buscar rarezas en él"
  - "Contar las líneas de pedidos.xlsx que se salen de esa definición"
  - "Decidir de cada rareza si importa o solo llama la atención"
conceptos: [anomalia, patron, normalidad, verbo]
dataset: [dataset/ficheros/pedidos.xlsx]
profundizar:
  - id: b2-p4-anomalia-no-es-error
    titulo: "Una anomalía no es un error"
---

Este verbo tiene una precondición que casi nadie declara: para saber qué es raro hay
que haber escrito antes qué es normal. Sin esa frase escrita no encuentras anomalías,
encuentras cosas que te llaman la atención, que es otra cosa y no sirve para decidir
nada. Aquí escribes la normalidad de un fichero de pedidos y luego cuentas lo que se
sale.

## Qué es

Encontrar, dentro de un conjunto, los casos que se salen de lo que has definido como
normal. La segunda mitad de esa frase es el verbo entero: sin definición previa no hay
anomalías, hay cosas que te llaman la atención.

Prueba a pedir «mira estos pedidos y dime qué te parece raro». Te devuelve una lista:
un pedido de un domingo, un cliente que compró una sola vez, un importe alto. Todo
cierto y ninguna útil, porque nadie ha dicho contra qué son raros.

Ahora escribe primero esto:

> Un pedido normal de Aguas del Norte lleva cantidad positiva, un producto del
> catálogo, una fecha dentro del periodo, un cliente que existe en el maestro y un
> importe parecido al de los demás pedidos de ese cliente.

Cinco líneas, cinco ejes. Con eso escrito, «se sale» deja de ser una impresión y pasa a
ser una comprobación: se sale de la línea 1, o de la 3, o de dos a la vez. Y sobre
todo, se puede **contar**.

Los umbrales concretos los sacas del fichero, no de mí: mira el rango de importes que
hay dentro y decide dónde pones la raya. Esa decisión es tuya y es la parte que
importa. Escribirla también te obliga a admitir que la estás tomando.

## Cuándo brilla

- **Cuando el conjunto es demasiado grande para mirarlo.** `pedidos.xlsx` tiene unas
  5.400 líneas. A dos segundos por línea son tres horas de mirar sin parpadear. Nadie
  lo hace, y por eso nadie sabe lo que hay ahí dentro. Aquí el verbo no te hace más
  rápida: te permite hacer algo que hoy no se hace en absoluto.
- **Cuando la normalidad es estrecha y se puede escribir.** Cantidades positivas,
  fechas laborables, códigos de una lista cerrada. Cuanto más cerrada la definición,
  más limpia la señal.
- **Cuando lo raro es caro.** Un abono mal registrado, un cobro a un cliente que ya se
  había dado de baja, una entrega a una dirección que no existe. No hace falta que sean
  muchos: uno solo puede pagar el rato.

## Cuándo esto falla

- **No hay normalidad escrita.** Es el fallo por defecto. Sin definición, todo lo que
  te llame la atención parecerá un hallazgo, y dentro de dos semanas no podrás repetir
  el mismo análisis con el mismo resultado.
- **Lo raro es raro y da igual.** Un pedido de 4 € un martes de agosto es una anomalía
  perfecta y no cambia ninguna decisión. Este verbo produce muchas de éstas. La pregunta
  que las filtra no es «¿es raro?» sino «¿qué haría yo distinto si esto fuera cierto?».
- **Lo raro es correcto y tu definición estaba corta.** El pedido de 2.400 € no es un
  error: son las fiestas del pueblo, una vez al año. Lo que hay que arreglar es la
  definición, no el dato. Los tres desenlaces posibles están en
  `b2-p4-anomalia-no-es-error`, «Una anomalía no es un error».
- **Se inventa la rareza.** Marcar algo como anómalo es fácil y suena bien. Si no
  puedes ir a la línea concreta del fichero y verlo con tus ojos, no lo has encontrado.
  Cada marca tiene que traer su fila.

> [!WARNING]
> **Y el aviso que más importa: lo importante muchas veces no es raro.** Una anomalía
> destaca porque es una excepción. Un fallo sistemático está en todas partes, así que
> es el paisaje: no se sale de nada porque es contra lo que se mide todo lo demás.
> En una clínica donde todas las citas se dan con quince minutos menos de los que hacen
> falta, ninguna cita es anómala; todas van igual de mal. En `pedidos.xlsx` hay al
> menos una cosa importante que este verbo no va a marcar por bien que lo uses. No la
> busques hoy: no se caza mirando lo que sobresale, se caza cruzando dos ficheros y
> preguntando por qué. Eso es el bloque 4.

## Las tres instancias

| Dónde | Lo normal, escrito | Lo que se sale, y qué significa |
|---|---|---|
| **Tu sector (CX)** | «Un pedido lleva cantidad positiva» | Las líneas con cantidad negativa. No llevan ninguna columna ni ninguna palabra que diga qué son: hay que abrirlas y averiguarlo. Mientras nadie lo haga, rompen en silencio cualquier suma hecha a la ligera |
| **Otro trabajo** | En una gestoría, «en la cuenta de este cliente entran cobros de clientes y salen nóminas, alquiler y proveedores, entre 200 y 4.000 €» | Un cargo de 7.800 € a un proveedor que no aparece en ningún otro mes. Puede ser un error, puede ser una compra legítima que nadie avisó, o puede ser el primero de una serie. Sin la frase escrita, ese cargo pasa desapercibido entre otros cuarenta |
| **Tu casa** | «La luz me viene entre 45 y 70 € al mes» | Una factura de 180 €. Con la frase escrita lo ves el primer mes; sin ella lo ves en septiembre, cuando miras el año entero de golpe. La diferencia entre las dos cosas son cinco meses pagando |

La instancia de casa enseña lo esencial del verbo: ya tienes una normalidad para la
luz, aunque nunca la hayas escrito. Por eso ves el pico. Donde no tienes ninguna
—en 5.400 líneas de pedidos— no ves nada, y no es porque no haya.

## Ejercicio

Material: `dataset/ficheros/pedidos.xlsx`.

1. **Escribe la normalidad a ciegas** (10 min). Mira solo los nombres de las columnas,
   nada más. Escribe cinco líneas, cada una con un valor o un rango concreto. Guárdala
   tal cual: es la versión 1 y no se toca.
2. **Ábrelo y corrige** (5 min). Ahora sí, mira el fichero. Escribe la versión 2 de tu
   normalidad y, al lado, **qué has cambiado y por qué**. Ese porqué es lo que
   aprendes hoy; la definición es solo el envase.
3. **Cuenta lo que se sale** (15 min). Empieza por un eje solo: las líneas con
   `cantidad` negativa. Cuéntalas. Abre cinco y míralas de verdad. Escribe en una frase
   qué son y **qué prueba tienes** de que lo son. «Me lo parece» no es prueba; «el
   importe también es negativo y el mismo cliente tiene un pedido igual tres días
   antes» sí.
4. **Decide qué haces con ellas** (5 min). Para el conjunto que has encontrado,
   contesta a «¿cuántas veces más pasa esto?» y clasifícalo: error suelto, caso legítimo
   que mi definición no contemplaba, o punta de un patrón.

**Trabaja línea a línea**, no por meses ni por totales. Las vistas agregadas son otro
verbo y otro bloque.

**Entregable:** `normalidad-pedidos.md` con las dos versiones de la definición, la
lista de cambios con su porqué, el recuento y la frase de qué son esas líneas.

**Regla de parada:** no arregles nada. No borres esas filas, no les cambies el signo y
no avises a nadie. Este verbo señala; decidir qué se hace con lo señalado no es este
verbo y hoy no te toca.

## Escribe tú la regla

En tu catálogo, en la fila del verbo 6, y en la bitácora:

- «Antes de buscar lo raro en un conjunto, escribo \_\_\_.»
- «Una rareza me importa cuando \_\_\_. Si no, la anoto y sigo.»

## Para la bitácora

- ¿En qué se diferenciaban tu versión 1 y tu versión 2 de la normalidad?
- ¿Cuántas líneas contaste, y qué prueba tienes de lo que son?
- ¿De qué conjunto de tu trabajo no sabrías escribir hoy la normalidad? Ése es el que
  no puedes vigilar.
