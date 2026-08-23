---
id: b3-m5-modos-de-fallo
bloque: 3
titulo: "Los cinco modos de fallo típicos"
tipo: concepto
duracion_min: 45
requisitos: [b3-m3-ficheros-de-contexto, b3-m4-sabotaje]
desbloquea: [b3-m6-verificacion-proporcional]
caduca: medio
objetivos:
  - "Poner nombre a cada fallo que cazaste en los sabotajes"
  - "Aplicar la señal de detección barata que corresponde a cada modo"
  - "Convertir un modo de fallo repetido en una línea nueva de tu fichero de contexto"
conceptos: [alucinacion, tono, generalizacion-falsa, omision, seguridad-excesiva]
---

Este nodo va después de los sabotajes a propósito. Una taxonomía leída antes de fallar es
una lista de palabras; leída después, es el nombre de cosas que ya has notado y no sabías
llamar. Cinco modos, cada uno con una señal que se comprueba en segundos y con la línea
que lo habría evitado.

## Por qué hace falta ponerles nombre

Lo que se transfiere al martes siguiente no es el fallo: es el tipo. Un dato inventado en
un resumen de tickets y otro en un borrador de correo son el mismo animal y se cazan con el
mismo gesto. Guardados como «lo del jueves» y «lo del correo del bar», son dos anécdotas.
Guardados como un modo, son un reflejo.

Y una segunda razón, más útil: cada modo tiene su señal barata. No se busca «un fallo» en
un texto; se buscan cinco cosas concretas, cada una en un sitio distinto.

## Los cinco

### 1. Dato inventado

Una cifra, un plazo o una condición que no está en ningún sitio y suena razonable. «El
plazo para reclamar una entrega es de 48 horas»: tamaño correcto, estilo del sector, y no
aparece en ninguno de los nueve procedimientos de la casa.

**Señal barata:** subraya cada cifra, cada fecha y cada condición, y escribe al lado de
dónde sale. Lo que no puedas señalar en el material, fuera. Empieza por el dato que más
cómodo te viene: es el que menos ganas tienes de comprobar y el que más veces está mal.

**Qué lo previene:** una restricción en el encargo —«no des ningún dato que no esté en el
material; donde no lo haya, escribe "no consta"»— y la comprobación de procedencia en tu
criterio de aceptación.

### 2. Tono inadecuado

Ningún error de contenido: un «estimado cliente» dirigido a un bar de ocho años, o tres
disculpas donde tocaba una. El daño es real y no genera reclamación. Nadie protesta por el
tono: se va sin decir nada.

**Señal barata:** léelo desde el sitio de quien lo recibe, no desde el tuyo. Y dos
recuentos de tres segundos: ¿cuántas veces se pide perdón? Más de una vez, sobra.
¿Empieza por su nombre o por una fórmula?

**Qué lo previene:** la pareja de ejemplos de tono de tu fichero de contexto, con la
diferencia escrita en una frase. Un adjetivo no previene nada.

### 3. Generalización falsa

Una conclusión razonable apoyada en menos casos de los que necesitaría. De doce correos
sale «los clientes prefieren el WhatsApp», y los doce venían de la misma carpeta porque los
elegiste tú de ahí. No es mentira: es que no se sostiene con eso.

**Señal barata:** por cada frase que empiece por «los clientes», «la mayoría» o «siempre»,
exige dos números: **cuántos casos** y **de cuántos distintos**. Doce correos de dos
clientes no son doce casos, son dos.

**Qué lo previene:** pedir en el formato que cada afirmación lleve detrás su recuento.
Cuando el número tiene que ir escrito al lado, las generalizaciones se caen solas.

### 4. Omisión silenciosa

Lo que falta. Un resumen de los nueve procedimientos del manual que recoge ocho. Un correo
del cliente que traía dos peticiones y una respuesta que contesta una.

> [!WARNING]
> Éste es el único de los cinco que **no se ve leyendo el output**. Los otros cuatro
> aparecen en el texto: hay una cifra rara, hay una frase con un tono que chirría, hay un
> «siempre». La omisión no aparece porque un texto al que le falta algo no deja hueco: se
> lee perfectamente bien y termina. Solo se detecta comparándolo con la fuente. Si te
> saltas la tercera pasada, este modo pasa siempre.

**Señal barata:** dos, y las dos van **antes** de leer. Una: escribe la lista de lo que
debería aparecer y tacha según leas. Dos: cuenta. ¿Cuántos había en la fuente y cuántos
salen? Nueve y ocho es una diferencia que solo existe si alguien cuenta.

**Qué lo previene:** un formato que obligue a listar todo, incluido lo que no aplica, y la
comprobación que casi nadie escribe: «¿qué debería estar y no está?».

### 5. Seguridad excesiva

El «por supuesto» sin nada detrás. «Por supuesto, lo habitual en el sector es abonar el
importe íntegro.» No hay ningún «habitual en el sector» y nadie ha dicho eso. Es un modo
de fallo propio porque el tono rotundo desactiva tu revisión justo cuando más falta hace.

**Señal barata:** busca «por supuesto», «sin duda», «siempre», «lo normal es», «como bien
sabes». Por cada una, pide la fuente de esa frase concreta. Si no la hay, no se suaviza la
frase: se cae entera.

**Qué lo previene:** decirlo en el encargo: «si algo no está en el material, dilo;
prefiero un "no consta" a una respuesta segura». Y no preguntar con prisa: cuanto más
rotunda va la pregunta, más rotunda vuelve la respuesta, y eso no la hace más cierta.

## En una tabla, para tenerla delante

| Modo | Dónde se mira | En cuánto se comprueba |
|---|---|---|
| Dato inventado | Cifras, fechas y condiciones, una a una | 1 min |
| Tono inadecuado | Primera línea, última, y el recuento de disculpas | 20 s |
| Generalización falsa | Frases con «los clientes», «la mayoría», «siempre» | 30 s |
| **Omisión silenciosa** | **La fuente, no el output** | 2 min |
| Seguridad excesiva | Los adverbios de rotundidad | 20 s |

## El que no está en esta lista

Hay un sexto, que en los sabotajes es el nivel 5: **conclusión correcta con razonamiento
roto**. El resultado es bueno, así que nadie mira cómo se llegó; la próxima vez, con otros
datos, el mismo camino da un resultado malo.

No está entre los cinco porque no tiene señal barata: la única forma de cazarlo es rehacer
el camino, y eso cuesta casi lo que hacer la tarea. Por eso no se hace siempre, se hace
cuando lo que hay en juego lo justifica. Ése es el nodo siguiente.

## Cuándo esto falla

- **Buscar los cinco en todo lo que produces.** Cinco barridos en un borrador interno que
  lee una persona son cinco minutos tirados, y una automatización que ha dejado de ahorrar.
  El reparto se decide en `b3-m6-verificacion-proporcional`, «Verificación proporcional al
  riesgo».
- **Las señales baratas dan falsos positivos.** Un «siempre» puede ser cierto y una fórmula
  de cortesía puede ser lo que toca con ese destinatario. La señal dice dónde mirar, no qué
  veredicto dar.
- **Tratar un modo repetido como mala suerte.** Si el mismo modo sale tres veces, el
  problema no está en el output: está en tu encargo o en tu contexto. Arreglar el texto es
  el síntoma; añadir la línea que faltaba es la causa.
- **Confundir modo con culpa.** Que el fallo tenga nombre no significa que el instrumento
  esté roto ni que tú lo hayas hecho mal. Sigue siendo `b0-m3-fallar-es-diagnostico`,
  «Fallar es diagnóstico, no fracaso»: información sobre lo que no dijiste.

## Las tres instancias

Los cinco modos no son de las máquinas. Son de cualquier texto que te llega hecho.

| Dónde | El modo que más aparece | Cómo suena |
|---|---|---|
| **Tu sector (CX)** | Omisión silenciosa | El resumen de la semana que le pasas a gerencia y que se deja fuera el caso que iba a explotar |
| **Otro trabajo** | Generalización falsa | En una tienda, «los clientes ya no compran esto», dicho por la persona que atiende los sábados |
| **Tu casa** | Seguridad excesiva | «Eso lo cubre el seguro, por supuesto», por teléfono, sin que nadie mire la póliza |

La tercera es la que más dinero cuesta en la vida real y la que menos se revisa, porque
viene dicha con mucho aplomo y por alguien que parece saber.

## Ejercicio

Veinte minutos, sobre lo que ya tienes.

Abre tu `sabotajes-<fecha>.md` de `b3-m4-sabotaje`, «Ejercicios de sabotaje». Etiqueta con
uno de los cinco nombres **cada fallo que cazaste y cada fallo que se te escapó**, y cuenta
por modo.

Después monta `modos-de-fallo.md`: cinco filas y, en cada una, tres cosas escritas por ti.
La señal barata con tus palabras —no copiada de aquí—, un caso tuyo donde ya te ha pasado o
donde podría pasarte, y, si el modo se te ha escapado más de una vez, **la línea que le
falta a tu `contexto-borrador.md`** para que no vuelva; añádela hoy, con la fecha, en la
tabla de mantenimiento.

Ese fichero es material del artefacto de `b3-m8-plantilla-de-verificacion`, «Tu plantilla
de verificación». No lo hagas bonito: hazlo tuyo.

**Regla de parada:** cinco filas y ni una más. Si te salen ocho modos, has partido uno en
tres trozos; júntalos. Una taxonomía con ocho casillas no se aplica con el texto delante y
la prisa encima.

## Escribe tú la regla

En la bitácora, con tus palabras:

- «El modo que más se me escapa es \_\_\_, y ahora lo busco mirando \_\_\_.»
- «Cuando el mismo modo me sale tres veces, lo que hago es \_\_\_.»

## Para la bitácora

- ¿Qué modo se te escapó más veces en los sabotajes? ¿Y cuál marcaste de más?
- ¿Cuántas líneas nuevas le has tenido que añadir a tu contexto?
- ¿Reconoces alguno de los cinco en algo que te llegó escrito por una persona esta semana?
