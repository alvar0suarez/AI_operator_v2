---
id: b3-p2-verificacion-numerica
bloque: 3
titulo: "Técnicas de verificación numérica rápida"
tipo: profundizacion
duracion_min: 25
requisitos: [b3-m4-sabotaje]
desbloquea: []
caduca: bajo
objetivos:
  - "Aplicar las cinco comprobaciones de diez segundos a un resultado numérico"
  - "Elegir los tres números que hay que comprobar en una tabla"
  - "Detectar un recuento de filas que no cuadra con la fuente"
conceptos: [verificacion, orden-de-magnitud, cuadre, coste-de-verificar]
---

Rama opcional de los sabotajes, y de las que más se amortizan. Cinco comprobaciones que
se hacen en diez segundos cada una, con ejemplos sobre los ficheros del gemelo
sintético. No hace falta saber estadística: hace falta saber dónde mirar.

## Las cinco

**1. ¿Suman las partes el total?**

En `dataset/ficheros/pedidos.xlsx` cada fila es una línea de pedido, y `total_pedido`
viene repetido en todas las filas del mismo pedido. Coge un pedido, suma sus
`importe_linea` y compara. Diez segundos, y caza la mitad de los desastres de cualquier
tabla resumida.

Aviso, que ya viste en `b2-m7-detectar-anomalias`, «Verbo 6: detectar anomalías»: hay
líneas con `cantidad` negativa. Si las dejas fuera de la suma, no va a cuadrar, y no
será culpa del total.

**2. ¿El porcentaje va sobre la base que crees?**

`tickets.xlsx` tiene 800 filas. Pero la columna `tiempo_dedicado_min` está vacía en algo
más de una de cada cinco. Si calculas «el tiempo medio por ticket», ¿divides entre 800 o
entre las que tienen dato? Los dos números son legítimos y significan cosas distintas.
Un resultado que no dice cuál de los dos es, no vale.

La pregunta de diez segundos: **¿cuántos casos hay en el denominador?**

**3. ¿El orden de magnitud es razonable?**

No se trata de calcular exacto, sino de mirar la escala. Supón que ese tiempo medio
saliera 200 minutos por ticket: 800 tickets × 200 min son unas 2.670 horas en seis
meses. En Aguas del Norte hay dos personas en atención al cliente y el periodo tiene 129
días laborables. Salen más de diez horas al día cada una, solo contestando tickets, sin
facturar, sin repartir y sin comer.

No hace falta conocer la respuesta correcta para saber que ésa no lo es. Esta
comprobación es la única de las cinco que funciona sin abrir el fichero.

**4. ¿Coinciden los extremos?**

El máximo, el mínimo, la primera fila y la última. Los extremos delatan lo que la media
esconde.

En `tickets.xlsx` el periodo va del 2 de septiembre de 2024 al 28 de febrero de 2025. Si
tu máximo de `fecha_apertura` cae fuera de ahí, no tienes un ticket raro: tienes un
problema de lectura de fechas, porque esa columna trae tres formatos mezclados
(`2024-11-03`, `03/11/2024`, `3-nov-2024`) y algo se ha interpretado mal. Y en
`tiempo_dedicado_min` hay un máximo de 1.440: un día entero, minuto a minuto, en un solo
ticket.

**5. ¿Cuadra el número de filas?**

Entran 800, salen 800. Si agrupas por `canal` y las categorías suman 780, se han caído
20 por el camino: esa columna trae grafías mezcladas —`Teléfono`, `TELEFONO`, `tel`— y
un filtro literal por una de ellas deja fuera las otras dos.

Lo mismo en `clientes.xlsx`: 300 filas, y la columna `tipo` tiene seis grafías para dos
categorías, más un 3 % en blanco. Contar por el valor literal de la celda no te va a dar
el reparto real de hostelería y particulares.

## Los tres números que hay que elegir

**Comprobar tres números bien elegidos detecta casi todo lo que detectarían treinta al
azar.** Los fallos no se reparten por igual: se concentran en tres sitios.

| Qué eliges | Por qué ése |
|---|---|
| **El total** | Si cuadra con la suma de las partes, casi todo lo de en medio está bien |
| **Un extremo** | El máximo o el mínimo, que es donde vive lo imposible |
| **El recuento de filas** | Cuántas entran y cuántas salen. Es por donde se pierde información sin avisar |

Treinta números del medio de la tabla te confirman treinta veces lo mismo: que la parte
fácil está bien. Y te dejan sin atención para lo que importaba, que es lo que cuenta
`b3-p5-coste-de-verificar-de-mas`, «Verificar de más también es un error».

## Cuándo esto falla

- **Cuando cuadra porque está calculado sobre el mismo error.** Si el total lo ha
  producido la misma pasada que las partes, que cuadre no prueba que sea cierto: prueba
  que es consistente. Consistente y cierto no es lo mismo, y la diferencia solo se ve en
  la fuente.
- **Cuando el fallo es una ausencia.** Ninguna de las cinco caza lo que no está. Para
  eso está la pregunta de `b3-m8-plantilla-de-verificacion`, «Tu plantilla de
  verificación»: ¿qué debería estar aquí y no está?
- **Cuando el número es impecable y la pregunta era otra.** Un total perfecto de una
  columna que no era la que hacía falta pasa las cinco comprobaciones.
- **Cuando los diez segundos se convierten en veinte minutos.** Si para comprobar un
  número tienes que rehacer el cálculo entero, eso ya no es esta técnica: es hacer la
  tarea dos veces.

## Las tres instancias

- **En tu mesa.** Lo de arriba, sobre pedidos y tickets. El total del pedido, el importe
  más alto y el recuento de filas.
- **En otro oficio: la gestoría.** En un resumen de facturación trimestral: el total
  contra la suma de facturas, la factura más grande, y cuántas facturas hay. Tres
  comprobaciones, dos minutos, y no hace falta abrir las 180.
- **En tu casa.** La factura del móvil. El total contra la suma de conceptos, el cargo
  más caro, y cuántas líneas hay facturadas. Se hace en el ascensor y es exactamente la
  misma técnica.

## Escribe tú la regla

En la bitácora, y de paso en la ficha que corresponda de tu plantilla de verificación:

- «Los tres números que compruebo siempre en \_\_\_ son \_\_\_.»
- «Un número que cuadra no me vale cuando \_\_\_.»

## Para la bitácora

- ¿Cuál de las cinco no habías hecho nunca?
- ¿Qué resultado de esta semana pasaría las cinco? ¿Y cuál no pasaría la del recuento?
