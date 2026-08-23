# Ejercicios de sabotaje

`ESPECIFICACION.md` §5.1. El curso te entrega outputs de IA **con errores plantados
dentro**. Tú los cazas. Después destapas la solución y ves qué había.

## Por qué esto existe

Porque el problema central de aprender esto sola es que **el texto malo parece bien**.
Un informe con un dato inventado se lee igual de bien que uno correcto: no hay
subrayado rojo, no hay aviso, no hay nada. Producir con una máquina es fácil. Saber si
lo producido sirve es la habilidad escasa, y es la que no caduca.

No se puede entrenar leyendo. Solo cazando.

## Las reglas de la casa

1. **Se intenta antes de destapar.** La solución está en fichero aparte y el tutor no
   la tiene hasta que marcas "ya lo he intentado". Puedes hacer trampa; solo te la
   harías a ti.
2. **No basta con decir "hay un fallo".** Marca **dónde** está y **de qué tipo** es.
   El tipo es lo que se transfiere al martes siguiente.
3. **A veces no hay ningún fallo.** El nivel 6 es un output impecable. Si marcas
   errores que no existen, también has aprendido algo, y algo caro: revisar de más
   cuesta dinero y desgasta la confianza en lo que produces.

## El método de las tres pasadas

Siempre en este orden, de lo barato a lo caro:

**1ª — Los números.** Cada cifra, contra la fuente. ¿Suman las partes el total? ¿El
porcentaje va sobre la base que crees? ¿Cuadra el número de filas?

**2ª — Las afirmaciones.** Cada frase que afirma algo sobre la realidad: ¿de dónde
sale? Si no puedes señalar dónde, es un dato inventado hasta que se demuestre lo
contrario. Sospecha sobre todo de lo que te viene cómodo.

**3ª — Lo que falta.** La difícil, porque no se ve leyendo: hay que comparar con la
fuente. ¿Está el caso excepcional? ¿Está el cliente que siempre da problemas?

## Los seis niveles

| Nivel | Qué se planta | Por qué cuesta |
|---|---|---|
| [1](nivel-1/) | Dato numérico que no cuadra con la fuente | Se ve si comparas. Casi nadie compara. |
| [2](nivel-2/) | Tono inadecuado para el destinatario | Hay que leerlo desde el sitio de quien lo recibe, no desde el tuyo. |
| [3](nivel-3/) | Dato inventado plausible | No cuadra con nada porque no existe. Y suena perfectamente razonable. |
| [4](nivel-4/) | Omisión silenciosa | No se ve leyendo. Solo comparando. Es el más caro de los seis. |
| [5](nivel-5/) | Conclusión correcta con razonamiento erróneo | El resultado es bueno, así que nadie revisa cómo se llegó. La próxima vez no lo será. |
| [6](nivel-6/) | **Nada. El output es impecable.** | Enseña lo contrario que los otros cinco. |

## Formato

Cada ejercicio es un directorio con:

```
nivel-N/
  NN-nombre/
    ejercicio.md    la fuente + el output saboteado + la consigna
    solucion.md     qué había, cómo se cazaba, y qué señal barata lo delataba
```

`solucion.md` **no se publica como página del sitio** y **no entra en el contexto del
tutor** hasta que marcas el ejercicio como intentado.

## Cuántos hay

Mínimo cuatro por bloque a partir del bloque 3, que es donde vive la verificación.
Si te quedas corta, el tutor te fabrica más del mismo nivel en el modo **"Ponme más
práctica"**, con su solución escondida igual que aquí.

Si aciertas tres seguidos del mismo nivel, sube. Repetir lo que ya cazas no entrena
nada.
