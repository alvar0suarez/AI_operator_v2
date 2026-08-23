---
id: b3-m1-anatomia-encargo
bloque: 3
titulo: "Anatomía de un encargo"
tipo: concepto
duracion_min: 50
requisitos: [b2-m10-catalogo-de-patrones]
desbloquea: [b3-m2-especificacion-implicita]
caduca: bajo
objetivos:
  - "Separar un encargo en sus cinco piezas y señalar cuál falta"
  - "Reescribir un encargo vago pieza a pieza hasta que un tercero pudiera ejecutarlo"
  - "Escribir un criterio de aceptación de tres a cinco comprobaciones que se puedan mirar"
conceptos: [encargo, objetivo, restriccion, formato, criterio-de-aceptacion]
profundizar:
  - id: b3-p3-criterio-de-aceptacion
    titulo: "Escribir un criterio de aceptación que sirva"
---

Ya sabes qué se puede pedir. Ahora, cómo se pide. Un encargo tiene cinco piezas y casi
todo el mundo escribe dos. Aquí hay un encargo malo que se reescribe pieza a pieza, con
lo que sale de cada versión, para que veas cuál cambia el resultado y cuál no está nunca.

## Esto ya lo hiciste en el bloque 1

No es materia nueva. Es la descomposición de `b1-m4-descomposicion`, «Descomponer:
entrada, decisiones, salida, criterio», escrita para un destinatario que no sabe nada de
tu oficina.

| Bloque 1: descomponer, para ti | Bloque 3: encargar, para otro |
|---|---|
| **Entrada**: qué llega y qué falta | **Contexto**: qué le pongo delante, porque no lo tiene |
| **Decisiones**: qué eliges y con qué | **Restricciones**: qué no decide por su cuenta |
| **Salida**: qué queda y con qué forma | **Formato**: con qué forma exacta lo quiero |
| **Criterio de «bien hecho»** | **Criterio de aceptación**: cómo compruebo que sirve |

Falta la pieza que antes no hacía falta escribir: el **objetivo**. Cuando la tarea la
haces tú, ya sabes para qué. Y la prueba de calidad es la de entonces: **un tercero podría
ejecutarlo sin preguntarte nada**.

## El encargo malo, pieza a pieza

Un bar escribe porque el reparto del jueves no ha llegado. Tú sabes que se averió el
camión de esa ruta y que su pedido sale el lunes a primera hora.

**Versión 0.** «Escríbeme la respuesta a este cliente.»

> Estimado cliente:
> Lamentamos profundamente las molestias ocasionadas por la incidencia sufrida en su
> entrega. Le confirmamos que su pedido será entregado en un plazo máximo de 24 horas y
> que, por supuesto, procederemos a compensarle. Quedamos a su entera disposición.

Bien escrito y con cuatro problemas, ninguno de estilo: las 24 horas no las ha dicho
nadie, la compensación no la ha autorizado nadie, «estimado cliente» a un bar de ocho años
es un error de tono, y no dice si él tiene que hacer algo.

**Versión 1: el objetivo.** «Que sepa qué día recibe el pedido y no tenga que volver a
escribir para preguntarlo.» El texto ya empieza por la fecha en vez de por las disculpas.
Pero la fecha sigue inventada, porque sigues sin darla. **El objetivo ordena el texto; no
lo hace cierto.**

**Versión 2: el contexto.** «Cliente de hostelería, pedido semanal, ocho años con
nosotros, reparto los jueves. El jueves 13 se averió el camión de su ruta; sale el lunes
17 a primera hora. A los de toda la vida los tuteamos.» El tono se arregla solo y la fecha
ya es la buena. Pero ahora ofrece por su cuenta que «el porte corre de nuestra cuenta».
**El contexto arregla lo que sabe; no impide lo que se añade.**

**Versión 3: las restricciones.** «Ninguna compensación, descuento ni porte gratis.
Ninguna fecha que no esté en el contexto. Sin la palabra "incidencia". Una disculpa y solo
una. Máximo 120 palabras.» Ya no promete nada, pero llega en cuatro párrafos y sigue sin
decir qué tiene que hacer el cliente. **Las restricciones dicen lo que no; falta quien
diga lo que sí.**

**Versión 4: el formato.** «Tres párrafos: qué ha pasado, qué día y en qué franja llega, y
qué tiene que hacer él; si no tiene que hacer nada, decirlo.»

> Hola, Manuel:
> El jueves se averió el camión de tu ruta y tu pedido no salió. Siento el lío.
> Sale el lunes 17 a primera hora, con el reparto de siempre: lo tienes por la mañana.
> No tienes que hacer nada ni volver a pedirlo. Si al mediodía no ha llegado, llámame.

Cuatro piezas, ciento veinte palabras, y ya se puede mandar. Parece terminado. No lo está:
queda la quinta.

## La pieza que falta siempre

Falta el **criterio de aceptación**: cómo compruebas que lo que ha salido sirve. Y falta
casi siempre, por una razón que no tiene nada de tonta.

Esa comprobación llevas años haciéndola. La haces mientras lees, en tres segundos, sin
nombrarla. Nunca ha necesitado estar escrita porque siempre ha estado tu cabeza delante
del texto. En cuanto lo produce otro y tú solo lo apruebas, tiene que salir de tu cabeza
y aterrizar en el papel. Si no aterriza, se sustituye por una impresión.

Prueba de bolsillo: alguien te enseña un texto y te pregunta si está bien. Si contestas
«sí» y no puedes decir contra qué lo has mirado, era una impresión. **Un criterio de
aceptación sirve si dos personas lo aplican por separado y coinciden.** Si no, no es un
criterio: es un gusto con formato de norma.

### Las tres comprobaciones que se pueden mirar

| Tipo | La pregunta | Ejemplo |
|---|---|---|
| **Cantidad** | ¿cuántos? | ¿120 palabras o menos? ¿una sola disculpa? |
| **Presencia** | ¿está o no está? | ¿está el día concreto? ¿aparece «incidencia»? |
| **Procedencia** | ¿de dónde sale? | esa fecha, ¿puedo señalarla en lo que le di? |

Las dos primeras las escribe cualquiera. La tercera casi nadie, y es la que caza lo que
las otras dos no ven: un dato inventado pasa las dos primeras sin despeinarse, porque
tiene el tamaño correcto y está en el sitio correcto.

Y se olvida una mitad entera: **qué no puede aparecer**. La lista de prohibiciones de
`b2-m5-redactar-borrador`, «Verbo 4: redactar borrador», ya era medio criterio de
aceptación sin nombre.

### El criterio del ejemplo

> 1. 120 palabras o menos.
> 2. Aparece el día y la franja, y coinciden con el contexto.
> 3. Se dice qué tiene que hacer él, aunque sea nada.
> 4. No aparece ningún importe, descuento ni porte.
> 5. Hay una disculpa y solo una.

Cinco líneas, cuarenta segundos, mismo resultado el lunes que el jueves. Y cambian lo que
puedes decir después: en vez de «no me convence», «falla la 3». Con lo segundo se arregla
el encargo; con lo primero solo se puede repetir y cruzar los dedos.

Cuando la comprobación es de tono, que es la difícil, no se escribe con adjetivos: se
escribe con un ejemplo que aceptarías y otro que rechazarías, y la regla es la diferencia
entre los dos. Eso está entero en `b3-p3-criterio-de-aceptacion`, «Escribir un criterio de
aceptación que sirva».

**Regla de parada: entre tres y cinco comprobaciones.** Con doce no aplicas ninguna y
vuelves a la impresión. Y cada una necesita dueño: un criterio sin dueño no es un
criterio, y eso ya lo sabías.

## Cuándo esto falla

- **Tareas de una vez.** Quince minutos de encargo para algo que haces en seis, una vez al
  año, son quince minutos tirados. Sigue vigente el umbral del bloque 1: por debajo de unas
  dos horas al mes, se hace y ya está.
- **Cuando «bien hecho» cambia el jueves.** Es la cuarta pregunta de
  `b1-m5-filtro-automatizabilidad`, «El filtro de automatizabilidad: cuatro preguntas». Sin
  criterio estable no hay criterio de aceptación que escribir: toca documentar por qué
  cambia, no encargar.
- **Cuando la tarea no se delega.** Un encargo impecable de algo de
  `b2-m9-que-no-es-ninguno`, «Lo que no es ninguno de los seis», sigue siendo un error.
- **Cuando el destinatario es una persona.** Las piezas son las mismas; las palabras, no.
  «Restricciones», leído por un compañero, suena a desconfianza.

## Las tres instancias

| Dónde | Objetivo → contexto → restricción → formato → criterio |
|---|---|
| **Tu sector (CX)** | El ejemplo de arriba. Lo que faltaba no era contexto: eran las cinco comprobaciones que aplicabas de memoria |
| **Otro trabajo** | En una gestoría, el aviso trimestral encargado a la persona nueva: que ningún cliente se entere el día 18 / a los domiciliados no se les avisa / sin importes ni borradores adjuntos / seis líneas y los tres documentos en lista / ¿lleva fecha límite?, ¿están los tres?, ¿no hay ningún importe? |
| **Tu casa** | La tarta de cumpleaños, por teléfono: postre para doce el sábado a las cinco / hay una niña alérgica a los frutos secos / sin fondant / redonda y de menos de 28 cm / ¿el nombre bien escrito?, ¿mide menos de 28?, ¿trae etiqueta de alérgenos? |

La de casa es la más clara: quien no dice la medida se lleva una tarta que no entra en la
nevera, y no es culpa del pastelero. El formato cuesta cuatro palabras y es la pieza que
más se salta.

## Ejercicio

Coge de tu `inventario-de-procesos.md` una tarea ya descompuesta y que sea de uno de los
seis verbos. No la más difícil: la que más repites. Escríbele las cinco piezas en
`encargo-<tarea>.md` con estos mínimos: objetivo en una frase y que sea un resultado, no
un tema; contexto sin nombres de clientes —«un bar con contrato mensual» describe el caso
igual de bien y no te crea un problema—; tres restricciones, dos empezando por «no»;
formato con los nombres de las columnas si es una tabla; y de tres a cinco comprobaciones
de aceptación, una de cada tipo, con su dueño.

Después, la prueba: diez minutos más tarde, lee **solo** el encargo y ejecútalo al pie de
la letra, sin usar nada que no esté escrito ahí. Cada vez que tengas que tirar de lo que
sabes, una marca al margen. Es la ejecución literal del bloque 1 y mide lo mismo:
agujeros. Apunta cuántas marcas debajo del encargo.

**Regla de parada:** no se lo des a nadie todavía. Eso es el nodo siguiente.

## Escribe tú la regla

En la bitácora, con tus palabras:

- «Un encargo mío está terminado cuando \_\_\_.»
- «Mi criterio de aceptación sirve si \_\_\_, y sé que no sirve cuando \_\_\_.»

## Para la bitácora

- ¿Qué pieza te ha costado más escribir, y cuál te saltaste sin darte cuenta hasta releer?
- ¿Cuántas marcas te salieron en la ejecución literal?
- La comprobación de procedencia, la de «¿de dónde sale este dato?», ¿la habías hecho
  alguna vez por escrito?
