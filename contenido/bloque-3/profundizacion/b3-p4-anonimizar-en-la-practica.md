---
id: b3-p4-anonimizar-en-la-practica
bloque: 3
titulo: "Anonimizar de verdad, en dos minutos"
tipo: profundizacion
duracion_min: 20
requisitos: [b3-m7-datos-y-rgpd]
desbloquea: []
caduca: medio
objetivos:
  - "Aplicar los cuatro pasos del procedimiento a un texto de cliente"
  - "Detectar el dato que reidentifica por cruce aunque no sea un nombre"
  - "Decidir qué se conserva porque la tarea lo necesita"
conceptos: [anonimizar, dato-personal, reidentificacion, rgpd]
---

Rama del nodo de datos. Aquí está el procedimiento repetible, que es lo que convierte
una buena intención en un hábito: cuatro pasos, dos minutos, y el caso que engaña a todo
el mundo la primera vez.

## Los cuatro pasos

**1. Recorta primero.** Antes de sustituir nada, quita lo que la tarea no necesita: la
cabecera del correo, la firma, el historial pegado debajo, el hilo entero. Casi siempre
sobra más de la mitad. Es el paso que más identificación elimina y el que menos tiempo
cuesta, y por eso va el primero.

**2. Sustituye los identificadores directos por etiquetas estables.** CLIENTE_A, BAR_1,
POBLACIÓN_B, RUTA_2. **Estables** significa la misma etiqueta para la misma persona
dentro del mismo trabajo: si en el tercer párrafo CLIENTE_A se convierte en CLIENTE_C,
el texto deja de entenderse y el resultado sale mal. Si necesitas apuntar qué es cada
etiqueta, ese papel se queda en tu ordenador y no viaja con el texto.

**3. Quita los cuasi-identificadores.** Los que no son un nombre y hacen el mismo
trabajo: dirección exacta, matrícula, número de factura o de albarán, un importe con
céntimos que solo puede ser de un pedido, la fecha exacta junto a la población.

**4. Lee lo que queda y hazte la pregunta del vecino:** si esto lo leyera alguien de esa
zona, ¿sabría de quién hablas? Si la respuesta es que sí, vuelve al paso 3.

## El caso que engaña

> «Bar con terraza de un pueblo de la costa, dos empleados, nos compra garrafas los
> martes y dice que la factura de enero no le cuadra.»

Ni un nombre, ni un teléfono, ni una dirección. Y en ese pueblo hay exactamente un bar
con terraza.

La identificación no vive en el nombre: **vive en la combinación**. Tres detalles
corrientes, inofensivos por separado, se cruzan y dan una persona. Es el mismo mecanismo
por el que en tu oficina decís «el del puerto» y todo el mundo sabe quién es, sin haber
dicho ningún dato personal.

De ahí la regla que hay que recordar: **cuanto más pequeño es el conjunto del que
hablas, menos detalles hacen falta para identificar.** En una ciudad, «un bar con
terraza» no es nadie. En un pueblo de 900 habitantes, es alguien.

## Qué se conserva

Anonimizar no es borrar. Si te llevas por delante lo que la tarea necesita, el resultado
no valdrá y acabarás pegando el original, que es lo que queríamos evitar.

| Se queda | Se va |
|---|---|
| La estructura del problema: qué pasó y en qué orden | Nombre, teléfono, correo, dirección |
| El tipo de cliente (hostelería o particular) y la ruta como etiqueta | El identificador interno, si existe un fichero que lo traduce |
| El importe en tramo: «unos 40 €» | El importe exacto con céntimos |
| El mes | La fecha exacta |
| El tono de la queja, entero, que muchas veces es lo que importaba | La firma y el historial pegado debajo |

Y la regla de corte, que ya viste en `b3-m7-datos-y-rgpd`, «Datos y RGPD: qué no se pega
jamás»: si al terminar la tarea deja de tener sentido, no has anonimizado mal. Has
averiguado que esa tarea no se hace ahí.

## Cuándo esto falla

- **Etiquetas que bailan.** CLIENTE_A en un párrafo y CLIENTE_C en el siguiente. El
  texto se vuelve incoherente y el resultado también.
- **El mapa viajando con el texto.** Si pegas también la tabla de qué cliente es
  CLIENTE_A, no has anonimizado: has añadido un paso.
- **El texto limpio y el fichero adjunto sucio.** O la captura de pantalla, que lleva
  dentro todo lo que hubiera abierto en esa ventana.
- **Muchas columnas juntas.** Un caso descrito como «hostelería, ruta 2, cliente desde
  2019, pide garrafas» puede dejar dos candidatos entre 300. Cada columna que añades
  resta anonimato, aunque ninguna sea un nombre.
- **Anonimizar como excusa para no pensar.** Si la tarea consiste en decidir sobre una
  persona concreta, el problema no era el nombre.

## Las tres instancias

- **En tu mesa.** El correo de reclamación: recortas la firma y el hilo, sustituyes al
  cliente por CLIENTE_A, quitas el número de factura y dejas «unos 40 €» y «enero». El
  borrador de respuesta sale igual de bien.
- **En otro oficio: la gestoría.** Una nómina sin nombre sigue identificando si dejas el
  puesto y la antigüedad: en una empresa de ocho personas, «responsable de almacén desde
  2016» es una persona con nombre y apellidos.
- **En tu casa.** El justificante de pago al que le tachas el nombre y le dejas el número
  de cuenta. O la foto del grupo de la excursión del colegio, donde lo identificable no
  es lo que escribes: son las caras.

## Escribe tú la regla

En la bitácora, y en tu `contexto-trabajo.md` si tiene sitio:

- «Antes de pegar un texto de cliente quito siempre \_\_\_.»
- «El dato que más se me olvida quitar es \_\_\_.»

## Para la bitácora

- ¿Cuántos segundos has tardado en el tercer texto? ¿Y en el primero?
- ¿Qué cuasi-identificador se te coló y te delató en la prueba de reidentificación?
