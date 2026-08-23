# El gemelo sintético — especificación de generación

Deriva de `ESPECIFICACION.md` §4. Contrato para `scripts/generar-dataset.py`.

> **Por qué existe esto.** Sin datos reales no hay riesgo RGPD, hay realismo, y —lo
> decisivo— como los datos los generamos nosotros **existe respuesta correcta**. Eso
> permite corregir sin profesor, que es imposible con datos reales donde nadie sabe
> la respuesta. Cada número de este fichero es, por tanto, normativo.

## Empresa

**Aguas del Norte, S.L.** — distribuidora de agua envasada y bebidas a hostelería y
particulares. Cantabria y oriente de Asturias. 300 clientes en el maestro, 6
empleados, 4 rutas de reparto.

Plantilla (aparece como `agente` en tickets y como firmante en correos):

| Nombre | Rol | Aparece como |
|---|---|---|
| Marta Ibáñez | Atención al cliente | `M. Ibáñez`, `Marta`, `marta` |
| Rubén Solana | Atención al cliente | `R. Solana`, `Ruben`, `rubén` |
| Nieves Palacio | Administración / facturación | `N. Palacio`, `Nieves` |
| Chema Ortiz | Reparto ruta 1 y 2 | `Chema` |
| Iván Cuadrado | Reparto ruta 3 y 4 | `Iván`, `Ivan` |
| Begoña Salces | Gerencia | `Begoña`, `B. Salces` |

La inconsistencia de grafía del agente es **suciedad deliberada**, no un descuido.

**Periodo:** 2024-09-02 → 2025-02-28 (6 meses, 129 días laborables).

**Semilla:** `SEMILLA = 20250901`, fija. Toda aleatoriedad sale de un único
`random.Random(SEMILLA)`. Prohibido depender del orden de iteración de `set` o de
`dict` sin ordenar, o de la hora del sistema: dos ejecuciones deben producir
ficheros byte a byte equivalentes en contenido.

## Catálogo de producto

| Código | Producto | Precio ud (€) | Unidad |
|---|---|---|---|
| AG-05 | Agua mineral 0,5 L (pack 24) | 0.42 | botella |
| AG-15 | Agua mineral 1,5 L (pack 6) | 0.58 | botella |
| AG-GA | Agua con gas 1 L (pack 12) | 0.71 | botella |
| GF-19 | Garrafa 19 L retornable | 6.85 | garrafa |
| RE-05 | Refresco cola 0,33 L (pack 24) | 0.63 | lata |
| RE-NA | Refresco naranja 0,33 L (pack 24) | 0.63 | lata |
| CE-33 | Cerveza 0,33 L (pack 24) | 0.79 | botella |
| ZU-20 | Zumo 0,2 L (pack 18) | 0.55 | brik |
| FU-AL | Alquiler fuente refrigerada | 18.00 | mes |
| PO-10 | Portes fuera de ruta | 9.50 | servicio |

Márgenes brutos por producto (solo en `SOLUCIONES/`, nunca en los ficheros del
alumno): AG-05 0.22, AG-15 0.24, AG-GA 0.26, GF-19 0.31, RE-05 0.15, RE-NA 0.15,
CE-33 0.13, ZU-20 0.19, FU-AL 0.65, PO-10 0.10.

---

## Fichero 1 — `clientes.xlsx`

300 filas. Una hoja, `Clientes`.

| Columna | Contenido | Suciedad |
|---|---|---|
| `id_cliente` | `CLI-0001` … `CLI-0300` | — |
| `nombre` | Razón social o nombre | Mojibake en ~8% (`José`→`JosÃ©`) |
| `tipo` | hostelería / particular | 6 grafías mezcladas: `Hostelería`, `HOSTELERIA`, `hosteleria`, `Particular`, `part.`, vacío (~3%) |
| `direccion` | Calle y número | Mojibake en ~8% |
| `poblacion` | 14 municipios reales de la zona | — |
| `cp` | Código postal | ~5% guardado como número (pierde el cero inicial: `39001` bien, `9001` mal) |
| `telefono` | — | **4 formatos**: `942 12 34 56`, `+34942123456`, `942123456`, `942-12-34-56` |
| `email` | — | ~18% vacío; ~2% sin `@` |
| `fecha_alta` | Fecha | — |
| `ruta` | `RUTA-1`…`RUTA-4` | ~2% vacío |
| `forma_pago` | domiciliado / transferencia / efectivo | — |
| `descuento_pct` | 0, 3, 5, 8, 10, 12 | ~4% vacío (equivale a 0) |
| `observaciones` | Texto libre | ~70% vacío |

Reparto: **110 hostelería, 190 particulares**. Los descuentos > 0 se concentran en
hostelería: particular casi siempre 0.

### V2 — los 12 duplicados

De las 300 filas, **12 son duplicados** de otro cliente: 288 clientes reales.

Un duplicado comparte con su original la **dirección normalizada** y el **teléfono
normalizado** (mismos 9 dígitos), y difiere en:

- `id_cliente` (correlativo distinto, casi siempre muy posterior)
- `nombre`, con una de estas transformaciones: añadir/quitar forma jurídica
  (`Bar Manolo` / `BAR MANOLO S.L.`), abreviar (`Restaurante El Puerto` /
  `Rest. El Puerto`), mayúsculas, mojibake, o cambiar el orden (`Casa Pepe` /
  `Pepe, Casa`)
- `telefono` en **otro formato** de los cuatro (por eso la comparación literal falla)
- `direccion` con variación tipográfica (`C/ Alta 14` / `Calle Alta, 14`)
- `fecha_alta` distinta
- en **5 de los 12**, `descuento_pct` distinto entre las dos fichas — el mismo
  cliente facturado con dos condiciones. Ese es el daño real del duplicado.

Ambas fichas del par tienen pedidos: por eso el duplicado no se detecta "porque una
esté vacía". Normalización que los revela: teléfono a 9 dígitos + dirección en
minúsculas sin puntuación ni abreviaturas.

---

## Fichero 2 — `pedidos.xlsx`

Una hoja, `Pedidos`. **Una fila por línea de pedido** (así lo lleva la gente en
Excel). ~1.900 pedidos, ~5.400 líneas.

| Columna | Contenido |
|---|---|
| `id_pedido` | `PED-00001`… |
| `fecha` | Fecha del pedido (formato ISO, aquí sí uniforme) |
| `id_cliente` | FK a `clientes.xlsx` |
| `producto` | Código del catálogo |
| `descripcion` | Nombre del producto |
| `cantidad` | Unidades |
| `precio_ud` | Precio de tarifa |
| `dto_pct` | Descuento aplicado (heredado del cliente) |
| `importe_linea` | **Lo facturado** (ver bug) |
| `total_pedido` | Suma de las líneas del pedido, repetida en cada fila |

### V1 — el fallo de redondeo en pedidos con descuento

El sistema de facturación calcula así:

```
precio_neto_exacto     = precio_ud * (1 - dto_pct/100)
precio_neto_facturado  = ceil(precio_neto_exacto * 100) / 100     # ← el fallo
importe_linea          = round(precio_neto_facturado * cantidad, 2)
```

Lo correcto sería `importe_correcto = round(precio_neto_exacto * cantidad, 2)`.

El redondeo **al alza del precio unitario** antes de multiplicar hace que el error se
multiplique por la cantidad. Ejemplo real del dataset: AG-05 a 0,42 € con 8% de
descuento → neto exacto 0,3864 → facturado 0,39 → sobre 120 botellas se cobran
**0,43 € de más** en una sola línea.

Propiedades que el generador debe garantizar y `verificar-verdades.py` comprobar:

- `dto_pct == 0` ⇒ `desviacion == 0` siempre. El fallo **solo** toca pedidos con
  descuento. Ésa es la pista.
- `dto_pct > 0` ⇒ `desviacion >= 0`, y > 0 en al menos el 85% de esas líneas.
- La desviación acumulada del periodo se escribe en `SOLUCIONES/` al céntimo.

### Devoluciones no documentadas

~45 pedidos son devoluciones registradas como **pedidos con `cantidad` negativa** y
`importe_linea` negativo, sin ninguna marca que lo diga: ni columna `tipo`, ni
`abono` en la descripción, nada. Es lo que rompe cualquier suma ingenua y lo que
hace de anzuelo en el verbo 6. El manual (PR-05) dice que las devoluciones se
registran con albarán de abono; nadie lo hace.

### V3 — el pico de diciembre que no es demanda

Diciembre sube de verdad (~+12%, Navidad, es un distribuidor de bebidas). Pero el
volumen registrado sube ~+41%, porque **la carga del 9 al 13 de diciembre de 2024 se
importó dos veces**. Los pedidos fantasma:

- son copia exacta de un pedido real de esa semana: mismo `id_cliente`, misma
  `fecha`, mismos productos, mismas cantidades, mismos importes
- llevan `id_pedido` distinto, del bloque `PED-9xxxx` (correlativo aparte que nadie
  miró)
- son **62 pedidos** duplicados
- **no generan tickets** (son registros fantasma: nunca se sirvieron)

Se detectan agrupando por `(id_cliente, fecha, producto, cantidad)` y buscando
grupos de tamaño 2 concentrados en esos cinco días. Quitándolos, diciembre queda en
+12%: hay estacionalidad, pero cuatro veces menor de la que aparenta.

---

## Fichero 3 — `tickets.xlsx`

Una hoja, `Tickets`. **800 filas**.

| Columna | Contenido | Suciedad |
|---|---|---|
| `id_ticket` | `TCK-0001`… | — |
| `fecha_apertura` | — | **3 formatos mezclados**: `2024-11-03`, `03/11/2024`, `3-nov-2024`. Reparto ~55/30/15% |
| `canal` | telefono / email / whatsapp / presencial | Grafías mezcladas (`Teléfono`, `TELEFONO`, `tel`) |
| `id_cliente` | FK | ~4% vacío |
| `categoria` | — | **Inconsistente a propósito**: 14 etiquetas para 8 categorías reales, más `Otros` (~11%) y vacío (~5%) |
| `subcategoria` | — | ~78% vacío |
| `descripcion` | Texto libre, 1–3 frases, en español coloquial | — |
| `id_pedido` | FK, solo cuando aplica | ~52% vacío |
| `estado` | abierto / cerrado / pendiente | Grafías mezcladas |
| `fecha_cierre` | — | ~14% vacío en tickets cerrados; **9 filas con cierre anterior a la apertura** |
| `agente` | Plantilla | Grafías mezcladas; ~6% vacío |
| `tiempo_dedicado_min` | Entero | ~22% vacío; 7 valores absurdos (`999`, `0`, `1440`) |

### Taxonomía real (solo en `SOLUCIONES/`)

| Categoría real | Nº tickets | % | Verdad |
|---|---|---|---|
| `facturacion-redondeo` | 304 | 38,0% | **V1** |
| `entrega-sin-aviso` | 72 | 9,0% | **V5** |
| `entrega-retraso` | 96 | 12,0% | — |
| `producto-defectuoso` | 58 | 7,25% | — |
| `pedido-erroneo` | 74 | 9,25% | — |
| `cambio-datos` | 63 | 7,875% | — |
| `informacion-producto` | 89 | 11,125% | — |
| `otros` | 44 | 5,5% | — |

Las 14 etiquetas sucias de la columna `categoria` mapean a estas 8 de forma
**no biyectiva**: `Facturación`, `facturacion`, `FACTURACION`, `Facturas`,
`Incidencia facturación` → todas a `facturacion-redondeo` o a `pedido-erroneo` según
el caso; `Entrega`, `entregas`, `Reparto` → mezclan `entrega-sin-aviso` y
`entrega-retraso`; `Otros` recoge de todo. El mapeo exacto vive en `SOLUCIONES/`.

> El objetivo pedagógico de esta suciedad es que la columna `categoria` **no sirva**
> para el análisis y ella tenga que reclasificar desde `descripcion`. Ése es el
> puente del verbo 1 al bloque 4.

### V1 en los tickets

Los 304 tickets `facturacion-redondeo`:

- llevan `id_pedido` informado en el **86%** (el resto obliga a cruzar por cliente y
  fecha, que es donde se aprende de verdad)
- todos apuntan a pedidos con `dto_pct > 0` y `desviacion > 0`
- su `descripcion` nunca dice "redondeo": dice *"la factura no me cuadra con el
  albarán"*, *"me habéis cobrado 0,43 de más"*, *"otra vez descuadre en la factura"*,
  *"el descuento no está bien aplicado"*
- **17 tickets de facturación adicionales NO vienen del fallo** (error de precio,
  factura duplicada, IVA mal). El hallazgo no es "el 100% de facturación": es una
  concentración. Si ella dice 100%, la rúbrica lo marca.

### V5 en los tickets

Los 72 tickets `entrega-sin-aviso` son todos de clientes de **hostelería** y su texto
gira alrededor de lo mismo: *"vinisteis y estaba cerrado"*, *"no sabía que veníais
hoy"*, *"nadie me avisó"*, *"he perdido la entrega"*. Cruzando con
`procedimientos.docx` PR-07 (aviso previo de entrega el día anterior) se ve que el
procedimiento existe y no se cumple: **cero** menciones a aviso previo en los correos
y en las descripciones de tickets.

### V4 — los tres clientes

Tres clientes de hostelería concentran **176 tickets = 22,0%**:

| Cliente | Tickets | Facturado 6 meses | Margen bruto | Coste de contacto | Resultado |
|---|---|---|---|---|---|
| CLI-0042 | 62 | ver `SOLUCIONES/` | — | 62 × 11,00 € | **negativo** |
| CLI-0118 | 58 | — | — | 58 × 11,00 € | **negativo** |
| CLI-0233 | 56 | — | — | 56 × 11,00 € | **negativo** |

Condiciones que el generador debe garantizar: los tres tienen `descuento_pct` alto
(10–12), volumen de compra medio-bajo, y margen bruto de los 6 meses **inferior** al
coste de sus contactos con el coste unitario de 11,00 € que se deriva en el nodo
4.4. Las cifras exactas se calculan en generación y se escriben en `SOLUCIONES/`.

> Nota de diseño: los tickets de estos tres solapan con V1 y V5. Es deliberado. El
> mismo dato sostiene dos hallazgos distintos, y eso es exactamente lo que pasa en
> un análisis real.

---

## Fichero 4 — `correos/` (+ `bandeja.mbox`)

**200 correos** en `dataset/ficheros/correos/` como ficheros `.eml` (RFC 5322,
UTF-8, cabeceras `From`, `To`, `Subject`, `Date`, `Message-ID`, `In-Reply-To`), más
`dataset/ficheros/bandeja.mbox` con los mismos 200 en un solo fichero para quien
prefiera abrirlo así.

Suciedad deliberada, cada una con su cuota:

| Patología | Nº | Detalle |
|---|---|---|
| Asunto y cuerpo intercambiados | 34 | El asunto es `Consulta` / `Buenos días` / `-` y la incidencia está en el cuerpo; o el asunto lo cuenta todo y el cuerpo dice "según lo hablado" |
| Hilos rotos | 28 | `RE:` sin correo original en la carpeta, o `In-Reply-To` que apunta a un `Message-ID` inexistente |
| Adjuntos mencionados que no están | 22 | "te adjunto la factura", sin adjunto |
| Dos incidencias en un solo correo | 15 | Obliga a decidir si son uno o dos casos |
| Firma que no coincide con el remitente | 9 | El correo sale de la cuenta del bar y lo firma otra persona |
| Reenvío en cadena con historial pegado | 12 | Tres niveles de `>` y el dato útil al final |

Contenido: ~40% facturación (V1), ~14% entregas sin aviso (V5), resto repartido.
Los correos de los tres clientes de V4 están sobrerrepresentados.

Direcciones y nombres son inventados y **coherentes** con `clientes.xlsx`: el
ejercicio de extracción debe poder cruzarse.

---

## Fichero 5 — `procedimientos.docx`

Manual interno "oficial". Portada que dice **"v3 — revisado en marzo de 2019"**, que
ya es la primera pista. Índice y 9 procedimientos con formato de empresa pequeña que
copió una plantilla:

| Código | Procedimiento | Estado real |
|---|---|---|
| PR-01 | Alta de cliente nuevo | Se sigue a medias |
| PR-02 | Toma de pedido por teléfono | Se sigue |
| PR-03 | Preparación y carga de ruta | Se sigue |
| PR-04 | Entrega y firma de albarán | Se sigue |
| PR-05 | Devoluciones y abonos | **No se sigue** → devoluciones como negativos |
| PR-06 | Facturación mensual | Se sigue; describe el cálculo del descuento **de forma distinta a como lo hace el sistema** — ahí está V1 por escrito |
| PR-07 | **Aviso previo de entrega** | **No se sigue** → **V5**, el 9% de los tickets |
| PR-08 | Reclamaciones | Se sigue mal |
| PR-09 | Actualización de datos de cliente | No se sigue → alimenta los duplicados de V2 |

Contradicciones plantadas con la realidad de los otros ficheros:

- Dice **3 rutas**; en `clientes.xlsx` hay 4.
- Dice horario de reparto **8:00–16:00**; los albaranes y correos hablan de 7:00–15:00.
- Menciona un **"Departamento de Calidad"** que en una empresa de 6 personas no existe.
- PR-06 describe el descuento aplicado **sobre el importe de línea y redondeado al
  final**, que es lo correcto y lo contrario de lo que hace el sistema (V1). El
  manual tiene razón y nadie lo ha leído.
- PR-01 obliga a comprobar duplicados por teléfono antes de dar de alta (V2).

---

## `SOLUCIONES/` — fuera del alcance de la alumna

Se genera junto con los datos, **nunca a mano**, para que no pueda desfasarse.
Excluido del build del sitio (§8) y marcado en `.gitignore` del sitio, no del repo:
tiene que estar versionado para que el corrector funcione.

- `verdades-escondidas.md` — las cinco verdades con sus cifras exactas del run,
  el camino de detección esperado y el principio de CX del bloque 4 al que engancha
  cada una (§4: *no son acertijos, son ejemplos de la disciplina*).
- `taxonomia-real.csv` — `id_ticket, categoria_sucia, categoria_real`.
- `mapa-duplicados.csv` — los 12 pares con la clave que los une.
- `pedidos-fantasma.csv` — los 62 `id_pedido` duplicados de diciembre.
- `cuentas-v4.csv` — la cuenta completa de los tres clientes deficitarios.
- `metricas-generacion.json` — todos los conteos, para el verificador.

## Verificación

`scripts/verificar-verdades.py` **no lee `SOLUCIONES/`**: reconstruye las cinco
verdades desde los ficheros del alumno y las compara con los porcentajes de esta
especificación con tolerancia declarada. Si una verdad no es derivable desde los
datos publicados, el dataset está mal generado y el ejercicio central del bloque 4
sería irresoluble. Es el test de regresión del curso.
