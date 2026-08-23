---
id: b3-m7-datos-y-rgpd
bloque: 3
titulo: "Datos y RGPD: qué no se pega jamás"
tipo: concepto
duracion_min: 45
requisitos: [b3-m6-verificacion-proporcional]
desbloquea: [b3-m8-plantilla-de-verificacion]
caduca: alto
objetivos:
  - "Aplicar una regla de tres líneas antes de pegar cualquier texto en una herramienta"
  - "Distinguir el dato que identifica del que solo lo parece"
  - "Redactar la pregunta por escrito que se le hace a quien decide cuando nadie ha decidido nada"
  - "Anonimizar un texto de cliente sin que la tarea pierda el sentido"
conceptos: [rgpd, dato-personal, anonimizar, responsable-del-tratamiento, riesgo]
profundizar:
  - id: b3-p4-anonimizar-en-la-practica
    titulo: "Anonimizar de verdad, en dos minutos"
---

Primero la regla, que es lo que necesitas mañana a las nueve; la razón viene después y
viene corta. Esto no te convierte en experta en protección de datos: te deja un reflejo
de tres segundos y una pregunta escrita para quien decide.

## La regla, en tres líneas

1. **No pegues en ninguna herramienta un texto que permita llegar a una persona:**
   nombre, teléfono, correo, dirección, DNI, matrícula, número de cuenta o de factura.
2. **Si necesitas el caso, pega el caso sin la persona.** «CLIENTE_A, bar de la zona,
   dos facturas sin pagar, se queja del descuento» sirve exactamente igual para redactar
   una respuesta.
3. **Si al quitarlo la tarea pierde el sentido, esa tarea no se hace ahí.** No es un
   fallo del anonimizado: es la respuesta.

Con esas tres líneas estás por encima de lo que se hace en casi cualquier oficina
pequeña, y sin saber qué artículo lo dice.

## Por qué esto es un marrón real, y de quién

Quien responde ante la autoridad es **la empresa**, no tú: es la responsable del
tratamiento, la que decidió qué datos guarda, para qué y dónde. Tú no firmas nada de eso,
y aun así te cae a ti: la que pegó el texto fuiste tú, la conversación con gerencia es
contigo, y en una empresa de seis personas no hay ningún departamento entre tu teclado y
el problema.

El marco prevé multas de hasta 20 millones de euros o el 4 % de la facturación anual.
Ese número no es el tuyo y no sirve para pensar. Lo tuyo es esto: un cliente que reclama
a la autoridad de protección de datos, seis personas contestando por escrito qué datos
salieron, adónde y por qué, y una brecha que se notifica en 72 horas. Días de trabajo,
con plazos y sin nadie que lo haga por vosotros. Y al cliente cuyos datos salieron le da
igual quién tenía razón.

## Qué cuenta como dato personal

Dato personal no es «el nombre». Es **cualquier cosa que permita llegar a una persona,
directamente o cruzando**.

| | Ejemplos |
|---|---|
| Lo es, y se ve | Nombre, teléfono, correo, dirección, DNI, IBAN, matrícula |
| Lo es, y sorprende | Un `id_cliente` cuando existe un fichero que lo traduce; una dirección sin nombre; la firma de un albarán; una foto |
| Lo es por combinación | «Bar con terraza de un pueblo de 900 habitantes, dos empleados, nos compra los martes» |
| No lo es | Un importe agregado, una categoría de incidencia, un texto ya limpio de referencias |

La tercera fila es la que se cuela siempre. Quitas el nombre, te quedas tranquila y
dejas escrito «el bar de la plaza que nos compra garrafas los martes y debe dos
facturas». En un pueblo de 900 habitantes eso es el nombre escrito de otra manera.

## Cuando en tu empresa nadie ha decidido nada

Que es el caso normal, no la excepción: no hay política, no hay lista de herramientas
permitidas y nadie te ha dicho ni que sí ni que no.

Lo que **no** vale: dar por hecho que si nadie lo prohíbe está permitido; preguntarlo de
palabra en el pasillo y quedarte con un «haz lo que veas»; esperar.

Lo que haces, en este orden:

1. **Aplicas la regla de tres líneas hoy mismo.** Para no pegar datos no necesitas
   autorización de nadie.
2. **Escribes media página**, con fecha y tu nombre: qué herramienta, para qué, qué datos
   entran —ninguno personal— y qué haces en su lugar.
3. **La mandas por escrito** a quien decide, con una pregunta concreta: «¿puedo usar
   esto para redactar borradores, con los datos ya anonimizados?». Una pregunta concreta
   se contesta; «¿qué hacemos con la IA?» no se contesta nunca. Si la empresa tiene
   contratado un servicio de protección de datos, ésa es la pregunta que le llega.
4. **Mientras no haya respuesta, no montas nada que dependa de pegar datos personales.**
   El día que llegue la norma te lo tumban y habrás tirado el trabajo.

Los pasos 2 y 3 cuestan veinte minutos y dejan constancia de que preguntaste. Es el tipo
de gesto que en el bloque 6 se convierte en tener voz.

## Anonimizar antes de pegar

Tres movimientos, dos minutos:

- **Recorta.** Quédate con lo que la tarea necesita. La mitad de lo que ibas a pegar no
  hacía falta.
- **Sustituye.** Identificadores directos por etiquetas estables: CLIENTE_A, RUTA_1,
  POBLACIÓN_B. Estables dentro del mismo trabajo, para que el texto se siga entendiendo.
- **Quita el cruce.** Dirección exacta, número de factura, fecha exacta junto a la
  población, un importe tan raro que solo puede ser de uno.

El tercero es el que casi nadie hace y el que decide si esto sirve de algo. El
procedimiento completo está en `b3-p4-anonimizar-en-la-practica`, «Anonimizar de verdad,
en dos minutos».

> [!NOTE]
> Esto no vale solo para las herramientas nuevas. Es la misma higiene de reenviar un
> correo, pegar una captura en un grupo o mandar un fichero a un proveedor. Lo que cambia
> aquí no es el riesgo: es lo fácil que resulta pegar 200 filas de golpe sin mirarlas.

## Las tres instancias

- **En tu mesa.** El correo de reclamación que ibas a pegar entero lleva firma con
  teléfono, dirección de reparto y número de factura. Ninguno de los tres hace falta para
  redactar la respuesta, y cualquiera de ellos identifica al cliente.
- **En otro oficio: la clínica dental.** Los datos de salud tienen protección reforzada,
  así que «el paciente de la endodoncia del martes» no es un caso anónimo, es una
  persona. En una gestoría pasa igual con nóminas, DNI y salarios.
- **En tu casa.** La foto del DNI por un chat para reservar un apartamento, o el informe
  médico de tu madre pegado en cualquier sitio para que te lo expliquen con palabras
  normales. El segundo es el que más se hace y el que menos se piensa: no es tu dato, es
  el suyo, y no te lo ha dado para eso.

## Cuándo esto falla

- **Anonimizar tanto que la tarea pierde el sentido.** No has anonimizado mal: has
  descubierto que esa tarea no se hace ahí.
- **Creer que un identificador interno es anónimo.** Un `id_cliente` es un nombre para
  cualquiera que tenga abierto el maestro de clientes.
- **Guardar el mapa de equivalencias junto al texto**, o anonimizar el texto y adjuntar
  el fichero original. Las dos pasan más de lo que parece.
- **Fiarte de lo que promete un proveedor.** Puede ser cierto hoy y cambiar mañana, y en
  ningún caso traslada la responsabilidad de tu empresa por haber leído una página web.
- **El extremo contrario: no tocar nada.** Cómodo y también un error: con el texto
  anonimizado se puede trabajar casi todo.

## Por qué este nodo caduca alto

Va a cambiar todo esto: las obligaciones concretas, los criterios de la autoridad, qué
proveedor sirve para qué y lo que prometen los productos. Cuando pase, este nodo se tira
y se escribe otro sin tocar nada más del curso. Lo que no cambia es el reflejo: **mirar
un texto y quitar lo que lleva a una persona antes de pegarlo.** Quédate con el reflejo,
no con los detalles.

## Ejercicio

Quince minutos. Material: `dataset/ficheros/correos/`, correos inventados de una empresa
que no existe. **Con correos de tu empresa esto no se hace nunca**, ni de prueba.

1. Coge **tres correos** cualquiera de la carpeta.
2. Anonimiza cada uno en dos minutos con los tres movimientos, y apunta debajo qué has
   quitado y qué has sustituido.
3. **La prueba de reidentificación:** abre `dataset/ficheros/clientes.xlsx` y trata de
   averiguar de qué cliente era cada uno usando solo tu texto anonimizado. Si lo
   consigues, no estaba anonimizado: vuelve al paso 2 y quita el cruce que te delató.

**Entregable:** los tres textos anonimizados, la lista de lo que quitaste y la pista que
sobrevivió a la primera pasada, si la hubo. Esa pista es lo que aprendes hoy.

## Escribe tú la regla

Dos frases tuyas, y déjalas donde las veas al trabajar:

- «Antes de pegar cualquier cosa en cualquier sitio, me pregunto \_\_\_.»
- «Lo que no sale de mi ordenador es \_\_\_, aunque me lo pidan con prisa.»

## Para la bitácora

- ¿Qué has pegado en los últimos seis meses que hoy no pegarías?
- ¿Qué pista se te quedó dentro del texto en la primera pasada del ejercicio?
- ¿A quién le vas a mandar la media página, y qué te juegas si no contesta?
