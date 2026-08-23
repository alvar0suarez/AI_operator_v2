# Guardarraíles

`ESPECIFICACION.md` §7.3. Tres restricciones. Las tres se aplican **antes** de llamar
a la API, en la función serverless, no confiando en que el modelo se porte bien.

| Fichero | Guardarraíl | Dónde se aplica |
|---|---|---|
| `01-solucion-bloqueada.md` | No da la solución de un sabotaje antes de que ella lo haya intentado | Servidor: se comprueba el estado `intentado` y se retira la solución del contexto |
| `02-datos-personales.md` | Detecta pegado de datos que parezcan reales, y **avisa**, no bloquea en silencio | Servidor: detección previa + aviso en la respuesta |
| `03-no-inventar-contenido.md` | No inventa contenido de curso que no exista | Contexto acotado + instrucción + comprobación de citas |

## Por qué en el servidor y no en el prompt

Un prompt es una petición. Un guardarraíl es una garantía. Las soluciones de los
ejercicios no se le piden al modelo que no las diga: **no se le mandan**.

Regla que ordena todo lo demás: si un guardarraíl se puede hacer no enviando algo,
se hace no enviándolo.

## Tests

`tutor/serverless/pruebas/` contiene un test por guardarraíl. El de `SOLUCIONES/` es
el crítico: falla si cualquier ruta bajo `dataset/SOLUCIONES/` acaba dentro del
prompt ensamblado, por cualquier vía.
