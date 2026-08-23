---
id: b1-m5-filtro-automatizabilidad
bloque: 1
titulo: "El filtro de automatizabilidad: cuatro preguntas"
tipo: ejercicio
duracion_min: 50
requisitos: [b1-m4-descomposicion]
desbloquea: [b1-m6-trabajo-visible-invisible]
caduca: bajo
objetivos:
  - "Puntuar de 1 a 5 las cuatro preguntas del filtro sobre diez tareas propias"
  - "Ordenar esas diez tareas por orden de ataque y no por nota"
  - "Separar lo que toca documentar de lo que toca aparcar"
conceptos: [volumen, explicabilidad, tolerancia-al-fallo, estabilidad-del-criterio, riesgo]
profundizar:
  - id: b1-p2-variabilidad-mata-automatizaciones
    titulo: "La variabilidad es la que mata automatizaciones"
---

Ya tienes el mapa —cuánto pesa cada tarea— y una tarea descompuesta —qué hay dentro—.
Falta decidir por dónde se empieza, y eso no se decide por intuición ni por lo mucho
que te fastidie una tarea. Cuatro preguntas, en este orden, y una escala de 1 a 5 para
que la respuesta sea la misma el lunes y el jueves. Sigue sin haber ninguna
herramienta por medio: esto es un filtro de papel.

## Las cuatro preguntas

1. **Volumen:** frecuencia × minutos. Por debajo de unas 2 h/mes, se aparca.
2. **Explicabilidad:** ¿podrías enseñárselo a alguien nuevo en 10 minutos? Si no, no
   está lista para delegarse: está lista para **documentarse**. Ese es el paso previo,
   no un rechazo.
3. **Tolerancia al fallo:** ¿qué pasa si sale mal 1 de cada 20? Separa «borrador
   interno» de «correo al cliente».
4. **Estabilidad del criterio:** ¿«bien hecho» significa lo mismo el lunes y el
   jueves? **Esta es la que más gente se salta y la que más automatizaciones mata.**

## 1. Volumen — cuánto pesa de verdad

El número ya lo tienes del mapa: minutos/mes = veces al mes × mediana. El umbral son
**120 minutos al mes**. Consultas de estado de pedido, 60 × 4 = 240 min/mes: entra.
Revisión trimestral de tarifas, 4 veces al año × 45 min = 15 min/mes: fuera, por
insoportable que sea.

| Puntuación | Minutos al mes |
|---|---|
| 1 | menos de 30 |
| 2 | de 30 a 120 |
| 3 | de 2 a 4 horas |
| 4 | de 4 a 8 horas |
| 5 | más de 8 horas |

La raya de las dos horas cae entre el 2 y el 3.

## 2. Explicabilidad — ¿sabrías enseñarla?

La prueba es literal: coge la descomposición de `b1-m4-descomposicion`, «Descomponer:
entrada, decisiones, salida, criterio», ponte un cronómetro y explícala en voz alta
como si tuvieras delante a alguien que entró ayer. Registrar un pedido: cuatro
minutos, y la otra persona lo hace bien a la primera.
Decidir el tono de una respuesta a alguien enfadado: no lo consigues, y te oyes decir
«es que ya lo ves».

| Puntuación | Qué significa |
|---|---|
| 1 | No lo consigues ni con tiempo. Te salen tres «depende». |
| 2 | Más de 30 minutos, y hay que acompañar a la persona varias veces. |
| 3 | Entre 10 y 30 minutos, con alguien al lado la primera vez. |
| 4 | 10 minutos con tu descomposición delante. |
| 5 | 10 minutos sin apuntes, y sale bien a la primera. |

> [!NOTE]
> Un 1 o un 2 aquí **no es un no**. Es un «todavía no, y ya sabes qué toca»:
> documentarla. Buena parte del valor de este bloque está justo en las tareas que
> puntúan bajo en explicabilidad, porque son las que solo sabes hacer tú, y eso es un
> problema mucho antes de que aparezca ninguna herramienta.

## 3. Tolerancia al fallo — qué pasa si sale mal 1 de cada 20

La pregunta no es «¿fallará?». Falla todo. Es cuánto cuesta el fallo. Y uno de cada
veinte es más frecuente de lo que suena: en 60 consultas al mes son tres al mes.

Un dato mal en tu resumen interno lo ves tú: cinco minutos. Un plazo inventado en un
correo a un cliente cuesta una promesa incumplida, una reclamación y una llamada de
gerencia. La misma acción de escribir, con dos riesgos que no se parecen en nada.

| Puntuación | Qué pasa si sale mal |
|---|---|
| 1 | Sale fuera y no se puede deshacer: correo a cliente, aviso masivo, dinero o plazos legales. |
| 2 | Sale fuera y se arregla con una llamada incómoda. |
| 3 | Es interno, pero alguien decide con eso sin revisarlo. |
| 4 | Es interno y lo revisa otra persona antes de usarse. |
| 5 | Es un borrador interno que revisas tú de arriba abajo antes de que salga de tu pantalla. |

Dos cosas que la puntuación no recoge y tienes que mirar aparte:

- **Hay trabajo que no se delega aunque puntúe alto en todo lo demás:** decisiones con
  consecuencias para una persona, cualquier cosa con responsabilidad legal y la
  relación con un cliente cuando está mal. Esas no entran en la lista aunque saquen 20
  sobre 20.
- **Si para hacer la tarea hay que mover nombres, teléfonos o direcciones de
  clientes**, la tolerancia baja sola: ahí el fallo no es un texto mal escrito, es un
  problema de datos personales. En el bloque 3 se trabaja entero; por ahora, basta con
  que lo anotes en la fila.

## 4. Estabilidad del criterio — ¿bien hecho significa lo mismo el jueves?

> [!WARNING]
> Esta es la que más gente se salta y la que más automatizaciones mata. Una tarea con
> volumen alto, explicable y de riesgo bajo, pero cuyo «bien hecho» cambia según la
> semana, produce montajes que funcionan un mes y luego hacen daño en silencio: siguen
> produciendo, y lo que producen ya no vale. Si dudas entre dos puntuaciones, pon la
> baja.

La prueba: coge la casilla «criterio» de tu descomposición. ¿La habrías escrito igual
hace tres meses? ¿Seguirá valiendo el mes que viene?

«Bien hecho» en un alta de cliente son los campos obligatorios rellenos y el CIF
verificado: eso no cambió el jueves, es un 5. «Bien hecho» al decidir qué reclamación
merece un detalle comercial depende de cómo vaya el mes, del cliente y del ánimo de
gerencia: es un 1. No tiene nada de malo; simplemente no se delega.

| Puntuación | Qué significa |
|---|---|
| 1 | Cambia caso a caso y nadie lo ha escrito nunca. |
| 2 | Cambia por temporada, por persona o por cómo vaya el mes. |
| 3 | Es estable, pero tiene excepciones que sabes nombrar y no están escritas. |
| 4 | Es estable y las excepciones están escritas. |
| 5 | Cabe en una frase, la misma el lunes que el jueves, y dentro de tres meses también. |

Si quieres la versión larga —hay tres variabilidades distintas y solo una se
absorbe—, está en la rama `b1-p2-variabilidad-mata-automatizaciones`, «La variabilidad
es la que mata automatizaciones».

## La suma, y los frenos que la suma no ve

**Total = Volumen + Explicabilidad + Tolerancia + Estabilidad.** De 4 a 20. Ordena de
mayor a menor. Pero el total ordena, no decide. Antes van los frenos:

| Freno | Qué hace |
|---|---|
| Volumen ≤ 2 | **Aparcar.** Da igual lo bonita que sea. |
| Explicabilidad ≤ 2 | **Documentar.** No es un no: es el paso previo. |
| Estabilidad ≤ 2 | **Documentar el criterio**, no automatizar. Aunque el total sea 15. |
| Tolerancia = 1 | Nunca sin una persona revisando cada salida. |

Y el siguiente paso de cada fila es una de estas cuatro, no otra cosa: `documentar`,
`probar`, `aparcar`, `eliminar`.

## Cuatro tareas puntuadas

Con la misma semana inventada del mapa:

| Tarea | min/mes | Vol | Exp | Tol | Est | Total | Freno | Siguiente paso |
|---|---|---|---|---|---|---|---|---|
| Reclamaciones de factura | 432 | 4 | 2 | 1 | 2 | 9 | Exp, Est y Tol | documentar |
| Consultas de estado de pedido | 240 | 3 | 5 | 4 | 5 | 17 | — | probar |
| Informe semanal para gerencia | 140 | 3 | 4 | 4 | 3 | 14 | — | probar |
| Revisión trimestral de tarifas | 15 | 1 | 3 | 2 | 4 | 10 | Volumen | aparcar |

Lee la primera fila despacio. La tarea que más pesa no es por la que se empieza, y no
porque no valga: su criterio no está escrito, el fallo sale fuera y todavía no sabes
explicarla en diez minutos. Su siguiente paso es documentar, que es exactamente lo que
hiciste en el nodo anterior. Gana una tarea de cuatro minutos que nadie habría mirado.
Eso pasa casi siempre.

Y si marcaste esas 24 reclamaciones como «no debería existir», su siguiente paso puede
ser `eliminar`. Eso no se resuelve puntuando: se resuelve con evidencia, que es justo
lo que estás construyendo.

## Cuándo esto falla

- **Puntuar de memoria.** Si las cifras no salen del diario y del mapa, esto es una
  opinión con números encima.
- **Obedecer la suma.** La suma ordena, los frenos deciden. Un 17 con Estabilidad 2 no
  es un 17.
- **Puntuarte a ti en vez de a la tarea.** «Es que yo me explico bien» no es
  Explicabilidad 5.
- **Poner Estabilidad alta porque nadie te ha dicho nunca que estuviera mal.** A veces
  eso solo significa que nadie lo mira.
- **Un total alto en una tarea que no debería existir.** Automatizarla la consolida y
  la vuelve invisible para siempre.

## Las tres instancias

Las cuatro preguntas no son de tu oficina. Puntúan cualquier tarea repetida:

| Dónde | Puntuación y qué sale |
|---|---|
| **Tu sector (CX)** | La tabla de arriba: gana la tarea pequeña y frecuente, no la que amarga la mañana. |
| **Otro trabajo** | En una gestoría, reclamar documentación cada trimestre: Vol 3, Exp 5, Tol 4, Est 5. Total 17 y nadie la mira, porque son llamadas de dos minutos que no parecen trabajo. |
| **Tu casa** | La colada. Las cuatro preguntas se hacen igual: cuántas veces al mes por cuántos minutos, si sabrías explicarle a alguien que acaba de llegar qué va a 30 grados y qué no, qué pasa si sale mal una de cada veinte, y si «bien hecho» significa lo mismo en enero que en julio. Puntuar una tarea de casa entera es lo que toca en `b1-m7-caso-cruzado-domestico`, «Caso cruzado: la misma lente en tu casa». |

## Ejercicio

**Qué:** aplicar el filtro a **diez tareas** de tu mapa y ordenarlas.

1. Puntúa las cuatro preguntas de 1 a 5 con las tablas de este nodo. Sin inventar
   escalas propias: la gracia es que dentro de un mes puntúes igual.
2. Suma. Ordena de mayor a menor.
3. Aplica los frenos y tacha lo que corresponda.
4. Asigna a cada fila un siguiente paso: `documentar`, `probar`, `aparcar` o
   `eliminar`.
5. Escribe **una línea de justificación por cada 1 y por cada 5**. Las puntuaciones
   del medio no hace falta justificarlas; los extremos sí, porque son los que mandan.

**Dónde:** abre `plantillas/inventario-de-procesos.md`. Trae estas mismas cuatro
columnas y los extremos de la escala, así que puedes puntuar directamente ahí: en
`b1-m8-inventario-de-procesos`, «Tu inventario de procesos», vas a terminar ese
fichero de todas formas.

**Entregable:** diez tareas puntuadas, ordenadas, con freno aplicado y siguiente paso.

**Regla de parada:** no montes nada. Este bloque no toca ninguna herramienta, y no es
un descuido. La primera prueba con IA es `b1-m9-primera-victoria`, «Anticipo: una
victoria pequeña, medida»: es un anticipo medido de media hora, no el método.

## Escribe tú la regla

En la bitácora, con tus palabras:

- «No voy a intentar delegar una tarea mientras \_\_\_.»
- Y la contraria, que es la que se olvida: «voy a empezar por \_\_\_ aunque parezca
  poca cosa, porque \_\_\_.»

## Para la bitácora

- ¿Qué tarea puntuó mucho más alto de lo que esperabas? ¿Y cuál se cayó por un solo
  freno?
- ¿Cuántas de tus diez acabaron en `documentar`? Ese número es el estado real de tu
  trabajo escrito.
- ¿Hay alguna con total alto que, aun así, no delegarías? Escribe por qué. Esa razón
  vale más que la puntuación.
