# Las cinco verdades escondidas — clave de corrección

> **No se le enseña a la alumna.** Es la clave de corrección del ejercicio
> central del bloque 4 (`b4-m10-analisis-completo`) y de los ejercicios del
> bloque 2 que corren sobre el mismo dataset. Se destapa después del intento,
> nunca antes (ESPECIFICACION.md §5.3).
>
> Este fichero **se genera**, no se escribe a mano: lo produce
> `scripts/generar-dataset.py` en la misma ejecución que los datos, para que no
> pueda desfasarse. Todas las cifras son las de esta ejecución, con semilla
> 20250901.

ESPECIFICACION.md §4 lo dice sin rodeos: **no son acertijos, son ejemplos de la
disciplina**. Cada verdad existe porque detrás hay un principio de CX que se
puede enseñar con ella y no sin ella.

## Rúbrica de tres niveles (§5.3)

| Nivel | Qué significa |
|---|---|
| No llegó | No identificó la concentración, o la atribuyó a la columna `categoria` |
| Llegó | Identificó la causa raíz y la cuantificó con un margen razonable |
| Llegó y encontró algo | Además cruzó dos ficheros por su cuenta o cuestionó un dato |

---

## Antes de las verdades: por qué `categoria` no sirve

La columna `categoria` de `tickets.xlsx` trae 15
etiquetas distintas (más los vacíos) para 8 categorías reales. El reparto de las
más frecuentes:

| Etiqueta | Tickets | % |
|---|---:|---:|
| `Consulta` | 126 | 15,75 % |
| `Entrega` | 110 | 13,75 % |
| `Otros` | 77 | 9,62 % |
| `Pedidos` | 67 | 8,38 % |
| `Facturación` | 61 | 7,62 % |
| `Facturas` | 48 | 6,00 % |
| `(vacío)` | 43 | 5,38 % |
| `Info` | 42 | 5,25 % |

Quien agrupe por esa columna y sume las etiquetas de facturación obtiene
**185 tickets = 23,12 %**, de los
cuales solo el 81,08 % son de verdad del fallo de facturación. La
respuesta correcta es 38,00 %. **Fiarse de la columna
cuesta 14,88 % de error**, en
la dirección peligrosa: infravalora el problema.

Ése es el puente del verbo 1 (clasificar) al bloque 4: hay que reclasificar
desde `descripcion`, no desde `categoria`.

---

## V1 — El fallo de redondeo en pedidos con descuento

### 1. Enunciado

El sistema de facturación aplica el descuento **al precio unitario**, redondea
ese precio unitario **al alza** al céntimo, y sólo después multiplica por las
unidades. El error se multiplica por la cantidad. El manual (PR-06) describe el
cálculo correcto: descuento sobre el importe de la línea y redondeo al final.
Nadie ha leído el manual. Resultado: **38,00 % de los
tickets** son un cliente diciendo que su factura no cuadra.

### 2. Cifras exactas de esta ejecución

| Dato | Valor |
|---|---|
| Líneas de pedido con descuento | 3282 |
| De ellas, con sobrecoste | 3120 (95,06 %) |
| Líneas sin descuento con sobrecoste | 0 (invariante dura) |
| Pedidos afectados | 1139 |
| **Sobrefacturación acumulada en 6 meses** | **615,51 €** |
| Proyección a 12 meses | 1.231,02 € |
| Sobrecoste máximo en una sola línea | 1,14 € |
| Facturación total del periodo | 137.545,65 € |
| Tickets de la causa | 304 = 38,00 % |
| De ellos, con `id_pedido` informado | 261 (85,86 %) |
| Coste de atender esos tickets a 11,00 €/contacto | 3.344,00 € |

> El dinero mal facturado (615,51 €) es **calderilla** al lado
> del coste de atender las llamadas que provoca
> (3.344,00 €). Ése es el hallazgo de verdad, y es
> el que hay que llevar a Gerencia.

**Trampa deliberada:** hay 17 tickets más que también son
de facturación y **no** vienen de este fallo (factura duplicada, IVA mal, precio
mal pactado). Quien concluya "el 100 % de las incidencias de facturación es el
mismo fallo" se equivoca. El hallazgo es una **concentración**, no una
totalidad.

### 3. Camino de detección esperado

1. Reclasificar los 800 tickets desde `descripcion`, no desde `categoria`
   (verbo 1 sobre texto libre).
2. Ver que la clase mayoritaria es "la factura no cuadra" y que pesa ~38 %.
3. Coger los tickets de esa clase que llevan `id_pedido` y buscar esos pedidos
   en `pedidos.xlsx`.
4. Observar que **todos** tienen `dto_pct > 0`. Ésa es la pista: el fallo va con
   el descuento.
5. Recalcular la línea a mano: `precio_ud × cantidad × (1 − dto/100)`, redondear
   al final, y comparar con `importe_linea`.
6. Comprobar el signo: la diferencia es **siempre a favor de la empresa**. Un
   error aleatorio no tiene signo.
7. Comprobar el contraejemplo: en las líneas con `dto_pct = 0` la diferencia es
   exactamente cero. Eso confirma la hipótesis y descarta un error de tarifa.
8. Abrir `procedimientos.docx`, leer PR-06 y ver que el manual describe el
   cálculo correcto. El sistema no hace lo que dice el procedimiento.
9. Multiplicar: sobrefacturación del periodo, y coste de los contactos que
   genera.

### 4. Errores típicos

- **Fiarse de la columna `categoria`.** Da 23,12 % en
  vez de 38,00 %. Es el error más frecuente y el más caro.
- **Quedarse en el dinero mal facturado.** 615,51 € en seis
  meses no mueve a nadie. El argumento está en el coste de los contactos.
- **Decir "el 100 % de facturación es este fallo"** e ignorar los
  17 tickets que no lo son.
- **Comparar totales de factura en vez de líneas.** El descuadre se diluye al
  sumar; hay que bajar a la línea.
- **Redondear al comparar.** Si se recalcula con dos decimales desde el
  principio, se reproduce el propio fallo y sale que todo cuadra.
- **Concluir "se equivocó alguien al teclear".** Es sistemático: afecta al
  95,06 % de las líneas con descuento y
  a ninguna sin él.

### 5. Principio de CX al que engancha

**Análisis de causa raíz** (`b4-m2-causa-raiz`) y **contacto evitable**
(`b4-m3-contacto-evitable`). Los 304 tickets no son demanda de
atención: son la factura de un error de cálculo. Ninguno de ellos debería
existir. Arreglar el cálculo elimina la causa; contestarlos mejor solo acelera
el síntoma. Enlaza también con `b4-m8-del-sintoma-al-sistema`.

---

## V2 — Los doce clientes duplicados

### 1. Enunciado

`clientes.xlsx` tiene 300 filas pero
288 clientes: **12 son fichas duplicadas** de un
cliente que ya estaba. Cambian el nombre, el formato del teléfono y la tipografía
de la dirección, así que ningún cotejo literal los encuentra. PR-01 obliga a
comprobar el teléfono antes de dar de alta y PR-09 prohíbe crear ficha nueva por
un cambio de titular. Ninguno de los dos se cumple.

### 2. Cifras exactas de esta ejecución

| Dato | Valor |
|---|---|
| Filas en el maestro | 300 |
| Clientes reales | 288 |
| Pares duplicados | 12 |
| Pares en los que **el descuento difiere** | 5 |
| Pares en los que **ambas fichas tienen pedidos** | 11 de 12 |

| Original | Nombre original | Duplicado | Nombre duplicado | Teléfono normalizado | Dto. orig. / dup. |
|---|---|---|---|---|---|
| CLI-0036 | Antonio Villar | CLI-0155 | ANTONIO VILLAR | 942172767 | 0 / 0 |
| CLI-0023 | Francisco Herrera | CLI-0169 | FRANCISCO HERRERA | 942168404 | 0 / 0 |
| CLI-0033 | Laura Corral | CLI-0178 | LAURA CORRAL S.L. | 985440746 | 0 / 12 |
| CLI-0095 | Antonio Gómez | CLI-0185 | Antonio Gómez S.L. | 681332477 | 0 / 8 |
| CLI-0031 | Patricia Salces | CLI-0238 | Patricia Salces S.L. | 942176695 | 0 / 0 |
| CLI-0120 | Pensión Casa Pepe | CLI-0249 | PENSIÓN CASA PEPE | 637664533 | 12 / 12 |
| CLI-0101 | Pizzería La Terraza | CLI-0258 | PIZZERÍA LA TERRAZA | 722758866 | 12 / 10 |
| CLI-0094 | Pilar Corral | CLI-0265 | PILAR CORRAL S.L. | 942648257 | 0 / 12 |
| CLI-0081 | Bar Restaurante La Herradura | CLI-0277 | Bar Restaurante La Herradura S.L. | 651053873 | 0 / 10 |
| CLI-0001 | Cafetería El Molino | CLI-0294 | El Molino, Cafetería | 722765182 | 3 / 3 |
| CLI-0013 | Marta Villegas | CLI-0296 | MARTA VILLEGAS | 942689258 | 0 / 0 |
| CLI-0046 | Pizzería Casa Julián | CLI-0300 | Casa Julián, Pizzería | 690511282 | 10 / 10 |

### 3. Camino de detección esperado

1. Normalizar el teléfono: quitar espacios, guiones y el prefijo `+34`, quedarse
   con los 9 dígitos.
2. Normalizar la dirección: minúsculas, sin tildes, sin puntuación, desplegando
   `C/` → `calle` y `Avda.` → `avenida`.
3. Agrupar por la pareja (teléfono normalizado, dirección normalizada) y buscar
   grupos de más de una fila.
4. Comprobar que en cada grupo las dos fichas tienen pedidos: no es que una esté
   muerta, es que **se está facturando dos veces al mismo cliente**.
5. Mirar `descuento_pct` dentro de cada par. En
   5 de los 12 no coincide.
6. Leer PR-01 y PR-09 y ver que el procedimiento ya lo prohíbe.

### 4. Errores típicos

- **Comparar nombres.** `Bar Manolo` y `BAR MANOLO S.L.` no se parecen para una
  comparación literal, y `Pepe, Casa` menos todavía.
- **Comparar teléfonos sin normalizar.** Los cuatro formatos conviven a
  propósito: `942 12 34 56`, `+34942123456`, `942123456`, `942-12-34-56`.
- **Normalizar solo el teléfono** y dar por duplicados casos que no lo son (o al
  revés, no cruzar la dirección y no poder demostrarlo).
- **Contar 12 duplicados y parar ahí.** El daño no es tener filas de más: es que
  5 clientes están comprando con dos
  condiciones distintas según la ficha por la que entre el pedido.
- **Olvidar el mojibake.** Algunas fichas traen la codificación rota
  (`JosÃ©`); si no se arregla antes de normalizar, el cotejo falla.

### 5. Principio de CX al que engancha

**Taxonomías y calidad del dato maestro** (`b4-m1-taxonomias`) y, de lleno, la
capa transversal de *causa vs. síntoma*: limpiar los 12 duplicados a mano es el
síntoma; el sistema es que el alta no comprueba nada. Alimenta también
`b4-m8-del-sintoma-al-sistema`.

---

## V3 — El pico de diciembre que no es demanda

### 1. Enunciado

Diciembre parece dispararse. Sube de verdad —es un distribuidor de bebidas y
llega la Navidad— pero **el volumen registrado sube casi cuatro veces más de lo
que subió el negocio**, porque la carga de pedidos del 9 al 13 de diciembre de
2024 **se importó dos veces**. Los 62 pedidos duplicados
llevan `id_pedido` de un bloque aparte (`PED-9xxxx`) que nadie miró, y **no
generan ni un solo ticket**: nunca se sirvieron.

### 2. Cifras exactas de esta ejecución

| Mes | Líneas reales | Líneas registradas |
|---|---:|---:|
| 2024-09 | 868 | 868 |
| 2024-10 | 902 | 902 |
| 2024-11 | 856 | 856 |
| 2024-12 | 944 | 1188 |
| 2025-01 | 790 | 790 |
| 2025-02 | 796 | 796 |

| Dato | Valor |
|---|---|
| Media de líneas de los cinco meses que no son diciembre | 842.4 |
| Diciembre real | 944 líneas → **12,06 %** |
| Diciembre registrado | 1188 líneas → **41,03 %** |
| Pedidos fantasma | 62 |
| Líneas fantasma | 244 |
| Importe fantasma (ventas que nunca existieron) | 6.970,29 € |
| Ventana de la doble importación | 2024-12-09 → 2024-12-13 |
| Mismo cálculo contando pedidos en vez de líneas | real 16,44 % / registrado 37,25 % |

### 3. Camino de detección esperado

1. Agrupar `pedidos.xlsx` por mes y contar. Diciembre destaca.
2. Bajar a día: la anomalía se concentra en la semana del 9 al 13.
3. Agrupar por `(id_cliente, fecha, producto, cantidad)` y buscar grupos de
   tamaño 2. Aparecen 62 pedidos idénticos a otro.
4. Mirar los `id_pedido` de los duplicados: todos empiezan por `PED-9`. Es una
   numeración distinta, de otra carga.
5. Comprobar que ninguno de esos `id_pedido` aparece en `tickets.xlsx`. Pedidos
   que nadie reclamó nunca, ni para bien ni para mal.
6. Recalcular diciembre sin ellos. La estacionalidad existe, pero es cuatro
   veces menor de lo que aparentaba.

### 4. Errores típicos

- **Celebrar el pico.** Es lo primero que pasa: "diciembre va genial". Un dato
  que sube no se valida solo porque nos guste.
- **Buscar los duplicados por `id_pedido`.** Son distintos a propósito. Hay que
  agrupar por el contenido del pedido, no por su identificador.
- **Agrupar solo por cliente y fecha.** Un cliente puede pedir dos veces el
  mismo día en la vida real; hay que meter producto y cantidad en la clave.
- **Borrarlos y no preguntar por qué están.** La causa raíz es el proceso de
  importación, no las 62 filas.
- **No comprobar el contraste con tickets.** Es la prueba más limpia de que son
  fantasma: mercancía que nunca se sirvió no genera ni una queja.

### 5. Principio de CX al que engancha

**Detección de anomalías** (verbo 6 del bloque 2) y `b4-m5-metricas`: una
métrica que sube no es una buena noticia mientras no se sepa qué la mueve. Es el
ejemplo canónico de por qué se verifica el dato antes de construir encima.

---

## V4 — Los tres clientes que cuestan dinero

### 1. Enunciado

Tres clientes de hostelería concentran **176 tickets =
22,00 %** de todas las incidencias. Los tres tienen
descuento alto y compran poco. Con un coste de contacto de
11,00 € (que ella deriva en `b4-m4-coste-de-un-contacto`), su
margen bruto de seis meses **no paga ni de lejos** lo que cuesta atenderlos.

### 2. Cifras exactas de esta ejecución

| Cliente | Nombre | Dto. | Pedidos | Facturado 6 m | Margen bruto 6 m | Tickets | Coste contactos | Resultado |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| CLI-0042 | Cafetería El Cantábrico | 12 % | 44 | 805,32 € | 94,88 € | 62 | 682,00 € | **-587,12 €** |
| CLI-0118 | Hotel La Ría | 10 % | 40 | 695,76 € | 91,68 € | 58 | 638,00 € | **-546,32 €** |
| CLI-0233 | Mesón Casa Ramón | 12 % | 38 | 694,72 € | 73,23 € | 56 | 616,00 € | **-542,77 €** |

| Dato | Valor |
|---|---|
| Tickets de los tres | 176 de 800 = 22,00 % |
| Margen bruto conjunto | 259,79 € |
| Coste de sus contactos | 1.936,00 € |
| **Resultado conjunto** | **-1.676,21 €** |
| Facturación media de un cliente de hostelería (6 m) | 1.045,30 € |

### 3. Camino de detección esperado

1. Contar tickets por `id_cliente`. Tres clientes se despegan del resto.
2. Sumar cuánto suponen sobre el total: 22,00 %.
3. Ir a `pedidos.xlsx` y sumar lo facturado a esos tres en los seis meses.
4. Aplicar el margen por producto para obtener margen bruto, no facturación.
   Ojo: el descuento se come el margen, y estos tres tienen el descuento alto.
5. Multiplicar sus tickets por el coste de contacto de
   11,00 €.
6. Restar. Los tres salen en negativo.
7. Antes de proponer nada, mirar **por qué** llaman: sus tickets solapan con V1 y
   con V5. Parte de su coste no es culpa suya.

### 4. Errores típicos

- **Confundir facturación con margen.** Son los clientes con más descuento: la
  facturación engaña y el margen es la mitad de lo que parece.
- **Proponer echarlos.** Es la conclusión fácil y casi siempre está mal. Sus
  tickets solapan con V1 (facturas que no cuadran) y V5 (entregas sin avisar):
  buena parte de esas llamadas las provoca la propia empresa. Arreglado eso, el
  cliente puede dejar de ser deficitario.
- **Olvidar el `id_cliente` vacío.** 32 tickets no
  lo llevan; hay que recuperar el cliente por `id_pedido` o aceptar el hueco y
  decirlo.
- **Contar tickets sin normalizar el cliente.** Si además hay duplicados (V2),
  la cuenta de tickets por cliente puede estar partida en dos fichas.
- **Dar la cifra sin el coste unitario.** "22 % de las incidencias" no es un
  argumento; "-1.676,21 € de pérdida en seis meses"
  sí.

### 5. Principio de CX al que engancha

**El coste real de un contacto** (`b4-m4`) y **escalado y excepciones**
(`b4-m7`). Es el nodo donde se ve que la rentabilidad de un cliente no está en
lo que compra sino en lo que cuesta servirle, y donde se enseña a diseñar el
camino del caso raro en vez de sufrirlo.

---

## V5 — PR-07, el procedimiento que nadie sigue

### 1. Enunciado

El manual tiene un procedimiento entero, **PR-07 — Aviso previo de entrega**,
que obliga a avisar al cliente el día antes con la franja horaria. No se cumple
nunca. El resultado es **72 tickets =
9,00 %** de clientes de hostelería que estaban cerrados,
que no sabían que tocaba reparto, o que perdieron la entrega.

### 2. Cifras exactas de esta ejecución

| Dato | Valor |
|---|---|
| Tickets de la causa | 72 = 9,00 % |
| ¿Todos de hostelería? | sí |
| Menciones a "aviso previo" en `tickets.xlsx` | 0 |
| Menciones a "aviso previo" en los 200 correos | 0 |
| Menciones en `procedimientos.docx` | PR-07 completo, 4 apartados |
| Coste de esos contactos a 11,00 € | 792,00 € |

### 3. Camino de detección esperado

1. Reclasificar desde `descripcion` y separar dos cosas que la columna
   `categoria` mezcla: **entrega con retraso** y **entrega sin avisar**. No son
   el mismo problema ni tienen la misma solución.
2. Contar los "sin avisar": 72 tickets, 9,00 %.
3. Ver que **todos** son de hostelería. Un particular no pierde una entrega por
   no estar; un bar cerrado sí.
4. Leer `procedimientos.docx`. PR-07 existe, es explícito y describe justo lo
   que evitaría estos tickets.
5. Buscar en tickets y correos cualquier rastro de que ese aviso se dé alguna
   vez. **Cero.** El procedimiento existe en papel y no existe en la operación.
6. Cruzarlo con las contradicciones del propio manual (3 rutas frente a 4
   reales, horario 8:00–16:00 frente al 7:00–15:00 del que hablan los clientes,
   un "Departamento de Calidad" que en una empresa de 6 personas no existe):
   el manual lleva sin tocarse desde marzo de 2019.

### 4. Errores típicos

- **Meter "sin aviso" dentro de "retraso".** Es el error de taxonomía clásico y
  se lleva por delante todo el hallazgo: un retraso se arregla con logística, un
  aviso que falta se arregla con un mensaje el día antes.
- **Concluir que el procedimiento no existe.** Existe. El problema es otro:
  está escrito y nadie lo aplica. Son dos diagnósticos distintos y dos
  soluciones distintas.
- **Proponer "formar al equipo".** Sin preguntarse por qué un procedimiento de
  2019 nunca se ha aplicado. Casi nunca es que la gente no sepa.
- **No comprobar el perfil de cliente.** Que sean todos de hostelería es lo que
  permite acotar la solución y estimar su coste.
- **Tomarse el manual como verdad.** Contradice a los datos en cuatro puntos
  distintos. Es una fuente, no un oráculo.

### 5. Principio de CX al que engancha

**Contacto evitable** (`b4-m3`) y **del síntoma al sistema** (`b4-m8`), con
`b4-m7-escalado-y-excepciones` detrás. Es el caso más barato de arreglar de los
cinco y el que mejor enseña que la diferencia entre "documentado" y "hecho" es
donde vive la mayor parte del trabajo de CX.

---

## Resumen para el corrector

| Verdad | Cifra que tiene que salir | Tolerancia razonable |
|---|---|---|
| V1 | 38,00 % de los tickets | ±2 puntos |
| V1 | 615,51 € sobrefacturados en 6 meses | ±5 % |
| V2 | 12 pares duplicados | exacto |
| V3 | 62 pedidos fantasma | exacto |
| V3 | diciembre real 12,06 % frente a 41,03 % registrado | ±3 puntos |
| V4 | 22,00 % de las incidencias en 3 clientes | ±1,5 puntos |
| V4 | resultado conjunto -1.676,21 € | ±10 % |
| V5 | 9,00 % de los tickets | ±1,5 puntos |

`scripts/verificar-verdades.py` reconstruye estas cinco verdades **sin leer este
fichero**, solo desde `dataset/ficheros/`. Si falla, el ejercicio central del
bloque 4 ha dejado de tener solución.
