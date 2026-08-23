# Solución — Nivel 1, el resumen del reparto

## Qué había

**El importe total está mal.** Dice 1.080,80 € y la suma real de las nueve líneas es
**1.292,95 €**.

Faltan exactamente 212,15 €, que es la línea 3, la Pensión Casa Pepe. El resumen la
contó al decir «9 entregas» pero no la sumó.

Y de ahí sale el segundo síntoma, que no es un fallo aparte sino el mismo:

- **Importe medio:** dice 120,09 €. Es 1.080,80 ÷ 9, o sea el total equivocado dividido
  entre el número correcto. El real es 1.292,95 ÷ 9 = **143,66 €**.
- **El porcentaje del Hotel Rialto:** dice 31,5 %. Es 340,08 ÷ 1.080,80, otra vez sobre
  la base equivocada. El real es **26,3 %**.

Todo lo demás es correcto: nueve entregas, cinco poblaciones, tres en Santander, y el
Hotel Rialto sí es la entrega mayor.

## Por qué esto engaña

Porque **es internamente coherente**. Si compruebas el resumen contra sí mismo, cuadra:
el medio sale del total, el porcentaje sale del total. Puedes releerlo tres veces
buscando incoherencias y no encontrar ninguna.

Ésa es la lección del nivel 1, y no es «revisa las sumas». Es más incómoda:
**la coherencia interna no demuestra nada.** Un resultado puede estar perfectamente
cuadrado consigo mismo y no tener nada que ver con la fuente.

## La comprobación de diez segundos

Suma la columna. Una vez. Contra el total que te da.

Es lo más barato que existe y detecta la familia entera de fallos: líneas olvidadas,
líneas contadas dos veces, filtros que se comieron algo. Si al sumar te sale otra cosa,
ya no hace falta comprobar nada más de ese documento: está mal y hay que rehacerlo.

Segunda comprobación, igual de barata: **¿cuadra el número de filas?** Aquí sí cuadraba,
y por eso hacía falta la suma. Cuando no cuadra el recuento, ni te molestes en sumar.

## Rúbrica

| Nivel | |
|---|---|
| **No llegó** | No encontró el fallo, o dijo «los números no cuadran» sin señalar cuál ni cuánto. |
| **Llegó** | Señaló que el total está mal, dio la cifra correcta (1.292,95 €) y nombró la comprobación: sumar la columna contra el total. |
| **Llegó y encontró algo que no estaba previsto** | Lo anterior, y además vio que el medio y el porcentaje **no son fallos independientes** sino consecuencias del mismo, y que el documento era internamente coherente. Quien ve eso ha entendido el nivel. |

## El error típico

Contar tres fallos en vez de uno. Es comprensible —hay tres cifras mal— pero lleva a un
diagnóstico equivocado: si crees que hay tres errores sueltos, piensas «esto lo hace mal
todo el rato». Si ves que hay uno con dos consecuencias, sabes exactamente qué arreglar
y qué volver a comprobar después.

**Un fallo aguas arriba produce varios síntomas aguas abajo.** Te lo vas a encontrar
otra vez en el bloque 4, con datos de verdad.
