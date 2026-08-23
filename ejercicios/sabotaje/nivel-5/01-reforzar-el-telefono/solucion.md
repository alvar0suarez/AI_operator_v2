# Solución — Nivel 5, «hay que reforzar el teléfono»

## Qué había

**El razonamiento es inválido.** La conclusión es correcta por razones que el informe no
usa y ni siquiera menciona.

La frase que lo rompe todo:

> «Siendo el canal que acumula casi la mitad de las incidencias, es también el que peor
> está funcionando.»

Eso no se deduce. Un canal puede acumular la mitad de las incidencias simplemente
**porque por ahí entra la mitad de todo**. Y aquí es peor que eso: entra mucho más.

Haz la división. La tabla te da las dos columnas que hacen falta:

| Canal | Incidencias ÷ contactos | Tasa |
|---|---|---|
| Teléfono | 368 ÷ 5.200 | **7,1 %** |
| Presencial | 64 ÷ 700 | 9,1 % |
| Email | 240 ÷ 1.900 | 12,6 % |
| WhatsApp | 128 ÷ 900 | **14,2 %** |

**Por tasa de incidencia, el teléfono es el mejor canal de los cuatro.** Es el que menos
problemas genera por contacto atendido, y con diferencia: la mitad que el email, la
mitad que WhatsApp.

El informe llega a la conclusión correcta apoyándose en el dato que dice justo lo
contrario de lo que él cree que dice.

## Entonces, ¿por qué sí hay que reforzar el teléfono?

Por dos cosas que están en la tabla y que el informe ni mira:

**1. Se lleva dos tercios del tiempo.** Incidencias × tiempo medio:

| Canal | Cálculo | Minutos | % del tiempo |
|---|---|---|---|
| Teléfono | 368 × 22 | 8.096 | **66,3 %** |
| Email | 240 × 11 | 2.640 | 21,6 % |
| WhatsApp | 128 × 7 | 896 | 7,3 % |
| Presencial | 64 × 9 | 576 | 4,7 % |
| | | **12.208** | |

El teléfono es el 46 % de las incidencias y el **66 %** del tiempo de trabajo. Ahí es
donde se va la jornada, y por eso es donde una mejora rinde.

**2. Es el que peor cierra.** Un 14 % de reabiertas, frente al 6 % del email y el 2 % del
presencial. Una de cada siete llamadas hay que volver a tocarla.

Ésa es la recomendación bien fundada: no «el teléfono falla más», sino **«el teléfono
consume dos tercios del tiempo y es el que peor resuelve a la primera»**.

## Por qué importa, si la decisión iba a ser la misma

Ésta es la pregunta buena, y tiene tres respuestas.

**Porque la próxima vez no acertará.** Un método que dice «más incidencias = peor canal»
va a fallar en cuanto los volúmenes cambien. Si mañana WhatsApp crece y pasa a 400
incidencias, el mismo razonamiento dirá que hay que reforzar WhatsApp, y estará mal.
Aquí ha acertado de casualidad.

**Porque la decisión sería distinta al bajar un nivel.** «El teléfono falla mucho» lleva
a formar mejor a quien coge el teléfono. «El teléfono consume 22 minutos por incidencia y
se reabre el 14 %» lleva a otro sitio: a mirar por qué esas llamadas duran tanto y por
qué hay que repetirlas. Son proyectos distintos y cuestan dinero distinto.

**Porque te lo van a discutir.** El día que alguien en esa reunión divida 368 entre
5.200, tu informe se cae entero, y con él tu credibilidad para el siguiente. Y esa
persona tendrá razón.

> **La regla:** una conclusión correcta con un razonamiento inválido no es medio acierto.
> Es un acierto que no se puede repetir, y no se sostiene delante de nadie que mire.

## Cómo se caza barato

Esto no lo pilla la primera pasada (los números están bien) ni la segunda (las
afirmaciones son ciertas). Hace falta una pregunta distinta:

**«¿Se sigue esto de aquello?»**

Coge la conclusión, coge el dato en que se apoya, y pregúntate si uno lleva al otro.
Aquí: ¿de «tiene el 46 % de las incidencias» se sigue «es el que peor funciona»? No, si
no sabes cuánto volumen mueve.

Y una señal muy barata que casi siempre funciona: **si te dan un número absoluto y
existe el denominador, sospecha.** «368 incidencias» no significa nada sin «de cuántos
contactos». Cuando la tabla trae la columna del denominador y el informe no la usa, algo
va mal.

Aquí la columna estaba puesta. Nadie la dividió.

## Rúbrica

| Nivel | |
|---|---|
| **No llegó** | Dio el informe por bueno porque la recomendación le parecía razonable; o marcó un error numérico, que no lo hay. |
| **Llegó** | Vio que del 46 % no se deduce que sea el peor canal, hizo la división por contactos y señaló que por tasa el teléfono es el mejor. |
| **Llegó y encontró algo que no estaba previsto** | Lo anterior, y además **reconstruyó la justificación buena** con los datos de la tabla: el 66 % del tiempo, o el 14 % de reabiertas. Quien hace eso no ha detectado un fallo: ha rehecho el análisis. |

## El error típico

Quedarse tranquila porque la recomendación coincide con lo que ya se pensaba. El
teléfono da mucha guerra, todo el mundo lo sabe en la oficina, así que el informe suena
verdadero.

Eso es exactamente lo que hace que este nivel sea el más caro: **cuando la conclusión te
gusta, no revisas cómo se ha llegado a ella.** Y un razonamiento que nadie revisa se
queda en la casa, se repite en la siguiente reunión, y acaba decidiendo algo importante.
