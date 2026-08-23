# El generador del gemelo sintético

El código está en [`../../scripts/generar-dataset.py`](../../scripts/generar-dataset.py).
El contrato, en [`../ESPECIFICACION-DATASET.md`](../ESPECIFICACION-DATASET.md).

## Por qué existe un generador y no unos ficheros a mano

`ESPECIFICACION.md` §4 pide reproducibilidad desde script con semilla fija, y da la
razón práctica: poder regenerar con variaciones si hiciera falta una segunda vuelta.

Pero la razón de fondo es otra y es más importante. **Como los datos los generamos
nosotros, existe respuesta correcta.** Eso es lo que permite corregir sin profesor
(§5.3), algo imposible con datos reales, donde nadie sabe la respuesta. Un dataset
escrito a mano se desincroniza de sus propias soluciones a la tercera corrección; uno
generado no puede.

## Reglas de mantenimiento

1. **Los ficheros de `../ficheros/` no se editan nunca a mano.** Se cambia el
   generador, se regenera y se pasa `scripts/verificar-verdades.py`.
2. **La semilla no se cambia sin motivo.** Cambiarla invalida cualquier solución
   escrita a mano en el contenido del curso, y hay nodos del bloque 4 que citan cifras.
3. **`verificar-verdades.py` no lee `../SOLUCIONES/`.** Reconstruye las cinco verdades
   desde los ficheros publicados. Si deja de pasar, el ejercicio central del bloque 4
   se ha quedado sin solución y el curso está roto por dentro aunque todo lo demás
   compile.
4. **La suciedad tiene cuotas, y son normativas.** Están en la especificación del
   dataset. Suciedad de menos y el ejercicio se vuelve trivial; de más y se vuelve
   frustrante, que es el riesgo que §9 marca como "el dataset sintético se siente
   artificial".

## Si hiciera falta una segunda vuelta

Cambiar `SEMILLA` produce un dataset distinto con las mismas propiedades: los mismos
porcentajes, las mismas cinco verdades, otros nombres y otras cifras exactas. Sirve
para una segunda alumna, o para volver a hacer el bloque 4 sin acordarse de las
respuestas.

Lo que hay que hacer entonces: regenerar, pasar el verificador, y revisar los nodos
del bloque 4 que citen cifras concretas del run anterior.
