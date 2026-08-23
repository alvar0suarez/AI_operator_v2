---
id: b3-m4-sabotaje
bloque: 3
titulo: "Ejercicios de sabotaje"
tipo: ejercicio
duracion_min: 45
requisitos: [b3-m3-ficheros-de-contexto, b2-m2-clasificar]
desbloquea: [b3-m5-modos-de-fallo, b3-m6-verificacion-proporcional]
caduca: bajo
objetivos:
  - "Aplicar el barrido de tres pasadas a un output que no has producido"
  - "Marcar cada fallo con su sitio y su tipo, no solo señalar que hay uno"
  - "Contar tus falsos positivos y usarlos como medida, igual que los fallos que se te escapan"
conceptos: [verificacion, alucinacion, riesgo, omision, tono]
profundizar:
  - id: b3-p1-por-que-alucinan
    titulo: "Por qué los modelos inventan datos"
  - id: b3-p2-verificacion-numerica
    titulo: "Técnicas de verificación numérica rápida"
---

Éste es el nodo central del curso. Todo lo anterior sirve para producir; a partir de aquí
se trata de saber si lo producido vale, que es la parte escasa y la que no caduca. El
material está en `ejercicios/sabotaje/`: outputs con errores metidos dentro a propósito.
Aquí va por qué existen y con qué método se cazan.

## El texto malo parece bien

Cuando una fórmula de Excel se rompe, la celda te lo dice: sale `#¡VALOR!` y no hay manera
de no verlo. Cuando un texto está mal, no sale nada. Se lee igual de bien un informe con un
dato inventado que uno correcto: mismo ritmo, misma ortografía, misma seguridad. La única
señal es la que produce tu cabeza, y tu cabeza asocia «bien escrito» con «cierto». Son
cosas independientes.

Y hay una asimetría que lo empeora. Cuando escribes tú, sabes dónde dudaste: la frase que
te costó, el importe que fuiste a comprobar, el párrafo que reescribiste tres veces. Ese
mapa de dudas es la mitad de tu verificación y lo tienes gratis. Cuando el texto lo produce
otro, el mapa no existe: todas las frases llegan con el mismo aplomo, la que salió de un
dato que le diste y la que salió de la nada.

## Por qué no basta con leerlo con atención

Porque para reconocer un fallo hay que haberlo visto antes. Quien lleva quince años
revisando facturas detecta un descuadre de reojo; no es más lista, tiene el repertorio. Tú
lo tienes en lo tuyo. Para el output de una máquina, todavía no.

Se construye de dos formas. Una es esperar a que te lo enseñe la realidad: mandar un correo
con un plazo inventado y aprenderlo con la reclamación puesta. La otra es cazar fallos que
alguien plantó a propósito, con la solución guardada y sin coste. No hay una tercera. **No
se aprende a verificar leyendo sobre verificación.**

## Los seis niveles

Son los seis tipos de sabotaje, de menos a más difícil. En `ejercicios/sabotaje/README.md`
tienes qué se planta en cada uno y cómo está organizada la carpeta. Aquí está lo otro: qué
pasada lo caza y qué cuesta cuando se te escapa.

| Nivel | Qué pasada lo caza | Qué cuesta si se te escapa |
|---|---|---|
| 1 · Número que no cuadra | La primera, en segundos | Un importe mal en un correo: una reclamación y una llamada de gerencia |
| 2 · Tono inadecuado | Ninguna de las tres; hay que releer desde el sitio de quien lo recibe | Un cliente de ocho años tratado como un desconocido. No reclama: se va |
| 3 · Dato inventado plausible | La segunda, preguntando de dónde sale | Prometes una condición que no existe. Toca cumplirla o retirarla, y las dos duelen |
| 4 · Omisión silenciosa | Solo la tercera | Contestas a una de las dos cosas que pedía. Vuelve a escribir, y ya enfadado |
| 5 · Conclusión correcta, razonamiento roto | Ninguna barata: hay que rehacer el camino | Esta vez acertó. La próxima, con otros datos, no, y ya te fiabas |
| 6 · Nada, el output es impecable | — | Rehaces lo que estaba bien y dejas de fiarte de lo que produces |

Fíjate en las dos filas sin pasada barata. El tono y el razonamiento no se cazan con
método rápido: se cazan sabiendo de qué va tu trabajo. Ahí llevas ventaja, y conviene que
lo sepas.

## El barrido en tres pasadas

Siempre en este orden, que va de lo barato a lo caro. Si la primera ya lo tumba, no gastas
la tercera.

**1ª pasada — los números.** Un minuto. Cada cifra contra la fuente: ¿suman las partes el
total?, ¿el porcentaje va sobre la base que crees?, ¿cuadra el número de filas? No hace
falta comprobarlas todas: tres bien elegidas detectan casi todo. Cuáles elegir está en
`b3-p2-verificacion-numerica`, «Técnicas de verificación numérica rápida».

**2ª pasada — las afirmaciones.** Subraya cada frase que afirme algo sobre la realidad —un
plazo, una política, una condición, un «siempre»— y escribe al lado de dónde sale. Si no
puedes señalarlo en el material que le diste, no existe. **Y sospecha especialmente de lo
que te viene cómodo:** el dato que te resuelve el problema es el que menos ganas tienes de
comprobar. El porqué está en `b3-p1-por-que-alucinan`, «Por qué los modelos inventan
datos».

**3ª pasada — lo que falta.** La difícil, porque no se hace leyendo. Un texto al que le
falta algo se lee perfectamente bien: no deja hueco. Solo aparece comparando. El método es
al revés de lo que apetece: **antes de leer el output, escribe la lista de lo que debería
aparecer** —los casos, los clientes, los apartados, las cantidades— y después tacha. Lo
que quede sin tachar es la omisión. Si haces la lista después de leer, no es una lista: es
un resumen de lo que ya has leído.

Y la disciplina que hace que esto sirva para algo: **no basta con marcar que hay un fallo.
Se marca dónde está y de qué tipo es.** El sitio te sirve para hoy; el tipo te sirve para
el martes que viene, porque el tipo es lo único que se repite. Los cinco tipos con nombre
llegan en el nodo siguiente, después de que hayas fallado unos cuantos, que es el orden
correcto.

## El nivel 6 existe por una razón

Uno de los seis niveles no tiene ningún fallo. El output es impecable y si marcas algo, te
equivocas.

No es una broma. Verificar de más tiene un precio y casi nunca se cuenta: rehaces trabajo
que estaba bien, tardas más que haciéndolo a mano y acabas discutiendo un error que no
existe. Quien marca fallos inexistentes pierde credibilidad igual de rápido que quien se
los traga. Cuánto verificar según lo que hay en juego es un tema entero:
`b3-m6-verificacion-proporcional`, «Verificación proporcional al riesgo».

## Cuándo esto falla

- **Sin fuente delante no hay verificación.** Si no tienes contra qué comparar, no estás
  verificando: estás opinando sobre un texto. Las tres pasadas necesitan el output y el
  material del que salió.
- **Entrena para errores plantados.** Son seis tipos porque son los que más aparecen, no
  los únicos. Cazarlos da repertorio, no inmunidad.
- **Verificar todo al máximo se rompe solo.** La atención no aguanta veinte revisiones
  minuciosas seguidas. Es más seguro revisar bien lo importante que todo regular.
- **Marcar sin tipificar no transfiere.** «Aquí hay algo raro» no sirve dentro de tres
  semanas. Sin nombre, has hecho un pasatiempo.
- **Destapar antes de intentarlo destruye el ejercicio.** No por moral: el único dato que
  produce es si tú lo habrías cazado, y se borra al leer la solución.

## Las tres instancias

Verificar lo que no has producido no es una habilidad de IA. Es una habilidad de oficina, y
llevas años ejerciéndola sin llamarla así.

| Dónde | Qué te llega hecho | La pasada que más falta hace |
|---|---|---|
| **Tu sector (CX)** | El resumen de incidencias del mes que le pasas a gerencia con tu nombre delante | La tercera: qué caso no está en el resumen |
| **Otro trabajo** | En una gestoría, el borrador de un trimestral que ha preparado otra persona | La primera: que las partes sumen el total |
| **Tu casa** | El presupuesto del taller, o el contrato de la luz que te llega «ya cumplimentado» | La segunda: cada condición, ¿dónde estaba escrita antes de hoy? |

La de casa es la que mejor lo enseña. Un contrato no se lee buscando frases mal escritas:
se lee buscando qué dice que no te habían dicho, y qué te habían dicho que no está. Eso es
el barrido.

## Ejercicio

**Material:** `ejercicios/sabotaje/`. Lee primero el `README.md` de esa carpeta: ahí está
el formato de cada ejercicio y cómo funcionan las soluciones.

**Haz cuatro, uno de cada nivel del 1 al 4, en ese orden.** No saltes: los niveles están
ordenados por lo que cuesta verlos, no por lo que cuesta entenderlos.

Por cada uno:

1. **Cronometra.** Apunta los minutos. Es un número que vas a querer tener dentro de un mes.
2. **Aplica las tres pasadas en orden**, aunque te parezca que ya lo has visto en la
   primera. Termina el barrido.
3. **Marca cada fallo con dos cosas: dónde y de qué tipo.** Con tus palabras; los nombres
   oficiales llegan en el nodo siguiente.
4. **Después, y solo después, destapa la solución.** Apunta tres números: fallos que había,
   fallos que cazaste, y **cosas que marcaste y no eran fallo**. Los falsos positivos
   cuentan igual que los fallos que se te escaparon.

**Entregable:** `sabotajes-<fecha>.md` con una fila por ejercicio: nivel, minutos, fallos
reales, cazados, falsos positivos y, en una línea, qué señal te lo delató o por qué se te
pasó. Esa última columna es la que vale.

**Regla de parada:** tres aciertos seguidos en un nivel y subes. Repetir lo que ya cazas no
entrena nada. Y al revés: si un nivel se te resiste dos veces, no es mala suerte, es un
agujero con nombre. Anótalo y vuelve a él dentro de una semana.

## Escribe tú la regla

En la bitácora, con tus palabras:

- «El tipo de fallo que más se me escapa es \_\_\_, y lo voy a buscar mirando \_\_\_.»
- «Antes de dar por bueno algo que no he escrito yo, hago siempre \_\_\_.»

## Para la bitácora

- ¿En qué nivel te has estrellado? ¿Y cuántos minutos tardaste en cada uno?
- ¿Cuántos falsos positivos marcaste? ¿Qué te hizo señalar algo que estaba bien?
- ¿En qué pasada apareció la mayoría de lo que cazaste? ¿Y cuál te saltaste sin darte
  cuenta?
