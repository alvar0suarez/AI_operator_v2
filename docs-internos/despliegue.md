# Despliegue — cómo llega el curso a ella

El repositorio no es el entregable. El entregable es **una dirección web** que ella abre
en el móvil o en el portátil, sin instalar nada, sin cuenta y sin contraseña.

Hay dos caminos. Cuál te conviene depende de dos hechos del repositorio, no de gustos:

**El repositorio es privado**, y **su rama por defecto es `claude/revisar-especificacion-ukp7rd`**,
no `main`. Las dos cosas condicionan el despliegue.

| | Sitio | Tutor | Repo privado | Coste |
|---|---|---|---|---|
| **Cloudflare Pages** | sí | **sí** | sí, sin problema | gratis |
| **GitHub Pages** | sí | no | **requiere plan de pago** (Pro/Team) | gratis solo si el repo es público |

**Recomendación: Cloudflare Pages.** Con el repositorio privado es el único de los dos que
funciona en gratis, y además trae el tutor, que en GitHub Pages no puede funcionar: Pages
sirve ficheros, no ejecuta código, y la clave de API no puede estar en el navegador (§7.5).

Si prefieres GitHub Pages tienes dos formas de desbloquearlo, y conviene saber qué implica
cada una:

- **Hacer público el repositorio.** Gratis e inmediato, pero entonces `dataset/SOLUCIONES/`
  queda legible por cualquiera. Los datos son sintéticos y no hay riesgo de privacidad, pero
  las cinco verdades escondidas —que son el examen del bloque 4— dejan de estar escondidas
  para quien sepa mirar el repositorio. Ella recibiría una URL, no el repo, así que en la
  práctica no las va a ver; decídelo tú.
- **Subir de plan.** GitHub Pro habilita Pages en repositorios privados.

> Los nodos, los ejercicios, los sabotajes, el dataset, las plantillas y la página de
> progreso funcionan igual en los dos caminos. La única diferencia es el tutor.

## Camino A — GitHub Pages (sitio solo)

**Antes:** el repositorio tiene que ser público, o tener plan de pago. Si no, la opción de
Pages aparece desactivada y no hay forma de saltársela.

1. En GitHub, `Settings` → `Pages` (columna izquierda, en «Code and automation»).
2. En **Source**, elige **GitHub Actions**. No elijas «Deploy from a branch»: el workflow
   ya construye el sitio y esa opción publicaría el repositorio en crudo.
3. Ve a la pestaña `Actions` → «Publicar el sitio» → **Run workflow**, para lanzarlo la
   primera vez sin esperar a un push.

El workflow dispara con push a `main` y a `claude/revisar-especificacion-ukp7rd`, que es la
rama por defecto actual. **Si renombras la rama principal, cámbialo también en
`.github/workflows/sitio.yml`** o el sitio dejará de publicarse sin avisar.

La dirección queda en `https://alvar0suarez.github.io/AI_operator_v2/`.

## Camino B — Cloudflare Pages (sitio + tutor)

Un solo despliegue sirve las dos cosas: el sitio estático y la función en `/api/tutor`.

**1. Crear el proyecto.** En Cloudflare → Workers & Pages → Pages → conectar este
repositorio. Configuración de compilación:

| Campo | Valor |
|---|---|
| Comando de compilación | `pip install -r requirements.txt && python3 scripts/generar-glosario.py && python3 scripts/empaquetar-tutor.py && python3 scripts/construir-sitio.py && mkdocs build -f sitio/mkdocs.yml` |
| Directorio de salida | `sitio/build` |
| Directorio raíz | (vacío) |

**2. La clave.** En Settings → Environment variables, añadir `ANTHROPIC_API_KEY`.
Marcarla como **secreta**. No va en ningún fichero del repositorio, ni en el HTML, ni en
una variable de build que acabe en el cliente.

**3. El registro de preguntas (opcional, §7.4).** Crear un KV namespace y enlazarlo al
proyecto con el nombre `REGISTRO_PREGUNTAS`. Si no se hace, el tutor funciona igual y no
registra nada.

`functions/api/tutor.js` ya está en la raíz, que es donde Cloudflare lo busca; el código
de verdad sigue en `tutor/serverless/`.

### Antes de encender el tutor

```bash
cd tutor/serverless && npm install && node --test "pruebas/*.test.mjs"
```

Dieciocho pruebas. Las dos primeras comprueban que ninguna solución de ejercicio puede
llegar al contexto del tutor. **Si esas fallan, no se despliega**: el curso habría
perdido su corrector objetivo.

---

## Qué NO hay, a propósito

**No hay cuentas ni contraseñas.** §8 dice que el estado de progreso vive en el
almacenamiento del navegador. Consecuencia real, y está dicha en la propia página
«Dónde vas»: si abre el curso en el móvil, empieza en blanco. Por eso esa página tiene
un cuadro para copiar el estado y pegarlo en el otro dispositivo.

Montar cuentas exigiría base de datos, recuperación de contraseña y una política de
privacidad, y añadiría un problema de datos personales a un curso que precisamente
enseña a no tenerlos. Si algún día hace falta sincronizar de verdad, es un backend
mínimo con un identificador aleatorio, no un sistema de usuarios.

**Sus artefactos y su bitácora no se guardan aquí.** Son ficheros suyos, en su ordenador
(§8). El curso le da las plantillas y las rúbricas; los documentos son de ella y no
pasan por ningún servidor nuestro. Eso es deliberado y conviene decírselo.

**No hay analítica.** Ni Google Analytics ni nada parecido. El curso no necesita saber
cuánto tarda, y ella no necesita que la midan sin pedirlo.

---

## Qué mirar durante el piloto

Lo único que hay que recoger, y ya está implementado:

- **El registro de preguntas** (§7.4). Es el input directo para escribir el bloque 4.
  Sin él, el bloque 4 se escribe a ciegas y la especificación dice que no se haga.
- **Su bitácora.** Los atascos anotados y los minutos.
- **Dónde abandona**, si abandona. §9 apunta al bloque 1 como el riesgo.

Con eso se escribe la fase 5.
