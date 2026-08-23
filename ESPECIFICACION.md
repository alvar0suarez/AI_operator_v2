# Especificación maestra — Programa "CX + IA"

> Documento de diseño para construir el curso con Claude Code.
> Este fichero es la **fuente de verdad conceptual**. El repositorio implementa esto; si algo en el código contradice este documento, gana este documento hasta que se actualice explícitamente.

---

## 0. Resumen ejecutivo

Programa autodidacta, autocontenido y profundo para una profesional de atención al cliente / customer experience en una PyME, con nivel actual de "usuaria de chatbot". El objetivo no es que aprenda herramientas de IA: es que adquiera el **criterio para ver su trabajo como procesos, decidir qué delegar a una máquina, verificar lo que la máquina produce, y rediseñar cómo se trabaja**. La IA es el instrumento; el pensamiento sistemático y el dominio de CX son la materia.

**Tesis central del diseño:** el 70% del contenido debe seguir siendo válido dentro de tres años. Todo lo que caduque va etiquetado como desechable y se enseña al final de cada bloque, nunca al principio.

**Doble track deliberado:** cada ejercicio enseña simultáneamente (a) una habilidad de trabajo con IA y (b) una idea real de customer experience. El mismo dataset sirve para las dos cosas.

---

## 1. Perfil y supuestos

| Dimensión | Estado actual |
|---|---|
| Rol | Atención al cliente / CX ops en PyME |
| Herramientas reales | Excel para casi todo, correo, quizá un CRM básico |
| Nivel IA | Usa un chatbot conversacionalmente; no conoce patrones ni límites |
| Autoridad organizativa | Ninguna para rediseñar procesos. Puede cambiar *su* forma de trabajar |
| Datos disponibles | **Ninguno real.** Todo el curso corre sobre datos sintéticos |
| Tiempo | Estudia después de trabajar. Sesiones de 45–60 min |

**Consecuencias de diseño que se derivan de esto:**

1. No se le puede pedir que suba datos de su empresa. Nunca. El curso funciona al 100% sin ellos.
2. No se le puede prometer "transformarás tu empresa". Se le enseña a hacerlo y a *ganarse el derecho* a proponerlo, que es otra cosa.
3. Cada bloque debe producir una victoria concreta antes de introducir abstracción. Primero el ahorro medido, después el concepto.

---

## 2. Principios pedagógicos (no negociables)

1. **Artefacto sobre lección.** Ningún módulo termina en "has leído". Termina en un fichero, plantilla o proceso que ella conserva y usa.
2. **Concreto → patrón → generalización escrita por ella.** El pensamiento sistemático no transfiere si se enseña en abstracto. Se repite el mismo patrón sobre tres dominios y ella redacta la regla al cierre del módulo.
3. **Tres instancias por patrón:** su sector (CX), otro dominio profesional (gestoría, tienda, clínica), y vida personal.
4. **La verificación es la asignatura troncal.** Producir con IA es fácil; saber si lo producido sirve es la habilidad escasa y la que no caduca.
5. **Fallar es diagnóstico, no fracaso.** Si el modelo no hace la tarea, casi siempre significa que ella no sabía explicar su propio proceso. Esto se le dice **antes** del primer ejercicio.
6. **Regla de parada explícita.** Se enseña a no sobre-construir. La mayoría de tareas de oficina terminan en el nivel 3 de la escalera y eso es un éxito, no una limitación.
7. **Sin gamificación.** El progreso se demuestra con minutos ahorrados medidos y con el portfolio. No con insignias.

---

## 3. Arquitectura del programa

Seis bloques. 17 semanas nominales, ritmo flexible.

**Estrategia de construcción: los bloques 1–3 se escriben, se publican y se pilotan ANTES de escribir el 4.** El bloque 4 se diseña mucho mejor sabiendo dónde se atascó de verdad.

### Capa transversal (presente en todos los bloques, nunca como módulo suelto)

- Criterio sobre qué **no** delegar
- Lectura de riesgo (¿qué pasa si sale mal 1 de cada 20 veces?)
- Pensamiento en sistemas: arreglar la causa, no el síntoma
- Ética y protección de datos (RGPD aplicado, no teórico)
- Coste de oportunidad: automatizar algo que no debería existir es peor que no automatizarlo

---

### BLOQUE 1 — Ver el trabajo (2 semanas)

**Sin IA. A propósito.** Es el bloque que más resistencia va a generar y el más importante.

**Objetivos**
- Producir una línea base cuantitativa de su propia semana
- Descomponer una tarea hasta el nivel en que sería explicable a una persona nueva
- Aplicar un filtro de automatizabilidad de forma mecánica

**Contenidos**
- 1.1 Por qué nadie sabe explicar su propio trabajo
- 1.2 El diario de tareas: cómo registrar sin volverse loca (5 días, granularidad de 15 min)
- 1.3 Mapa de la semana: frecuencia × duración × variabilidad
- 1.4 Descomposición: entrada → decisiones → salida → criterio de "bien hecho"
- 1.5 El filtro de automatizabilidad (cuatro preguntas)
- 1.6 Trabajo visible vs. trabajo invisible (interrupciones, contexto, coordinación)

**El filtro de automatizabilidad — las cuatro preguntas**
1. **Volumen:** frecuencia × minutos. Por debajo de ~2h/mes, se aparca.
2. **Explicabilidad:** ¿podrías enseñárselo a alguien nuevo en 10 minutos? Si no → no está lista para delegarse, está lista para **documentarse**. Ese es el paso previo, no un rechazo.
3. **Tolerancia al fallo:** ¿qué pasa si sale mal 1 de cada 20? Separa "borrador interno" de "correo al cliente".
4. **Estabilidad del criterio:** ¿"bien hecho" significa lo mismo el lunes y el jueves? **Esta es la que más gente se salta y la que más automatizaciones mata.**

**Ejercicios**
- E1.1 Diario de 5 días (obligatorio, bloqueante para el resto del curso)
- E1.2 Descomponer una tarea propia hasta que un tercero pudiera ejecutarla
- E1.3 Aplicar el filtro a 10 tareas del diario y ordenarlas
- E1.4 Caso cruzado: descomponer una tarea doméstica recurrente (compra semanal, gestión de facturas del hogar)

**Artefacto:** `inventario-de-procesos.md` — sus tareas priorizadas con las cuatro puntuaciones. Documento vivo que se reutiliza en los bloques 5 y 6.

---

### BLOQUE 2 — Los seis verbos (3 semanas)

Resuelve el problema real: **la gente no automatiza lo que no sabe que es automatizable.** No es fallo de pensamiento crítico, es falta de imaginación informada. Se le da un mapa de lo posible en **patrones, no en productos**.

**Los seis verbos**
1. **Clasificar** — meter cosas en categorías (tickets por tipo, correos por urgencia)
2. **Extraer** — sacar datos estructurados de texto desordenado
3. **Transformar** — cambiar de formato manteniendo el contenido
4. **Redactar borrador** — producir un primer texto que ella corrige
5. **Comparar contra criterio** — evaluar algo frente a una norma explícita
6. **Detectar anomalías** — encontrar lo raro en un conjunto

Cada verbo: qué es, cuándo brilla, **cuándo falla y por qué**, tres instancias (CX / otro dominio / vida personal), y un ejercicio sobre el dataset sintético.

**Contenido adicional del bloque**
- 2.7 Verbos compuestos: extraer → clasificar → detectar anomalía
- 2.8 Qué NO es ninguno de los seis verbos (juicio con consecuencias, decisiones con responsabilidad legal, relación humana)

**Artefacto:** `catalogo-de-patrones.md` — los seis verbos con ejemplos propios de su trabajo real escritos por ella.

---

### BLOQUE 3 — Especificar y verificar (3 semanas)

El bloque troncal. Aquí vive la habilidad que no caduca.

**Objetivos**
- Escribir un encargo que un tercero podría ejecutar sin preguntar
- Construir y mantener contexto reutilizable
- Detectar errores en output que ella no ha producido

**Contenidos**
- 3.1 Anatomía de un encargo: objetivo, contexto, restricciones, formato, criterio de aceptación
- 3.2 El error de la especificación implícita (todo lo que "se da por hecho" en su oficina)
- 3.3 Ficheros de contexto: glosario propio, criterios de tono, plantillas, casuística
- 3.4 **Ejercicios de sabotaje** (ver §5)
- 3.5 Modos de fallo típicos: dato inventado, tono inadecuado, generalización falsa, omisión silenciosa, seguridad excesiva
- 3.6 Verificación proporcional al riesgo: no todo se revisa igual
- 3.7 **Datos y RGPD** — qué no se pega jamás en una herramienta, cómo anonimizar antes, por qué en una PyME esto es un marrón real y no una formalidad

**Artefacto:** `plantilla-de-verificacion.md` — su checklist por tipo de tarea, calibrado por riesgo. Y su primer `contexto-trabajo.md`.

---

### BLOQUE 4 — CX como disciplina (4 semanas)

El bloque que la diferencia de cualquiera que haya hecho un curso de IA. Aquí la IA es la lupa, no el tema.

**Contenidos**
- 4.1 Taxonomías de incidencia: cómo se construye una y por qué la mayoría están mal
- 4.2 Análisis de causa raíz sobre volumen real de tickets
- 4.3 **Contacto evitable**: el concepto más rentable del sector. Cada ticket que no debería haber existido
- 4.4 Coste real de un contacto (directo, indirecto, y coste de la insatisfacción)
- 4.5 Métricas: por qué el NPS a solas es casi inútil, qué es CES, tasa de resolución en primer contacto, tiempo de ciclo
- 4.6 Diseño de respuesta bajo carga emocional: reconocimiento, claridad, siguiente paso
- 4.7 Escalado y excepciones: diseñar el camino del caso raro
- 4.8 Del síntoma al sistema: cómo se convierte un patrón de tickets en un cambio de proceso
- 4.9 Voz del cliente: convertir texto libre en decisión

**Ejercicio central del bloque:** análisis completo de los 800 tickets del dataset sintético. Ella debe llegar sola a la concentración de causa raíz plantada en los datos.

**Artefacto:** `informe-causa-raiz.md` — un informe ejecutivo de una página con hallazgo, evidencia, coste estimado y recomendación. Es también la pieza que enseñará en el bloque 6.

---

### BLOQUE 5 — Construir (3 semanas)

**La escalera de implementación**

| Nivel | Qué es | Cuándo parar aquí |
|---|---|---|
| 1 | Conversación suelta | Tareas únicas o exploratorias |
| 2 | Encargo guardado y reutilizable | Tarea recurrente, criterio estable |
| 3 | Encargo + fichero de contexto | **Aquí termina la mayoría de tareas de oficina. Es un éxito.** |
| 4 | Proceso en pasos con verificación intermedia | Volumen alto, varios pasos encadenados |
| 5 | Ejecución sin ella en el bucle | Riesgo bajo, criterio muy estable, volumen alto |

**Regla de parada:** no se sube de nivel hasta que el anterior haya funcionado **tres veces seguidas sin retoques**.

**Contenidos**
- 5.1 La escalera y la regla de parada
- 5.2 Del encargo al proceso documentado
- 5.3 Construcción de su fichero de contexto de trabajo
- 5.4 Encadenar pasos y dónde poner los puntos de control humanos
- 5.5 Mantenimiento: qué se rompe con el tiempo y cómo detectarlo
- 5.6 Cuándo desmontar una automatización

**Artefacto:** dos o tres procesos suyos funcionando de verdad, documentados y medidos contra la línea base del bloque 1.

---

### BLOQUE 6 — Mover la organización (2 semanas)

Se estudia ahora aunque se aplique en seis meses. **El cuello de botella para rediseñar procesos no es analítico, es político.**

**Contenidos**
- 6.1 Por qué nadie te ha pedido que rediseñes nada, y qué hacer con eso
- 6.2 Ganarse el derecho: la secuencia evidencia → piloto → propuesta
- 6.3 El caso de negocio en una página
- 6.4 Cómo enseñar una mejora sin que parezca que sobras tú o que sobra un compañero
- 6.5 El miedo del compañero: por qué la resistencia rara vez es técnica
- 6.6 Qué hacer cuando el jefe dice que no (y por qué a veces tiene razón)
- 6.7 Documentar para que sobreviva sin ti

**Artefacto:** su propuesta real de una página, lista para presentar cuando llegue el momento.

---

## 4. El gemelo sintético (dataset)

**Decisión clave del diseño.** Sin datos reales, se construye una PyME ficticia completa. Esto resuelve tres problemas a la vez: no hay riesgo RGPD, hay realismo, y —lo más importante— **como los datos los generamos nosotros, existe respuesta correcta**. Eso permite corrección objetiva sin profesor, algo imposible con datos reales donde nadie sabe la respuesta.

**Empresa:** distribuidora de agua y bebidas a hostelería y particulares, ~300 clientes, 6 empleados. Nombre provisional: *Aguas del Norte*.

**Ficheros a generar**
| Fichero | Contenido | Suciedad deliberada |
|---|---|---|
| `tickets.xlsx` | ~800 tickets, 6 meses | Categorías inconsistentes, campos vacíos, fechas en 3 formatos |
| `bandeja.mbox` o `correos/` | ~200 correos de clientes | Incidencia en el asunto y asunto en el cuerpo, hilos rotos, adjuntos mencionados que no están |
| `clientes.xlsx` | Maestro de 300 clientes | 12 duplicados con grafías distintas, acentos mal codificados, teléfonos en 4 formatos |
| `pedidos.xlsx` | Histórico de pedidos | Devoluciones registradas como pedidos negativos, sin documentar |
| `procedimientos.docx` | Manual interno "oficial" | Desactualizado y contradice lo que se hace de verdad |

**Verdades escondidas (fichero `SOLUCIONES/` fuera del alcance del alumno)**
- ~38% de los tickets provienen de un único fallo de facturación (redondeo en pedidos con descuento)
- 12 clientes duplicados, identificables por dirección + teléfono
- Un pico estacional que parece demanda pero es un error de registro
- Tres clientes que concentran el 22% de las incidencias y son deficitarios
- Un procedimiento del manual que **nadie sigue** y cuya ausencia causa el 9% de los tickets

Cada verdad escondida tiene detrás un principio de CX del bloque 4. No son acertijos, son ejemplos de la disciplina.

**Requisito de generación:** los ficheros deben ser reproducibles desde un script con semilla fija, para poder regenerarlos con variaciones si hiciera falta una segunda vuelta.

---

## 5. Sistema de autoevaluación

El problema central del curso autodidacta: la habilidad más crítica es verificar output que no has producido, y es justo donde una principiante no puede autoevaluarse, porque **el texto malo parece bien**. Cuatro mecanismos que funcionan sin profesor:

### 5.1 Ejercicios de sabotaje
El curso entrega outputs de IA con errores plantados. Ella marca los fallos y luego destapa la solución.

Tipología de sabotaje, con dificultad creciente:
- **Nivel 1 (visible):** dato numérico que no cuadra con la fuente
- **Nivel 2:** tono inadecuado para el destinatario
- **Nivel 3:** dato inventado plausible (una política de devoluciones que no existe)
- **Nivel 4:** omisión silenciosa (falta el caso excepcional)
- **Nivel 5:** conclusión correcta con razonamiento erróneo
- **Nivel 6 (trampa):** output impecable. Si marca errores inexistentes, también aprende algo.

Formato: `ejercicio.md` + `solucion.md` colapsable. Mínimo 4 por bloque a partir del 3.

### 5.2 La realidad como corrector
Preguntas que se responden con hechos, no con sensaciones:
- ¿Lo aceptó el compañero/cliente sin retocar?
- ¿Tuviste que rehacerlo? ¿Cuántas veces?
- Minutos empleados **contra la línea base medida en el bloque 1**

### 5.3 Claves de corrección del dataset
Todo ejercicio analítico sobre el gemelo sintético tiene solución objetiva. Se destapa después del intento, nunca antes, con rúbrica de tres niveles (no llegó / llegó / llegó y encontró algo que no estaba previsto).

### 5.4 Portfolio
Al terminar tiene 6 artefactos reales. Eso es la prueba de progreso y es, literalmente, el material del bloque 6.

### 5.5 Bitácora
Fichero `bitacora.md` propio. Cada sesión: qué intentó, minutos, qué falló, qué aprendió. Es autoevaluación, es material del bloque 6, y es lo que le da sensación de avance sin necesidad de gamificación.

---

## 6. Estructura modular / árbol semántico

Cada unidad de contenido es un **nodo** en markdown con frontmatter. Esto es lo que hace posible tanto la navegación en profundidad como el tutor con IA.

```yaml
---
id: b3-m4-sabotaje
bloque: 3
titulo: "Ejercicios de sabotaje"
tipo: ejercicio          # concepto | ejercicio | caso | artefacto | profundizacion
duracion_min: 45
requisitos: [b3-m1-anatomia-encargo, b2-m1-clasificar]
desbloquea: [b3-m6-verificacion-proporcional]
caduca: bajo             # bajo | medio | alto  (visible para el alumno)
objetivos:
  - "Detectar dato inventado en un output plausible"
  - "Distinguir error de contenido de error de tono"
conceptos: [verificacion, alucinacion, riesgo]
profundizar:
  - id: b3-p1-por-que-alucinan
    titulo: "Por qué los modelos inventan datos"
  - id: b3-p2-verificacion-numerica
    titulo: "Técnicas de verificación numérica rápida"
---
```

**Reglas del árbol**
- Tronco lineal: los 6 bloques en orden, con requisitos que bloquean de verdad (el diario del bloque 1 es bloqueante).
- Ramas de profundización: nodos `tipo: profundizacion` opcionales, colgando de un nodo tronco. Son la respuesta a "esto me interesa, quiero más".
- Todo nodo declara su **caducidad**, visible para la alumna. Le enseña a distinguir lo que está aprendiendo para siempre de lo que está aprendiendo para este año.
- Los conceptos alimentan un glosario global autogenerado y la navegación lateral.

---

## 7. Tutor con IA integrado

**Principio rector: el tutor no da respuestas, da tracción.** Si responde por ella, destruye exactamente la habilidad que el curso construye.

### 7.1 Modos del tutor
| Modo | Qué hace | Restricción dura |
|---|---|---|
| Explícamelo de otra forma | Reformula el concepto del nodo actual | No avanza materia |
| Socrático | Preguntas que la acercan a la respuesta | **Nunca da la solución de un ejercicio** |
| Revisa mi artefacto | Feedback contra la rúbrica del nodo | Señala, no reescribe |
| Genera más práctica | Nuevos ejercicios de sabotaje del mismo tipo | Con su solución oculta |
| Aplícalo a mi caso | Traduce el concepto a una situación suya | Ella describe el caso, no pega datos |

### 7.2 Contexto que se le inyecta
- Nodo actual completo + sus requisitos ya cubiertos
- El glosario del curso
- Los artefactos que ella ya ha producido (si los ha guardado)
- Su bitácora reciente
- **No** las soluciones de los ejercicios del nodo activo

### 7.3 Guardarraíles
- Rechaza dar la solución de un sabotaje antes de que ella lo haya intentado (el estado "intentado" lo marca la propia interfaz)
- Detecta y bloquea pegado de datos que parezcan reales (nombres + teléfonos + emails juntos) con un aviso de RGPD, no con un bloqueo silencioso
- No inventa contenido de curso que no exista: si le preguntan por algo no cubierto, lo dice y sugiere el nodo más cercano

### 7.4 Registro de preguntas
Cada consulta se guarda asociada al nodo: `{nodo_id, pregunta, timestamp, modo}`.

Tres usos:
1. Ella ve su propio histórico de dudas por nodo — es una forma de progreso muy real
2. Tú ves dónde se atasca la gente → es el input directo para escribir el bloque 4
3. Las preguntas repetidas se promueven a nodos de profundización permanentes

### 7.5 Nota técnica
La llamada a la API va **siempre** a través de una función servidor (serverless), nunca desde el navegador: la clave no puede estar en el cliente. Consultar los identificadores de modelo actuales y los parámetros en la documentación oficial antes de implementar, no asumirlos:
- API: https://docs.claude.com/en/api/overview
- Mapa de docs: https://docs.claude.com/en/docs_site_map.md

---

## 8. Stack e implementación

**Recomendación:** markdown en el repositorio como fuente de verdad + sitio estático generado. Nada de plataforma LMS ni app nativa: multiplica el trabajo y no aporta a este perfil.

- **Contenido:** markdown con frontmatter (§6)
- **Sitio:** generador estático con buena navegación, búsqueda y lectura en móvil (MkDocs Material es la opción de menor fricción; Astro si se quiere más control sobre el tutor)
- **Tutor:** función serverless que proxea la API
- **Persistencia del alumno:** su bitácora y artefactos viven en ficheros suyos; el estado de progreso, en almacenamiento del navegador o en un backend mínimo si se quiere sincronizar entre dispositivos
- **Validación:** script que verifica el grafo de requisitos (sin ciclos, sin referencias rotas, todo nodo alcanzable)

### Estructura de repositorio propuesta

```
/contenido
  /bloque-1  ... /bloque-6
    b1-m1-*.md
    /profundizacion
  /glosario
/dataset
  /generador          # script con semilla fija
  /ficheros           # los .xlsx, correos, docx
  /SOLUCIONES         # excluido del build público
/ejercicios
  /sabotaje
    /nivel-1 ... /nivel-6
  /rubricas
/plantillas           # los 6 artefactos en blanco
/tutor
  /prompts            # un fichero por modo
  /guardarrailes
/sitio
/scripts
  validar-grafo.py
  generar-dataset.py
ESPECIFICACION.md     # este documento
```

### Fases de construcción

1. **Fase 0:** esqueleto del repo, esquema de frontmatter, validador del grafo, 2 nodos de muestra
2. **Fase 1:** generador del dataset sintético con las verdades escondidas documentadas
3. **Fase 2:** bloques 1–3 completos con ejercicios y artefactos
4. **Fase 3:** sitio estático navegable en móvil
5. **Fase 4:** tutor con los 5 modos y guardarraíles
6. **— PILOTO CON ELLA —** los bloques 1–3 se prueban de verdad antes de continuar
7. **Fase 5:** bloque 4 (CX), diseñado con lo aprendido en el piloto
8. **Fase 6:** bloques 5–6

---

## 9. Riesgos del diseño y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Abandona en el bloque 1 (sin IA, poco gratificante) | Acortarlo a lo mínimo viable; una victoria pequeña con IA al final de la semana 1 como anticipo |
| El dataset sintético se siente artificial | Suciedad realista, y que las verdades escondidas requieran cruzar dos ficheros |
| El tutor se convierte en muleta | Guardarraíles duros; el modo socrático como predeterminado |
| 17 semanas es demasiado | Bloques independientes; cada uno vale por sí solo. El 1+2+3 ya es un curso completo |
| Aprende el proceso pero no consigue aplicarlo en su empresa | Bloque 6, y expectativas honestas desde la primera página |
| El contenido caduca | Etiqueta de caducidad por nodo; lo de nivel `alto` está aislado y es sustituible sin tocar el resto |

---

## 10. Criterio de éxito

No es que termine el curso. Es que, seis meses después:

1. Cuando le cae una tarea nueva, la descompone antes de hacerla
2. Nunca acepta un output sin verificarlo, y sabe *cuánto* verificar según el riesgo
3. Ha eliminado al menos un proceso en lugar de acelerarlo
4. Puede explicar a su jefe, con números, por qué algo debería cambiar
5. Cuando salga una herramienta nueva, la evalúa en diez minutos porque sabe qué está buscando
