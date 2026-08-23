---
id: b3-p5-coste-de-verificar-de-mas
bloque: 3
titulo: "Verificar de más también es un error"
tipo: profundizacion
duracion_min: 15
requisitos: [b3-m6-verificacion-proporcional]
desbloquea: []
caduca: bajo
objetivos:
  - "Calcular el tiempo máximo de verificación que admite una tarea"
  - "Decidir si una tarea deja de compensar al nivel de verificación que exige su riesgo"
  - "Reconocer cuándo verificar de más está justificado"
conceptos: [coste-de-verificar, riesgo, coste-de-oportunidad]
---

Rama corta de la verificación proporcional. Quince minutos para tener una cuenta que se
hace de cabeza y que decide si una tarea merece un montaje o si lo que has construido es
una pérdida disfrazada de modernidad.

## La aritmética

Tres números, y ninguno es difícil:

- **T mano:** lo que tardas haciéndolo tú, de principio a fin.
- **T producir:** escribir el encargo y obtener el resultado.
- **T verificar:** comprobarlo al nivel que pide su riesgo.

Compensa si **T producir + T verificar < T mano**. No hay más teoría.

De ahí sale el número que conviene tener escrito en la ficha de cada tarea:

> **V máx = T mano − T producir**

Es el tiempo máximo que puedes dedicar a verificar antes de que esto deje de tener
sentido. Si tu verificación pasa de ahí, estás haciendo el trabajo dos veces y pagando
además el rato de montarlo.

## Un ejemplo con números

Clasificar 200 tickets por tipo de incidencia.

| | Cuentas | Total |
|---|---|---|
| A mano | 200 × 25 s | **83 min** |
| Producir | Encargo y resultado | 5 min |
| Verificar línea a línea | 200 × 20 s de abrir y comparar | 67 min → **72 min**, ahorras 11 |
| Verificar por muestra | 70 tickets (5 + 2 extremos por lote de 20) × 20 s | 23 min → **28 min**, ahorras 55 |

V máx aquí son 78 minutos. La verificación línea a línea cabe por los pelos y deja un
ahorro del 13 %: no paga montar nada, ni mantenerlo, ni acordarse de él. La muestra
ahorra el 66 % y sí lo paga.

## La regla de decisión, que es la parte incómoda

Si el riesgo de una tarea exige un nivel cuyo coste se pasa de V máx, la respuesta
correcta **no** es verificar menos. Es no montarlo.

Bajar la verificación por debajo de lo que pide el riesgo para que salgan las cuentas es
la forma más rápida de que un día salga caro, y de que además no te enteres hasta que
llame el cliente. Que una tarea no compense es una conclusión legítima y se apunta en el
inventario: `aparcar`.

## El efecto perverso

Quien revisa todo al máximo acaba revisando mal.

Las últimas treinta comprobaciones de una tanda de cuarenta se hacen a medio gas, y lo
peor es que no se nota: sigues pasando la vista por encima y marcando casillas. **Es más
seguro revisar bien lo importante que revisar todo regular.** Una checklist de tres
líneas que se hace entera vale más que una de doce que se abandona en la cuarta.

Y hay una tercera pérdida, más silenciosa: la automatización que hay que revisar entera
se abandona. A las tres semanas has vuelto a hacerlo a mano y encima has perdido el rato
de montarla. Cuando montes algo, pregúntate si el nivel de verificación que le has
puesto lo vas a poder sostener dentro de un mes.

## Cuándo verificar de más sí está justificado

- **Las tres primeras veces.** Eso es calibración, no régimen. Se paga una vez y se
  recupera; sin ella no puedes bajar de nivel con criterio.
- **Cuando el riesgo es irreversible, legal o hay dinero de por medio.** Ahí manda el
  riesgo y esta cuenta no discute.
- **Cuando cambia la fuente, el criterio o el volumen.** Vuelves al nivel de partida
  hasta que se estabilice.
- **Cuando lo que estás midiendo es si esto funciona.** Verificar un lote entero para
  poder bajar de nivel después es una inversión con fecha de fin, no una costumbre.

## Las tres instancias

- **En tu mesa.** La clasificación de arriba, frente a un correo a un cliente. En la
  primera la cuenta manda; en el segundo, no: el riesgo decide y punto.
- **En otro oficio: la tienda de barrio.** Contar el inventario entero cada semana cuesta
  más que las pérdidas que evita. Se cuentan las diez referencias caras, y una vez al año
  se cuenta todo.
- **En tu casa.** Repasar el extracto del banco movimiento a movimiento cada mes son
  veinte minutos. Mirar el saldo, los cargos de más de 50 € y cuántos movimientos hay son
  dos, y caza casi lo mismo.

## Escribe tú la regla

En la bitácora, con un número dentro:

- «Dejo de verificar una tarea cuando llevo \_\_\_ minutos, porque a mano tardaba \_\_\_.»
- «La tarea que no compensa aunque la verifique bien es \_\_\_.»

## Para la bitácora

- ¿Cuál es tu V máx en la tarea que más veces repites?
- ¿Qué has montado alguna vez y has acabado abandonando? ¿Fue por el rato de revisarlo?
