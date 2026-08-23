---
id: b1-m8-inventario-de-procesos
bloque: 1
titulo: "Tu inventario de procesos"
tipo: artefacto
duracion_min: 30
requisitos: [b1-m7-caso-cruzado-domestico]
desbloquea: [b2-m1-mapa-de-lo-posible]
caduca: bajo
objetivos:
  - "Reunir en un solo fichero las diez tareas con sus tres números y sus cuatro puntuaciones"
  - "Asignar a cada tarea un siguiente paso de entre cuatro posibles"
  - "Escribir arriba del fichero la regla propia de por dónde se empieza"
conceptos: [inventario, linea-base, riesgo, coste-de-oportunidad]
artefacto: plantillas/inventario-de-procesos.md
---

Aquí no se mide nada nuevo. Todo lo que has medido en dos semanas está repartido entre
el diario, el mapa y la hoja del filtro, y esta sesión consiste en juntarlo en un solo
fichero que vas a volver a abrir dentro de tres meses y dentro de seis. La plantilla
está en `plantillas/inventario-de-procesos.md`; cópiala a tu carpeta antes de seguir.

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

Todo sale de ficheros que ya tienes abiertos.

| Columna | De dónde sale |
|---|---|
| Tarea | De la lista de recurrentes del diario, con las duplicadas agrupadas |
| Veces/mes | Del mapa: veces por semana × 4,3 |
| Min (mediana) | Del mapa: la mediana en las que pasan de la raya, el número a ojo en las demás |
| Variabilidad | Del mapa: baja / media / alta, **y la razón en la nota** |
| Vol, Exp, Tol, Est | Del filtro de `b1-m5-filtro-automatizabilidad`, «El filtro de automatizabilidad: cuatro preguntas» |
| Total | La suma de las cuatro. Ordena, no decide |
| ¿Debería existir? | Sí / no / no lo sé |
| Siguiente paso | `documentar`, `probar`, `aparcar` o `eliminar`. Ninguna otra cosa |

**Diez filas como mínimo.** Con menos no se ve un patrón, se ven anécdotas. Si te salen
dieciocho, mejor: el inventario no tiene tope.

**Las puntuaciones se copian, no se reinventan.** La gracia de una escala es que dentro
de un mes puntúes igual que hoy. Si te inventas una propia por tarea, el orden de
ataque no significa nada.

**El total ordena, los frenos deciden.** Volumen ≤ 2 aparca. Explicabilidad ≤ 2 manda a
documentar, que no es un no, es el paso previo. Estabilidad ≤ 2 manda a documentar el
criterio aunque el total sea 15. Tolerancia 1 no se queda nunca sin una persona
revisando cada salida.

**Las notas valen más que las puntuaciones.** Un 3 no dice nada dentro de dos meses.
«Varía porque en 6 de cada 10 casos falta el número de albarán y hay que buscarlo» sí.

**La columna «¿debería existir?» se traslada, no se piensa otra vez:** el razonamiento
está en `b1-m3-mapa-de-la-semana`, «Mapa de la semana: frecuencia, duración,
variabilidad». Aquí solo hay una regla nueva: «no lo sé» es una respuesta válida, y
probablemente la más frecuente. En blanco, no.

**Y arriba del fichero, una línea tuya:** tu regla de por dónde se empieza, escrita con
tus palabras. No la copies de aquí. La vas a releer en el bloque 5 y quieres saber qué
pensabas hoy.

> [!WARNING]
> En este fichero no van nombres de clientes, ni teléfonos, ni números de factura, ni
> direcciones. «Reclamaciones de un cliente de hostelería» describe la tarea igual de
> bien. Este documento puede acabar delante de otra persona en el bloque 6, y para
> entonces tiene que estar limpio de datos personales. Cuesta cero hacerlo desde el
> principio y una tarde hacerlo después.

## Rúbrica

| Nivel | |
|---|---|
| **No llegó** | Menos de diez tareas, o las cuatro puntuaciones puestas a ojo sin los datos del diario, o la columna «¿debería existir?» en blanco. |
| **Llegó** | Diez tareas o más, con frecuencia y minutos sacados del diario, las cuatro puntuaciones justificables con las tablas del filtro, y un orden de ataque que se sostiene al leerlo. |
| **Llegó y encontró algo que no estaba previsto** | Lo anterior, y además al menos una tarea marcada como que **no debería existir**, con la razón escrita: de qué fallo aguas arriba nace ese trabajo. |

Autocorrección honesta: si lo lees y no eres capaz de justificar un solo 1 o un solo 5
sin volver al diario, estás en «no llegó», aunque la tabla esté preciosa.

## Mantenimiento

Un documento vivo es el que se vuelve a abrir. Este se abre tres veces:

- **Al terminar el bloque 2**, para marcar qué verbo es cada tarea. Ahí vas a poder
  nombrar cosas que hoy solo sabes describir.
- **Al terminar el bloque 5**, para anotar en qué nivel se quedó cada tarea y cuántos
  minutos ahorra de verdad, medidos contra la mediana que apuntaste hoy.
- **Cada vez que una tarea cambie de criterio.** Si `Est` baja, revisa lo que hayas
  montado encima: eso es exactamente lo que rompe automatizaciones sin avisar.

Y una fecha arriba. Un inventario sin fecha, dentro de seis meses, no se sabe si es una
foto vieja o el estado actual.

## Para la bitácora

- Con las diez filas juntas y ordenadas, ¿por cuál empezarías? ¿Es la misma que
  habrías dicho hace dos semanas, antes de medir nada?
- ¿Qué tarea marcaste como que no debería existir, y de qué fallo nace? Si no marcaste
  ninguna, ¿es que no hay, o es que no te has atrevido?
- ¿Cuál es tu regla de por dónde se empieza, la que escribiste arriba del fichero?
  Cópiala aquí tal cual. En el bloque 5 vas a comprobar si acertaste.
