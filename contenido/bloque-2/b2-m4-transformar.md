---
id: b2-m4-transformar
bloque: 2
titulo: "Verbo 3: transformar"
tipo: ejercicio
duracion_min: 40
requisitos: [b2-m3-extraer]
desbloquea: [b2-m5-redactar-borrador]
caduca: bajo
objetivos:
  - "Declarar por escrito qué se puede perder antes de cambiar de formato"
  - "Producir tres versiones del mismo ticket para tres destinatarios distintos"
  - "Detectar la pérdida silenciosa con la prueba de la vuelta"
conceptos: [transformar, formato, perdida-de-informacion, verbo]
dataset: [dataset/ficheros/tickets.xlsx]
---

Éste parece el verbo tonto. Cambiar algo de formato sin cambiar lo que dice suena a
trámite, y es donde más información se pierde sin que nadie se entere. Resumir es
transformar con pérdida, y casi nadie escribe antes qué estaba dispuesto a perder.
Hoy lo vas a escribir, y luego vas a medir si acertaste.

## Qué es

Cambiar de formato conservando el contenido. Un hilo de cuatro correos convertido en un
parte de incidencia de cinco líneas. Una tabla convertida en un párrafo. Tres formatos
de fecha en una columna convertidos en uno solo.

La palabra que hace todo el trabajo es **conservando**, y casi siempre es mentira a
medias. Un parte de cinco líneas no conserva un hilo de cuatro correos: se queda con
una parte. La pregunta útil no es «¿se pierde algo?» —siempre se pierde—, sino
**«¿qué estoy dispuesta a perder, y quién lo ha decidido?»**. Si no lo decides tú
antes, lo decide el resultado después, y no te avisa.

## Cuándo brilla

- **Cuando el contenido ya está bien y lo que falla es la forma.** No hay que
  averiguar nada ni decidir nada: solo reescribir. Es el verbo de riesgo más bajo de
  los seis.
- **Cuando cambia el lector y no el hecho.** El mismo incidente lo tienen que leer el
  compañero de reparto en el móvil, tú dentro de un mes y gerencia en una línea. Tres
  formatos, un solo hecho.
- **Normalizar.** Una columna con `2024-11-03`, `03/11/2024` y `3-nov-2024` no se puede
  ordenar ni filtrar. Unificarla es transformar, y es de las cosas que más tiempo
  devuelven por lo poco que cuestan.
- **La cuenta:** un parte de incidencia escrito a mano son unos 6 minutos. Veinte al
  mes son 120 minutos. Justo en la raya del filtro, y de las pocas tareas donde el
  resultado se comprueba de un vistazo.

## Cuándo esto falla

- **Pérdida no declarada.** Un hilo de cuatro correos se convierte en cinco líneas
  limpias y por el camino desaparece que el cliente ya había reclamado en noviembre,
  que era lo único importante. El fallo no fue perder: fue no haber dicho qué se podía
  perder.
- **Reordenar cambia el sentido.** «Te abonamos el importe si el albarán lo confirma»
  y «te abonamos el importe; el albarán lo confirmará» tienen las mismas palabras y no
  dicen lo mismo. Las condiciones se caen al reordenar, y son justo la parte por la
  que te van a reclamar.
- **Añadir en vez de cambiar.** Aparecen en el resumen palabras que no estaban:
  «urgente», «reiterado», «cliente molesto». Eso ya no es transformar, es opinar, y
  después alguien decidirá con esa opinión creyendo que es un dato.
- **Vacío y cero no son lo mismo.** Una celda de minutos vacía significa «nadie lo
  apuntó». Convertida en prosa se transforma en «0 minutos», que significa «no costó
  nada». Un dato inventado con toda la apariencia de dato.
- **La ida y vuelta.** Tabla → prosa → tabla no devuelve la tabla de partida. Y como el
  texto intermedio se lee bien, nadie sospecha.

**Cómo se comprueba: la prueba de la vuelta.** Coge tu versión corta y reconstruye
desde ella la versión larga, sin mirar el original. Compara. Lo que no vuelva es lo que
perdiste. La pregunta es una sola: **¿estaba en tu lista de «se puede perder»?** Si
estaba, la transformación es correcta. Si no estaba, acabas de encontrar una pérdida
silenciosa, y esa es la única forma barata de encontrarlas.

> [!TIP]
> La segunda comprobación cuesta treinta segundos: subraya en el resultado todas las
> cifras, fechas y adjetivos, y búscalos en el original. Lo que no esté en el original
> no se ha transformado: se ha añadido.

## Las tres instancias

| Dónde | De qué a qué | Se puede perder / no se puede perder |
|---|---|---|
| **Tu sector (CX)** | Hilo de correos a parte de incidencia | Se pierden los saludos, las repeticiones y el orden en que se contó. No se pierde el importe, la fecha del pedido ni que ya había reclamado antes. |
| **Otro trabajo** | Acta de reunión a lista de acuerdos | Se pierde el debate: quién opinó qué y en qué orden. No se pierde quién se comprometió a qué y para cuándo. Un acuerdo sin dueño y sin fecha no es un acuerdo. |
| **Tu casa** | Receta larga a tarjeta de nevera | Se pierden las explicaciones y las alternativas. No se pierden cantidades, tiempos ni el paso que no es obvio: la tarjeta que se come «reserva el agua de cocción» te lo dice sola a las dos semanas. |

## Ejercicio

**Material:** `dataset/ficheros/tickets.xlsx`, hoja `Tickets`. Elige **tres tickets con
la descripción larga**, de meses distintos. Trabaja con la fila entera, no solo con la
descripción: fecha, canal, cliente, estado, agente y minutos.

Para cada ticket, produce **tres versiones** del mismo hecho (20 min):

| Versión | Para quién | Formato |
|---|---|---|
| **A. Ficha** | Para ti dentro de un mes | Campos fijos: qué pasó, cuándo, quién, qué falta por hacer |
| **B. Aviso** | Para el compañero de reparto | Tres líneas de texto llano, que se lean en el móvil dentro de la furgoneta |
| **C. Línea de listado** | Para gerencia | Una sola línea, máximo 20 palabras |

**Antes de escribir cada versión**, rellena la casilla en una línea:

> Se puede perder: \_\_\_. No se puede perder: \_\_\_.

Dos decisiones que te van a salir por el camino, y que son parte del ejercicio: la
`fecha_apertura` viene escrita de tres maneras distintas en el fichero —elige un
formato y anótalo—, y algunas casillas de `tiempo_dedicado_min` están vacías. Vacío no
es cero: decide cómo lo escribes y déjalo por escrito.

**La prueba de la vuelta (10 min).** Coge la versión C de cada ticket y, sin mirar el
original, reconstruye la ficha A. Compara con la ficha A verdadera. Anota qué campos no
han vuelto y márcalos: `declarado` si estaba en tu casilla de «se puede perder»,
`silencioso` si no estaba.

**Entregable:** `transformaciones.md` con los tres tickets, sus tres versiones, las
casillas de pérdida declarada y el recuento de pérdidas silenciosas. Ese último número
es el que vale.

**Regla de parada:** tres formatos y se acabó. No montes una plantilla para cada
destinatario imaginable: la mayoría no volverá a aparecer, y una plantilla que no se
usa hay que mantenerla igual.

## Escribe tú la regla

En la bitácora, con tus palabras:

- «Antes de resumir algo, escribo \_\_\_.»
- «Sé que un resumen se ha dejado algo importante cuando \_\_\_.»

## Para la bitácora

- ¿Cuántas pérdidas silenciosas te salieron en la prueba de la vuelta, y en qué
  versión: en la de tres líneas o en la de una?
- ¿Apareció en alguna versión una palabra que no estaba en el original? ¿Cuál, y qué
  habría decidido alguien leyéndola?
- ¿Qué transformas tú cada semana sin haber declarado nunca qué se puede perder?
