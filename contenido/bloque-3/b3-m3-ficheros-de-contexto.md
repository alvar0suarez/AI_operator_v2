---
id: b3-m3-ficheros-de-contexto
bloque: 3
titulo: "Ficheros de contexto: glosario, tono, plantillas, casuística"
tipo: ejercicio
duracion_min: 50
requisitos: [b3-m2-especificacion-implicita]
desbloquea: [b3-m4-sabotaje, b3-m5-modos-de-fallo]
caduca: medio
objetivos:
  - "Repartir las líneas del ejercicio del intermediario en las cuatro piezas del contexto"
  - "Escribir un criterio de tono como pareja de ejemplos y no como adjetivo"
  - "Aplicar la regla de mantenimiento que hace converger el fichero en vez de inflarlo"
conceptos: [contexto, glosario, tono, plantilla, casuistica, reutilizacion]
---

Del nodo anterior te has traído una lista de preguntas y una lista de líneas escritas.
Ahora tienen que vivir en algún sitio que no sea tu cabeza ni el final de un encargo.
Cuatro piezas, una regla de mantenimiento, y una advertencia: el peligro de este fichero
no es quedarse corto, es engordar hasta que nadie lo lee.

## Escribirlo una vez o explicarlo veinte

Haz la cuenta. Ocho líneas de contexto, dos minutos de tecleo, veinte veces al mes: cuarenta
minutos. Recuperables, pero no es ahí donde está el dinero.

Está en la vez catorce. La vez catorce las escribes distintas: te dejas dos, cambias una
palabra, y el resultado sale distinto sin que sepas por qué. Un fichero de contexto no
ahorra sobre todo tecleo: **ahorra variación**. Lo que no está escrito cambia solo, y eso
ya lo viste con las rúbricas en `b2-m6-comparar-contra-criterio`, «Verbo 5: comparar contra
criterio».

La plantilla está en `plantillas/contexto-trabajo.md`. **Ábrela ahora y léela entera**: no
la repetimos aquí. Hoy la rellenas en borrador; se cierra como artefacto en
`b3-m9-contexto-trabajo`, «Tu primer fichero de contexto de trabajo».

## Las cuatro piezas

### 1. Glosario propio

Tus palabras, las que aquí significan algo distinto de lo que significan fuera. Es la
sección que más rinde y la que todo el mundo se salta, porque cuesta creer que «abono» no
signifique lo mismo en todas partes.

| Palabra | Qué significa aquí | Qué no significa |
|---|---|---|
| Abono | Nota de crédito en la siguiente factura | Un pago, ni una devolución de dinero |
| Retornable | Envase que vuelve en el siguiente reparto y tiene depósito | Reciclable |
| Portes | Cargo por servir fuera del día de ruta | El coste del transporte normal |
| Urgente | Que sale hoy, no mañana | Que se contesta ya |

Fíjate en la tercera columna: lo que fija una palabra no es la definición, es el límite.

### 2. Tono, con ejemplos y no con adjetivos

«Cercano pero profesional» no le dice nada a nadie: dos personas que lean eso escribirán
dos textos distintos. El tono se escribe con una pareja.

> **Así sí:** «Hola, Manuel: el jueves se averió el camión de tu ruta y tu pedido no salió.
> Siento el lío. Sale el lunes a primera hora.»
>
> **Así no:** «Estimado cliente: lamentamos profundamente las molestias ocasionadas por la
> incidencia acaecida en su servicio de entrega.»
>
> **La diferencia:** se le llama por su nombre, se dice qué pasó en concreto, se pide
> perdón una vez y en cuatro palabras, y hay una fecha.

Esa última línea es la pieza. Sin ella tienes dos ejemplos; con ella tienes una regla que
puede aplicar otra persona.

### 3. Plantillas

Los textos que ya tienes hechos y que funcionan, con el hueco variable marcado. Ahorran
tecleo y, sobre todo, evitan que nadie improvise un compromiso.

Cada plantilla lleva dos líneas que casi nadie escribe: **cuándo se usa** y **cuándo no se
usa**. La segunda es la que impide que la plantilla de «no me cuadra la factura» acabe
contestando una reclamación de producto en mal estado, que es como se manda un texto
correcto a la persona equivocada.

### 4. Casuística

Los casos raros con su tratamiento. Cuatro columnas: el caso, qué se hace, **quién lo
decide** y **desde cuándo es así**.

Las dos últimas parecen burocracia y son lo contrario. «Quién lo decide» evita que alguien
—tú incluida— resuelva por su cuenta algo que no le toca. «Desde cuándo» te permite tirar
la fila cuando la razón que la justificaba desapareció hace dos años.

Aquí van los «¿y si el cliente…?» del intermediario, y las excepciones declaradas del
bloque 1. Una excepción escrita no rompe el proceso; una escondida, sí.

## La regla que hace que converja

**El fichero crece cuando algo sale mal, no cuando se te ocurre algo.**

Parece disciplina y es aritmética. Las ocurrencias son infinitas: cada vez que abras el
fichero se te ocurrirán tres cosas más que «estaría bien poner». A ese ritmo tienes ocho
páginas en un mes y no las lee nadie, empezando por ti. Los fallos son finitos y se
repiten: los mismos seis o siete líos vuelven cada mes. Un fichero que solo crece por fallo
añade una línea por semana y se estabiliza en dos páginas. Uno que crece por ocurrencia no
se estabiliza nunca.

El gesto es siempre el mismo: cuando algo salga mal, la pregunta no es «¿qué herramienta
uso?» —eso ya lo sabes desde `b0-m3-fallar-es-diagnostico`, «Fallar es diagnóstico, no
fracaso»—, es **«¿qué línea le faltaba a mi contexto?»**. Se añade, con la fecha, en la
tabla de mantenimiento.

Y la mitad que nadie aplica: **también se quita**. Una línea que no ha hecho falta en seis
meses, o que describe un caso que ya no existe, sobra.

> [!WARNING]
> Este fichero se escribe anonimizado desde la primera línea. Nada de nombres, teléfonos,
> correos ni direcciones: etiquetas, CLIENTE_A. Es un fichero que vas a pegar en sitios, y
> no quieres tener que revisarlo cada vez antes de pegarlo. El porqué completo está en
> `b3-m7-datos-y-rgpd`, «Datos y RGPD: qué no se pega jamás».

## Cuándo esto falla

- **Contexto viejo.** Es el fallo que no avisa. `dataset/ficheros/procedimientos.docx`
  habla de tres rutas y en el maestro de clientes hay cuatro; la portada explica por qué, y
  es de 2019. Un contexto desactualizado no produce error: produce respuestas correctas
  según una realidad que ya no existe.
- **Contexto oficial en vez de contexto real.** Si escribes lo que pone el procedimiento y
  no lo que hacéis, tendrás un fichero impecable e inútil. Y si se parecen poco, eso es un
  hallazgo: se anota aparte.
- **Contexto que contradice al encargo.** Si el contexto dice «tuteamos» y el encargo pide
  «trato formal», gana el ruido. Las dos piezas se leen juntas o no se leen.
- **Contexto de veinte páginas.** Cuanto más largo, menos pesa cada línea. Si no cabe en
  dos páginas, no falta síntesis: sobra material que entró por ocurrencia.
- **Contexto para tapar un criterio inestable.** Si «bien hecho» cambia según la semana,
  ningún fichero lo arregla. No es falta de contexto: es falta de decisión, y no te toca a
  ti tomarla.

## Las tres instancias

| Dónde | Glosario | Casuística |
|---|---|---|
| **Tu sector (CX)** | Qué es aquí un abono, un retornable, un porte | Qué se hace con el cliente que reclama por segunda vez el mismo pedido |
| **Otro trabajo** | En una clínica dental, qué es una «revisión», una «urgencia» y una «primera» | Qué se hace con quien llega veinte minutos tarde y hay otro paciente detrás |
| **Tu casa** | Las instrucciones para quien te cuida la casa: qué es «la llave de abajo», «el cuarto de la caldera» | Qué se hace si el perro no come, si llama el vecino, si se va la luz |

La tercera es la prueba del algodón. Todo el mundo cree que sus ocho líneas están
completas hasta que la persona llega y pregunta cuatro cosas en dos horas.

## Ejercicio

**Material:** tu `preguntas-<tarea>.md` de `b3-m2-especificacion-implicita`, «Todo lo que
en tu oficina se da por hecho», y la plantilla `plantillas/contexto-trabajo.md` abierta al
lado.

**1. Reparte (10 min).** Cada línea que escribiste ayer va a una de las cuatro piezas:
palabra → glosario, cómo se dice → tono, cómo se hace normalmente → plantilla, caso raro →
casuística. Si una línea no encaja en ninguna, apártala: casi siempre es una decisión que
todavía no ha tomado nadie, y eso se anota, no se inventa.

**2. Glosario (10 min).** Cinco palabras, con las dos columnas: qué significa aquí y qué no
significa. Ojo con las que llevas tanto tiempo usando que ya no te parecen palabras.

**3. Tono (10 min).** Una sola pareja: un texto tuyo que aceptarías y uno que rechazarías,
y debajo **la diferencia en una frase**. La frase es el ejercicio; los dos ejemplos son la
excusa.

**4. Plantilla (8 min).** Una, la que más uses, con los huecos marcados y sus dos líneas:
cuándo se usa y cuándo no.

**5. Casuística (8 min).** Tres filas, con quién decide y desde cuándo. Salen de las
preguntas del intermediario que empezaban por «¿y si…?».

**6. Abre el mantenimiento (2 min).** La tabla de tres columnas con la fecha de hoy y una
línea vacía. No es adorno: la próxima vez que algo salga mal, ya sabes dónde se apunta.

**Entregable:** `contexto-borrador.md` con las cuatro piezas al mínimo indicado y la tabla
de mantenimiento abierta. Anonimizado, sin excepción.

**Regla de parada:** cincuenta minutos y se cierra, esté como esté. Este fichero no se
termina hoy, y no está diseñado para terminarse: está diseñado para crecer una línea cada
vez que algo salga mal.

## Escribe tú la regla

En la bitácora, con tus palabras:

- «Mi fichero de contexto crece cuando \_\_\_ y solo cuando \_\_\_.»
- «Una línea de mi contexto sobra cuando \_\_\_.»

## Para la bitácora

- ¿Cuántas de las líneas de ayer se te quedaron fuera de las cuatro piezas, y qué eran?
- ¿Qué palabra de tu glosario te ha sorprendido tener que explicar?
- La diferencia entre tus dos ejemplos de tono, ¿la has sabido escribir en una frase o has
  necesitado tres intentos?
