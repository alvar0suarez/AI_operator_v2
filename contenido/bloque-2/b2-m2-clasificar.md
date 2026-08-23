---
id: b2-m2-clasificar
bloque: 2
titulo: "Verbo 1: clasificar"
tipo: ejercicio
duracion_min: 45
requisitos: [b2-m1-mapa-de-lo-posible]
desbloquea: [b2-m3-extraer]
caduca: bajo
objetivos:
  - "Escribir una taxonomía con categorías excluyentes y una regla de desempate"
  - "Clasificar 40 tickets a partir de la descripción y no de la etiqueta que traen"
  - "Medir tu «otros» y la coherencia de tu propia clasificación al releerla"
conceptos: [clasificar, taxonomia, criterio, verbo]
dataset: [dataset/ficheros/tickets.xlsx]
profundizar:
  - id: b2-p1-clasificar-vs-buscar
    titulo: "Clasificar no es buscar"
---

Clasificar es el verbo con el que casi todo el mundo empieza, porque es el más fácil
de pedir y el más fácil de comprobar. También es el que esconde el fallo más caro del
bloque, y no está donde parece: no está en el reparto, está en la lista con la que
repartes. Hoy vas a clasificar cuarenta tickets y a medir si tu lista se sostiene.

## Qué es

Asignar a cada elemento de un conjunto una categoría de una lista cerrada. Todos
reciben una, y solo una. Ésas son las dos condiciones: **todos** y **una sola**.

Clasificar no es buscar. Buscar te trae los tickets que hablan de facturación y deja
el resto del montón sin tocar; clasificar reparte los 800 y no deja ninguno fuera. Se
confunden constantemente, y de esa confusión salen los «otros» que acaban comiéndose
cuatro de cada diez fichas. La diferencia operativa está en
`b2-p1-clasificar-vs-buscar`, «Clasificar no es buscar».

El verbo tiene dos piezas, y solo una se ve:

1. **La taxonomía:** la lista de categorías.
2. **La regla de decisión:** cómo se decide, caso a caso, cuál toca.

Casi todo el mundo trabaja la segunda y da la primera por buena, porque la primera ya
estaba ahí cuando llegó. Ahí está el nodo entero.

## Cuándo brilla

- **Volumen alto y criterio estable.** 800 tickets a quince segundos de lectura cada
  uno son tres horas y veinte minutos de trabajo mecánico. Es de las pocas cosas donde
  el ahorro se ve el primer día.
- **Cuando clasificar es el paso previo de una cuenta.** No se puede contar lo que no
  está agrupado, y no se puede decidir nada sin contar. Casi todos los análisis
  empiezan por aquí.
- **Encolar.** El caso aburrido y rentable: repartir lo que entra por «quién lo
  atiende», «hoy o mañana», «necesita datos que no tengo». Categorías pocas y obvias,
  y un reparto que hoy haces tú a mano cada mañana.

## Cuándo esto falla

- **Categorías que se solapan.** «Me llegó tarde y encima venía roto» cabe en dos. Si
  no está escrito qué manda cuando caben dos, cada pasada da un resultado distinto. Y
  no hablo de una máquina contra ti: tu pasada de hoy contra la tuya del jueves.
- **El «otros» que engorda.** Un «otros» pequeño es sano. Cuando pasa de una de cada
  diez fichas deja de ser un cajón de sastre y se convierte en la categoría principal:
  quiere decir que la lista no describe el material que tienes delante.
- **Más de un eje mezclado.** «Facturación», «Urgente» y «Teléfono» no van de lo
  mismo: son tipo, prioridad y canal. Mezclados en una sola columna, no se puede
  contar ninguna de las tres.
- **Heredar la etiqueta.** Aceptar la categoría que puso quien abrió la ficha con
  prisa, en dos segundos, con otro criterio y quizá otro año. Se hereda sin pensarlo
  porque viene rellena.
- **El fallo silencioso: clasificar perfectamente según una taxonomía que está mal.**
  No hay ningún aviso. El resultado sale impecable, las tablas cuadran, los
  porcentajes suman 100, y la conclusión es falsa. Este es el que cuesta dinero.

> [!WARNING]
> Un reparto correcto sobre una lista equivocada tiene exactamente el mismo aspecto
> que un reparto correcto sobre una lista buena. Por eso este verbo se verifica
> mirando la lista, no el reparto.

**Cómo se comprueba, en tres minutos.** Coge diez fichas ya clasificadas, tápate el
resultado y vuelve a clasificarlas mañana. Cuenta cuántas cambian. Si cambia más de
una de diez, el problema no es tu atención: es que la lista se solapa o la regla de
desempate no está escrita. Es la misma prueba tanto si has clasificado tú como si lo
ha hecho una máquina.

## Las tres instancias

| Dónde | La lista | Lo que enseña |
|---|---|---|
| **Tu sector (CX)** | Tickets por tipo de incidencia | La lista lleva años ahí, la escribió alguien que ya no está y nadie la ha vuelto a mirar. Es el caso de hoy. |
| **Otro trabajo** | En una gestoría, facturas de clientes por régimen fiscal | Aquí el verbo brilla: categorías pocas, excluyentes, definidas por ley y que no cambian el jueves. El «otros» es la factura que hay que mirar a mano, y su tamaño mide lo rara que es la cartera. |
| **Tu casa** | El correo personal: «hay que contestar» / «hay que hacer algo antes de una fecha» / «archivar» / «tirar» | Un eje, cuatro cajones, ninguna herramienta. Y si «hay que contestar» se te llena, la lista está mal partida: dentro hay dos cosas distintas. |

## Ejercicio

**Material:** `dataset/ficheros/tickets.xlsx`, hoja `Tickets`, 800 filas. Te interesan
tres columnas: `id_ticket`, `categoria` y `descripcion`.

**1. Mira la lista que ya existe (5 min).** Cuenta cuántas etiquetas distintas hay en
`categoria` y ordénalas por número de filas. Con una tabla dinámica o con `CONTAR.SI`.
Apunta dos números: cuántas etiquetas distintas y cuántas filas vienen vacías.

**2. Lee sin mirar la etiqueta (10 min).** Coge 40 tickets repartidos por todo el
fichero —uno de cada veinte, por ejemplo— y **tapa la columna `categoria`**. Lee solo
la `descripcion` y agrupa por lo que le pasa al cliente. Ponle nombre a cada grupo.

**3. Escribe tu taxonomía (5 min).** Cada categoría con una frase de qué entra y qué
no. Y una línea de desempate: «cuando un ticket cabe en dos, manda \_\_\_.» Sin esa
línea el ejercicio no cuenta.

**4. Clasifica los 40 con tu lista (8 min).** Cada uno en una sola categoría. Cuenta
cuántos han caído en «otros».

**5. Comprueba (5 min).** Coge 10 de los 40, tapa tu primera respuesta y reclasifica.
Cuenta cuántos cambian.

**6. Cruza (4 min).** Compara tu lista con las etiquetas del paso 1. ¿Cuántas etiquetas
del fichero corresponden a una sola categoría tuya? ¿Cuántas se reparten entre dos o
más? ¿Cuántas categorías tuyas no tienen etiqueta que las nombre?

**Entregable:** `taxonomia-tickets.md` con las etiquetas encontradas, tu lista con sus
definiciones y su regla de desempate, tu «otros» en número y en porcentaje, las que
cambiaron al releer, y una última línea: **qué pregunta no podrías contestar con la
columna `categoria` tal y como viene.**

**Regla de parada:** no reclasifiques los 800. Cuarenta bastan para saber si la lista
sirve, y saber si la lista sirve es todo lo que hoy hace falta.

## Lo que acabas de encontrar

Mira tus dos listas juntas: la del fichero y la tuya. Si te ha pasado lo que suele
pasar, no se parecen. Hay etiquetas del fichero que apuntan a dos cosas distintas,
grupos tuyos que no tienen ninguna etiqueta, y un «otros» que se traga casos que no se
parecen en nada entre sí.

Fíjate en lo que eso significa. Clasificar los cuarenta te ha llevado diez minutos y
lo has hecho bien. El problema nunca fue el reparto: **el problema era la lista.** Y
una lista mal hecha no da error, da porcentajes. Cualquiera que abra ese fichero y
haga una tabla dinámica sobre la columna `categoria` va a obtener números redondos,
convincentes y sin ningún parecido con lo que le pasa a los clientes.

Guarda tu `taxonomia-tickets.md`. Cómo se construye una taxonomía que aguante, y qué
se descubre cuando por fin se cuenta con la lista buena, es el bloque 4.

## Escribe tú la regla

En la bitácora, con tus palabras:

- «Una lista de categorías está lista para usarse cuando \_\_\_.»
- «Antes de fiarme de un porcentaje sacado de una columna de categorías, compruebo
  \_\_\_.»

## Para la bitácora

- ¿Cuántas etiquetas distintas había en la columna y cuántas categorías te salieron a
  ti? ¿Qué explica la diferencia?
- ¿Cuántos de los diez cambiaron al reclasificar? ¿Por solape, por desempate mal
  escrito o por cansancio?
- ¿Hay en tu trabajo alguna lista de categorías que estés heredando sin haberla mirado
  nunca? Escríbela por su nombre.
