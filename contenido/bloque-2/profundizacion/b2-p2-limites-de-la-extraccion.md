---
id: b2-p2-limites-de-la-extraccion
bloque: 2
titulo: "Dónde se rompe la extracción"
tipo: profundizacion
duracion_min: 20
requisitos: [b2-m3-extraer]
desbloquea: []
caduca: medio
objetivos:
  - "Reconocer los cinco orígenes en los que la extracción falla más"
  - "Exigir una columna «no consta» y usar su recuento como control"
conceptos: [extraer, dato-estructurado, verificacion]
---

Rama opcional del verbo 2. El verbo funciona bien con texto corrido; lo que lo rompe es
por dónde entra el texto. Aquí van los cinco orígenes duros y una defensa que cuesta
una columna. Este nodo es de caducidad media a propósito: los casos duros de hoy se
irán resolviendo solos con el tiempo, y la defensa no.

## Los cinco orígenes duros

**1. Una tabla dentro de un PDF.** Un PDF no guarda una tabla: guarda letras colocadas
en un sitio. Las columnas se funden, las celdas combinadas se reparten mal y las filas
que cruzan de página se parten. La señal característica: las tres primeras filas salen
perfectas y a partir de la cuarta todo se desplaza una columna. Si compruebas solo las
primeras, no ves nada.

**2. Escaneos y fotos.** Aquí el fallo no es de comprensión, es de lectura: `0` y `O`,
`1` y `l`, `5` y `S`, y sobre todo el separador decimal. Un importe con la coma leída
un sitio más a la derecha se equivoca por un factor de cien **y sigue pareciendo un
importe**. La revisión que paga en un escaneo es corta y concreta: solo los números, y
dentro de los números, solo los decimales.

**3. Documentos a dos columnas.** Se leen en el orden equivocado y las frases de la
izquierda se enganchan con las de la derecha. Sale un texto coherente hecho de dos
mitades que no iban juntas. Es el más traicionero de los cinco porque el resultado se
lee bien.

**4. El mismo dato en dos sitios con valores distintos.** El asunto del correo dice que
la entrega fue el jueves y el cuerpo dice que fue el viernes. No hay error visible: hay
que **elegir**, y elegir es una decisión que tú no has declarado. Defensa: dilo antes.
«Cuando el asunto y el cuerpo no coincidan, manda el cuerpo», o mejor todavía, «cuando
no coincidan, no elijas: márcalo como conflicto». Un conflicto marcado es información;
un conflicto resuelto en silencio es un dato falso.

**5. El campo que no está.** El más caro de los cinco. Un hueco no llama la atención, y
un hueco relleno con algo verosímil, tampoco. Media docena de referencias de pedido con
el formato correcto que no existen en ningún sitio pasan cualquier revisión rápida.

## La columna «no consta»

La defensa es esta, y es barata: **cada campo tiene tres estados posibles, no dos**.

| Estado | Cuándo |
|---|---|
| El valor | Está en el origen y es inequívoco |
| `no consta` | No está en el origen |
| `conflicto` | Está dos veces y no coincide |

Y luego se cuenta. El recuento por columna es el control, y se mira en treinta
segundos:

- **Cero «no consta» en un origen sucio es una alarma, no un éxito.** En la carpeta de
  correos hay hilos rotos, asuntos vacíos y adjuntos que se mencionan y no están. Si tu
  extracción sale completa, no es que los correos estuvieran completos.
- **Una columna con el 90 % en «no consta»** te está diciendo algo útil: ese dato no
  vive en ese origen. Deja de pedirlo ahí y búscalo donde esté.
- **Un «conflicto» que aparece siempre en la misma pareja de campos** ya no es ruido:
  es un patrón, y probablemente el síntoma de dos sitios que no se hablan.

## Cuándo esto falla

- **Verificar de más.** Contar los «no consta» cuesta medio minuto; releer los 200
  correos cuesta la tarde y no lo vas a hacer dos veces. La defensa tiene que ser barata
  o se abandona.
- **Fiarte solo del recuento.** El recuento no ve un dato mal leído: ve un dato ausente.
  Coge siempre cinco filas al azar y contrástalas con el original. Cinco, no cincuenta.
- **Pedir campos que el origen no tiene.** Si el número de albarán no está en el correo,
  ninguna forma de pedirlo lo va a hacer aparecer. Lo que puede pasar es que aparezca
  uno inventado.
- **Tratar «no consta» como un fallo.** Es lo contrario: es el verbo haciendo bien su
  trabajo. El fallo sería rellenarlo.

## Las tres instancias

- **En tu mesa.** Sacar cliente, referencia y motivo de doscientos correos. La columna
  que se llena de «no consta» es la referencia, y ese recuento es justo el argumento
  para pedir que el formulario de contacto la incluya.
- **En una gestoría.** Extraer base, cuota y CIF de facturas escaneadas. El «no consta»
  y el «conflicto» son la diferencia entre revisar cuatro y revisar cuarenta.
- **En tu casa.** Pasar a una lista los ingredientes de una receta de un blog. Faltan
  las cantidades de la mitad. Si la lista sale con cantidades en todas, alguien las ha
  puesto, y no ha sido la receta.

## Escribe tú la regla

En tu catálogo, en la fila del verbo 2:

- «Antes de fiarme de una extracción cuento \_\_\_.»
- «Cuando el mismo dato aparece dos veces y no coincide, yo \_\_\_.»

## Para la bitácora

- ¿Cuál de los cinco orígenes duros te toca a ti todas las semanas?
- ¿Qué campo de los que sacas habitualmente no existe de verdad en el origen del que lo
  sacas?
