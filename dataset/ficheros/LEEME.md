# Los ficheros de Aguas del Norte

Todo lo que vas a analizar en este curso sale de aquí. No necesitas datos de tu
empresa en ningún momento, ni ahora ni después.

## De qué empresa son

**Aguas del Norte, S.L.** es una distribuidora de agua envasada y bebidas.
Reparte a bares, restaurantes y hoteles, y también a particulares, en Cantabria
y el oriente de Asturias. Tiene unos 300 clientes en el maestro, seis empleados y cuatro rutas
de reparto. No existe: es una empresa inventada, con datos inventados, generada
por un script. Por eso puedes trastear con ella sin ningún problema de
privacidad.

Los ficheros cubren seis meses: del 2 de septiembre de 2024 al 28 de febrero de
2025.

## Qué hay en cada fichero

| Fichero | Qué es |
|---|---|
| `clientes.xlsx` | El maestro de clientes. Una fila por ficha: nombre, tipo, dirección, teléfono, ruta, descuento comercial y poco más. |
| `pedidos.xlsx` | El histórico de pedidos, **una fila por línea de pedido**, que es como lo lleva la gente en Excel. Producto, cantidad, precio, descuento, importe de la línea y total del pedido repetido en cada fila. |
| `tickets.xlsx` | Las 800 incidencias registradas en esos seis meses: canal, cliente, categoría, descripción escrita a mano, estado y tiempo dedicado. |
| `correos/` | 200 correos de clientes en formato `.eml`. Se abren con cualquier gestor de correo, y también con el Bloc de notas: por dentro son texto. |
| `bandeja.mbox` | Los mismos 200 correos en un solo fichero, por si prefieres abrirlos así. |
| `procedimientos.docx` | El manual interno "oficial" de la empresa. Nueve procedimientos, PR-01 a PR-09. |

## Aviso importante: están sucios a propósito

Esto no es un descuido. Los ficheros vienen **deliberadamente sucios**, con la
misma clase de porquería que tiene cualquier Excel que lleve años en una PyME:

- categorías escritas de mil maneras para decir bastantes menos cosas,
- fechas en tres formatos mezclados en la misma columna,
- teléfonos en cuatro formatos,
- acentos mal codificados (`JosÃ©` en vez de `José`),
- campos vacíos donde debería haber algo,
- códigos postales que a veces son texto y a veces número,
- nombres del mismo compañero escritos de cinco maneras,
- valores imposibles que alguien tecleó con prisa.

Si en algún momento piensas "esto está mal, ¿me lo habrán dado roto?": sí, y es
el ejercicio. Aprender a trabajar con datos limpios no sirve de nada, porque los
datos limpios no existen. La primera habilidad de todo este curso es mirar un
fichero y darte cuenta de qué no te puedes fiar.

## Cómo empezar

Ábrelos y míralos. Sin analizar nada todavía. Cuenta filas, mira qué columnas
hay, busca los huecos. Cuando el curso te pida algo concreto sobre ellos, ya
sabrás dónde está cada cosa.

> Estos ficheros se generan con `scripts/generar-dataset.py` a partir de una
> semilla fija. Si los tocas y quieres volver al punto de partida, se regeneran
> idénticos. No hace falta que lo hagas tú.
