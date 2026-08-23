# El tutor

`ESPECIFICACION.md` §7. **Principio rector: el tutor no da respuestas, da tracción.**
Si responde por ella, destruye exactamente la habilidad que el curso construye.

Todo lo de este directorio existe para hacer cumplir esa frase.

```
prompts/          Un fichero por modo. Se ensamblan sobre sistema-base.md.
  sistema-base.md   Lo que se le dice al modelo en TODOS los modos.
  modo-*.md         Los cinco modos de §7.1.
guardarrailes/    Las tres restricciones duras de §7.3, con su lógica.
serverless/       La función que proxea la API. La clave vive aquí y solo aquí.
```

## Los cinco modos (§7.1)

| Modo | Qué hace | Restricción dura |
|---|---|---|
| `explicar-de-otra-forma` | Reformula el concepto del nodo actual | No avanza materia |
| `socratico` | Preguntas que la acercan a la respuesta | **Nunca da la solución de un ejercicio** |
| `revisar-artefacto` | Feedback contra la rúbrica del nodo | Señala, no reescribe |
| `mas-practica` | Nuevos ejercicios de sabotaje del mismo tipo | Con su solución oculta |
| `aplicar-a-mi-caso` | Traduce el concepto a una situación suya | Ella describe el caso, no pega datos |

**`socratico` es el modo por defecto.** §9 lo marca como mitigación del riesgo de que
el tutor se convierta en muleta.

## Qué contexto se inyecta (§7.2)

Se inyecta:

- El nodo actual completo, y los nodos que son requisito suyo y ella ya ha cubierto
- El glosario del curso
- Los artefactos que ella ya ha producido, si los ha guardado
- Su bitácora reciente

**No se inyecta nunca:**

- Las soluciones de los ejercicios del nodo activo
- Nada que cuelgue de `dataset/SOLUCIONES/`
- Nodos que aún no ha desbloqueado (el tutor no adelanta materia)

El ensamblado vive en `serverless/contexto.js` y hay un test que falla si una ruta
de `SOLUCIONES/` entra en el prompt.

## Seguridad (§7.5)

La llamada a la API va **siempre** por la función serverless. La clave no puede estar
en el cliente, ni en el HTML, ni en una variable de build, ni en el repositorio.

Los identificadores de modelo y los parámetros **se consultan en la documentación
oficial antes de implementar, no se asumen**:

- <https://docs.claude.com/en/api/overview>
- <https://docs.claude.com/en/docs_site_map.md>

Lo que hay implementado ahora mismo en `serverless/handler.js`, y de dónde sale:

| Parámetro | Valor | Por qué |
|---|---|---|
| `model` | `claude-opus-5` | Consultado en la documentación oficial en agosto de 2026. **Vuelve a consultarlo antes de tocar nada**: este es el parámetro que más caduca de todo el repositorio. |
| `thinking` | `{type: "adaptive"}` | El modelo decide cuánto razonar. El presupuesto fijo de tokens de razonamiento está retirado en esta familia de modelos. |
| `output_config.effort` | `medium` | El tutor conversa, no está resolviendo el ejercicio por ella. Da respuestas rápidas y suficientemente pensadas, que es lo que hace falta a las nueve de la noche. |
| `max_tokens` | 64000 | Con flujo, para que una respuesta larga no se corte por tiempo de espera. |
| `cache_control` | `ephemeral` sobre el prompt de sistema | El sistema (índice del curso + glosario + nodo) es grande y se repite en cada turno de la conversación. |

> Esta tabla es de **caducidad alta**, igual que un nodo del curso. Si al leerla han
> pasado más de seis meses, dala por vencida y consulta la documentación.

Configuración en `serverless/.env.example`. El despliegue real usa las variables de
entorno del proveedor.

## Registro de preguntas (§7.4)

Cada consulta se guarda como `{nodo_id, pregunta, timestamp, modo}`. Tres usos, y los
tres importan:

1. Ella ve su propio histórico de dudas por nodo. Es una forma de progreso muy real.
2. Nosotros vemos dónde se atasca la gente. **Es el input directo para escribir el
   bloque 4**, que por eso está sin escribir.
3. Las preguntas repetidas se promueven a nodos de profundización permanentes.

---

## Despliegue

```bash
python3 scripts/empaquetar-tutor.py    # construye serverless/curso.json
cd tutor/serverless && npm install
node --test "pruebas/*.test.mjs"       # 18 pruebas, incluida la crítica
```

El sitio estático y la función se despliegan juntos. Adaptadores incluidos:

| Proveedor | Fichero | Ruta pública |
|---|---|---|
| Cloudflare Pages | `funciones/tutor.js` → `functions/api/tutor.js` | `/api/tutor` |
| Netlify | `funciones/tutor-netlify.mjs` | `/api/tutor` |
| Vercel | `funciones/tutor-vercel.mjs` | `/api/tutor` |

Variables de entorno: `ANTHROPIC_API_KEY` (obligatoria) y `REGISTRO_PREGUNTAS`
(opcional, almacén clave-valor para §7.4). Ver `serverless/.env.example`.

## La prueba que no se puede saltar

`pruebas/guardarrailes.test.mjs` empieza por dos comprobaciones que son la razón de
ser del fichero:

1. **El paquete del tutor no contiene ninguna solución.** Ni por ruta, ni por
   centinela, ni por campo de frontmatter.
2. **El prompt ensamblado no filtra soluciones por ninguna vía**, ni siquiera con un
   estado hostil que intente colarlas por los artefactos o la bitácora.

Si alguna de las dos falla, el curso ha perdido su corrector objetivo (§5.3) y el
ejercicio central del bloque 4 deja de tener sentido. No se despliega así.

Ese fichero ya ha cazado un fallo real: el empaquetado descartaba la cabecera de
cada prompt de modo, que es justo donde vive la restricción dura ("nunca da la
solución de un ejercicio", "señala, no reescribe"). El modelo estaba recibiendo el
modo sin su límite.
