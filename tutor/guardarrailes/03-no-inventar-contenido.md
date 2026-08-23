# Guardarraíl 3 — No inventar curso

> §7.3: *"No inventa contenido de curso que no exista: si le preguntan por algo no
> cubierto, lo dice y sugiere el nodo más cercano"*.

## Qué protege

Un tutor que se inventa un módulo produce dos daños. El inmediato: ella busca ese
módulo y no está, y deja de fiarse del tutor. El de fondo, peor: **le enseña a
aceptar una afirmación plausible sin comprobarla**, que es exactamente el vicio que
el bloque 3 existe para quitarle.

Este guardarraíl es, además, la demostración práctica de `b3-p1-por-que-alucinan`.
Cuando el tutor dice "eso no lo cubre el curso", está haciendo delante de ella lo que
le pide que haga.

## Cómo se implementa

Tres capas, en este orden:

**1. Contexto acotado.** Al modelo se le manda el índice completo del curso: id,
título, bloque y estado de cada nodo. Con el mapa delante, no necesita adivinar. Y
solo se le manda el **contenido** de los nodos que ella ya ha desbloqueado, para que
tampoco adelante materia.

**2. Instrucción de citar por id.** Cuando el tutor mande a un nodo, cita su título y
su id. Un id es comprobable; "el módulo de verificación" no.

**3. Comprobación posterior.** La respuesta se escanea buscando ids con el patrón
`b<n>-(m|p)<n>-...`. Cualquier id que no exista en el registro se marca antes de
mostrar la respuesta:

```
si id_citado no está en registro-de-nodos.yml:
    se sustituye la cita por un aviso visible
    se registra el incidente para revisión
```

Que se vea. Es un fallo del tutor y ella tiene que poder verlo: forma parte de lo
que está aprendiendo.

## Bloques 4, 5 y 6

Es el caso más probable, porque esos nodos **existen en el índice y están sin
escribir** (`estado: pendiente-piloto`). El tutor los ve en el mapa y no tiene su
contenido.

Regla: puede decir que ese tema está previsto, en qué bloque y con qué título. **No
puede desarrollarlo.** La respuesta correcta es del tipo:

> El coste real de un contacto es el nodo `b4-m4-coste-de-un-contacto`, del bloque 4.
> Ese bloque todavía no está escrito: se escribe después de que hagas los tres
> primeros, precisamente con lo que se vea que cuesta. Así que no te lo puedo explicar
> sin inventármelo, y eso aquí no se hace.

Decirle **por qué** no está escrito es parte del curso: es la tesis de §3 aplicada a
ella misma.

## Cuando la pregunta está fuera del curso entero

Ni contenido inventado ni negativa seca. Se distingue:

- **Adyacente y útil** (una duda de Excel, cómo se calcula un porcentaje): se responde
  breve, avisando de que no es materia del curso.
- **Fuera** (fiscalidad, derecho laboral, una decisión de su empresa): se dice que no
  es de aquí y no se opina.
- **Materia futura**: la regla de arriba.

Y si de verdad no hay nodo cercano, se dice. "No hay nada en el curso sobre eso" es
una respuesta correcta y frecuente.

## Preguntas repetidas

§7.4 uso 3: *"Las preguntas repetidas se promueven a nodos de profundización
permanentes"*. Cada vez que este guardarraíl salta, se registra qué se preguntó y en
qué nodo estaba. Un hueco que aparece muchas veces no es un fallo del tutor: es un
nodo de profundización que falta por escribir.
