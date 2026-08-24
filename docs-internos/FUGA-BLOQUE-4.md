# FUGA: el sitio publicaba las respuestas del bloque 4

> **Estado: arreglado.** Encontrado el 2026-08-23 al preparar el despliegue, arreglado el
> 2026-08-24. Se deja escrito entero porque la parte que importa no son las filtraciones,
> es por qué las comprobaciones que teníamos pasaban en verde con ellas dentro.

## Qué pasaba

El ejercicio central del curso (`b4-m10-analisis-completo`, §3 bloque 4) consiste en que
ella llegue **sola** a las cinco verdades escondidas del dataset. Ese ejercicio es la
razón de ser del gemelo sintético: §4 dice que los datos los generamos nosotros
precisamente para que *exista respuesta correcta* y se pueda corregir sin profesor.

**El sitio construido publicaba esas respuestas.** No en `dataset/SOLUCIONES/` —eso
estaba bien excluido— sino escritas a mano en sitios que nadie estaba mirando.

Alcance real, medido después con los centinelas de `scripts/centinelas.py` sobre el árbol
de aquel commit: **26 frases** en seis sitios distintos. El recuento a ojo del día del
hallazgo se quedó en 14 y en cuatro vías; faltaban dos vías enteras y la taxonomía real.

| Verdad | Frases |
|---|---:|
| V1 — el fallo de redondeo | 13 |
| V5 — PR-07, el procedimiento que nadie sigue | 5 |
| V4 — los tres clientes deficitarios | 3 |
| V0 — el tamaño de la taxonomía real (la puerta a V1 y V5) | 6 |

## Las seis vías

### A. El glosario (15 entradas) — la peor

`contenido/glosario/glosario.yml` usaba las verdades escondidas como **ejemplos** de sus
términos. El glosario se publica entero, está enlazado desde el pie de cada nodo, y es
de las primeras cosas que ella va a leer.

- `causa-raiz`: *«304 tickets de Aguas del Norte hablan de facturas que no cuadran. La
  causa raíz no son 304 clientes quisquillosos: es un redondeo al alza del precio…»*
  → V1 completa: la cifra, el porcentaje y el mecanismo.
- `contacto-evitable` y `omision`: PR-07, el aviso previo que nadie da → **V5 completa**,
  con el 9 %.
- `caso-de-negocio` y `coste-de-contacto`: los 11 € por contacto y los 3.344 € → el
  insumo de **V4**.
- `voz-del-cliente`: *«el 40 % dicen lo mismo: la factura no cuadra con el albarán»* →
  **V1 redondeada**, que es exactamente igual de válida como respuesta.
- `taxonomia` y `clasificar`: catorce etiquetas para ocho categorías reales → el número
  que hay que reconstruir en `b4-m1-taxonomias`.
- `normalidad`: *«las 45 líneas negativas»* → el recuento del paso 3 del ejercicio de
  `b2-m7-detectar-anomalias`, publicado junto al ejercicio.

Entradas afectadas: `caso-de-negocio`, `causa-raiz`, `clasificar`, `contacto-evitable`,
`coste-de-contacto`, `coste-de-oportunidad`, `evidencia`, `normalidad`, `nps`, `omision`,
`propuesta`, `resolucion-primer-contacto`, `sistema`, `taxonomia`, `voz-del-cliente`.

### B. El campo `brief` de los nodos pendientes (26 páginas, una causa)

`scripts/construir-sitio.py`, función `marcador_pendiente()`, imprimía
`meta.get('brief')` en la página de cada nodo `pendiente-piloto`.

`docs-internos/registro-de-nodos.yml` dice literalmente en su cabecera:

> Campo `brief`: qué tiene que cubrir el nodo. Es el encargo para quien lo escribe,
> no texto para la alumna. **No se publica.**

Y se publicaba. El brief de `b4-m2-causa-raiz` dice: *«Verdad escondida asociada: V1, el
fallo de redondeo»*. Los de `b4-m1`, `b4-m4`, `b4-m7`, `b2-m6` y `b2-m7` nombran las
suyas igual. (El parte original decía que también lo hacían `b4-m3` y `b4-m10`: no era
cierto, sus briefs no nombran ninguna verdad.)

Es una violación directa de un contrato escrito, cometida por nuestro propio código.

### C. El sabotaje de nivel 2

`ejercicios/sabotaje/nivel-2/01-respuesta-a-un-bar/ejercicio.md`, en la sección «Lo que
sabes en la oficina»:

> «El manual tiene un procedimiento de aviso previo el día anterior (PR-07). **No se
> está aplicando con nadie.**»

Eso **es** V5, enunciada. Y está en el bloque 3, que va antes del 4.

### D. La plantilla del informe de causa raíz

`plantillas/informe-causa-raiz.md` daba como ejemplo de buen título:

> *«El 38% de las incidencias vienen de un solo fallo de facturación»*

Es decir: la plantilla que ella rellena **después** de resolver el ejercicio traía la
respuesta impresa como muestra de estilo.

### E. Un criterio de aceptación del bloque 3

`b3-p3-criterio-de-aceptacion.md`: *«Cada caso en una de estas ocho categorías»*. El
número de categorías reales es lo que hay que reconstruir en `b4-m1`.

### F. El LEEME del dataset — y, por él, el contexto del tutor

`dataset/ficheros/LEEME.md`: *«categorías escritas de catorce formas distintas para decir
ocho cosas»*. Anunciar la suciedad está bien y es deliberado (§4); contarla, no.

Y el texto de la vía E viajaba dentro de `tutor/serverless/curso.json`, o sea que el
tutor lo tenía en su contexto. El guardarraíl 1 dice que el tutor no da la solución de
un ejercicio; lo que no se le puede pedir es que no suelte algo que lleva dentro.

## Por qué no lo cazó nada

Ésta es la parte que importa más que las 26 frases.

`scripts/comprobar-build.py` comprobaba **rutas y nombres de fichero**: que no se
publicara nada de `dataset/SOLUCIONES/`, que no aparecieran los nombres de sus ficheros.
Pasaba en verde, y tenía razón: ningún fichero de SOLUCIONES estaba publicado.

Lo que no comprobaba es **el contenido de las verdades**. La suposición implícita era «si
las soluciones no están en el build, las respuestas no están en el build», y es falsa:
las respuestas se pueden escribir a mano en cualquier otro sitio, y eso es exactamente lo
que pasó seis veces, por seis vías distintas, sin que nadie lo escribiera queriendo.

Mis propias comprobaciones durante la construcción tuvieron el mismo agujero: busqué
filtraciones en `contenido/bloque-2/` y `contenido/bloque-3/` —donde casi no había— y
nunca en el glosario, en el registro, en las plantillas ni en el build.

## Qué se ha arreglado

1. **`scripts/centinelas.py`** — nuevo. Las cinco verdades escritas como 41 patrones de
   contenido, con dos redes que las anteriores no tenían:
   - **por franja**, no por cifra clavada: «el 40 % de los correos hablan de facturas» se
     caza igual que «el 38,00 %», porque redondear una respuesta no deja de ser la
     respuesta;
   - **conjuntivas**: un porcentaje sólo delata si además cerca hay un conjunto
     («tickets», «correos») y un tema («factura», «aviso»). Así el «si Otros pasa del
     10 %» que enseña el bloque 2 no salta, y el dato real sí.

   Trae **autoprueba**: los centinelas se ejecutan contra `SOLUCIONES/verdades-escondidas.md`
   y, si alguno no reconoce ahí su propia verdad, el proceso falla antes de mirar nada
   más. Un centinela mudo da vía libre a la filtración que vigila.

2. **`comprobar-build.py`** ahora comprueba las dos cosas: procedencia (lo de antes) y
   contenido (los centinelas), sobre el sitio construido. Los bundles de terceros que
   copia MkDocs Material quedan fuera del barrido de contenido: llevan tablas de pesos
   dentro y disparan cualquier centinela numérico.

3. **`empaquetar-tutor.py`** pasa los mismos centinelas al paquete del tutor. El
   guardarraíl deja de ser una instrucción y pasa a ser una propiedad de lo que se
   empaqueta: lo que no viaja dentro no se puede soltar.

4. **`construir-sitio.py`** ya no publica `brief`. La página de un nodo pendiente dice su
   título, su duración y que se escribe después del piloto. Nada más.

5. **`validar-grafo.py`** comprueba el contrato del `brief` por las dos puntas: es
   **error** que el ensamblador vuelva a leer ese campo (se mira su AST, para que un
   comentario no cuente), y es **aviso** la lista de briefs que nombran una verdad, que
   es exactamente lo que se filtraría el día que alguien lo publique.

6. **Los seis textos**, reescritos. Los ejemplos del glosario siguen siendo concretos y
   del mundo de Aguas del Norte —eso es lo que los hace buenos— pero sobre hechos que no
   son las respuestas: garrafas que llegan rotas, un cambio de cuenta que nadie acusa,
   media caja que falta. El sabotaje de nivel 2 dice ahora «a este cliente no se le está
   avisando», que es lo que el propio correo del cliente ya cuenta y deja el ejercicio
   igual de bien.

7. **`make centinelas`**, y `make todo` lo incluye, el último, para que barra el build
   recién hecho y no el de ayer.

## Dónde queda la raya

Es la decisión de fondo, y conviene que esté escrita porque los centinelas la aplican:

- **Se puede decir que los datos están sucios y de qué clase de suciedad se trata.** Ella
  tiene que esperarla, §4 la declara deliberada y el bloque 2 entero se apoya en ella.
  «Hay clientes duplicados» en la portada del bloque 0 se queda.
- **No se puede decir cuántos, cuáles, cómo se encuentran, qué cuestan ni qué los causa.**
  Eso es la respuesta.

Un caso concreto para calibrar: V5 está en la **universalidad**, no en la negación. Que a
*ese* bar no le avisaran lo cuenta el propio cliente en su correo. Que no se avise a
**nadie** es V5 enunciada.

## Falsos positivos verificados

- `b1-p1-por-que-fallan-los-diarios` habla de **redondear tiempos en un diario**. No tiene
  nada que ver con V1 y los centinelas lo dejan pasar: exigen que cerca del redondeo haya
  dinero.
- `b3-p5-coste-de-verificar-de-mas` tiene un «67 min → 72 min» que no son los 72 tickets
  de V5. Por eso los números sueltos llevan una comprobación de unidad detrás.
- El bloque 2 enseña, con razón, que un «Otros» por encima del 10 % es señal de taxonomía
  mala. Esa regla general y el dato real del dataset se escriben igual, así que ese
  centinela se probó y se retiró: un centinela ruidoso acaba desactivado.

## Cómo comprobar que sigue arreglado

```bash
make todo          # incluye centinelas, el último, sobre el build recién hecho
```

Y la prueba de fuego, que es la que de verdad cuenta: **coger el sitio construido,
leerlo como lo leería ella, y ver si se puede llegar a alguna de las cinco verdades sin
haber tocado los datos.** Se hizo al arreglarlo —portada, glosario entero, los seis
sabotajes, los ejercicios del bloque 2 y las páginas de los nodos pendientes— y de ahí
salieron las vías D, E y F, que ningún centinela había pedido buscar todavía.

## Estado del despliegue

- `Settings → Pages → Source` está en **GitHub Actions**.
- El disparador `push` de `.github/workflows/sitio.yml` sigue **comentado**. Era lo
  último de la lista y lo único que no es una decisión técnica: activarlo publica el
  sitio, y el repositorio es privado pero el sitio sería público. Queda para quien
  decide, no para quien arregla.
- El workflow ya trae el paso de centinelas, así que el día que se active, un build con
  filtraciones no llega a publicarse.
