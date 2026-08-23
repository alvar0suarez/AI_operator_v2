---
id: b1-m8-inventario-de-procesos
bloque: 1
titulo: "Tu inventario de procesos"
tipo: artefacto
duracion_min: 45
requisitos: [b1-m7-caso-cruzado-domestico]
desbloquea: [b2-m1-mapa-de-lo-posible]
caduca: bajo
objetivos:
  - "Reunir diez tareas con sus tres números y sus cuatro puntuaciones en un solo fichero"
  - "Asignar a cada tarea un siguiente paso de entre cuatro posibles"
  - "Marcar al menos una tarea que no debería existir, con el fallo del que nace"
conceptos: [inventario, linea-base, riesgo, coste-de-oportunidad]
artefacto: plantillas/inventario-de-procesos.md
---

Este es el primero de los seis artefactos que te llevas del curso, y no es un ejercicio
que se entrega: es un fichero que vas a volver a abrir dentro de tres meses y dentro de
seis. Todo lo que has medido en dos semanas cabe en una tabla de diez filas. La
plantilla está en `plantillas/inventario-de-procesos.md`; cópiala a tu carpeta antes de
seguir.

## Qué contesta este fichero

Tres preguntas que ahora mismo no sabe contestar nadie de tu empresa, tú incluida:

1. ¿En qué se va tu semana, con números?
2. ¿Por dónde se empieza, y por qué no por la que más te fastidia?
3. ¿Qué trabajo estás haciendo que no debería existir?

Y le sirve a tres personas, que son las tres tú: a la de dentro de tres meses, que se
va a acordar de que miró una tarea pero no de por qué la descartó; a la del bloque 5,
que necesita una línea base contra la que medir; y a la del bloque 6, que va a tener
que enseñar algo con números a alguien que decide.

## Cómo se rellena

No hay nada que inventar aquí. Todo sale de lo que ya tienes.

| Columna | De dónde sale |
|---|---|
| Tarea | De la lista de recurrentes del diario, con las duplicadas agrupadas |
| Veces/mes | Del diario: veces por semana × 4,3 |
| Min (mediana) | Del mapa: los tiempos ordenados, el del medio |
| Variabilidad | Del mapa: baja / media / alta, **y la razón en la nota** |
| Vol, Exp, Tol, Est | Del filtro, con las tablas de `b1-m5-filtro-automatizabilidad`, «El filtro de automatizabilidad: cuatro preguntas» |
| Total | La suma de las cuatro. Ordena, no decide |
| ¿Debería existir? | Sí / no / no lo sé |
| Siguiente paso | `documentar`, `probar`, `aparcar` o `eliminar`. Ninguna otra cosa |

**Diez filas como mínimo.** Con menos no se ve un patrón, se ven anécdotas. Si te salen
dieciocho, mejor: el inventario no tiene tope.

**Las puntuaciones se copian, no se reinventan.** Usa la escala de 1 a 5 tal y como está
en la plantilla y en el filtro. La gracia de una escala es que dentro de un mes puntúes
igual que hoy; si te inventas una propia para cada tarea, el orden de ataque no
significa nada.

**El total ordena, los frenos deciden.** Volumen ≤ 2 aparca. Explicabilidad ≤ 2 manda a
documentar, que no es un no, es el paso previo. Estabilidad ≤ 2 manda a documentar el
criterio aunque el total sea 15. Tolerancia 1 no se queda nunca sin una persona
revisando cada salida.

**Las notas por tarea valen más que las puntuaciones.** Un 3 no dice nada dentro de dos
meses. «Varía porque en 6 de cada 10 casos falta el número de albarán y hay que
buscarlo» sí. Escribe nota en todas las que tengan variabilidad media o alta.

**Y arriba del fichero, una línea tuya:** tu regla de por dónde se empieza, escrita con
tus palabras. No la copies de aquí. La vas a releer en el bloque 5 y quieres saber qué
pensabas hoy.

> [!WARNING]
> En este fichero no van nombres de clientes, ni teléfonos, ni números de factura, ni
> direcciones. «Reclamaciones de un cliente de hostelería» describe la tarea igual de
> bien. Este documento va a acabar delante de otra persona en el bloque 6, y para
> entonces tiene que estar limpio de datos personales. Cuesta cero hacerlo desde el
> principio y cuesta una tarde hacerlo después.

## La columna que casi nadie pone

**¿Debería existir esta tarea?** Sí / no / no lo sé.

Es la columna más incómoda de la tabla y la que más dinero encuentra. Automatizar algo
que no debería existir es peor que no automatizarlo: lo consolida, lo vuelve invisible
y ya nadie se lo cuestiona, porque ahora «está resuelto».

Las 24 reclamaciones de factura al mes de la semana inventada son 432 minutos. Si
quince dicen lo mismo —el importe no cuadra con el albarán—, no tienes una tarea de 432
minutos: tienes un fallo de facturación que **produce** 432 minutos de trabajo al mes y
24 clientes molestos. Contestar más rápido ahorra 288 minutos. Que el importe salga
bien ahorra los 432 y los 24 enfados.

Dos cosas más sobre esta columna:

- **«No lo sé» es una respuesta legítima** y probablemente la más frecuente. Lo que no
  vale es dejarla en blanco.
- **Marcar `eliminar` no es tu decisión y no pasa nada.** Tú no arreglas la facturación
  desde tu silla. Lo que puedes hacer hoy es dejar escrito de qué fallo nace ese
  trabajo, con su número al lado. Eso es lo que se convierte en propuesta en el
  bloque 6, y sin el número no hay propuesta, hay queja.

## Las tres instancias

La misma columna, en tres sitios donde cambia por completo la respuesta:

| Dónde | La tarea | ¿Debería existir? |
|---|---|---|
| **Tu sector (CX)** | 24 reclamaciones de factura al mes, 432 min | No, si quince nacen del mismo error de importe |
| **Otro trabajo** | En una gestoría, perseguir documentación: 40 llamadas al mes, 120 min | No, si se persigue siempre a los mismos ocho clientes: el trabajo no nace de la tarea, nace de que nadie les explicó qué hacía falta y cuándo |
| **Tu casa** | Los veinte minutos del sábado buscando la póliza del seguro | No. No es una tarea que optimizar: es que no hay una carpeta |

En los tres casos la tarea se hace bien, con esfuerzo y con oficio. Y en los tres el
trabajo nace de algo que pasó antes.

## Rúbrica

| Nivel | |
|---|---|
| **No llegó** | Menos de diez tareas, o las cuatro puntuaciones puestas a ojo sin los datos del diario, o la columna «¿debería existir?» en blanco. |
| **Llegó** | Diez tareas o más, con frecuencia y minutos sacados del diario, las cuatro puntuaciones justificables con las tablas del filtro, y un orden de ataque que se sostiene al leerlo. |
| **Llegó y encontró algo que no estaba previsto** | Lo anterior, y además al menos una tarea marcada como que **no debería existir**, con la razón escrita: de qué fallo aguas arriba nace ese trabajo. |

Autocorrección honesta: si la lees y no eres capaz de justificar un solo 1 o un solo 5
sin volver al diario, estás en «no llegó», aunque la tabla esté preciosa.

## Mantenimiento

Un documento vivo es el que se vuelve a abrir. Este se abre cuatro veces:

- **Al terminar el bloque 2**, para anotar en cada fila qué patrón de trabajo es. Ahí
  vas a poder nombrar cosas que ahora solo puedes describir.
- **En el bloque 3**, para separar cómo se verifica cada una según su riesgo.
- **Al terminar el bloque 5**, para anotar en qué nivel se quedó cada tarea y cuántos
  minutos ahorra de verdad, medidos contra la mediana que apuntaste hoy.
- **Cada vez que una tarea cambie de criterio.** Si `Est` baja, revisa lo que hayas
  montado encima: eso es exactamente lo que rompe automatizaciones sin avisar.

Y una fecha arriba. Un inventario sin fecha, dentro de seis meses, no se sabe si es una
foto vieja o el estado actual.

## Para la bitácora

- ¿Cuántas de tus diez tareas acabaron en `documentar`? Ese número es el estado real de
  tu trabajo escrito, y no dice nada malo de ti: dice cuánto de tu oficina vive solo en
  tu cabeza.
- ¿Qué tarea marcaste como que no debería existir, y de qué fallo nace? Si no marcaste
  ninguna, ¿es que no hay, o es que no te has atrevido?
- ¿Cuál es tu regla de por dónde se empieza, la que escribiste arriba del fichero?
  Cópiala aquí tal cual. En el bloque 5 vas a comprobar si acertaste.
