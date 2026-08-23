---
id: b3-m6-verificacion-proporcional
bloque: 3
titulo: "Verificación proporcional al riesgo"
tipo: concepto
duracion_min: 45
requisitos: [b3-m4-sabotaje, b3-m5-modos-de-fallo]
desbloquea: [b3-m7-datos-y-rgpd]
caduca: bajo
objetivos:
  - "Clasificar una tarea con los tres ejes de riesgo"
  - "Asignar a cada tarea uno de los tres niveles de verificación"
  - "Calcular si el rato de verificar se come el ahorro de la tarea"
  - "Marcar una tarea propia que se está verificando de más y bajarla de nivel"
conceptos: [riesgo, verificacion, reversibilidad, alcance, coste-de-verificar]
profundizar:
  - id: b3-p5-coste-de-verificar-de-mas
    titulo: "Verificar de más también es un error"
---

Ya sabes qué falla y cómo se ve. Falta decidir **cuánto** miras cada cosa, que es lo que
decide si esto te sirve de verdad. Sales de aquí con seis tareas tuyas clasificadas por
riesgo y con un nivel de verificación asignado a cada una.

## Tener un solo nivel es el error

Revisar todo línea a línea suena responsable. Lo que produce es que veinte minutos de
ahorro se conviertan en cero y que abandones el montaje a las tres semanas: «total, si
lo tengo que repasar entero». Revisarlo todo por encima funciona treinta veces, y a la
treinta y una sale un importe inventado en un correo a un cliente. Mismo fallo: un solo
nivel para todo.

La habilidad no es verificar mucho. Es saber cuánto verificar cada cosa y poder decir
por qué.

## Los tres ejes

Tres preguntas sobre la tarea concreta, contestadas **antes** de producir nada.

**1. ¿Se puede deshacer?** Un borrador se borra. Un correo enviado no se desenvía. Un
abono metido en el sistema exige que alguien lo corrija, y para entonces el cliente ya
lo ha visto.

**2. ¿A cuánta gente llega?** A ti, a un compañero, a un cliente, a los 300. El mismo
fallo pequeño por 300 llega el mismo día y entra por teléfono.

**3. ¿Qué pasa si falla 1 de cada 20?** La tercera pregunta del filtro del bloque 1,
ahora desde el otro lado. Uno de cada veinte no es raro: en 60 tareas al mes son tres al
mes.

Cuatro respuestas, de menos a más: lo arreglo yo; hay que llamar a alguien; perdemos un
cliente o cuesta dinero; hay datos personales o un plazo legal por medio.

**Los tres ejes no se promedian.** Manda el más alto. Algo irreversible que llega a una
sola persona sigue siendo irreversible.

## Los tres niveles

| Nivel | Qué haces exactamente | Cuánto cuesta |
|---|---|---|
| **Vistazo** | Lees por encima buscando lo que canta: una cifra imposible, un tono que no es el tuyo, un hueco | 30 segundos |
| **Muestra** | **5 al azar más los 2 extremos**, contra la fuente. Si falla uno, el lote entero sube a línea a línea | 3–5 min por lote de 20 |
| **Línea a línea** | Todo contra la fuente, con las tres pasadas: números, afirmaciones y lo que falta | Lo que haga falta |

Los dos extremos no son un capricho: los fallos se concentran en los bordes —la primera
fila, la última, el importe más grande, el caso más raro—. Y «al azar» es al azar: las
cinco primeras filas no son una muestra, son el principio.

## Tabla de decisión

Casos de tu mesa: la misma persona y el mismo martes, en tres niveles distintos.

| Tarea | ¿Deshacer? | ¿A cuántos? | Si falla 1 de 20 | Nivel |
|---|---|---|---|---|
| Resumen para ti de los correos de la semana | Sí | A ti | Nada | **Vistazo** |
| Clasificar 200 tickets para un análisis interno | Sí | A quien lea el análisis | Decides con el reparto torcido | **Muestra** |
| Pasar 40 correos a una tabla | Sí | Al informe que sale de ahí | Un dato mal en una fila | **Muestra**, línea a línea en los importes |
| Borrador de respuesta a un cliente | Antes de enviar sí; después no | Un cliente | Una promesa que no puedes cumplir | **Línea a línea** en fechas, importes y compromisos |
| Aviso a los 300 clientes de un cambio de reparto | No | 300 | 300 llamadas el mismo día | **Línea a línea** y que lo lea otra persona |
| Nota con una propuesta para gerencia | Sí | Quien decide con ella | Pierdes credibilidad | **Muestra** del texto, **línea a línea** de las cifras |

Falta una fila a propósito: reconocer por escrito un error de facturación. Ésa no es
cuestión de nivel de verificación, es de las de `b2-m9-que-no-es-ninguno`.

## Verificar de más es un error, no una virtud

Con números. Pasar 40 correos al mes a una tabla, a mano: 3 min por correo, **120
min/mes**.

| Cómo lo verificas | Cuentas | Total | Ahorro |
|---|---|---|---|
| Línea a línea | 10 min de encargo + 40 × 2 min campo a campo | 90 min | 25 % |
| Muestra (5 + 2 extremos por lote de 20) | 10 min de encargo + 14 × 2 min | 38 min | 68 % |

Verificar línea a línea una extracción cuesta casi lo mismo que hacerla: para comprobar
el dato hay que abrir el correo y buscarlo, que era el trabajo. Un 25 % no paga montar y
mantener nada.

> [!WARNING]
> Hay un segundo coste que no sale en la tabla: **la atención no se sostiene.** Quien
> revisa cuarenta cosas seguidas revisa mal las últimas treinta y no se entera. Es más
> seguro comprobar tres cosas bien elegidas al cien por cien que treinta a medias. La
> aritmética está en `b3-p5-coste-de-verificar-de-mas`.

Si una tarea exige línea a línea y el ahorro se queda en el 25 %, la pregunta ya no es
cómo verificarla: es si merece un montaje, o si lo que toca mirar es por qué existe.

## Cuándo se sube y cuándo se baja

- **Se sube en el acto.** Si la muestra falla una vez, el lote entero pasa a línea a
  línea. Sin «habrá sido mala suerte».
- **Se baja solo con pruebas: tres lotes seguidos sin un fallo.** Con dos, no.
- **Hay un suelo que no se baja nunca:** lo irreversible, lo que lleva dinero, lo que
  lleva datos personales y lo que tiene un plazo legal detrás.
- **La calibración caduca.** Si cambia la fuente o el criterio, vuelves al nivel de
  partida: lo que validaste era la combinación entera, no el instrumento.

## Las tres instancias

- **En tu mesa.** Clasificar 200 tickets para un análisis tuyo y avisar a 300 clientes
  de un cambio de horario: el mismo día, el mismo instrumento. Uno es muestra; el otro no
  baja de línea a línea con segunda lectura. Si los tratas igual, uno está mal tratado.
- **En otro oficio: la gestoría.** El modelo trimestral, con fecha de presentación y
  sanción detrás, se repasa entero siempre. La carta de documentación pendiente a 30
  clientes va con plantilla y vistazo: la segunda paga el rato de la primera.
- **En tu casa.** La lista de la compra la miras por encima; el número de cuenta de una
  transferencia lo lees dos veces, dígito a dígito, y eso no te lo enseñó nadie. Ya
  tienes el reflejo: en el trabajo hay que escribirlo porque allí las tareas llegan de
  veinte en veinte.

## Cuándo esto falla

- **Confundir «es fácil» con «es de riesgo bajo».** Decide qué pasa si sale mal, no lo
  sencilla que sea la tarea. Pegar un importe en un correo es facilísimo.
- **Verificar contra el resultado y no contra la fuente.** Releer tres veces un texto no
  es verificarlo: sin abrir el origen solo compruebas que se lee bien, que es justo lo
  que hace peligroso un texto malo.
- **Muestra que no es muestra.** Siempre las cinco primeras filas, siempre los casos
  fáciles.
- **Creer que subir de nivel lo cubre todo.** El nivel dice cuánto miras, no qué miras.
  Lo que falta no aparece mirando más rato: aparece comparando con la fuente.

## Ejercicio

Veinte minutos, con tu `inventario-de-procesos.md` delante.

1. Coge **seis tareas**: tres que ya hayas probado y tres que pienses probar.
2. Contesta los tres ejes con una línea cada uno. Sin «depende».
3. Asigna nivel: manda el eje más alto.
4. Para las tres de nivel más alto, haz la cuenta: minutos a mano frente a producir más
   verificar a ese nivel. Escribe el ahorro en porcentaje, aunque salga feo.
5. Marca **la que estás verificando de más hoy**. Hay al menos una.

**Entregable:** seis filas con los tres ejes, el nivel y el ahorro. Es la materia prima
de `b3-m8-plantilla-de-verificacion`, «Tu plantilla de verificación».

**Regla de parada:** hoy no escribas checklists. Clasificar y montarlas son dos trabajos
distintos, y hacerlos a la vez produce listas de doce líneas que no se usan.

## Escribe tú la regla

En la bitácora, con tus palabras:

- «Bajo el nivel de verificación de una tarea cuando \_\_\_.»
- «Y no lo bajo nunca en \_\_\_, aunque salga bien \_\_\_ veces.»

La segunda te protege el día que tengas prisa.

## Para la bitácora

- ¿Cuál estabas verificando de más? ¿Cuántos minutos al mes te devuelve bajarla de
  nivel?
- ¿Y cuál estabas verificando de menos? Ésa es la incómoda y es la que hay que anotar.
- ¿En alguna el ahorro baja del 30 % aunque verifiques bien? Escribe si aun así merece
  la pena, y por qué.
