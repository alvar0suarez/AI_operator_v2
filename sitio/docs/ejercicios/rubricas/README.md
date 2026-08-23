# Rúbricas — cómo se corrige sin profesor

`ESPECIFICACION.md` §5. El problema central de un curso autodidacta está enunciado
ahí sin rodeos: la habilidad más crítica es verificar output que no has producido, y
es justo donde una principiante no puede autoevaluarse, **porque el texto malo parece
bien**.

Todo lo de este directorio existe para resolver eso sin que haya nadie corrigiendo.

## Los tres niveles

Toda rúbrica del curso usa la misma escala. Tres niveles, no cinco, y sin nota
numérica: una nota invita a compararse, y aquí no hay con quién.

| Nivel | Qué significa |
|---|---|
| **No llegó** | Falta algo que el ejercicio pedía explícitamente, o el resultado no se sostiene contra la fuente. |
| **Llegó** | Hizo lo que se pedía, con el método que se enseñaba, y el resultado aguanta que lo comprueben. |
| **Llegó y encontró algo que no estaba previsto** | Lo anterior, y además vio algo que la rúbrica no anticipaba y que es cierto. |

El tercer nivel no es un extra decorativo. Es el nivel al que apunta el curso entero:
§10 dice que el criterio de éxito, seis meses después, es que ante una herramienta
nueva **sepa qué está buscando**. Eso solo se demuestra encontrando algo que nadie le
dijo que buscara.

> **Sobre el tercer nivel y la honestidad.** "Encontró algo que no estaba previsto"
> exige que sea **cierto y comprobable**, no interesante. Una intuición bonita que no
> se sostiene contra los datos es nivel *no llegó*, aunque suene mejor que la
> respuesta correcta. Ésa es la asignatura entera.

## Cuándo se destapa una rúbrica

**Después del intento. Nunca antes.** §5.3 es explícita, y no es una formalidad: si
ella lee la rúbrica primero, el ejercicio deja de medir su criterio y pasa a medir su
lectura comprensiva.

En el sitio, la solución de un ejercicio vive en fichero aparte y el tutor no la tiene
en el contexto hasta que ella marca "ya lo he intentado". El estado lo marca ella, y
puede mentir. Se acepta: el mecanismo impide el resbalón, no el fraude contra una
misma.

## Las cuatro formas de corregirse que tiene este curso

**1. Ejercicios de sabotaje** (`../sabotaje/`). Outputs con errores plantados, en seis
niveles de dificultad creciente. Ella marca, luego destapa.

**2. La realidad como corrector.** Preguntas que se responden con hechos y no con
sensaciones. Van en la bitácora:

- ¿Lo aceptó el compañero o el cliente sin retocarlo?
- ¿Tuviste que rehacerlo? ¿Cuántas veces?
- Minutos empleados **contra la línea base medida en el bloque 1**.

**3. Claves de corrección del dataset.** Todo ejercicio analítico sobre el gemelo
sintético tiene solución objetiva, porque los datos los generamos nosotros. Es la
única forma de tener respuesta correcta sin profesor: con datos reales, nadie sabe la
respuesta.

**4. El portfolio.** Al terminar tiene seis artefactos reales. Ésa es la prueba de
progreso, y es literalmente el material del bloque 6.

## Cómo se escribe una rúbrica de este curso

1. **Un criterio se puede aplicar si dos personas distintas coinciden.** Si "está
   bien redactado" admite dos lecturas, no es criterio: es gusto.
2. **Empieza por el nivel "llegó"**, que es el que hay que definir bien. Los otros dos
   salen de él: "no llegó" es lo que le falta, y el tercero es lo que sobra.
3. **Nombra el fallo típico.** Casi todos los ejercicios tienen uno que comete la
   mayoría. Decirlo en la rúbrica vale más que tres criterios genéricos.
4. **Nunca corrijas por cantidad.** "Diez tareas" es un mínimo del enunciado, no un
   criterio de calidad. Un inventario de diez filas puntuadas a ojo es peor que uno de
   diez filas con los números del diario detrás.
5. **Incluye qué hacer si salió mal.** Una rúbrica que solo juzga es media rúbrica. La
   otra mitad es: si estás en "no llegó", vuelve a tal sitio y repite tal cosa.

## Lo que una rúbrica de aquí no hace

- No pone nota numérica ni porcentaje.
- No compara con otra persona: no hay otra persona.
- No felicita. Si está bien, se dice y se sigue.
- No penaliza haber tardado más de lo previsto. Los `duracion_min` son una estimación
  para que pueda planificar su semana, no un examen cronometrado.
