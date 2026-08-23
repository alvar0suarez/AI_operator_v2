# Guardarraíl 2 — Datos que parecen reales

> §7.3: *"Detecta y bloquea pegado de datos que parezcan reales (nombres + teléfonos
> + emails juntos) con un aviso de RGPD, **no con un bloqueo silencioso**"*.

## Qué protege

Dos cosas a la vez, y la segunda importa más:

1. Que no salgan datos de clientes de su empresa hacia un servicio externo.
2. **Que aprenda a notarlo.** Un bloqueo silencioso protege el dato de hoy y no le
   enseña nada para mañana, cuando use otra herramienta que no tenga guardarraíl.

Por eso la especificación es explícita: aviso, no bloqueo mudo.

## Qué se detecta

Se busca la **coincidencia de varias señales en el mismo mensaje**, que es lo que
distingue "un dato suelto" de "he pegado un trozo del CRM":

| Señal | Ejemplo |
|---|---|
| Teléfono español | `6XX XXX XXX`, `9XX XX XX XX`, `+34…`, con o sin separadores |
| Correo electrónico | patrón `algo@algo.tld` |
| DNI / NIE / CIF | `12345678Z`, `X1234567L`, `B39123456` |
| IBAN | `ES` + 22 dígitos |
| Nombre de persona | dos palabras capitalizadas seguidas, o nombre + apellido de listas frecuentes |
| Dirección postal | vía + número (`C/`, `Calle`, `Avda.`, `Pza.`) |
| Código postal | 5 dígitos junto a un topónimo |
| Estructura tabular | tres o más líneas con el mismo separador (`;`, `\t`, `|`) |

**Umbral:** dos o más tipos distintos de señal en el mismo mensaje, o una sola señal
repetida en tres o más filas. Un correo suelto en una frase no salta; una tabla de
cuatro filas con nombre, teléfono y correo, sí.

## Falsos positivos que hay que dejar pasar

- Datos del dataset del curso: clientes `CLI-####`, tickets `TCK-####`, pedidos
  `PED-#####`, y los dominios ficticios de Aguas del Norte. Son sintéticos. Lista
  blanca explícita.
- Sus propios datos si se está describiendo a sí misma.
- Números que no son personales: importes, cantidades, códigos de producto.

Es preferible un falso positivo a un falso negativo, pero un guardarraíl que salta
cada dos mensajes se acaba ignorando. Se calibra para que sea raro y creíble.

## Qué pasa cuando salta

1. El mensaje **no se envía a la API tal cual**. Se sustituyen las señales detectadas
   por marcadores (`[TELÉFONO]`, `[NOMBRE]`, `[EMAIL]`) antes de cualquier llamada.
2. Se le muestra el aviso, con lo que se ha detectado y cómo reescribirlo.
3. Su pregunta se responde igual, con la versión enmascarada. **No se la deja colgada.**
4. No se registra el mensaje original en el registro de preguntas (§7.4): ahí va la
   versión enmascarada.

Texto del aviso, en el tono del curso —práctico, entre colegas, sin solemnidad:

> Ojo, que ahí hay dos teléfonos y un correo que parecen reales. Eso no se pega en
> una herramienta externa: en una PyME el responsable del tratamiento es la empresa,
> y el marrón acaba en quien lo pegó.
>
> No hace falta: cuéntamelo con etiquetas. "CLIENTE_A, pedido de unos 300 €, se
> queja del descuento" me sirve exactamente igual. Te respondo con lo que me has
> contado, ya enmascarado.

## Lo que este guardarraíl no es

No es asesoramiento legal ni una garantía de cumplimiento. Es un filtro y un aviso.
El contenido del curso sobre esto vive en `b3-m7-datos-y-rgpd` y en
`b3-p4-anonimizar-en-la-practica`; cuando el guardarraíl salta, el aviso enlaza a ese
nodo, que es donde de verdad se aprende.
