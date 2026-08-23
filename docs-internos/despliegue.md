# Despliegue — cómo llega el curso a ella

El repositorio no es el entregable. El entregable es **una dirección web** que ella abre
en el móvil o en el portátil, sin instalar nada, sin cuenta y sin contraseña.

Hay dos caminos. La diferencia entre ellos es **una sola cosa**: si el tutor funciona.

| | Sitio | Tutor | Cuenta que hace falta |
|---|---|---|---|
| **GitHub Pages** | sí | **no** | ninguna, ya tienes el repo |
| **Cloudflare Pages** | sí | **sí** | una gratuita de Cloudflare |

Los nodos, los ejercicios, los sabotajes, el dataset, las plantillas y la página de
progreso funcionan igual en los dos. El tutor necesita ejecutar código en servidor —para
que la clave de API no esté en el navegador (§7.5)— y GitHub Pages no ejecuta nada.

> **Para el piloto, GitHub Pages basta.** El tutor es la fase 4 y se puede encender
> después. Si sale sin tutor, el widget lo dice con todas las letras en vez de fingir un
> error.

---

## Camino A — GitHub Pages (sitio solo)

Ya está todo escrito en `.github/workflows/sitio.yml`. Solo hay que encenderlo:

1. En GitHub: **Settings → Pages → Source: GitHub Actions**.
2. Fusiona esta rama en la principal (o cambia la rama del workflow).

En cada push se valida el grafo, se comprueba que las cinco verdades escondidas siguen
siendo derivables, se construye el sitio en modo estricto y se comprueba que
`SOLUCIONES/` no se ha colado. Si algo de eso falla, **no publica**.

La dirección queda en `https://<usuario>.github.io/<repositorio>/`.

---

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
