---
id: b3-m8-plantilla-de-verificacion
bloque: 3
titulo: "Tu plantilla de verificación"
tipo: artefacto
duracion_min: 45
requisitos: [b3-m7-datos-y-rgpd]
desbloquea: [b3-m9-contexto-trabajo]
caduca: bajo
objetivos:
  - "Escribir tres checklists de verificación, una por familia de tareas, con su nivel de riesgo justificado"
  - "Anotar en cada comprobación contra qué fuente se hace y cuánto tarda"
  - "Incluir en las tres la comprobación de lo que falta"
conceptos: [verificacion, riesgo, rubrica, checklist]
artefacto: plantillas/plantilla-de-verificacion.md
---

Artefacto 3 de 6, y el primero que se usa en caliente: no se lee, se tiene abierto al
lado mientras trabajas. La plantilla está en `plantillas/plantilla-de-verificacion.md`.
**Ábrela ahora y léela entera**; aquí no se repite, aquí se explica cómo se rellena y
qué se hace mal.

## Qué contesta este fichero

Dos preguntas, en el momento en que tienes un resultado delante y prisa:

1. **¿Cuánto miro esto?** Que ya lo decidiste en `b3-m6-verificacion-proporcional`,
   «Verificación proporcional al riesgo», y aquí queda escrito para no volver a
   decidirlo cada vez ni decidirlo distinto según el día.
2. **¿Qué miro exactamente, y contra qué?** Tres comprobaciones concretas valen más que
   doce genéricas, porque las tres se hacen y las doce se saltan.

## Cómo se rellena

1. **Cópiala** a tu carpeta como `plantilla-de-verificacion.md`. No la edites en su
   sitio.
2. **Tres familias de tareas.** No una, y no diez. Salen de las seis filas que
   clasificaste en `b3-m6`. Y son familias, no casos: «responder consultas de estado de
   pedido» es una familia; «la consulta de ayer del bar» no lo es.
3. **El nivel de riesgo, con la razón y el eje que manda.** No basta «muestra»: escribe
   «muestra, porque es reversible pero alguien decide con esto sin revisarlo». Dentro de
   dos meses la razón es lo único que te dejará bajar o subir de nivel con criterio.
4. **Tres o cuatro comprobaciones**, cada una con las tres columnas: qué compruebo,
   contra qué fuente, cuánto tardo.
5. **La última fila es fija:** ¿qué debería estar aquí y no está?
6. **Y la línea que la convierte en procedimiento:** si falla algo, ¿qué hago? Rehacer,
   corregir a mano, subir de nivel el lote entero, avisar a alguien. Sin eso tienes una
   lista de dudas, no una checklist.

Cuatro cosas que se hacen mal casi siempre:

- **«Revisar que esté bien» no es una comprobación.** Escribe el verbo y el objeto:
  «comparo el total de la tabla con la suma de las líneas», «busco cada fecha del texto
  en el correo original».
- **Sin columna de fuente no hay verificación.** Si no puedes decir contra qué lo
  compruebas, eso es una opinión sobre un texto que se lee bien. Y un texto malo se lee
  bien: por eso existe este fichero.
- **Los tiempos se miden, no se estiman.** Cronometra la primera vez. Si la suma de tus
  comprobaciones se acerca a lo que tardas en hacer la tarea a mano, la checklist te está
  diciendo algo, y lo dice entero `b3-p5-coste-de-verificar-de-mas`, «Verificar de más
  también es un error».
- **Si las tres fichas te salen iguales, no has calibrado por riesgo.** Vuelve al paso 3.

> [!NOTE]
> Si la familia de tareas toca textos de clientes, la primera línea de su ficha es la de
> `b3-m7-datos-y-rgpd`, «Datos y RGPD: qué no se pega jamás», y va **antes** de producir
> nada: qué he quitado antes de pegar. Es la única comprobación de este fichero que no
> sirve de nada hecha al final.

## La comprobación que casi nadie escribe

**¿Qué debería estar aquí y no está?**

Las otras tres se ven leyendo. Ésta no: una omisión no deja hueco, deja un texto
perfectamente redondo al que le falta el caso que te iba a costar dinero. El correo que
no menciona la excepción. La tabla a la que le falta el mes que no tenía datos. El
resumen que se come al cliente que siempre da problemas.

Y como no se ve leyendo, se resuelve al revés: **escribe qué esperas encontrar antes de
mirar el resultado.** Dos líneas bastan. Cuántas filas tiene que haber —si has mandado
40 correos, la tabla trae 40 filas o una explicación de por qué no—, qué casos raros
tienen que aparecer, y qué categoría no puede faltar. Comparar contra esa lista de dos
líneas es lo único que caza ausencias.

## Las tres instancias

La misma ficha, con el mismo esqueleto, en tres sitios:

| Dónde | Familia | Nivel y comprobación que la define |
|---|---|---|
| **Tu sector (CX)** | Borrador de respuesta a un cliente por una incidencia | Línea a línea de fechas, importes y compromisos, contra el ticket y el pedido. Lo demás, vistazo |
| **Otro trabajo** | En un taller, presupuestos de reparación | Muestra: precios contra la tarifa vigente y horas contra el baremo. Y la fija: ¿falta alguna pieza que sí hay que cambiar? |
| **Tu casa** | El borrador de la declaración de la renta | Línea a línea de lo que cambió este año y de los datos bancarios; vistazo del resto. Nadie repasa entero un borrador de 40 páginas, y no hace falta |

La de casa enseña lo de siempre: ya verificas por niveles sin llamarlo así. Lo que
cambia en el trabajo es el volumen, y con volumen las reglas hay que escribirlas.

## Rúbrica

La de la plantilla, en corto, para que puedas aplicártela hoy:

| Nivel | Cómo se reconoce |
|---|---|
| **No llegó** | Una sola checklist para todo. Comprobaciones vagas del tipo «revisar que esté bien». Sin columna de fuente. Sin la comprobación de lo que falta |
| **Llegó** | Tres familias con su nivel de riesgo **justificado**, comprobaciones concretas con su fuente y su tiempo, la pregunta de la omisión en las tres, y cabe en una pantalla |
| **Llegó y además** | Lo anterior, y encima has identificado una tarea que **estabas verificando de más** y le has bajado el nivel con una razón escrita |

Autocorrección honesta: coge un resultado que produjeras la semana pasada y pásale la
ficha que le toque. Si tardas más de dos minutos en saber qué fila aplicar, o si al
terminar no sabrías decir si eso vale o no vale, la ficha está escrita para leerla, no
para usarla.

## Mantenimiento

Este fichero crece por fallos, igual que el del nodo siguiente:

- **Cada vez que se te cuele algo**, añade la fila que lo habría cazado. Una sola, y
  concreta. Así la checklist converge en vez de inflarse.
- **Cada vez que tres lotes seguidos salgan limpios**, plantéate bajar el nivel de esa
  familia y anota la fecha. Bajar de nivel también es una decisión que se justifica.
- **Si cambia la fuente, el criterio o el volumen**, vuelve al nivel de partida.

Y fecha arriba. Una checklist sin fecha no se sabe si está calibrada o es de cuando
empezaste.

## Para la bitácora

- ¿Cuántos minutos suman las comprobaciones de tu familia más cara, y qué porcentaje son
  del tiempo que tardabas en hacerla a mano?
- ¿Qué comprobación has escrito que no se te habría ocurrido hace dos semanas?
- ¿En cuál de las tres fichas te ha costado más rellenar la fila de lo que falta? Ésa es
  la tarea donde una omisión pasaría desapercibida hoy mismo.
