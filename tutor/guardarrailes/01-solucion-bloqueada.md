# Guardarraíl 1 — La solución no llega antes del intento

> §7.3: *"Rechaza dar la solución de un sabotaje antes de que ella lo haya intentado
> (el estado 'intentado' lo marca la propia interfaz)"*.

## Qué protege

El curso entero se apoya en un mecanismo: **el texto malo parece bien**, y por eso
una principiante no puede autoevaluarse sin intentarlo primero. Si la solución está
a un mensaje de distancia, el ejercicio de sabotaje se convierte en una lectura. Y
leer la solución de un sabotaje enseña aproximadamente nada.

## Cómo se implementa

**No es una instrucción al modelo. Es una regla de ensamblado de contexto.**

```
si nodo_actual.solucion existe:
    si estado_alumna.intentado[nodo_id] != true:
        NO se incluye el fichero de solución en el contexto
        se añade al prompt de sistema la nota de estado
    si no:
        se incluye
```

Mientras `intentado` sea falso, el modelo **no tiene** la solución. No puede darla
aunque ella insista, aunque lo pida de forma ingeniosa, aunque le diga que ya la ha
visto. No hay nada que filtrar porque no hay nada que decir.

El estado `intentado` lo marca la interfaz cuando ella pulsa "ya lo he intentado" o
envía su respuesta al ejercicio. Es un botón, no una promesa: puede mentir y pulsarlo
sin hacerlo. Se acepta. El guardarraíl impide el resbalón, no el fraude deliberado
contra una misma.

## Qué se le dice cuando pide la solución sin haberlo intentado

Ni negativa seca ni sermón. Una vez, la razón; después, tracción:

> Todavía no. Esto solo funciona si lo intentas antes: el problema de estos ejercicios
> es que el texto malo parece bien, y eso solo se aprende cazándolo, no leyéndolo.
> Márcalo como intentado aunque no hayas encontrado nada y te digo qué había.
>
> Si quieres, te doy la primera pasada del método: coge cada número del texto y
> búscalo en la fuente. ¿Cuadran todos?

## Alcance

Cubre todo nodo con campo `solucion` en su frontmatter, no solo los sabotajes:
también las claves de corrección del dataset (§5.3), que se destapan **después** del
intento y nunca antes.

El caso del ejercicio central del bloque 4 es el más sensible: `dataset/SOLUCIONES/`
no entra jamás en el contexto del tutor, con `intentado` o sin él. Ahí el guardarraíl
no es condicional, es absoluto — las verdades escondidas son el examen del curso.
