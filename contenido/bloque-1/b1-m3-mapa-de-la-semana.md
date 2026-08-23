---
id: b1-m3-mapa-de-la-semana
bloque: 1
titulo: "Mapa de la semana: frecuencia, duración, variabilidad"
tipo: ejercicio
duracion_min: 45
requisitos: [b1-m2-diario-de-tareas]
desbloquea: [b1-m4-descomposicion]
caduca: bajo
objetivos:
  - "Calcular los minutos al mes de cada tarea recurrente a partir del diario"
  - "Usar la mediana en lugar de la media y justificar por qué"
  - "Escribir por qué varía cada tarea, no solo cuánto"
  - "Marcar al menos una tarea que quizá no debería existir"
conceptos: [frecuencia, variabilidad, linea-base, coste-de-oportunidad]
---

El diario en bruto no dice nada: son cien líneas sueltas. Aquí lo conviertes en tres
números por tarea y una pregunta incómoda. Es la sesión más aritmética del curso y no
necesita más que una tabla y quince minutos de sumar. Al final tendrás la primera
cifra de tu vida laboral que puedes poner encima de una mesa.

## Un mapa terminado, antes de explicar cómo se hace

Esta es una semana inventada. No es la tuya y no tiene por qué parecerse.

| Tarea | Veces/mes | Mediana (min) | Rango (min) | Min/mes |
|---|---|---|---|---|
| Reclamaciones de factura | 24 | 18 | 4–45 | 432 |
| Consultas de estado de pedido | 60 | 4 | 2–10 | 240 |
| Cuadrar albaranes con pedidos | 20 | 9 | 5–40 | 180 |
| Informe semanal para gerencia | 4 | 35 | 30–40 | 140 |
| Alta de cliente nuevo | 8 | 12 | 10–15 | 96 |

Mírala treinta segundos. Casi todo el mundo esperaba que ganase la tarea que más
pesa en la cabeza —las reclamaciones, que son las que amargan la mañana— y se queda
mirando la tercera: cuadrar albaranes son nueve minutos que no molestan a nadie y son
tres horas al mes. Eso hace la aritmética: separa lo que te cansa de lo que te cuesta,
que no son lo mismo.

## La única multiplicación que importa

```
minutos/mes = veces al mes × duración mediana
```

Si tu diario cuenta semanas: **veces por semana × 4,3 = veces al mes**. Catorce
consultas por semana son sesenta al mes.

El umbral práctico es **2 horas al mes = 120 minutos**. Por debajo de esa raya, la
tarea se aparca. No es que no valga: es que no toca ahora.

La razón es aritmética, no filosófica. Una tarea de 90 minutos al mes que consigas
reducir a la mitad te devuelve 45 minutos al mes. Montar eso, probarlo, corregirlo
cuando cambie algo y acordarte de que existe cuesta más que 45 minutos. Por encima de
las dos horas ya hay margen para que el esfuerzo se pague.

> [!NOTE]
> El umbral no es una ley de la física, es un suelo prudente para que no gastes tu
> tiempo en calderilla. Si una tarea de 60 minutos al mes te resulta insoportable, es
> asunto tuyo y es legítimo. Pero anótala como lo que es: la haces por gusto, no por
> números.

## Mediana, y no media, y por qué

Los siete últimos casos de reclamación que salen del diario, en minutos:

```
4 · 6 · 12 · 15 · 18 · 20 · 45
```

- **Media:** 120 ÷ 7 = **17,1 minutos.**
- **Mediana:** el valor del medio una vez ordenados = **15 minutos.**

La media la levanta un solo caso, el de 45 minutos. Si planificas con 17 te
equivocas en los siete: seis duraron menos y uno duró muchísimo más. La mediana
describe el caso típico, que es el que se repite y el que decide tu semana. Se saca
sin fórmulas: ordenas los tiempos y coges el del medio; si son pares, el punto medio
entre los dos centrales. En una hoja de cálculo la función se llama `MEDIANA`.

Y un uso que casi nadie aprovecha: **la distancia entre media y mediana es
información.** Si la media es bastante mayor que la mediana, hay casos largos
escondidos ahí dentro, y esos casos largos son los que te van a interesar. Si media y
mediana van pegadas, la tarea es regular y previsible.

## La columna que todo el mundo se salta

La variabilidad se apunta en dos trozos: **el rango** (el caso más corto y el más
largo) y **la razón**.

Vuelve al mapa de arriba. Cuadrar albaranes va de 5 a 40 minutos. Ese 40 no es ruido
ni un mal día: es el albarán que venía sin número de pedido y hubo que buscarlo en el
histórico. Reclamaciones va de 4 a 45: el 45 fue el caso que hubo que consultar con
gerencia.

La razón se escribe en una línea, al lado del número:

- Sirve: «varía porque en 6 de cada 10 casos falta el número de albarán y hay que
  buscarlo».
- No sirve para nada: «varía bastante».

Esa línea de texto es la que más va a pesar dentro de tres bloques, cuando toque
decidir qué se puede delegar de verdad. Un rango ancho no descarta una tarea; lo que
la descarta es no saber por qué es ancho.

Dos avisos sobre esta columna:

- **No toda variabilidad es igual.** A veces cambia lo que entra, a veces cambia lo
  que se considera bien hecho, y a veces cambia el contexto. La primera se absorbe
  fácil; las otras dos no. Se separan en `b1-m5-filtro-automatizabilidad`, «El filtro
  de automatizabilidad: cuatro preguntas».
- **Con dos o tres observaciones no hay mediana, hay anécdota.** Si una tarea solo
  aparece dos veces en tu diario, pon el número con un interrogante al lado y no
  decidas nada con él.

## La pregunta incómoda

Vuelve a la primera fila: 24 reclamaciones de factura al mes, 432 minutos. La
pregunta obvia es «cómo contesto más rápido». La pregunta rentable es otra:

**¿Por qué hay 24 reclamaciones de factura al mes?**

Si quince de ellas dicen lo mismo —el importe no cuadra con el albarán—, entonces no
tienes una tarea de 432 minutos. Tienes un fallo de facturación que **produce** 432
minutos de trabajo al mes, más 24 clientes molestos.

Compara los dos caminos con números:

| Camino | Ahorro |
|---|---|
| Contestar cada reclamación en 6 minutos en vez de 18 | 288 min/mes |
| Que el importe salga bien | 432 min/mes, y 24 clientes que no se enfadan |

Automatizar una tarea que no debería existir es peor que no automatizarla: la deja
instalada para siempre, y con manual. Por eso el mapa lleva una columna más:
**¿debería existir esta tarea?** —sí / no / no lo sé—.

Ojo con la conclusión fácil: tú no puedes arreglar la facturación desde tu silla, y
esto no va de que la arregles mañana. Va de que la columna quede escrita con su número
al lado, que es lo único que se puede defender después. Se recoge en
`b1-m8-inventario-de-procesos`, «Tu inventario de procesos».

## Cuándo esto falla

- **Semana atípica.** El mapa mide la semana que mediste, no tu año. Anótalo y no lo
  tires: un mapa con una nota vale más que ningún mapa.
- **Filas demasiado gruesas.** «Correo» no es una tarea, es un canal. Si una sola
  fila se lleva más de un tercio de tu tiempo, pártela hasta que deje de hacerlo.
- **Ordenar por minutos y ponerte con la primera.** El ranking no dice «empieza por
  aquí», dice «mira por aquí». Quien decide es el filtro, en el nodo siguiente.
- **Confundir tu estimación con la medida.** Ahora es buen momento para abrir la
  estimación a ciegas que dejaste escrita en `b1-m1-nadie-sabe-explicar-su-trabajo`,
  «Por qué nadie sabe explicar su propio trabajo», y compararla. Si acertaste, enhorabuena y sigue midiendo igual. Si fallaste por más
  del 30%, ya sabes cuánto vale tu intuición en minutos.

## Las tres instancias

La cuenta es la misma en cualquier sitio donde algo se repita:

| Dónde | La cuenta |
|---|---|
| **Tu sector (CX)** | Consultas de estado de pedido: 60 × 4 min = 240 min/mes. Entra de sobra, y nadie la habría nombrado. |
| **Otro trabajo** | En una gestoría, reclamar documentación a clientes: 40 llamadas al mes × 3 min = 120 min/mes. Justo en la raya. |
| **Tu casa** | La compra: 4 veces al mes × 75 min = 300 min/mes, con un rango de 45 a 120. Y la razón por la que varía es de la misma familia que en el trabajo: unas veces vas con lista y otras no. |

## Ejercicio

**Qué:** convertir el diario en una tabla. Mínimo diez filas.

1. Lista todas las tareas que marcaste como recurrentes. Agrupa las que sean lo
   mismo con distinto nombre.
2. Para cada una: cuenta las veces en los cinco días y multiplica por 4,3. Si es
   mensual o semanal, cuéntala directamente.
3. Anota **todos** los tiempos que observaste, ordénalos y coge el del medio: esa es
   tu mediana. Apunta también el más corto y el más largo.
4. Escribe **en una línea por qué varía**. Sin esa línea la fila no está terminada.
5. Calcula minutos/mes = veces/mes × mediana.
6. Marca la columna **¿debería existir?**: sí / no / no lo sé.
7. Ordena de más a menos minutos/mes y traza una raya en los 120 minutos.

**Entregable.** Un fichero tuyo —`mapa-de-la-semana.md` o una hoja de cálculo— guardado
junto al diario, con las siete columnas y la raya de las dos horas. Es la materia
prima de los tres nodos siguientes; no lo cierres.

**Regla de parada:** no decidas todavía qué delegar y no montes nada. El mapa ordena.
Decidir es el nodo siguiente y tiene cuatro preguntas.

## Escribe tú la regla

En la bitácora, con tus palabras:

- «Uso la mediana y no la media cuando \_\_\_.»
- «Una tarea que se lleva muchos minutos al mes no merece la pena tocarla si \_\_\_.»

Y añade una línea sobre lo que te haya sorprendido de tu propia tabla. Esa línea vale
más que las dos reglas juntas, porque es la única que no habrías podido escribir antes
de medir.

## Para la bitácora

- ¿Qué tarea pesaba mucho en tu cabeza y poco en la tabla? ¿Y al revés?
- ¿En cuántas filas has sido capaz de escribir la razón de la variabilidad, y en
  cuántas te has quedado en «depende»?
- ¿Cuántas tareas has marcado como «no debería existir» o «no lo sé»?
