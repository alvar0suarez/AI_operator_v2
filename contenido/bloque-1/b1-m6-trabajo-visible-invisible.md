---
id: b1-m6-trabajo-visible-invisible
bloque: 1
titulo: "Trabajo visible y trabajo invisible"
tipo: concepto
duracion_min: 35
requisitos: [b1-m5-filtro-automatizabilidad]
desbloquea: [b1-m7-caso-cruzado-domestico]
caduca: bajo
objetivos:
  - "Calcular la diferencia entre las horas registradas y las horas trabajadas de un día"
  - "Separar en una tarea los minutos de hacer de los de buscar, y estimar los que no llegaron al diario"
  - "Marcar en el mapa las tareas cuyo coste real no aparece en el diario"
conceptos: [trabajo-invisible, coste-de-coordinacion, interrupcion, sistema]
profundizar:
  - id: b1-p3-coste-de-cambio-de-contexto
    titulo: "Lo que cuesta volver a donde estabas"
---

Tu diario suma seis horas y cuarto. Estuviste ocho. Esa hora y tres cuartos no se ha
perdido en ninguna parte: es trabajo, y es el que decide cómo te sale el día. Aquí se
le pone nombre, se cuenta con un número, y se ve por qué hacer más rápida la parte que
sí aparece a veces no ahorra ni un minuto.

## Los tres minutos que no eran tres minutos

Un cliente pregunta si su pedido salió el jueves. Miras y no consta. Escribes a
reparto. Sigues con otra cosa. Veinte minutos después te contestan, vuelves al correo,
lees otra vez qué preguntaba y le respondes.

En tu diario esa consulta ni siquiera tiene línea propia: va agrupada con otras dos.

```
11:00 | 3 consultas de estado de pedido | 15 |
```

Lo que ocupó una sola de las tres, en cambio:

| Trozo | Minutos | ¿Está en el diario? |
|---|---|---|
| Mirar si consta | 1 | sí, dentro de los 3 |
| Escribir a reparto | 1 | sí, dentro de los 3 |
| Esperar la respuesta | 20 | no |
| Volver a leer qué preguntaba | 2 | no |
| Escribir la respuesta | 1 | sí, dentro de los 3 |
| El asunto abierto hasta cerrarlo | — | no, y es el que más pesa |

Tres minutos de trabajo, dos cambios de asunto y un tema abierto durante veinte
minutos. Las dos cosas son ciertas y solo una está escrita.

## Las seis familias

Casi todo el trabajo invisible cabe en seis:

| Familia | Cómo suena por dentro | Dónde estaba en tu diario |
|---|---|---|
| **Esperar** | «a ver si contesta reparto» | En ningún sitio |
| **Coordinar** | preguntar, avisar, confirmar | Escondido dentro de otra tarea |
| **Reconstruir dónde estabas** | «¿por dónde iba?» | En ningún sitio |
| **Buscar** | dónde estaba ese fichero, qué se le dijo a este cliente en marzo | Dentro de la tarea, inflando el rango |
| **Saber a quién preguntar** | lo haces tú porque nadie más sabe a quién | Invisible del todo, incluso para ti |
| **Absorber el enfado de alguien** | la llamada que te deja media hora sin poder con el informe | Figura como diez minutos |

La última no es un adorno. Es la razón de que un día con dos llamadas duras cunda la
mitad que un día con veinte llamadas normales.

## La prueba de la resta

Coge un día de tu diario, suma los minutos registrados y resta ese total de las horas
que estuviste. La diferencia es tu trabajo invisible de ese día, más lo que se te
olvidó apuntar, que casi siempre también es trabajo invisible.

En una jornada de ocho horas —480 minutos—, un diario honesto suele sumar entre 330 y
390. El hueco es de hora y media a dos horas y media. Si el tuyo suma 450, no eres más
eficiente que nadie: es que has apuntado el trabajo y no lo que pasa entre trabajo y
trabajo.

> [!NOTE]
> El hueco no es culpa tuya ni un fallo del diario. La mayor parte del trabajo
> invisible no lo generas tú: lo genera cómo está montado lo demás. «Me organizo mal»
> es la lectura más común y casi siempre la equivocada.

## Por qué esto rompe la cuenta del mapa

Vuelve a las consultas de estado de pedido: 60 al mes, 4 minutos de mediana, 240
minutos al mes. En el filtro sacaron 17 puntos y siguiente paso `probar`.

Supón que escribes cada respuesta en un minuto en vez de en cuatro. La cuenta fácil
dice: 60 × 3 = **180 minutos al mes**. La cuenta con lo invisible dentro dice otra
cosa. De esas 60 consultas:

- En **35** la respuesta está en pantalla: miras y contestas. Ahí sí ahorras los tres
  minutos. 35 × 3 = **105 minutos**.
- En **25** la respuesta no está en ningún sitio hasta que reparto la da. Ahí escribir
  el texto nunca fue el problema: no quitas ni la pregunta, ni la espera, ni el volver
  a empezar.

Ahorro real: 105 minutos, no 180. Y lo importante no es que sea menos, es de dónde
sale la diferencia.

## La pregunta que cambia el resultado

¿Por qué en 25 de cada 60 casos hay que preguntarle a una persona? Porque el estado
del reparto no está escrito en ninguna parte hasta que el repartidor vuelve por la
tarde. Eso no es una tarea tuya que se pueda hacer más rápido: es una pieza que falta
en el sistema, y esa pieza no cuesta una herramienta, cuesta una línea apuntada al
terminar cada ruta.

| Camino | Qué ahorra |
|---|---|
| Escribir la respuesta más rápido | 105 min/mes |
| Que el estado esté escrito | Las 25 esperas, los 50 cambios de asunto y los 105 minutos, porque entonces esos 25 casos se contestan como los otros 35 |

Esto es arreglar la causa en vez de pulir el síntoma. Y sí: tú no montas eso desde tu
silla, ni tienes por qué. Lo que puedes hacer hoy es dejarlo escrito con su número al
lado, que es el material de `b6-m2-ganarse-el-derecho`, «Ganarse el derecho: evidencia,
piloto, propuesta», dentro de cinco bloques. Sin el número es una queja.

## Cuándo esto falla

- **Convertirlo todo en trabajo invisible.** Si toda tu jornada es invisible, la
  categoría ya no distingue nada. Sirve para nombrar lo que decide tu día, no para
  justificar cualquier hueco.
- **Contar la espera como tiempo tuyo.** Los veinte minutos que esperas a reparto no
  son tuyos si mientras tanto haces otra cosa. Lo que cuesta es el cambio de asunto y
  el tema abierto. Sumar las esperas enteras infla tu ahorro y te deja sin defensa el
  primer día que alguien lo mire con calma.
- **Intentar cronometrarlo.** Esto se cuenta con marcas, no con cronómetro. Si te
  pones a medir cuántos segundos tardas en volver a lo que estabas, abandonas el jueves.
- **Automatizar la parte visible de una tarea cuyo coste es invisible.** Cero ahorro
  medible. Y encima parece que la herramienta no funciona, cuando lo que falló fue el
  diagnóstico.

## Las tres instancias

El mismo hueco entre lo que figura y lo que cuesta, en tres sitios:

| Dónde | Lo que figura | Lo que cuesta |
|---|---|---|
| **Tu sector (CX)** | «Consulta estado de pedido: 3 min» | 3 minutos de trabajo, 20 de espera y dos cambios de asunto, en 25 de cada 60 casos |
| **Otro trabajo** | En un taller, la hoja pone «sustitución de pieza: 40 min» | Más tres días esperando la pieza y cuatro llamadas al cliente para decirle que sigue sin llegar. Nada de eso está en la hoja, y decide si el cliente vuelve |
| **Tu casa** | «Cenar: 25 minutos de cocina» | Más mirar qué hay, decidir, ver que falta un ingrediente y cambiar de plan. Decidir qué se cena no está en la lista de nadie y es la parte que pesa |

## Ejercicio

Veinte minutos, con tu diario y tu mapa delante.

1. **La resta**, en dos días distintos. Minutos registrados contra horas que estuviste.
   Anota las dos diferencias y qué había en el hueco: tres líneas por día, en el
   apartado «Lo que no cabía en la tabla» de la plantilla del diario.
2. **Parte los minutos de tus tres tareas principales.** Dos preguntas por tarea. De
   los minutos que sí apuntaste, ¿qué porcentaje era hacer y qué porcentaje era
   buscar? Y aparte: ¿cuántos minutos de esperar o preguntar no llegaron a la tabla?
   A ojo. No hace falta más precisión.
3. **Marca en el mapa** las tareas cuyo coste real es invisible, con una nota de una
   línea diciendo dónde está ese coste.

**Entregable:** tu mapa con esa marca y esa nota, y los dos días del diario con su
resta y sus tres líneas.

**Regla de parada:** no reorganices nada esta semana. Agrupar tareas es tentador y a
veces es el mayor ahorro del curso; está en la rama
`b1-p3-coste-de-cambio-de-contexto`, «Lo que cuesta volver a donde estabas», si quieres
verlo ahora.

## Escribe tú la regla

En la bitácora, con tus palabras:

- «Antes de intentar hacer una tarea más rápida, miro \_\_\_.»
- «En mi semana, el trabajo que no aparece en ninguna lista es sobre todo \_\_\_, y
  viene de \_\_\_.»

La segunda mitad de esa segunda frase es la que importa. «Viene de mí» casi nunca es
la respuesta correcta.

## Para la bitácora

- ¿Cuánto te dio la resta en cada día? ¿Y qué había en el hueco?
- De las seis familias, ¿cuál es la tuya, y cuántas veces al día aparece?
- ¿Qué tarea de tu mapa cambiaría de sitio si contaras lo invisible?
