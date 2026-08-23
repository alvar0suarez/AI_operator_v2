---
id: b2-p4-anomalia-no-es-error
bloque: 2
titulo: "Una anomalía no es un error"
tipo: profundizacion
duracion_min: 15
requisitos: [b2-m7-detectar-anomalias]
desbloquea: []
caduca: bajo
objetivos:
  - "Clasificar una anomalía en uno de los tres desenlaces posibles"
  - "Decidir qué hacer con ella a partir del recuento, no de la impresión"
conceptos: [anomalia, normalidad, causa-raiz]
---

Rama opcional del verbo 6. Encontrar algo raro no te dice qué hacer con ello. La
reacción por defecto —arreglarlo— solo sirve para uno de los tres desenlaces posibles;
en los otros dos sale caro. Quince minutos para saber cuál tienes delante.

## Los tres desenlaces

**1. Es un error.** Alguien tecleó 1.200 donde iban 12. Se corrige y se acabó. Coste:
dos minutos.

**2. Es legítimo y tu definición de normalidad estaba corta.** El pedido de 2.400 € de
un pueblo pequeño en agosto no es un error: son las fiestas, y pasa todos los años. Aquí
no se corrige el dato, se corrige **la definición**. Si lo tratas como error, borras
algo cierto y encima pierdes la información de que existe esa temporada.

**3. Es la punta de un patrón.** No es una vez: son cuarenta, y las otras treinta y
nueve no sobresalen lo suficiente como para que las hayas visto. Esta es la cara y la
que cambia decisiones.

## La pregunta que los separa

**¿Cuántas veces más pasa esto?**

No preguntes «¿es raro?»; cuenta. Una vez: error o caso legítimo. Cuarenta veces: no es
una rareza, es cómo funciona algo.

Y para separar el 1 del 2, una segunda pregunta: **¿el dato es imposible o solo poco
frecuente?**

| Señal | Desenlace probable |
|---|---|
| Imposible (una fecha de cierre anterior a la de apertura, un 1.440 en un campo de minutos) | Error |
| Poco frecuente pero coherente (un importe alto un día concreto del año) | Caso legítimo, definición corta |
| Poco frecuente y repetido con la misma forma | Patrón |

## Por qué el tercero es el que importa

La reacción natural ante un patrón es arreglar los casos. Cuarenta casos arreglados a
mano cuestan cuarenta veces el rato y no evitan el cuarenta y uno. Cuando el recuento
sale alto, la anomalía deja de ser un dato raro y se convierte en una pregunta sobre
cómo está montado algo. Ese salto tiene nombre —causa raíz— y es el trabajo del bloque
4 (`b4-m2-causa-raiz`, «Análisis de causa raíz»). Hoy basta con que no lo confundas: si
te ves arreglando el mismo caso por décima vez, no estabas ante una anomalía.

## Cuándo esto falla

- **Cuando no puedes contar.** Sin histórico no hay recuento y no hay desenlace. Lo
  honesto es anotar la fecha y volver a mirar dentro de un mes.
- **Cuando el recuento sale 3.** Ni error suelto ni patrón. Se anota, se le pone fecha y
  se revisa. Forzar la conclusión con tres casos es de donde salen las historias que
  luego no se sostienen delante de nadie.
- **Cuando tu definición de normalidad era demasiado estrecha.** Si se sale el 30 % del
  conjunto, no has encontrado 1.600 anomalías: has escrito mal la definición.
- **Cuando conviertes el desenlace en acusación.** «Esto lo hace mal fulano» cierra la
  investigación en el primer paso. Casi siempre lo raro lo produce cómo está montado el
  proceso, no quien lo ejecuta.

## Las tres instancias

- **En tu mesa.** Una línea de pedido en negativo. ¿Es una, o son muchas? Con una, es un
  error de tecleo. Si son muchas y todas tienen la misma forma, hay una manera de
  trabajar que nadie ha escrito en ningún sitio.
- **En una clínica dental.** Un paciente que no aparece a su cita es un despiste.
  Cuarenta que no aparecen y casi todos a primera hora de la tarde no son cuarenta
  despistes: es la hora.
- **En tu casa.** La factura de la luz de 180 €. Si es un mes, fue el mes del frío. Si
  son los seis últimos con subida constante, no era el frío.

## Escribe tú la regla

En tu catálogo, en la fila del verbo 6:

- «Cuando algo se sale, antes de tocarlo cuento \_\_\_.»
- «Dejo de arreglar casos y empiezo a preguntar por qué cuando \_\_\_.»

## Para la bitácora

- ¿Qué cosa llevas arreglando a mano más de cinco veces?
- De las rarezas que encontraste en `pedidos.xlsx`, ¿en cuál de los tres desenlaces las
  colocaste, y con qué recuento?
