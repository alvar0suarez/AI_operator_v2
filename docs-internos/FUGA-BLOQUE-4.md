# FUGA: el sitio publica las respuestas del bloque 4

> **Estado: sin arreglar.** La publicación automática del sitio está desactivada en
> `.github/workflows/sitio.yml` para que esto no salga a producción mientras tanto.
> Documento escrito el 2026-08-23 tras encontrarlo al preparar el despliegue.

## Qué pasa

El ejercicio central del curso (`b4-m10-analisis-completo`, §3 bloque 4) consiste en que
ella llegue **sola** a las cinco verdades escondidas del dataset. Ese ejercicio es la
razón de ser del gemelo sintético: §4 dice que los datos los generamos nosotros
precisamente para que *exista respuesta correcta* y se pueda corregir sin profesor.

**El sitio construido publica esas respuestas.** No en `dataset/SOLUCIONES/` —eso está
bien excluido— sino en tres sitios que nadie estaba mirando.

Alcance medido: **14 filtraciones**. Por verdad: V1 en 10, V5 en 3, V4 en 2.

## Las tres vías

### A. El glosario (11 entradas) — la peor

`contenido/glosario/glosario.yml` usa las verdades escondidas como **ejemplos** de sus
términos. El glosario se publica entero, está enlazado desde el pie de cada nodo, y es
de las primeras cosas que ella va a leer.

Ejemplos textuales de lo que hay dentro:

- `causa-raiz`: *«304 tickets de Aguas del Norte hablan de facturas que no cuadran. La
  causa raíz no son 304 clientes quisquillosos: es un redondeo al alza del precio…»*
  → V1 completa: la cifra, el porcentaje y el mecanismo.
- `contacto-evitable` y `omision`: PR-07, el aviso previo que nadie da → **V5 completa**,
  con el 9 %.
- `caso-de-negocio` y `coste-de-contacto`: los 11 € por contacto y los 3.344 € → el
  insumo de **V4**.

Entradas afectadas: `caso-de-negocio`, `causa-raiz`, `contacto-evitable`,
`coste-de-contacto`, `coste-de-oportunidad`, `evidencia`, `nps`, `omision`, `propuesta`,
`resolucion-primer-contacto`, `sistema`.

### B. El campo `brief` de los nodos pendientes (1, pero sistémica)

`scripts/construir-sitio.py`, función `marcador_pendiente()`, imprime
`meta.get('brief')` en la página de cada nodo `pendiente-piloto`.

`docs-internos/registro-de-nodos.yml` dice literalmente en su cabecera:

> Campo `brief`: qué tiene que cubrir el nodo. Es el encargo para quien lo escribe,
> no texto para la alumna. **No se publica.**

Y se publica. El brief de `b4-m2-causa-raiz` dice: *«Verdad escondida asociada: V1, el
fallo de redondeo»*. Los briefs de `b4-m3`, `b4-m7` y `b4-m10` nombran las suyas igual.

Es una violación directa de un contrato escrito, cometida por nuestro propio código.

### C. El sabotaje de nivel 2 (1)

`ejercicios/sabotaje/nivel-2/01-respuesta-a-un-bar/ejercicio.md`, en la sección «Lo que
sabes en la oficina»:

> «El manual tiene un procedimiento de aviso previo el día anterior (PR-07). **No se
> está aplicando con nadie.**»

Eso **es** V5, enunciada. Y está en el bloque 3, que va antes del 4.

## Por qué no lo cazó nada

Ésta es la parte que importa más que las 14 filtraciones.

`scripts/comprobar-build.py` comprueba **rutas y nombres de fichero**: que no se publique
nada de `dataset/SOLUCIONES/`, que no aparezcan los nombres de sus ficheros. Pasa en
verde, y tiene razón: ningún fichero de SOLUCIONES está publicado.

Lo que no comprueba es **el contenido de las verdades**. La suposición implícita era «si
las soluciones no están en el build, las respuestas no están en el build», y es falsa:
las respuestas se pueden escribir a mano en cualquier otro sitio, y eso es exactamente
lo que pasó tres veces, por tres vías distintas, sin que nadie lo escribiera queriendo.

Mis propias comprobaciones durante la construcción tuvieron el mismo agujero: busqué
filtraciones en `contenido/bloque-2/` y `contenido/bloque-3/` —donde no había— y nunca
en el glosario, en el registro ni en el build.

## Qué hay que arreglar

1. **`comprobar-build.py`: centinelas de contenido, no solo de ruta.** Que falle si en
   `sitio/build/` aparece cualquier señal de las cinco verdades (el mecanismo de V1, los
   pares de V2, los fantasma de V3, los tres clientes de V4, PR-07 como procedimiento
   incumplido de V5). Éste es el arreglo que impide que vuelva; los otros tres son
   consecuencias.
2. **`construir-sitio.py`: dejar de publicar `brief`.** La página del nodo pendiente
   debe decir el título, la duración y que se escribe después del piloto. Nada más. Y
   `validar-grafo.py` debería avisar si un `brief` nombra una verdad escondida.
3. **Reescribir las 11 entradas del glosario.** Los ejemplos tienen que seguir siendo
   concretos y del mundo de Aguas del Norte —eso es lo que las hace buenas— pero sobre
   hechos que **no** sean las respuestas: una entrega que llegó tarde, un cliente que
   cambió de dirección, un pedido con la cantidad mal. Hay dataset de sobra para ello.
4. **Reescribir la sección «Lo que sabes en la oficina» del sabotaje de nivel 2.** El
   ejercicio funciona igual si dice «hay un procedimiento de aviso previo que en la
   práctica no se sigue con este cliente». Lo que no puede decir es que no se sigue con
   nadie, ni cuántos tickets causa.
5. **Verificar que `b1-p1-por-que-fallan-los-diarios` es un falso positivo.** Su
   «redondeo» habla de redondear tiempos en un diario. Probablemente inofensivo, pero
   conviene mirarlo con ojos nuevos.

## Cómo comprobar que está arreglado

```bash
make todo                       # tiene que seguir en verde
python3 scripts/comprobar-build.py   # ahora con centinelas de contenido
```

Y la prueba de fuego, que es la que de verdad cuenta: **coger el sitio construido,
leerlo como lo leería ella, y ver si se puede llegar a alguna de las cinco verdades sin
haber tocado los datos.** Si se puede, sigue roto.

## Estado del despliegue

- `Settings → Pages → Source` ya está en **GitHub Actions**.
- El workflow tiene el disparador `push` **comentado** para que esto no se publique.
  Restaurarlo es lo último que hay que hacer, después de arreglar y verificar.
- El repositorio es privado; el sitio publicado sería público (Pages privado exige
  Enterprise). Con las filtraciones arregladas eso no es problema: el build no lleva
  ni `SOLUCIONES/` ni los ficheros del dataset.
