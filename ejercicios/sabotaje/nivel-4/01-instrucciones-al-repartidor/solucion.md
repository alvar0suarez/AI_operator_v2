# Solución — Nivel 4, las instrucciones al repartidor

## Qué había

**Falta que la Sidrería Llanes cierra los martes.**

En las notas de Iván, esa entrada tiene dos cosas: el cierre de los martes y la descarga
en la acera. En las instrucciones ha sobrevivido la segunda y ha desaparecido la
primera.

El repartidor nuevo va a plantarse allí un martes con el género. Y como el resto de la
lista es correcto y completo, no va a tener ninguna razón para dudar.

## Por qué esto no se ve leyendo

Porque **no hay nada que chirríe**. El documento no tiene un hueco, ni una frase rara,
ni un número que no cuadre. Al contrario: es correcto, está ordenado, tiene los seis
clientes, y el recuento del final refuerza la sensación de que está todo.

Una omisión no deja marca. Un dato inventado añade algo que puedes comprobar; un dato
que falta no añade nada, y lo que no está no llama la atención.

Y hay un detalle deliberado que empeora las cosas: la Sidrería Llanes **sí aparece** en
la lista. Si faltara el cliente entero, lo verías al contar. Lo que falta es media
entrada, y eso es invisible salvo que compares.

## La comprobación que lo caza

Solo hay una, y es la tercera pasada del barrido:

**Coge la fuente y ve tachando.** Cada dato de las notas, búscalo en el resultado. Lo
que no encuentres, es lo que falta.

Se hace al revés de como apetece. Lo natural es leer el resultado y comprobarlo contra
la fuente; para las omisiones hay que leer **la fuente** y comprobarla contra el
resultado. Es la única forma, y por eso casi nadie lo hace.

Aquí, tachando:

| Nota original | ¿Está? |
|---|---|
| Rialto: puerta de servicio, preguntar por Kevin | sí |
| Llanes: **cierra los martes, pasar el miércoles** | **no** |
| Llanes: descargar en acera, sin muelle | sí |
| Molino: peatonal 11–20, entrar antes | sí |
| Casa Julián: timbre roto, llamar al móvil | sí |
| Casa Pepe: garrafa al primer piso | sí |
| El Puerto: agosto cerrado | sí |

Siete datos en seis clientes. Seis sobreviven.

## Y una pregunta más, que vale por el ejercicio entero

**¿Qué tipo de dato es el que se ha perdido?**

No es casualidad que sea ése. De los siete, es el único que es una **excepción
temporal**: una regla que solo se aplica un día concreto. Los demás son permanentes
(«entra por atrás», «el timbre está roto») o estacionales y evidentes («agosto
cerrado», que además va en su propia frase).

Cuando algo se resume, lo que se cae primero es el caso raro. Y el caso raro es
justamente el que hace falta escribir, porque el habitual ya lo aprende cualquiera a la
segunda semana.

> Por eso tu plantilla de verificación lleva una línea que parece de relleno y no lo es:
> **«¿qué debería estar aquí y no está?»**

## Rúbrica

| Nivel | |
|---|---|
| **No llegó** | No encontró la omisión, o dijo «falta información» sin señalar cuál. |
| **Llegó** | Señaló el cierre de los martes y nombró la comprobación: recorrer la fuente tachando, no el resultado. |
| **Llegó y encontró algo que no estaba previsto** | Lo anterior, y además vio que lo que se cae es la **excepción**, no un dato cualquiera, y que la Sidrería sí aparece en la lista —lo que hace que ningún recuento lo detecte—. |

## El error típico

Fiarse del recuento. «Seis clientes en cuatro poblaciones» es cierto, cuadra, y no
demuestra absolutamente nada sobre si cada entrada está completa.

Un recuento correcto tranquiliza, y ése es el problema: te da una sensación de haber
comprobado que no se corresponde con lo que has comprobado. Contar filas detecta filas
que faltan. No detecta nada de lo que pasa dentro de una fila.
