---
id: b1-p2-variabilidad-mata-automatizaciones
bloque: 1
titulo: "La variabilidad es la que mata automatizaciones"
tipo: profundizacion
duracion_min: 25
requisitos: [b1-m5-filtro-automatizabilidad]
desbloquea: []
caduca: bajo
objetivos:
  - "Distinguir variabilidad de entrada, de criterio y de contexto en una tarea propia"
  - "Clasificar diez casos de tu diario según por qué salieron distintos"
  - "Declarar como excepción lo que no baja a nada observable"
conceptos: [variabilidad, estabilidad-del-criterio, excepcion, riesgo]
---

En el filtro, la variabilidad aparece como una columna con tres valores: baja, media,
alta. Eso sirve para ordenar y no sirve para decidir, porque debajo de esa palabra hay
tres cosas distintas que se comportan de forma opuesta. Una se absorbe casi sin
esfuerzo. Otra obliga a documentar antes de tocar nada. La tercera es la que produce
montajes que funcionan un mes y luego hacen daño en silencio.

## Tres cosas distintas con el mismo nombre

| Tipo | Qué cambia | Cómo suena | Qué hacer |
|---|---|---|---|
| **De entrada** | Llega distinto cada vez | «Unos mandan el número de factura y otros no» | Se absorbe: se declara qué pasa cuando falta el dato |
| **De criterio** | Lo que se considera bien hecho cambia | «Depende de cómo vaya el mes» | Documentar el criterio primero. No se automatiza lo que no está escrito |
| **De contexto** | La misma entrada exige salida distinta por algo que no está escrito | «Es que a ese cliente se le trata distinto» | Sacarlo del proceso como excepción declarada, con nombre |

## De entrada: la fácil

El albarán falta en 6 de cada 10 reclamaciones. Las fechas vienen en tres formatos. Hay
quien escribe el número de pedido en el asunto y quien lo escribe en el cuerpo, y hay
quien no lo escribe.

Esto se absorbe porque el criterio de «bien hecho» no se ha movido: en todos los casos
lo que hay que producir es lo mismo. Lo único que se necesita es **declarar la salida
para cuando el dato no está**. Ese es el error clásico: si no dices qué hacer cuando
falta el número de albarán, quien ejecute la tarea —persona o máquina— pondrá algo en
esa casilla, y lo que salga va a parecer correcto.

Regla práctica: toda entrada opcional necesita una salida «no consta» explícita, y una
cuenta de cuántas veces sale. Si nunca sale, no es que siempre venga el dato; es que
alguien lo está rellenando por su cuenta.

## De criterio: la que obliga a parar

«Bien hecho» cambia. No la entrada: el listón.

Qué reclamación merece un detalle comercial depende del mes, del cliente y del ánimo de
gerencia. El tono de una respuesta cambia según si la campaña va bien. Cuánto se aprieta
con un impago depende de la tesorería de esa semana.

Aquí no hay nada que absorber, porque no hay contra qué comparar. El paso previo es
escribir el criterio, y escribirlo tiene un dueño: alguien tiene que decir cuál es. Si
nadie lo dice, la tarea no está lista para delegarse en nadie, ni en una persona nueva
ni en una máquina. Eso es un `Est` de 1 o 2, y su siguiente paso es `documentar` aunque
el total sea 15.

Hay una consecuencia que no se ve venir: cuando por fin escribes ese criterio, casi
siempre descubres que dos personas de tu oficina lo tenían distinto en la cabeza. Eso
solo aparece al escribirlo.

## De contexto: la que hace daño en silencio

La misma entrada, la misma tarea, y la salida correcta es otra por algo que sabes tú y
no está en ningún sitio.

> Dos reclamaciones idénticas, con el mismo importe y la misma redacción. A una se le
> abona sin preguntar; a la otra se le pide el albarán primero. ¿Por qué? Porque una es
> de un hotel que factura todos los meses desde hace ocho años, y hay un acuerdo verbal
> de 2021 que nadie escribió.

Esta es la peligrosa, y no por el error: por **cuándo se detecta**. Una automatización
con variabilidad de contexto funciona perfectamente en las pruebas, porque en las
pruebas coges casos normales. Falla en los casos raros, que son pocos, y los casos raros
son justo los que nadie revisa. Sigue produciendo, sale bien escrita, y el fallo aparece
tres meses después en forma de un cliente antiguo que se va sin decir por qué.

Lectura de riesgo: aquí no cuenta la frecuencia, cuenta el daño. Un fallo en 1 de cada
20 casos con clientes normales es un incordio. El mismo fallo, si ese 1 de cada 20 son
siempre tus tres clientes más grandes, es otra cosa completamente distinta.

## Cómo se distingue en la práctica

Coge diez casos de la misma tarea en tu diario, de los que recuerdes cómo acabaron. Por
cada uno, una sola pregunta: **¿por qué salió distinto?**

- Si la razón está en **lo que llegó** → de entrada.
- Si la razón está en **qué se consideraba bien hecho ese día** → de criterio.
- Si la razón está en **algo que sabías tú y no está escrito** → de contexto.

Cuenta los tres montones. El tamaño del tercero es el mejor indicador que vas a tener
de si esa tarea se puede delegar, y no aparece en ninguna de las cuatro puntuaciones
del filtro.

Y la señal de campo, la que funciona sin contar nada: **«eso no se le puede explicar a
la persona nueva».** Si te oyes decir eso, hay variabilidad de contexto debajo.

## Cuándo esto falla

- **Clasificar sin casos delante.** De memoria todo parece variabilidad de entrada,
  porque es la que se recuerda.
- **Convertir toda excepción en regla.** Un proceso con quince reglas ya no es un
  proceso. Tres o cuatro excepciones declaradas y bien nombradas funcionan mejor que
  quince reglas que nadie recuerda.
- **Confundir «poco frecuente» con «poco importante».** El caso raro suele ser el caro.
- **Creer que la variabilidad se arregla con más instrucciones.** La de entrada sí. La
  de criterio necesita una decisión de alguien. La de contexto necesita que alguien
  escriba lo que sabe.

## Las tres instancias

| Dónde | De entrada | De criterio | De contexto |
|---|---|---|---|
| **Tu sector (CX)** | Falta el número de albarán | Cuándo se abona sin preguntar | El acuerdo verbal de 2021 con un cliente |
| **Otro trabajo** | En una gestoría, cada cliente manda las facturas en un formato | Qué gasto se considera deducible en un caso dudoso | Los dos clientes a los que se les persigue por teléfono porque el correo no lo leen |
| **Tu casa** | Unas semanas hay lista y otras no | Cuánto se puede gastar este mes | Que el domingo viene alguien a comer y nadie lo ha escrito |

## Escribe tú la regla

En la bitácora: «de mis diez casos, \_\_\_ eran de entrada, \_\_\_ de criterio y \_\_\_
de contexto. Con eso, esta tarea \_\_\_.»

## Para la bitácora

- ¿Cuál de tus tareas tiene el montón de contexto más grande? ¿Y quién más en tu empresa
  sabría resolver esos casos?
- ¿Qué excepción llevas años aplicando sin que esté escrita en ninguna parte?
