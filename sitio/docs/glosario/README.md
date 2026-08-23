<!-- FICHERO GENERADO. No lo edites a mano: se sobreescribe.
     Fuente: contenido/glosario/glosario.yml
     Generador: scripts/generar-glosario.py -->

# Glosario

Las 106 palabras que usa este curso, con un ejemplo cada una y los nodos donde aparecen. Está ordenado alfabéticamente, así que se puede leer de golpe o consultar suelto.

Cada entrada dice también en qué bloque aparece por primera vez. Si un término te suena a chino y su bloque de origen es posterior al que estás haciendo, déjalo: te lo vas a encontrar explicado a su debido tiempo.

## Índice

**A** · [Alcance](#alcance), [Alucinación](#alucinacion), [Anomalía](#anomalia), [Anonimizar](#anonimizar), [Artefacto](#artefacto), [Autoridad](#autoridad)

**B** · [Bitácora](#bitacora), [Borrador](#borrador)

**C** · [Cadena](#cadena), [Caducidad](#caducidad), [Caso de negocio](#caso-de-negocio), [Casuística](#casuistica), [Catálogo de patrones](#catalogo), [Causa raíz](#causa-raiz), [CES (esfuerzo del cliente)](#ces), [Checklist](#checklist), [Claridad](#claridad), [Clasificar](#clasificar), [Comparar contra criterio](#comparar), [Conocimiento tácito](#conocimiento-tacito), [Contacto evitable](#contacto-evitable), [Contexto](#contexto), [Coste de arranque](#coste-de-arranque), [Coste de coordinación](#coste-de-coordinacion), [Coste de la insatisfacción](#insatisfaccion), [Coste de oportunidad](#coste-de-oportunidad), [Coste de un contacto](#coste-de-contacto), [Coste de verificar](#coste-de-verificar), [Criterio](#criterio), [Criterio de aceptación](#criterio-de-aceptacion), [Cuadre](#cuadre)

**D** · [Dato estructurado](#dato-estructurado), [Dato personal](#dato-personal), [Decisión](#decision), [Deriva](#deriva), [Descomposición](#descomposicion), [Diagnóstico](#diagnostico), [Doble track](#doble-track), [Documentación](#documentacion)

**E** · [Encargo](#encargo), [Escalado](#escalado), [Escalera de implementación](#escalera), [Especificación implícita](#especificacion-implicita), [Estabilidad del criterio](#estabilidad-del-criterio), [Evidencia](#evidencia), [Excepción](#excepcion), [Explicabilidad](#explicabilidad), [Extraer](#extraer)

**F** · [Formato](#formato), [Frecuencia](#frecuencia)

**G** · [Generalización falsa](#generalizacion-falsa), [Glosario propio](#glosario), [Granularidad](#granularidad)

**H** · [Herramienta](#herramienta)

**I** · [Imaginación informada](#imaginacion-informada), [Interrupción](#interrupcion), [Inventario de procesos](#inventario)

**J** · [Juicio](#juicio)

**L** · [Línea base](#linea-base)

**M** · [Mantenimiento](#mantenimiento)

**N** · [Nivel de implementación](#nivel), [Normalidad](#normalidad), [NPS](#nps)

**O** · [Objetivo](#objetivo), [Omisión silenciosa](#omision), [Orden de magnitud](#orden-de-magnitud)

**P** · [Patrón](#patron), [Pérdida de información](#perdida-de-informacion), [Piloto](#piloto), [Plantilla](#plantilla), [Plausibilidad](#plausibilidad), [Política organizativa](#politica-organizativa), [Proceso](#proceso), [Propuesta](#propuesta), [Punto de control](#punto-de-control)

**Q** · [Qué no delegar](#no-delegar)

**R** · [Reconocimiento](#reconocimiento), [Regla de parada](#regla-de-parada), [Reidentificación](#reidentificacion), [Relación](#relacion), [Resistencia](#resistencia), [Resolución en primer contacto](#resolucion-primer-contacto), [Responsabilidad](#responsabilidad), [Responsable del tratamiento](#responsable-del-tratamiento), [Restricción](#restriccion), [Reutilización](#reutilizacion), [Reversibilidad](#reversibilidad), [RGPD](#rgpd), [Riesgo](#riesgo), [Rúbrica](#rubrica)

**S** · [Seguridad excesiva](#seguridad-excesiva), [Siguiente paso](#siguiente-paso), [Sistema](#sistema)

**T** · [Taxonomía](#taxonomia), [Tiempo de ciclo](#tiempo-de-ciclo), [Tolerancia al fallo](#tolerancia-al-fallo), [Tono](#tono), [Trabajo invisible](#trabajo-invisible), [Transferencia](#transferencia), [Transformar](#transformar), [Tutor](#tutor)

**V** · [Variabilidad](#variabilidad), [Verbo](#verbo), [Verificación](#verificacion), [Volumen](#volumen), [Voz del cliente](#voz-del-cliente)

---

<a id="alcance"></a>

### Alcance

Cuánta gente y cuántos casos toca lo que has producido. Un borrador que lee una persona y una circular que sale a 300 clientes no merecen la misma revisión.

**Ejemplo.** La misma plantilla de respuesta sirve para contestar a un cliente concreto o para el correo mensual de Aguas del Norte a sus 300 clientes. En el segundo caso se lee palabra por palabra, aunque sea el mismo texto.

**Ver también:** [Riesgo](#riesgo), [Reversibilidad](#reversibilidad), [Verificación](#verificacion)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Verificación proporcional al riesgo](../bloque-3/b3-m6-verificacion-proporcional.md)

---

<a id="alucinacion"></a>

### Alucinación

Un dato inventado que el sistema presenta con la misma seguridad que uno correcto. No hay señal de aviso: el texto sale igual de bien escrito con el dato cierto que con el falso.

**Ejemplo.** Le pides las condiciones de devolución de Aguas del Norte y te contesta que el plazo es de 14 días naturales. Ese plazo no está en ningún procedimiento de la empresa: lo ha rellenado porque encajaba.

**Ver también:** [Plausibilidad](#plausibilidad), [Verificación](#verificacion), [Omisión silenciosa](#omision)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Ejercicios de sabotaje](../bloque-3/b3-m4-sabotaje.md)
- Bloque 3 — [Los cinco modos de fallo típicos](../bloque-3/b3-m5-modos-de-fallo.md)
- Bloque 3 — [Por qué los modelos inventan datos](../bloque-3/profundizacion/b3-p1-por-que-alucinan.md) *(profundización)*

---

<a id="anomalia"></a>

### Anomalía

Un caso que se sale de lo que habías definido como normal. Sin definición previa de normalidad no hay anomalías, solo cosas que te llaman la atención.

**Ejemplo.** En `pedidos.xlsx` aparecen líneas con cantidad negativa. Son devoluciones que nadie marcó como tales, y rompen cualquier suma hecha a la ligera.

**Ver también:** [Normalidad](#normalidad), [Causa raíz](#causa-raiz), [Patrón](#patron)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 6: detectar anomalías](../bloque-2/b2-m7-detectar-anomalias.md)
- Bloque 2 — [Una anomalía no es un error](../bloque-2/profundizacion/b2-p4-anomalia-no-es-error.md) *(profundización)*
- Bloque 4 — [Análisis completo de los 800 tickets](../bloque-4/b4-m10-analisis-completo.md)
- Bloque 4 — [Análisis de causa raíz](../bloque-4/b4-m2-causa-raiz.md)

---

<a id="anonimizar"></a>

### Anonimizar

Quitar de un texto lo que permite saber de quién habla, antes de pegarlo en ninguna herramienta. Sustituir el nombre no basta: hay que quitar también lo que identifica por cruce.

**Ejemplo.** Antes de pedir ayuda con una reclamación cambias "Bar Manolo, C/ Alta 14, Santoña" por "CLIENTE_01" y borras el importe exacto, que por sí solo señala a un único pedido.

**Ver también:** [Dato personal](#dato-personal), [Reidentificación](#reidentificacion), [RGPD](#rgpd)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Datos y RGPD: qué no se pega jamás](../bloque-3/b3-m7-datos-y-rgpd.md)
- Bloque 3 — [Anonimizar de verdad, en dos minutos](../bloque-3/profundizacion/b3-p4-anonimizar-en-la-practica.md) *(profundización)*

---

<a id="artefacto"></a>

### Artefacto

El fichero, plantilla o proceso que te queda al terminar un módulo y que sigues usando después. Es la prueba de que el módulo sirvió para algo.

**Ejemplo.** El inventario de procesos del bloque 1: tus tareas con frecuencia, duración y las cuatro puntuaciones del filtro. Lo vuelves a abrir en el bloque 5 para medir cuánto has ahorrado de verdad.

**Ver también:** [Inventario de procesos](#inventario), [Catálogo de patrones](#catalogo), [Bitácora](#bitacora)

**Aparece en** (bloque de origen: 0):

- Bloque 0 — [Qué es este curso y qué no es](../bloque-0/b0-m1-que-es-este-curso.md)
- Bloque 0 — [Cómo se usa este repositorio](../bloque-0/b0-m2-como-usar-esto.md)

---

<a id="autoridad"></a>

### Autoridad

El permiso, formal o tácito, para cambiar cómo se trabaja. Tu forma de trabajar la cambias mañana; la de los demás requiere que alguien te lo conceda.

**Ejemplo.** Puedes reorganizar hoy mismo cómo contestas tú los correos de facturación. Cambiar el procedimiento de facturación de la empresa pasa por gerencia, y por eso el bloque 6 va de evidencia y no de tener razón.

**Ver también:** [Política organizativa](#politica-organizativa), [Evidencia](#evidencia), [Propuesta](#propuesta)

**Aparece en** (bloque de origen: 6):

- Bloque 6 — [Nadie te ha pedido que rediseñes nada](../bloque-6/b6-m1-nadie-te-lo-ha-pedido.md)

---

<a id="bitacora"></a>

### Bitácora

Tu registro por sesión: qué intentaste, cuántos minutos, qué falló y qué aprendiste. Convierte una sensación de avance en un dato que se puede enseñar.

**Ejemplo.** "Martes: borrador de respuesta a una reclamación por garrafas rotas. 9 min contra los 20 que tenía anotados en el diario. Se inventó un plazo de devolución; lo corregí antes de enviar."

**Ver también:** [Línea base](#linea-base), [Artefacto](#artefacto), [Diagnóstico](#diagnostico)

**Aparece en** (bloque de origen: 0):

- Bloque 0 — [Cómo se usa este repositorio](../bloque-0/b0-m2-como-usar-esto.md)
- Bloque 0 — [Abre tu bitácora](../bloque-0/b0-m4-tu-bitacora.md)

---

<a id="borrador"></a>

### Borrador

Un primer texto que existe para que tú lo corrijas, no para enviarse. Su valor está en quitarte el folio en blanco, no en acertar a la primera.

**Ejemplo.** Pides un primer texto de respuesta al bar que se queja del cuarto retraso en su ruta. Reescribes la mitad, pero has tardado 6 minutos en lugar de 18.

**Ver también:** [Coste de arranque](#coste-de-arranque), [Tono](#tono), [Verificación](#verificacion)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 4: redactar borrador](../bloque-2/b2-m5-redactar-borrador.md)
- Bloque 2 — [Por qué el valor está en el borrador cero](../bloque-2/profundizacion/b2-p3-el-borrador-cero.md) *(profundización)*

---

<a id="cadena"></a>

### Cadena

Varios verbos ejecutados uno detrás de otro, donde la salida de cada paso es la entrada del siguiente. El error no se queda quieto: se arrastra y se multiplica.

**Ejemplo.** Extraer los datos de 200 correos, clasificarlos por tipo de incidencia y buscar lo raro. Si cada paso acierta el 90%, al final del tercero no te queda un 90%.

**Ver también:** [Punto de control](#punto-de-control), [Verbo](#verbo), [Verificación](#verificacion)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbos compuestos: encadenar sin perder el hilo](../bloque-2/b2-m8-verbos-compuestos.md)
- Bloque 5 — [Encadenar pasos y poner los controles humanos](../bloque-5/b5-m4-encadenar-y-controles.md)

---

<a id="caducidad"></a>

### Caducidad

Cuánto va a durar lo que estás aprendiendo en un nodo, declarado en tres niveles: bajo, medio y alto. Está a la vista para que sepas a qué merece la pena dedicarle memoria.

**Ejemplo.** "Descomponer una tarea en entrada, decisiones, salida y criterio" es caducidad baja. "Qué herramientas hay ahora mismo en el mercado" es alta, y por eso va al final del bloque y no al principio.

**Ver también:** [Herramienta](#herramienta), [Patrón](#patron), [Verbo](#verbo)

**Aparece en** (bloque de origen: 0):

- Bloque 0 — [Cómo se usa este repositorio](../bloque-0/b0-m2-como-usar-esto.md)
- Bloque 2 — [Apéndice desechable: cómo está el panorama ahora mismo](../bloque-2/profundizacion/b2-p5-herramientas-hoy.md) *(profundización)*

---

<a id="caso-de-negocio"></a>

### Caso de negocio

Una página que dice qué pasa hoy, cuánto cuesta, qué propones y qué se ahorra, con los números a la vista. No es una presentación: es un argumento que cualquiera puede comprobar.

**Ejemplo.** "304 de los 800 tickets del semestre salen de un fallo de redondeo. A 11 € por contacto son 3.344 €. Corregir el cálculo es media mañana de trabajo del informático."

**Ver también:** [Evidencia](#evidencia), [Coste de un contacto](#coste-de-contacto), [Propuesta](#propuesta)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [Tu informe de causa raíz](../bloque-4/b4-m11-informe-causa-raiz.md)
- Bloque 6 — [El caso de negocio en una página](../bloque-6/b6-m3-caso-de-negocio.md)
- Bloque 6 — [Tu propuesta de una página](../bloque-6/b6-m8-propuesta-de-una-pagina.md)

---

<a id="casuistica"></a>

### Casuística

La lista de los casos raros de tu trabajo con el tratamiento que le das a cada uno. Es la parte del contexto que nadie escribe y que decide la mitad de las respuestas.

**Ejemplo.** "Si el cliente es de la ruta 4 y pide entrega en martes, no se puede: se le ofrece el jueves." Eso vive en tu cabeza; en un fichero de contexto vive por escrito y deja de depender de que estés tú.

**Ver también:** [Contexto](#contexto), [Excepción](#excepcion), [Especificación implícita](#especificacion-implicita)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Ficheros de contexto: glosario, tono, plantillas, casuística](../bloque-3/b3-m3-ficheros-de-contexto.md)
- Bloque 3 — [Tu primer fichero de contexto de trabajo](../bloque-3/b3-m9-contexto-trabajo.md)
- Bloque 5 — [Construir tu fichero de contexto de trabajo](../bloque-5/b5-m3-contexto-de-trabajo.md)

---

<a id="catalogo"></a>

### Catálogo de patrones

Tu colección de los seis verbos con ejemplos sacados de tu propio trabajo. Sirve para reconocer, cuando llega una tarea nueva, de qué tipo es en realidad.

**Ejemplo.** En la fila "comparar contra criterio" escribes "revisar que los presupuestos que manda Rubén lleven las condiciones de pago". Hasta ese momento eso era "revisar cosas".

**Ver también:** [Verbo](#verbo), [Inventario de procesos](#inventario), [Artefacto](#artefacto)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Tu catálogo de patrones](../bloque-2/b2-m10-catalogo-de-patrones.md)

---

<a id="causa-raiz"></a>

### Causa raíz

El fallo de fondo que produce muchos síntomas distintos. Se reconoce por una prueba: si lo arreglas, desaparece un montón de trabajo de golpe.

**Ejemplo.** 304 tickets de Aguas del Norte hablan de facturas que no cuadran. La causa raíz no son 304 clientes quisquillosos: es un redondeo al alza del precio unitario en los pedidos con descuento.

**Ver también:** [Sistema](#sistema), [Contacto evitable](#contacto-evitable), [Anomalía](#anomalia)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Una anomalía no es un error](../bloque-2/profundizacion/b2-p4-anomalia-no-es-error.md) *(profundización)*
- Bloque 4 — [Análisis completo de los 800 tickets](../bloque-4/b4-m10-analisis-completo.md)
- Bloque 4 — [Tu informe de causa raíz](../bloque-4/b4-m11-informe-causa-raiz.md)
- Bloque 4 — [Análisis de causa raíz](../bloque-4/b4-m2-causa-raiz.md)
- Bloque 4 — [Contacto evitable](../bloque-4/b4-m3-contacto-evitable.md)
- Bloque 4 — [Del síntoma al sistema](../bloque-4/b4-m8-del-sintoma-al-sistema.md)

---

<a id="ces"></a>

### CES (esfuerzo del cliente)

Una medida del esfuerzo que le ha costado al cliente resolver su asunto, preguntada justo al cerrarlo. Predice si va a volver a contactar mejor que la satisfacción declarada, aunque solo habla del episodio y no de la relación.

**Ejemplo.** Al cerrar una incidencia de facturación preguntas: "¿cuánto esfuerzo le ha costado resolver esto?". Si contesta que mucho, volverá a llamar el mes que viene aunque diga que está satisfecho.

**Ver también:** [NPS](#nps), [Resolución en primer contacto](#resolucion-primer-contacto), [Contacto evitable](#contacto-evitable)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [Métricas que dicen algo](../bloque-4/b4-m5-metricas.md)

---

<a id="checklist"></a>

### Checklist

La lista corta de comprobaciones que aplicas a un tipo de tarea, siempre las mismas y en el mismo orden. Si no cabe en una pantalla, no la vas a usar.

**Ejemplo.** Para una tabla extraída de correos: ¿cuadra el número de filas?, ¿cuántos campos han quedado vacíos?, ¿coinciden la primera y la última fila con el correo original?

**Ver también:** [Verificación](#verificacion), [Rúbrica](#rubrica), [Criterio de aceptación](#criterio-de-aceptacion)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Tu plantilla de verificación](../bloque-3/b3-m8-plantilla-de-verificacion.md)

---

<a id="claridad"></a>

### Claridad

Que el cliente entienda a la primera qué ha pasado y qué va a pasar ahora. Se mide en si vuelve a preguntar lo mismo, no en lo bien escrito que quedó el correo.

**Ejemplo.** "Estamos revisando su incidencia" no aclara nada. "Le hemos cobrado 4,30 € de más en la factura de enero y se los abonamos en la de febrero" sí.

**Ver también:** [Reconocimiento](#reconocimiento), [Siguiente paso](#siguiente-paso), [Tono](#tono)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [Responder bajo carga emocional](../bloque-4/b4-m6-respuesta-bajo-carga-emocional.md)

---

<a id="clasificar"></a>

### Clasificar

Asignar a cada elemento de un conjunto una categoría de una lista cerrada. Todos reciben una, y solo una.

**Ejemplo.** Repartir los 800 tickets entre las ocho categorías reales de incidencia. Es distinto de buscar: buscar te trae los de facturación y deja el resto del montón sin tocar.

**Ver también:** [Taxonomía](#taxonomia), [Verbo](#verbo), [Criterio](#criterio)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 1: clasificar](../bloque-2/b2-m2-clasificar.md)
- Bloque 2 — [Clasificar no es buscar](../bloque-2/profundizacion/b2-p1-clasificar-vs-buscar.md) *(profundización)*
- Bloque 4 — [Taxonomías de incidencia](../bloque-4/b4-m1-taxonomias.md)
- Bloque 4 — [Voz del cliente: de texto libre a decisión](../bloque-4/b4-m9-voz-del-cliente.md)

---

<a id="comparar"></a>

### Comparar contra criterio

Evaluar algo frente a una norma escrita. La palabra que sostiene el verbo es "escrita": sin criterio explícito esto degenera en opinión con aire de autoridad.

**Ejemplo.** Contrastas veinte respuestas enviadas a clientes contra el procedimiento PR-08 de reclamaciones. De paso descubres que el procedimiento es de 2019 y ya no describe lo que hacéis.

**Ver también:** [Criterio](#criterio), [Rúbrica](#rubrica), [Verbo](#verbo)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 5: comparar contra criterio](../bloque-2/b2-m6-comparar-contra-criterio.md)

---

<a id="conocimiento-tacito"></a>

### Conocimiento tácito

Lo que sabes hacer y no sabes explicar. Cuanto mejor haces una tarea, más automática se te ha vuelto y menos capaz eres de describirla.

**Ejemplo.** Sabes en dos segundos qué reclamación pasa a gerencia y cuál no. Cuando intentas escribir la regla te salen tres "depende" seguidos.

**Ver también:** [Descomposición](#descomposicion), [Especificación implícita](#especificacion-implicita), [Explicabilidad](#explicabilidad)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Por qué nadie sabe explicar su propio trabajo](../bloque-1/b1-m1-nadie-sabe-explicar-su-trabajo.md)
- Bloque 1 — [Descomponer: entrada, decisiones, salida, criterio](../bloque-1/b1-m4-descomposicion.md)
- Bloque 3 — [Todo lo que en tu oficina se da por hecho](../bloque-3/b3-m2-especificacion-implicita.md)

---

<a id="contacto-evitable"></a>

### Contacto evitable

Un contacto que no debería haber existido porque algo falló antes: una factura mal calculada, un aviso que no se dio, una información que no estaba donde tocaba. Es el concepto más rentable del sector porque cada uno que eliminas no vuelve.

**Ejemplo.** Los 72 tickets de "vinisteis y estaba cerrado" de Aguas del Norte. El procedimiento PR-07 obliga a avisar la víspera y nadie avisa: ninguna de esas 72 llamadas tenía que haberse producido.

**Ver también:** [Causa raíz](#causa-raiz), [Coste de un contacto](#coste-de-contacto), [Sistema](#sistema)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [Análisis completo de los 800 tickets](../bloque-4/b4-m10-analisis-completo.md)
- Bloque 4 — [Contacto evitable](../bloque-4/b4-m3-contacto-evitable.md)
- Bloque 4 — [Del síntoma al sistema](../bloque-4/b4-m8-del-sintoma-al-sistema.md)

---

<a id="contexto"></a>

### Contexto

La información de fondo que hace falta para ejecutar bien un encargo y que en tu oficina se da por sabida. Escrita una vez en un fichero, deja de reexplicarse cada vez.

**Ejemplo.** Que aquí "abono" significa nota de crédito y no un pago; que en agosto se reparte con media plantilla; que a un bar de toda la vida no se le escribe "estimado cliente".

**Ver también:** [Especificación implícita](#especificacion-implicita), [Glosario propio](#glosario), [Casuística](#casuistica)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Todo lo que en tu oficina se da por hecho](../bloque-3/b3-m2-especificacion-implicita.md)
- Bloque 3 — [Ficheros de contexto: glosario, tono, plantillas, casuística](../bloque-3/b3-m3-ficheros-de-contexto.md)
- Bloque 3 — [Tu primer fichero de contexto de trabajo](../bloque-3/b3-m9-contexto-trabajo.md)
- Bloque 5 — [Construir tu fichero de contexto de trabajo](../bloque-5/b5-m3-contexto-de-trabajo.md)

---

<a id="coste-de-arranque"></a>

### Coste de arranque

Lo que cuesta empezar algo, separado de lo que cuesta hacerlo. En redactar es la mayor parte del coste, y por eso un borrador imperfecto ahorra tiempo de verdad.

**Ejemplo.** Contestar una reclamación te lleva 18 minutos, de los cuales 11 son mirar la pantalla decidiendo por dónde empezar.

**Ver también:** [Borrador](#borrador), [Línea base](#linea-base), [Coste de oportunidad](#coste-de-oportunidad)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Por qué el valor está en el borrador cero](../bloque-2/profundizacion/b2-p3-el-borrador-cero.md) *(profundización)*

---

<a id="coste-de-coordinacion"></a>

### Coste de coordinación

El tiempo que se va en ponerse de acuerdo: preguntar, esperar respuesta, avisar, confirmar. No figura en ninguna tarea y se lleva un trozo grande del día.

**Ejemplo.** Para saber si el pedido del hotel salió el jueves escribes a Chema, esperas veinte minutos y luego contestas al cliente. En tu diario esa tarea pone "consultar estado de pedido: 3 minutos".

**Ver también:** [Trabajo invisible](#trabajo-invisible), [Interrupción](#interrupcion), [Sistema](#sistema)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Trabajo visible y trabajo invisible](../bloque-1/b1-m6-trabajo-visible-invisible.md)
- Bloque 1 — [Lo que cuesta volver a donde estabas](../bloque-1/profundizacion/b1-p3-coste-de-cambio-de-contexto.md) *(profundización)*

---

<a id="insatisfaccion"></a>

### Coste de la insatisfacción

Lo que cuesta un cliente descontento y no aparece en ninguna factura: compra menos, se va, y lo cuenta. Es la parte del coste de contacto que todo el mundo omite porque es la difícil de estimar.

**Ejemplo.** El bar que se cansó de reclamar la misma factura tres meses seguidos no puso ninguna hoja de reclamaciones. Redujo el pedido semanal a la mitad y no dijo nada.

**Ver también:** [Coste de un contacto](#coste-de-contacto), [Contacto evitable](#contacto-evitable), [Voz del cliente](#voz-del-cliente)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [El coste real de un contacto](../bloque-4/b4-m4-coste-de-un-contacto.md)

---

<a id="coste-de-oportunidad"></a>

### Coste de oportunidad

Lo que dejas de hacer por hacer otra cosa. Aplicado aquí: automatizar una tarea que no debería existir es peor que no automatizarla, porque la deja instalada para siempre.

**Ejemplo.** Puedes bajar de 20 a 6 minutos el tiempo de contestar a las quejas de facturación. O puedes arreglar el redondeo y quedarte sin las quejas.

**Ver también:** [Contacto evitable](#contacto-evitable), [Causa raíz](#causa-raiz), [Coste de verificar](#coste-de-verificar)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Mapa de la semana: frecuencia, duración, variabilidad](../bloque-1/b1-m3-mapa-de-la-semana.md)
- Bloque 1 — [Tu inventario de procesos](../bloque-1/b1-m8-inventario-de-procesos.md)
- Bloque 3 — [Verificar de más también es un error](../bloque-3/profundizacion/b3-p5-coste-de-verificar-de-mas.md) *(profundización)*
- Bloque 4 — [El coste real de un contacto](../bloque-4/b4-m4-coste-de-un-contacto.md)
- Bloque 5 — [Cuándo desmontar una automatización](../bloque-5/b5-m6-cuando-desmontar.md)
- Bloque 6 — [Cuando el jefe dice que no (y a veces tiene razón)](../bloque-6/b6-m6-cuando-el-jefe-dice-que-no.md)

---

<a id="coste-de-contacto"></a>

### Coste de un contacto

Lo que le cuesta a la empresa cada interacción de atención: el tiempo de quien la atiende, la parte proporcional de estructura y lo que se pierde por el cliente descontento. Sin este número no hay conversación de negocio posible.

**Ejemplo.** En Aguas del Norte sale a 11 € por contacto. Los 176 tickets de tres clientes de hostelería suman 1.936 € en seis meses, más de lo que esos tres dejan de margen bruto.

**Ver también:** [Contacto evitable](#contacto-evitable), [Coste de la insatisfacción](#insatisfaccion), [Caso de negocio](#caso-de-negocio)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [Análisis completo de los 800 tickets](../bloque-4/b4-m10-analisis-completo.md)
- Bloque 4 — [Tu informe de causa raíz](../bloque-4/b4-m11-informe-causa-raiz.md)
- Bloque 4 — [El coste real de un contacto](../bloque-4/b4-m4-coste-de-un-contacto.md)
- Bloque 6 — [El caso de negocio en una página](../bloque-6/b6-m3-caso-de-negocio.md)

---

<a id="coste-de-verificar"></a>

### Coste de verificar

El tiempo que cuesta comprobar lo producido. Cuenta dentro del ahorro: si revisar línea a línea te lleva más que hacerlo a mano, la automatización es una pérdida disfrazada de modernidad.

**Ejemplo.** Extraer los datos de 40 correos te lleva 5 minutos y comprobarlos uno a uno, 35. A mano eran 30. Has perdido diez minutos y has añadido un riesgo.

**Ver también:** [Verificación](#verificacion), [Riesgo](#riesgo), [Coste de oportunidad](#coste-de-oportunidad)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Verificación proporcional al riesgo](../bloque-3/b3-m6-verificacion-proporcional.md)
- Bloque 3 — [Técnicas de verificación numérica rápida](../bloque-3/profundizacion/b3-p2-verificacion-numerica.md) *(profundización)*
- Bloque 3 — [Verificar de más también es un error](../bloque-3/profundizacion/b3-p5-coste-de-verificar-de-mas.md) *(profundización)*

---

<a id="criterio"></a>

### Criterio

La regla que dice cuándo algo está bien hecho. Es la casilla que más se salta al describir una tarea y la que decide si se puede delegar o no.

**Ejemplo.** "Contestar bien una reclamación" no es un criterio. "Menciona el importe exacto, da una fecha concreta y no promete nada que no esté en el procedimiento" sí lo es.

**Ver también:** [Criterio de aceptación](#criterio-de-aceptacion), [Estabilidad del criterio](#estabilidad-del-criterio), [Descomposición](#descomposicion)

**Aparece en** (bloque de origen: 0):

- Bloque 0 — [Qué es este curso y qué no es](../bloque-0/b0-m1-que-es-este-curso.md)
- Bloque 0 — [Fallar es diagnóstico, no fracaso](../bloque-0/b0-m3-fallar-es-diagnostico.md)
- Bloque 1 — [Descomponer: entrada, decisiones, salida, criterio](../bloque-1/b1-m4-descomposicion.md)
- Bloque 1 — [Caso cruzado: la misma lente en tu casa](../bloque-1/b1-m7-caso-cruzado-domestico.md)
- Bloque 2 — [Verbo 1: clasificar](../bloque-2/b2-m2-clasificar.md)
- Bloque 2 — [Verbo 5: comparar contra criterio](../bloque-2/b2-m6-comparar-contra-criterio.md)
- Bloque 2 — [Clasificar no es buscar](../bloque-2/profundizacion/b2-p1-clasificar-vs-buscar.md) *(profundización)*
- Bloque 4 — [Taxonomías de incidencia](../bloque-4/b4-m1-taxonomias.md)
- Bloque 4 — [Escalado y excepciones](../bloque-4/b4-m7-escalado-y-excepciones.md)

---

<a id="criterio-de-aceptacion"></a>

### Criterio de aceptación

La parte del encargo que dice cómo se comprueba que el resultado sirve. Un criterio útil es el que dos personas distintas aplican por separado y coinciden.

**Ejemplo.** "Que quede profesional" no se puede comprobar. "Máximo 120 palabras, con el número de pedido, sin disculparse dos veces y sin ofrecer compensación" sí.

**Ver también:** [Encargo](#encargo), [Criterio](#criterio), [Rúbrica](#rubrica)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Anatomía de un encargo](../bloque-3/b3-m1-anatomia-encargo.md)
- Bloque 3 — [Escribir un criterio de aceptación que sirva](../bloque-3/profundizacion/b3-p3-criterio-de-aceptacion.md) *(profundización)*

---

<a id="cuadre"></a>

### Cuadre

Comprobar que las partes suman el total y que las cuentas encajan entre sí. Es la verificación numérica más barata que existe y caza la mayoría de los desastres.

**Ejemplo.** El resumen dice 800 tickets; las categorías suman 786. Todavía no sabes dónde están los 14 que faltan, pero ya sabes que el resumen no vale.

**Ver también:** [Verificación](#verificacion), [Orden de magnitud](#orden-de-magnitud), [Omisión silenciosa](#omision)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Técnicas de verificación numérica rápida](../bloque-3/profundizacion/b3-p2-verificacion-numerica.md) *(profundización)*

---

<a id="dato-estructurado"></a>

### Dato estructurado

Información colocada en campos con nombre, de forma que se pueda contar, ordenar y cruzar. Es lo que convierte 200 correos en una tabla sobre la que se puede pensar.

**Ejemplo.** De "os escribo porque el pedido del martes llegó con dos garrafas menos" salen tres campos: fecha, referencia de pedido y tipo de incidencia.

**Ver también:** [Extraer](#extraer), [Formato](#formato), [Transformar](#transformar)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 2: extraer](../bloque-2/b2-m3-extraer.md)
- Bloque 2 — [Dónde se rompe la extracción](../bloque-2/profundizacion/b2-p2-limites-de-la-extraccion.md) *(profundización)*

---

<a id="dato-personal"></a>

### Dato personal

Cualquier información que permita identificar a una persona física, directamente o cruzándola con otra. Incluye correo, teléfono y dirección, y también el conjunto de detalles que señala a una sola persona sin nombrarla.

**Ejemplo.** "El bar de la plaza de Ruiloba que solo abre los fines de semana" no lleva ningún nombre y es un dato personal, porque solo hay uno.

**Ver también:** [RGPD](#rgpd), [Anonimizar](#anonimizar), [Reidentificación](#reidentificacion)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Datos y RGPD: qué no se pega jamás](../bloque-3/b3-m7-datos-y-rgpd.md)
- Bloque 3 — [Anonimizar de verdad, en dos minutos](../bloque-3/profundizacion/b3-p4-anonimizar-en-la-practica.md) *(profundización)*

---

<a id="decision"></a>

### Decisión

Cada punto de una tarea en el que eliges entre dos caminos, junto con la información que usas para elegir. Es la casilla del medio de la descomposición y donde se esconde el trabajo de verdad.

**Ejemplo.** Al leer un ticket decides si es facturación o pedido erróneo. Lo que usas para decidirlo (si el importe cuadra con el albarán) es la decisión; el resto es teclear.

**Ver también:** [Descomposición](#descomposicion), [Criterio](#criterio), [Juicio](#juicio)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Descomponer: entrada, decisiones, salida, criterio](../bloque-1/b1-m4-descomposicion.md)
- Bloque 4 — [Voz del cliente: de texto libre a decisión](../bloque-4/b4-m9-voz-del-cliente.md)

---

<a id="deriva"></a>

### Deriva

El deterioro lento de algo que funcionaba, sin que nada se rompa de golpe. Cambia el formato de un fichero, cambia una condición comercial, y tu proceso empieza a fallar en silencio.

**Ejemplo.** Tu clasificación de tickets funciona seis meses. Alguien añade una categoría nueva y a partir de ahí todo lo nuevo cae en "otros" sin que salte ningún aviso.

**Ver también:** [Mantenimiento](#mantenimiento), [Punto de control](#punto-de-control), [Verificación](#verificacion)

**Aparece en** (bloque de origen: 5):

- Bloque 5 — [Qué se rompe con el tiempo y cómo enterarte](../bloque-5/b5-m5-mantenimiento.md)

---

<a id="descomposicion"></a>

### Descomposición

Partir una tarea en entrada, decisiones, salida y criterio de "bien hecho". La prueba de que está bien hecha: un tercero podría ejecutarla sin preguntarte nada.

**Ejemplo.** "Gestionar reclamaciones" no es una tarea, es una etiqueta. Descompuesta son siete pasos, dos decisiones y un criterio que hasta ahora no estaba escrito en ninguna parte.

**Ver también:** [Decisión](#decision), [Criterio](#criterio), [Conocimiento tácito](#conocimiento-tacito)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Por qué nadie sabe explicar su propio trabajo](../bloque-1/b1-m1-nadie-sabe-explicar-su-trabajo.md)
- Bloque 1 — [Descomponer: entrada, decisiones, salida, criterio](../bloque-1/b1-m4-descomposicion.md)
- Bloque 1 — [Caso cruzado: la misma lente en tu casa](../bloque-1/b1-m7-caso-cruzado-domestico.md)

---

<a id="diagnostico"></a>

### Diagnóstico

Leer un fallo como información sobre tu especificación y no sobre tu capacidad. Cuando el resultado no sirve, la primera pregunta es qué has dado por sabido.

**Ejemplo.** Pides que clasifique tickets y te devuelve un cajón de sastre enorme. No es que no sepa: es que no le has dicho qué separa "pedido erróneo" de "facturación".

**Ver también:** [Especificación implícita](#especificacion-implicita), [Encargo](#encargo), [Conocimiento tácito](#conocimiento-tacito)

**Aparece en** (bloque de origen: 0):

- Bloque 0 — [Fallar es diagnóstico, no fracaso](../bloque-0/b0-m3-fallar-es-diagnostico.md)

---

<a id="doble-track"></a>

### Doble track

El diseño de este curso: cada ejercicio enseña a la vez una habilidad de trabajo con IA y una idea de atención al cliente, sobre el mismo material.

**Ejemplo.** Clasificar los 800 tickets te enseña el verbo clasificar y, de paso, que la taxonomía de incidencias de tu empresa probablemente esté mal construida.

**Ver también:** [Verbo](#verbo), [Taxonomía](#taxonomia), [Patrón](#patron)

**Aparece en** (bloque de origen: 0):

- Bloque 0 — [Qué es este curso y qué no es](../bloque-0/b0-m1-que-es-este-curso.md)

---

<a id="documentacion"></a>

### Documentación

Dejar escrito un proceso con el detalle suficiente para que otra persona lo ejecute igual. Es también el paso previo obligatorio cuando una tarea todavía no se puede delegar.

**Ejemplo.** Escribes los siete pasos de la respuesta a una incidencia de facturación, con sus dos excepciones. Ahora Rubén puede hacerlo la semana que tú estás de vacaciones.

**Ver también:** [Proceso](#proceso), [Explicabilidad](#explicabilidad), [Mantenimiento](#mantenimiento)

**Aparece en** (bloque de origen: 5):

- Bloque 5 — [Del encargo al proceso documentado](../bloque-5/b5-m2-del-encargo-al-proceso.md)
- Bloque 5 — [Tus procesos, funcionando y medidos](../bloque-5/b5-m7-procesos-medidos.md)
- Bloque 6 — [Documentar para que sobreviva sin ti](../bloque-6/b6-m7-documentar-para-que-sobreviva.md)

---

<a id="encargo"></a>

### Encargo

La petición escrita completa: objetivo, contexto, restricciones, formato y criterio de aceptación. Se juzga por si un tercero podría ejecutarla sin preguntar, no por si la máquina la entiende.

**Ejemplo.** "Resume estos correos" es un deseo. "De estos 40 correos saca una tabla con fecha, cliente, tipo de incidencia y si menciona un pedido; pon 'no consta' donde no lo diga" es un encargo.

**Ver también:** [Objetivo](#objetivo), [Restricción](#restriccion), [Criterio de aceptación](#criterio-de-aceptacion)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Anatomía de un encargo](../bloque-3/b3-m1-anatomia-encargo.md)
- Bloque 3 — [Escribir un criterio de aceptación que sirva](../bloque-3/profundizacion/b3-p3-criterio-de-aceptacion.md) *(profundización)*

---

<a id="escalado"></a>

### Escalado

El camino que sigue un caso cuando se sale de lo previsto: a quién pasa, con qué información y en cuánto tiempo. Diseñarlo es lo que evita que el caso raro se quede tres días parado.

**Ejemplo.** Un cliente de hostelería amenaza con darse de baja por el cuarto descuadre. La regla dice: pasa a gerencia el mismo día, con el histórico de las cuatro facturas adjunto.

**Ver también:** [Excepción](#excepcion), [Siguiente paso](#siguiente-paso), [Proceso](#proceso)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [Escalado y excepciones](../bloque-4/b4-m7-escalado-y-excepciones.md)

---

<a id="escalera"></a>

### Escalera de implementación

Los cinco niveles que van de una conversación suelta a un proceso que corre sin ti. Sirve sobre todo para saber en qué escalón hay que quedarse.

**Ejemplo.** Tu respuesta a incidencias de facturación empieza como conversación, pasa a encargo guardado y se queda en encargo más fichero de contexto. Ahí funciona y ahí se queda.

**Ver también:** [Nivel de implementación](#nivel), [Regla de parada](#regla-de-parada), [Proceso](#proceso)

**Aparece en** (bloque de origen: 5):

- Bloque 5 — [La escalera de implementación y la regla de parada](../bloque-5/b5-m1-la-escalera.md)

---

<a id="especificacion-implicita"></a>

### Especificación implícita

Todo lo que en tu oficina se da por hecho y no está escrito en ninguna parte. Es la causa más frecuente de que un encargo salga mal y no se ve hasta que alguien de fuera pregunta.

**Ejemplo.** Que a los clientes de la ruta 3 se les factura a 30 días aunque el resto sea a 15. Nadie lo escribió nunca; lo sabéis los cinco que lleváis aquí tiempo.

**Ver también:** [Conocimiento tácito](#conocimiento-tacito), [Contexto](#contexto), [Encargo](#encargo)

**Aparece en** (bloque de origen: 0):

- Bloque 0 — [Fallar es diagnóstico, no fracaso](../bloque-0/b0-m3-fallar-es-diagnostico.md)
- Bloque 3 — [Todo lo que en tu oficina se da por hecho](../bloque-3/b3-m2-especificacion-implicita.md)

---

<a id="estabilidad-del-criterio"></a>

### Estabilidad del criterio

Si "bien hecho" significa lo mismo el lunes y el jueves. Es la cuarta pregunta del filtro de automatizabilidad, la que más gente se salta y la que más automatizaciones mata.

**Ejemplo.** Qué reclamación merece un detalle comercial depende de cómo vaya el mes, de quién sea el cliente y de con qué ánimo esté gerencia. Ese criterio no está listo para delegarse.

**Ver también:** [Criterio](#criterio), [Variabilidad](#variabilidad), [Explicabilidad](#explicabilidad)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [El filtro de automatizabilidad: cuatro preguntas](../bloque-1/b1-m5-filtro-automatizabilidad.md)
- Bloque 1 — [La variabilidad es la que mata automatizaciones](../bloque-1/profundizacion/b1-p2-variabilidad-mata-automatizaciones.md) *(profundización)*

---

<a id="evidencia"></a>

### Evidencia

Un dato comprobable sobre lo que pasa de verdad, medido por ti. Es lo que te da derecho a proponer un cambio cuando nadie te ha pedido opinión.

**Ejemplo.** No "creo que perdemos tiempo con las facturas", sino "en seis meses hemos atendido 304 incidencias del mismo origen; aquí está el listado y aquí el cálculo".

**Ver también:** [Caso de negocio](#caso-de-negocio), [Piloto](#piloto), [Línea base](#linea-base)

**Aparece en** (bloque de origen: 6):

- Bloque 6 — [Nadie te ha pedido que rediseñes nada](../bloque-6/b6-m1-nadie-te-lo-ha-pedido.md)
- Bloque 6 — [Ganarse el derecho: evidencia, piloto, propuesta](../bloque-6/b6-m2-ganarse-el-derecho.md)
- Bloque 6 — [El caso de negocio en una página](../bloque-6/b6-m3-caso-de-negocio.md)
- Bloque 6 — [Tu propuesta de una página](../bloque-6/b6-m8-propuesta-de-una-pagina.md)

---

<a id="excepcion"></a>

### Excepción

El caso que no sigue la regla y que sí tiene un tratamiento propio. Declararla por escrito es lo que distingue un proceso de un proceso que funciona a medias.

**Ejemplo.** Los pedidos entran hasta las 17:00. Menos el del hotel de Comillas, que entra hasta las 19:00 porque lo pactó gerencia en 2021 y nadie lo ha escrito.

**Ver también:** [Casuística](#casuistica), [Escalado](#escalado), [Variabilidad](#variabilidad)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [La variabilidad es la que mata automatizaciones](../bloque-1/profundizacion/b1-p2-variabilidad-mata-automatizaciones.md) *(profundización)*
- Bloque 3 — [Todo lo que en tu oficina se da por hecho](../bloque-3/b3-m2-especificacion-implicita.md)
- Bloque 4 — [Escalado y excepciones](../bloque-4/b4-m7-escalado-y-excepciones.md)

---

<a id="explicabilidad"></a>

### Explicabilidad

Si podrías enseñar la tarea a alguien nuevo en diez minutos. Cuando la respuesta es no, no significa que no se pueda delegar: significa que primero toca documentarla.

**Ejemplo.** Explicar cómo se registra un pedido: cuatro minutos. Explicar cómo decides el tono de una respuesta a un cliente enfadado: no lo consigues, y ahí tienes tu siguiente tarea.

**Ver también:** [Documentación](#documentacion), [Conocimiento tácito](#conocimiento-tacito), [Descomposición](#descomposicion)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [El filtro de automatizabilidad: cuatro preguntas](../bloque-1/b1-m5-filtro-automatizabilidad.md)

---

<a id="extraer"></a>

### Extraer

Sacar datos concretos de un texto desordenado y ponerlos en campos. Es el verbo con mejor relación entre esfuerzo y ahorro en una empresa pequeña.

**Ejemplo.** De 200 correos con hilos rotos y asuntos que ponen "Consulta" sacas una tabla con cliente, fecha, referencia de pedido y tipo de incidencia.

**Ver también:** [Dato estructurado](#dato-estructurado), [Verbo](#verbo), [Verificación](#verificacion)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 2: extraer](../bloque-2/b2-m3-extraer.md)
- Bloque 2 — [Dónde se rompe la extracción](../bloque-2/profundizacion/b2-p2-limites-de-la-extraccion.md) *(profundización)*
- Bloque 4 — [Voz del cliente: de texto libre a decisión](../bloque-4/b4-m9-voz-del-cliente.md)

---

<a id="formato"></a>

### Formato

La forma en la que pides que salga el resultado: tabla con estas columnas, lista de cinco puntos, correo de 100 palabras. Es la pieza más barata del encargo y la que más retrabajo evita.

**Ejemplo.** Pides "un resumen de los tickets de diciembre" y recibes tres párrafos. Pides "una tabla con categoría, número de tickets y minutos totales" y ya puedes sumar.

**Ver también:** [Encargo](#encargo), [Transformar](#transformar), [Dato estructurado](#dato-estructurado)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 3: transformar](../bloque-2/b2-m4-transformar.md)
- Bloque 3 — [Anatomía de un encargo](../bloque-3/b3-m1-anatomia-encargo.md)

---

<a id="frecuencia"></a>

### Frecuencia

Cuántas veces a la semana o al mes haces una tarea. Multiplicada por la duración da los minutos al mes, que es el único número que decide si merece la pena tocarla.

**Ejemplo.** Contestar consultas de estado de pedido: 14 veces por semana, 4 minutos cada una. Son 224 minutos al mes, casi cuatro horas.

**Ver también:** [Volumen](#volumen), [Línea base](#linea-base), [Variabilidad](#variabilidad)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Mapa de la semana: frecuencia, duración, variabilidad](../bloque-1/b1-m3-mapa-de-la-semana.md)

---

<a id="generalizacion-falsa"></a>

### Generalización falsa

Una conclusión que suena razonable pero se apoya en menos casos de los que necesitaría. Aparece cuando "he visto tres" se convierte en "los clientes".

**Ejemplo.** Un resumen de veinte tickets concluye que "los clientes de hostelería están descontentos con el reparto". Los veinte tickets eran de dos bares de la misma ruta.

**Ver también:** [Alucinación](#alucinacion), [Verificación](#verificacion), [Causa raíz](#causa-raiz)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Los cinco modos de fallo típicos](../bloque-3/b3-m5-modos-de-fallo.md)

---

<a id="glosario"></a>

### Glosario propio

La lista de tus palabras con lo que significan aquí. En atención al cliente casi todo el vocabulario es local: lo que en tu empresa es un abono, en la de al lado es un vale.

**Ejemplo.** "Aviso" en Aguas del Norte es la llamada de la víspera para confirmar la entrega, no una notificación del sistema. Sin esa línea escrita, medio encargo se malinterpreta.

**Ver también:** [Contexto](#contexto), [Casuística](#casuistica), [Plantilla](#plantilla)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Ficheros de contexto: glosario, tono, plantillas, casuística](../bloque-3/b3-m3-ficheros-de-contexto.md)
- Bloque 3 — [Tu primer fichero de contexto de trabajo](../bloque-3/b3-m9-contexto-trabajo.md)
- Bloque 5 — [Construir tu fichero de contexto de trabajo](../bloque-5/b5-m3-contexto-de-trabajo.md)

---

<a id="granularidad"></a>

### Granularidad

El tamaño del trozo con el que registras o describes algo. Demasiado fino y lo abandonas al tercer día; demasiado grueso y no se ve nada.

**Ejemplo.** El diario de tareas va en bloques de 15 minutos. En bloques de un minuto no lo terminas; en bloques de una hora te sale "correo: 4 horas" y no has aprendido nada.

**Ver también:** [Línea base](#linea-base), [Trabajo invisible](#trabajo-invisible), [Descomposición](#descomposicion)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [El diario de tareas: cinco días, quince minutos](../bloque-1/b1-m2-diario-de-tareas.md)
- Bloque 1 — [Por qué casi todos los diarios de tiempo mienten](../bloque-1/profundizacion/b1-p1-por-que-fallan-los-diarios.md) *(profundización)*

---

<a id="herramienta"></a>

### Herramienta

El producto concreto con el que ejecutas un verbo hoy. Cambia cada pocos meses, así que se aprende al final y se evalúa preguntando qué verbo hace y cómo se verifica.

**Ejemplo.** Da igual con qué programa clasifiques los tickets. Lo que no cambia es que necesitas una taxonomía cerrada y una forma de comprobar una muestra.

**Ver también:** [Caducidad](#caducidad), [Verbo](#verbo), [Patrón](#patron)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Apéndice desechable: cómo está el panorama ahora mismo](../bloque-2/profundizacion/b2-p5-herramientas-hoy.md) *(profundización)*

---

<a id="imaginacion-informada"></a>

### Imaginación informada

Saber qué es posible delegar, que es distinto de tener criterio para decidirlo. Casi nadie deja de automatizar por falta de juicio: no automatiza porque no se le ocurre que se pueda.

**Ejemplo.** Llevas tres años pasando a mano los datos de los correos a una hoja de Excel. No es que hayas decidido que no se puede: es que nadie te ha dicho nunca que eso tenga nombre.

**Ver también:** [Verbo](#verbo), [Patrón](#patron), [Catálogo de patrones](#catalogo)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [El mapa de lo posible](../bloque-2/b2-m1-mapa-de-lo-posible.md)

---

<a id="interrupcion"></a>

### Interrupción

Cada vez que dejas lo que estabas haciendo para atender otra cosa. Lo caro no es la interrupción: es volver a donde estabas.

**Ejemplo.** Diez llamadas de cinco minutos no son cincuenta minutos. Son cincuenta minutos más diez regresos al informe que estabas escribiendo, y el informe no sale.

**Ver también:** [Coste de coordinación](#coste-de-coordinacion), [Trabajo invisible](#trabajo-invisible), [Granularidad](#granularidad)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Trabajo visible y trabajo invisible](../bloque-1/b1-m6-trabajo-visible-invisible.md)
- Bloque 1 — [Lo que cuesta volver a donde estabas](../bloque-1/profundizacion/b1-p3-coste-de-cambio-de-contexto.md) *(profundización)*

---

<a id="inventario"></a>

### Inventario de procesos

La lista de tus tareas con sus números: frecuencia, duración, variabilidad y las cuatro puntuaciones del filtro. Es un documento vivo, no un ejercicio que se entrega y se olvida.

**Ejemplo.** Dieciocho tareas ordenadas por minutos al mes. Las tres primeras se llevan el 40% de tu semana, y una de ellas no debería existir.

**Ver también:** [Artefacto](#artefacto), [Línea base](#linea-base), [Coste de oportunidad](#coste-de-oportunidad)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Tu inventario de procesos](../bloque-1/b1-m8-inventario-de-procesos.md)
- Bloque 2 — [Tu catálogo de patrones](../bloque-2/b2-m10-catalogo-de-patrones.md)

---

<a id="juicio"></a>

### Juicio

Valorar algo cuando la respuesta correcta no está escrita en ninguna parte y alguien va a responder por ella. No es ninguno de los seis verbos y no se delega.

**Ejemplo.** Decidir si al bar que lleva quince años comprando se le perdona el descuadre de 40 € o se le reclama. No hay procedimiento: hay una relación y una cuenta.

**Ver también:** [Qué no delegar](#no-delegar), [Responsabilidad](#responsabilidad), [Relación](#relacion)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Lo que no es ninguno de los seis](../bloque-2/b2-m9-que-no-es-ninguno.md)

---

<a id="linea-base"></a>

### Línea base

La medida de cómo están las cosas antes de cambiar nada. Sin ella cualquier mejora es una impresión, y las impresiones no se defienden delante de un jefe.

**Ejemplo.** "Antes tardaba 20 minutos por reclamación y atendía 14 a la semana." Ese par de números es lo que hace demostrable todo lo que venga después.

**Ver también:** [Bitácora](#bitacora), [Frecuencia](#frecuencia), [Evidencia](#evidencia)

**Aparece en** (bloque de origen: 0):

- Bloque 0 — [Abre tu bitácora](../bloque-0/b0-m4-tu-bitacora.md)
- Bloque 1 — [El diario de tareas: cinco días, quince minutos](../bloque-1/b1-m2-diario-de-tareas.md)
- Bloque 1 — [Mapa de la semana: frecuencia, duración, variabilidad](../bloque-1/b1-m3-mapa-de-la-semana.md)
- Bloque 1 — [Tu inventario de procesos](../bloque-1/b1-m8-inventario-de-procesos.md)
- Bloque 1 — [Anticipo: una victoria pequeña, medida](../bloque-1/b1-m9-primera-victoria.md)
- Bloque 1 — [Por qué casi todos los diarios de tiempo mienten](../bloque-1/profundizacion/b1-p1-por-que-fallan-los-diarios.md) *(profundización)*
- Bloque 5 — [Tus procesos, funcionando y medidos](../bloque-5/b5-m7-procesos-medidos.md)

---

<a id="mantenimiento"></a>

### Mantenimiento

El trabajo de mantener vivo un proceso que ya funciona: comprobar cada cierto tiempo que sigue haciendo lo que crees. Un proceso sin mantenimiento no se para, se estropea callado.

**Ejemplo.** Una vez al mes coges cinco casos al azar de los que salieron solos y los revisas a fondo. Cinco minutos que evitan enterarte en marzo de que falla desde diciembre.

**Ver también:** [Deriva](#deriva), [Punto de control](#punto-de-control), [Proceso](#proceso)

**Aparece en** (bloque de origen: 5):

- Bloque 5 — [Qué se rompe con el tiempo y cómo enterarte](../bloque-5/b5-m5-mantenimiento.md)
- Bloque 5 — [Cuándo desmontar una automatización](../bloque-5/b5-m6-cuando-desmontar.md)
- Bloque 6 — [Documentar para que sobreviva sin ti](../bloque-6/b6-m7-documentar-para-que-sobreviva.md)

---

<a id="nivel"></a>

### Nivel de implementación

Cada escalón de la escalera, del 1 (conversación suelta) al 5 (funciona sin ti en el bucle). El 3 es donde termina la mayoría del trabajo de oficina, y terminar ahí es un éxito.

**Ejemplo.** Tu respuesta a incidencias vive en el nivel 3: un encargo guardado más el fichero de contexto. Subirla al 4 costaría dos tardes y ahorraría cuatro minutos al mes.

**Ver también:** [Escalera de implementación](#escalera), [Regla de parada](#regla-de-parada), [Coste de oportunidad](#coste-de-oportunidad)

**Aparece en** (bloque de origen: 5):

- Bloque 5 — [La escalera de implementación y la regla de parada](../bloque-5/b5-m1-la-escalera.md)

---

<a id="normalidad"></a>

### Normalidad

La descripción explícita de lo que es habitual en un conjunto. Se escribe antes de buscar rarezas, o cada cosa que te llame la atención parecerá un hallazgo.

**Ejemplo.** "Un pedido normal en Aguas del Norte va de 30 a 400 €, con cantidades positivas y en día laborable." Con eso escrito, las 45 líneas negativas saltan solas.

**Ver también:** [Anomalía](#anomalia), [Patrón](#patron), [Criterio](#criterio)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 6: detectar anomalías](../bloque-2/b2-m7-detectar-anomalias.md)
- Bloque 2 — [Una anomalía no es un error](../bloque-2/profundizacion/b2-p4-anomalia-no-es-error.md) *(profundización)*

---

<a id="nps"></a>

### NPS

La pregunta de si recomendarías la empresa del 0 al 10, resumida en un único número. A solas es casi inútil: se mueve por cosas que no controlas, tarda meses en reaccionar y no te dice qué arreglar.

**Ejemplo.** El NPS de Aguas del Norte baja cuatro puntos en enero. Eso no te dice nada. Los 304 tickets de facturación sí te dicen qué hacer el lunes por la mañana.

**Ver también:** [CES (esfuerzo del cliente)](#ces), [Resolución en primer contacto](#resolucion-primer-contacto), [Voz del cliente](#voz-del-cliente)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [Métricas que dicen algo](../bloque-4/b4-m5-metricas.md)

---

<a id="objetivo"></a>

### Objetivo

Qué quieres conseguir con el encargo, dicho en una frase y sin ambigüedad. Es la primera pieza, y mucha gente la escribe como si fuera un tema en vez de un resultado.

**Ejemplo.** "Tickets de diciembre" es un tema. "Saber qué tres categorías concentran más minutos de atención en diciembre" es un objetivo.

**Ver también:** [Encargo](#encargo), [Criterio de aceptación](#criterio-de-aceptacion), [Formato](#formato)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Anatomía de un encargo](../bloque-3/b3-m1-anatomia-encargo.md)

---

<a id="omision"></a>

### Omisión silenciosa

Lo que falta en un resultado y no se ve leyéndolo, porque un texto al que le falta algo se sigue leyendo bien. Solo aparece comparando con la fuente.

**Ejemplo.** El resumen de los procedimientos de entrega recoge ocho de los nueve y se salta el PR-07, el del aviso previo. Justo el que explica el 9% de vuestros tickets.

**Ver también:** [Verificación](#verificacion), [Cuadre](#cuadre), [Alucinación](#alucinacion)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Ejercicios de sabotaje](../bloque-3/b3-m4-sabotaje.md)
- Bloque 3 — [Los cinco modos de fallo típicos](../bloque-3/b3-m5-modos-de-fallo.md)

---

<a id="orden-de-magnitud"></a>

### Orden de magnitud

Comprobar si un número es del tamaño que debería ser, sin calcularlo exacto. Es la verificación más rápida que existe y descarta la mitad de los errores graves.

**Ejemplo.** Un informe dice que las incidencias de facturación cuestan 340.000 € al año en una empresa de seis personas. No hace falta revisar el cálculo: está mal.

**Ver también:** [Cuadre](#cuadre), [Verificación](#verificacion), [Coste de verificar](#coste-de-verificar)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Técnicas de verificación numérica rápida](../bloque-3/profundizacion/b3-p2-verificacion-numerica.md) *(profundización)*

---

<a id="patron"></a>

### Patrón

Una forma de hacer las cosas que se repite en dominios que no se parecen entre sí. Se aprende una vez y se reconoce en todas partes, que es justo lo que no hacen los productos.

**Ejemplo.** Clasificar tickets, clasificar facturas por régimen fiscal en una gestoría y clasificar el correo personal por "requiere respuesta" son la misma operación con distinta ropa.

**Ver también:** [Verbo](#verbo), [Transferencia](#transferencia), [Imaginación informada](#imaginacion-informada)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [El mapa de lo posible](../bloque-2/b2-m1-mapa-de-lo-posible.md)
- Bloque 2 — [Tu catálogo de patrones](../bloque-2/b2-m10-catalogo-de-patrones.md)
- Bloque 2 — [Verbo 6: detectar anomalías](../bloque-2/b2-m7-detectar-anomalias.md)
- Bloque 2 — [Apéndice desechable: cómo está el panorama ahora mismo](../bloque-2/profundizacion/b2-p5-herramientas-hoy.md) *(profundización)*

---

<a id="perdida-de-informacion"></a>

### Pérdida de información

Lo que se queda por el camino al cambiar algo de formato. Resumir es transformar con pérdida, y el error no está en perder: está en no haber declarado qué estabas dispuesta a perder.

**Ejemplo.** Conviertes un hilo de cuatro correos en un parte de incidencia de cinco líneas. Se pierde que el cliente ya había reclamado en noviembre, que era lo importante.

**Ver también:** [Transformar](#transformar), [Formato](#formato), [Omisión silenciosa](#omision)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 3: transformar](../bloque-2/b2-m4-transformar.md)

---

<a id="piloto"></a>

### Piloto

Probar un cambio en pequeño, con fecha de inicio y de final, para tener datos antes de pedir nada. Es el paso intermedio entre tener razón y que te dejen aplicarla.

**Ejemplo.** Durante tres semanas avisas tú la víspera a los doce clientes de la ruta 2 y cuentas las entregas fallidas antes y después. Eso ya no es una opinión.

**Ver también:** [Evidencia](#evidencia), [Propuesta](#propuesta), [Línea base](#linea-base)

**Aparece en** (bloque de origen: 6):

- Bloque 6 — [Ganarse el derecho: evidencia, piloto, propuesta](../bloque-6/b6-m2-ganarse-el-derecho.md)

---

<a id="plantilla"></a>

### Plantilla

Un texto base con los huecos marcados, para no reescribir desde cero lo que se repite. Es la forma más barata de estabilizar el tono y de que nadie improvise compromisos.

**Ejemplo.** La respuesta a "no me cuadra la factura": tres párrafos fijos y tres huecos (importe, número de factura, fecha de abono). Quien la rellena no promete nada nuevo.

**Ver también:** [Contexto](#contexto), [Tono](#tono), [Reutilización](#reutilizacion)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Ficheros de contexto: glosario, tono, plantillas, casuística](../bloque-3/b3-m3-ficheros-de-contexto.md)

---

<a id="plausibilidad"></a>

### Plausibilidad

Que algo suene bien y encaje con lo que esperabas, sin que eso tenga nada que ver con que sea cierto. Un sistema que produce continuaciones plausibles acierta casi siempre, y eso es justo lo que hace peligroso el resto.

**Ejemplo.** Te dice que el plazo para reclamar una entrega son 48 horas. Es una cifra razonable, del tamaño correcto y del estilo del sector, y no está escrita en ninguno de vuestros nueve procedimientos.

**Ver también:** [Alucinación](#alucinacion), [Verificación](#verificacion), [Seguridad excesiva](#seguridad-excesiva)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Por qué los modelos inventan datos](../bloque-3/profundizacion/b3-p1-por-que-alucinan.md) *(profundización)*

---

<a id="politica-organizativa"></a>

### Política organizativa

Cómo se decide de verdad en tu empresa: quién manda, a quién escucha, qué se intentó antes y a quién le salió caro. El cuello de botella para cambiar un proceso rara vez es analítico.

**Ejemplo.** Tu propuesta de arreglar la facturación toca el sistema que eligió gerencia hace cuatro años. El argumento técnico es correcto y por sí solo no va a bastar.

**Ver también:** [Autoridad](#autoridad), [Resistencia](#resistencia), [Propuesta](#propuesta)

**Aparece en** (bloque de origen: 6):

- Bloque 6 — [Nadie te ha pedido que rediseñes nada](../bloque-6/b6-m1-nadie-te-lo-ha-pedido.md)
- Bloque 6 — [Enseñar una mejora sin que parezca que sobra alguien](../bloque-6/b6-m4-ensenar-sin-amenazar.md)
- Bloque 6 — [El miedo del compañero](../bloque-6/b6-m5-el-miedo-del-companero.md)
- Bloque 6 — [Cuando el jefe dice que no (y a veces tiene razón)](../bloque-6/b6-m6-cuando-el-jefe-dice-que-no.md)

---

<a id="proceso"></a>

### Proceso

Una secuencia de pasos escrita, con sus entradas, sus controles y su criterio de salida. Se diferencia de un encargo en que sobrevive a que tú te pongas mala.

**Ejemplo.** "Incidencias de facturación": cinco pasos, dos puntos de control, una excepción declarada y el nombre de quién lo hace si tú no estás.

**Ver también:** [Documentación](#documentacion), [Punto de control](#punto-de-control), [Escalera de implementación](#escalera)

**Aparece en** (bloque de origen: 5):

- Bloque 5 — [Del encargo al proceso documentado](../bloque-5/b5-m2-del-encargo-al-proceso.md)
- Bloque 5 — [Tus procesos, funcionando y medidos](../bloque-5/b5-m7-procesos-medidos.md)
- Bloque 6 — [Documentar para que sobreviva sin ti](../bloque-6/b6-m7-documentar-para-que-sobreviva.md)

---

<a id="propuesta"></a>

### Propuesta

Lo que le llevas a quien decide: una página con el problema, la evidencia, lo que propones y qué hace falta. No es pedir permiso para tener razón, es ponerle fácil la decisión a otra persona.

**Ejemplo.** Una hoja con el fallo de redondeo, los 304 tickets, el coste de seis meses, las tres semanas de piloto y lo único que pides: media mañana del informático.

**Ver también:** [Caso de negocio](#caso-de-negocio), [Evidencia](#evidencia), [Piloto](#piloto)

**Aparece en** (bloque de origen: 6):

- Bloque 6 — [Ganarse el derecho: evidencia, piloto, propuesta](../bloque-6/b6-m2-ganarse-el-derecho.md)
- Bloque 6 — [Enseñar una mejora sin que parezca que sobra alguien](../bloque-6/b6-m4-ensenar-sin-amenazar.md)
- Bloque 6 — [Tu propuesta de una página](../bloque-6/b6-m8-propuesta-de-una-pagina.md)

---

<a id="punto-de-control"></a>

### Punto de control

El sitio de una cadena donde te paras a mirar antes de seguir. Regla práctica: que cada eslabón produzca algo que puedas revisar en treinta segundos.

**Ejemplo.** Después de extraer los datos de los correos y antes de clasificarlos, miras cuántos campos han quedado en "no consta". Si son cero, desconfía.

**Ver también:** [Cadena](#cadena), [Verificación](#verificacion), [Proceso](#proceso)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbos compuestos: encadenar sin perder el hilo](../bloque-2/b2-m8-verbos-compuestos.md)
- Bloque 5 — [Encadenar pasos y poner los controles humanos](../bloque-5/b5-m4-encadenar-y-controles.md)

---

<a id="no-delegar"></a>

### Qué no delegar

El conjunto de tareas que no se pasan a una máquina, no por dificultad técnica sino por quién responde y por lo que se rompe si sale mal. Se decide con tres preguntas, no con una lista cerrada.

**Ejemplo.** Reconocer por escrito un error de la empresa, dar el pésame a un cliente de veinte años, cancelar un contrato. Sale rápido y sale mal.

**Ver también:** [Juicio](#juicio), [Responsabilidad](#responsabilidad), [Relación](#relacion)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Lo que no es ninguno de los seis](../bloque-2/b2-m9-que-no-es-ninguno.md)

---

<a id="reconocimiento"></a>

### Reconocimiento

Decirle al cliente que has entendido qué le ha pasado y qué le supone, antes de explicar nada. Ocupa una frase y evita la mitad de los escalados.

**Ejemplo.** "Es la tercera vez este trimestre que le facturamos de más, y entiendo que a estas alturas no se fíe del importe." Después ya vienen los datos.

**Ver también:** [Claridad](#claridad), [Siguiente paso](#siguiente-paso), [Tono](#tono)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [Responder bajo carga emocional](../bloque-4/b4-m6-respuesta-bajo-carga-emocional.md)

---

<a id="regla-de-parada"></a>

### Regla de parada

La condición escrita de antemano que dice cuándo dejas de construir. Sin ella se siguen subiendo escalones por inercia hasta que el mantenimiento cuesta más que la tarea.

**Ejemplo.** No se sube de nivel hasta que el anterior haya funcionado tres veces seguidas sin un solo retoque. Si retocas, esa vez no cuenta y la cuenta empieza otra vez.

**Ver también:** [Escalera de implementación](#escalera), [Nivel de implementación](#nivel), [Mantenimiento](#mantenimiento)

**Aparece en** (bloque de origen: 5):

- Bloque 5 — [La escalera de implementación y la regla de parada](../bloque-5/b5-m1-la-escalera.md)
- Bloque 5 — [Cuándo desmontar una automatización](../bloque-5/b5-m6-cuando-desmontar.md)

---

<a id="reidentificacion"></a>

### Reidentificación

Volver a saber de quién habla un texto al que le quitaron el nombre, cruzando lo que queda. Es la razón de que anonimizar mal sea peor que no anonimizar: da tranquilidad falsa.

**Ejemplo.** "Cliente de hostelería de Ruiloba, ruta 2, con fuente refrigerada alquilada." En una cartera de 300 clientes eso es una persona concreta y la identifica cualquiera de la oficina.

**Ver también:** [Anonimizar](#anonimizar), [Dato personal](#dato-personal), [RGPD](#rgpd)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Anonimizar de verdad, en dos minutos](../bloque-3/profundizacion/b3-p4-anonimizar-en-la-practica.md) *(profundización)*

---

<a id="relacion"></a>

### Relación

El vínculo con la persona que está al otro lado, que a veces es el valor entero de la tarea. Cuando lo que importa es que lo hiciste tú, delegarlo lo destruye aunque el texto salga mejor.

**Ejemplo.** La llamada al cliente de quince años para decirle que os habéis equivocado vosotros. El valor está en que le llamas tú y le dices tu nombre.

**Ver también:** [Qué no delegar](#no-delegar), [Juicio](#juicio), [Reconocimiento](#reconocimiento)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Lo que no es ninguno de los seis](../bloque-2/b2-m9-que-no-es-ninguno.md)

---

<a id="resistencia"></a>

### Resistencia

La oposición a un cambio, que casi nunca es técnica. Detrás suele haber miedo a sobrar, a quedar en evidencia o a cargar con un riesgo que no es suyo.

**Ejemplo.** Nieves lleva nueve años haciendo la facturación de una manera. Tu propuesta dice, sin decirlo, que esos nueve años se podían haber hecho de otra forma.

**Ver también:** [Política organizativa](#politica-organizativa), [Autoridad](#autoridad), [Propuesta](#propuesta)

**Aparece en** (bloque de origen: 6):

- Bloque 6 — [Enseñar una mejora sin que parezca que sobra alguien](../bloque-6/b6-m4-ensenar-sin-amenazar.md)
- Bloque 6 — [El miedo del compañero](../bloque-6/b6-m5-el-miedo-del-companero.md)

---

<a id="resolucion-primer-contacto"></a>

### Resolución en primer contacto

El porcentaje de asuntos que se cierran sin que el cliente tenga que volver. Es de las métricas más honestas de atención, con una trampa: se infla sola si el cliente reabre el caso con otro número de ticket.

**Ejemplo.** De los 304 casos de facturación, la mitad vuelven al mes siguiente con la factura nueva. Sobre el papel se habían resuelto todos a la primera.

**Ver también:** [Contacto evitable](#contacto-evitable), [CES (esfuerzo del cliente)](#ces), [Tiempo de ciclo](#tiempo-de-ciclo)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [Métricas que dicen algo](../bloque-4/b4-m5-metricas.md)

---

<a id="responsabilidad"></a>

### Responsabilidad

Quién responde si esto sale mal, con nombre y apellidos. Es la pregunta que más rápido decide si una tarea se delega o no se delega.

**Ejemplo.** Si el borrador mete un plazo de devolución que no existe y el cliente lo reclama, no responde la herramienta. Responde la empresa y, en la reunión del lunes, tú.

**Ver también:** [Qué no delegar](#no-delegar), [Riesgo](#riesgo), [Juicio](#juicio)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Lo que no es ninguno de los seis](../bloque-2/b2-m9-que-no-es-ninguno.md)

---

<a id="responsable-del-tratamiento"></a>

### Responsable del tratamiento

La figura del RGPD que decide para qué se usan unos datos personales y que responde ante la agencia de protección de datos. En tu caso es la empresa, no tú; el marrón práctico te cae igual.

**Ejemplo.** Si pegas el listado de clientes en una herramienta que nadie ha aprobado, quien incumple es Aguas del Norte. Quien lo hizo eres tú, y esa conversación la vas a tener.

**Ver también:** [RGPD](#rgpd), [Dato personal](#dato-personal), [Riesgo](#riesgo)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Datos y RGPD: qué no se pega jamás](../bloque-3/b3-m7-datos-y-rgpd.md)

---

<a id="restriccion"></a>

### Restricción

Los límites del encargo: qué no se puede hacer, qué no se puede decir, qué longitud, qué fuentes se pueden usar. Las restricciones que no escribes son las que se incumplen.

**Ejemplo.** "No ofrezcas compensación económica, no des fechas de entrega concretas y no uses la palabra 'incidencia'." Tres líneas que evitan tres problemas caros.

**Ver también:** [Encargo](#encargo), [Criterio de aceptación](#criterio-de-aceptacion), [Tono](#tono)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Anatomía de un encargo](../bloque-3/b3-m1-anatomia-encargo.md)

---

<a id="reutilizacion"></a>

### Reutilización

Escribir una vez lo que ibas a explicar veinte veces. Es lo que separa un truco puntual de algo que ahorra tiempo mes tras mes.

**Ejemplo.** Las quince líneas de contexto sobre vuestros clientes de hostelería no se vuelven a teclear: viven en un fichero y se adjuntan cada vez que hacen falta.

**Ver también:** [Contexto](#contexto), [Plantilla](#plantilla), [Proceso](#proceso)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Ficheros de contexto: glosario, tono, plantillas, casuística](../bloque-3/b3-m3-ficheros-de-contexto.md)
- Bloque 5 — [Del encargo al proceso documentado](../bloque-5/b5-m2-del-encargo-al-proceso.md)

---

<a id="reversibilidad"></a>

### Reversibilidad

Si lo que has hecho se puede deshacer, y a qué coste. Es el primer eje para decidir cuánto revisar: un borrador interno se corrige, un correo ya enviado no.

**Ejemplo.** Cambiar la categoría de 800 tickets en tu hoja de trabajo se deshace con control+Z. Mandar la circular de subida de tarifas con el porcentaje mal, no.

**Ver también:** [Riesgo](#riesgo), [Alcance](#alcance), [Verificación](#verificacion)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Verificación proporcional al riesgo](../bloque-3/b3-m6-verificacion-proporcional.md)

---

<a id="rgpd"></a>

### RGPD

El reglamento europeo que regula qué se puede hacer con los datos de personas identificables. En una PyME sin departamento jurídico se traduce en una regla de tres líneas y un reflejo: anonimizar antes de pegar.

**Ejemplo.** Los 800 tickets de este curso los puedes trabajar sin ningún problema porque son inventados. Con los de tu empresa, primero quitas nombre, teléfono, correo y dirección.

**Ver también:** [Dato personal](#dato-personal), [Anonimizar](#anonimizar), [Responsable del tratamiento](#responsable-del-tratamiento)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Datos y RGPD: qué no se pega jamás](../bloque-3/b3-m7-datos-y-rgpd.md)
- Bloque 3 — [Tu primer fichero de contexto de trabajo](../bloque-3/b3-m9-contexto-trabajo.md)
- Bloque 3 — [Anonimizar de verdad, en dos minutos](../bloque-3/profundizacion/b3-p4-anonimizar-en-la-practica.md) *(profundización)*

---

<a id="riesgo"></a>

### Riesgo

Qué pasa si esto sale mal una de cada veinte veces, medido en consecuencias y no en probabilidad. Es lo que decide cuánto verificas y qué no delegas.

**Ejemplo.** Un borrador interno mal hecho cuesta cinco minutos. Un correo a un cliente con un plazo inventado cuesta una reclamación y una llamada de gerencia.

**Ver también:** [Tolerancia al fallo](#tolerancia-al-fallo), [Verificación](#verificacion), [Reversibilidad](#reversibilidad)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [El filtro de automatizabilidad: cuatro preguntas](../bloque-1/b1-m5-filtro-automatizabilidad.md)
- Bloque 1 — [Tu inventario de procesos](../bloque-1/b1-m8-inventario-de-procesos.md)
- Bloque 1 — [Anticipo: una victoria pequeña, medida](../bloque-1/b1-m9-primera-victoria.md)
- Bloque 1 — [La variabilidad es la que mata automatizaciones](../bloque-1/profundizacion/b1-p2-variabilidad-mata-automatizaciones.md) *(profundización)*
- Bloque 2 — [Verbo 4: redactar borrador](../bloque-2/b2-m5-redactar-borrador.md)
- Bloque 3 — [Ejercicios de sabotaje](../bloque-3/b3-m4-sabotaje.md)
- Bloque 3 — [Verificación proporcional al riesgo](../bloque-3/b3-m6-verificacion-proporcional.md)
- Bloque 3 — [Datos y RGPD: qué no se pega jamás](../bloque-3/b3-m7-datos-y-rgpd.md)
- Bloque 3 — [Tu plantilla de verificación](../bloque-3/b3-m8-plantilla-de-verificacion.md)
- Bloque 3 — [Verificar de más también es un error](../bloque-3/profundizacion/b3-p5-coste-de-verificar-de-mas.md) *(profundización)*
- Bloque 5 — [La escalera de implementación y la regla de parada](../bloque-5/b5-m1-la-escalera.md)
- Bloque 5 — [Encadenar pasos y poner los controles humanos](../bloque-5/b5-m4-encadenar-y-controles.md)
- Bloque 6 — [Cuando el jefe dice que no (y a veces tiene razón)](../bloque-6/b6-m6-cuando-el-jefe-dice-que-no.md)

---

<a id="rubrica"></a>

### Rúbrica

La tabla que distingue un trabajo insuficiente de uno correcto y de uno bueno. Sirve para corregirte sola, que es el problema central de estudiar sin profesor.

**Ejemplo.** Tres niveles para el informe de causa raíz: no llegó al hallazgo, llegó, o llegó y además encontró algo que no estaba previsto.

**Ver también:** [Criterio de aceptación](#criterio-de-aceptacion), [Checklist](#checklist), [Comparar contra criterio](#comparar)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 5: comparar contra criterio](../bloque-2/b2-m6-comparar-contra-criterio.md)
- Bloque 3 — [Tu plantilla de verificación](../bloque-3/b3-m8-plantilla-de-verificacion.md)
- Bloque 3 — [Escribir un criterio de aceptación que sirva](../bloque-3/profundizacion/b3-p3-criterio-de-aceptacion.md) *(profundización)*

---

<a id="seguridad-excesiva"></a>

### Seguridad excesiva

El tono rotundo sin fuente detrás: el "por supuesto" y el "siempre" que no se apoyan en nada. Es un modo de fallo porque desactiva tu revisión justo cuando más falta hace.

**Ejemplo.** "Por supuesto, en estos casos la política estándar del sector es abonar el importe íntegro." No hay ninguna política estándar del sector y nadie ha dicho eso.

**Ver también:** [Alucinación](#alucinacion), [Plausibilidad](#plausibilidad), [Verificación](#verificacion)

**Aparece en** (bloque de origen: 3):

- Bloque 3 — [Los cinco modos de fallo típicos](../bloque-3/b3-m5-modos-de-fallo.md)

---

<a id="siguiente-paso"></a>

### Siguiente paso

Qué va a pasar ahora, quién lo hace y cuándo, dicho al cliente antes de que lo pregunte. Es la parte de la respuesta que decide si vuelve a llamar.

**Ejemplo.** "Nieves revisa la factura mañana y le llamamos el jueves antes de las 12." Sin esa frase, el jueves a las 9 llama él.

**Ver también:** [Claridad](#claridad), [Contacto evitable](#contacto-evitable), [Escalado](#escalado)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [Responder bajo carga emocional](../bloque-4/b4-m6-respuesta-bajo-carga-emocional.md)

---

<a id="sistema"></a>

### Sistema

El conjunto de piezas y reglas que produce un resultado, incluidas las que nadie diseñó. Mirar el sistema es preguntar qué genera esto, en lugar de atender el caso que ha llegado hoy.

**Ejemplo.** Contestar bien a 304 quejas de facturación es atender síntomas. El sistema es un cálculo de descuento que redondea al alza y que mañana va a generar tres quejas más.

**Ver también:** [Causa raíz](#causa-raiz), [Contacto evitable](#contacto-evitable), [Coste de oportunidad](#coste-de-oportunidad)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Trabajo visible y trabajo invisible](../bloque-1/b1-m6-trabajo-visible-invisible.md)
- Bloque 4 — [Análisis de causa raíz](../bloque-4/b4-m2-causa-raiz.md)
- Bloque 4 — [Contacto evitable](../bloque-4/b4-m3-contacto-evitable.md)
- Bloque 4 — [Del síntoma al sistema](../bloque-4/b4-m8-del-sintoma-al-sistema.md)

---

<a id="taxonomia"></a>

### Taxonomía

El conjunto cerrado de categorías con el que clasificas. Una sana tiene un solo eje, categorías que no se solapan, tamaños comparables y un "otros" que no engorda.

**Ejemplo.** En `tickets.xlsx` hay catorce etiquetas para ocho categorías reales, más un "Otros" del 11%. Clasificar perfectamente con esa lista sigue sin servir de nada.

**Ver también:** [Clasificar](#clasificar), [Criterio](#criterio), [Causa raíz](#causa-raiz)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 1: clasificar](../bloque-2/b2-m2-clasificar.md)
- Bloque 2 — [Clasificar no es buscar](../bloque-2/profundizacion/b2-p1-clasificar-vs-buscar.md) *(profundización)*
- Bloque 4 — [Taxonomías de incidencia](../bloque-4/b4-m1-taxonomias.md)

---

<a id="tiempo-de-ciclo"></a>

### Tiempo de ciclo

Lo que tarda un asunto desde que entra hasta que queda cerrado de verdad, contado en tiempo real y no en tiempo trabajado. Incluye las esperas, que es donde se va casi todo.

**Ejemplo.** Una incidencia de facturación se resuelve con 12 minutos de trabajo y tarda nueve días en cerrarse, porque espera al ciclo de facturación del mes siguiente.

**Ver también:** [Resolución en primer contacto](#resolucion-primer-contacto), [Coste de un contacto](#coste-de-contacto), [Coste de coordinación](#coste-de-coordinacion)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [Métricas que dicen algo](../bloque-4/b4-m5-metricas.md)

---

<a id="tolerancia-al-fallo"></a>

### Tolerancia al fallo

Cuánto daño hace un error aislado en esta tarea concreta. Es la tercera pregunta del filtro y la que separa el borrador interno del correo que sale a un cliente.

**Ejemplo.** Que se cuele un dato mal en tu resumen semanal interno lo ves tú. Que se cuele en el aviso de subida de tarifas lo ven 300 clientes el mismo día.

**Ver también:** [Riesgo](#riesgo), [Reversibilidad](#reversibilidad), [Alcance](#alcance)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [El filtro de automatizabilidad: cuatro preguntas](../bloque-1/b1-m5-filtro-automatizabilidad.md)

---

<a id="tono"></a>

### Tono

Cómo suena un texto para quien lo recibe: cercanía, formalidad y cuánto se disculpa. Es lo que más rápido delata un texto que no ha escrito nadie de la casa.

**Ejemplo.** A un bar de toda la vida al que se le ha facturado mal se le escribe distinto que a un ayuntamiento. En el primer caso, "estimado cliente" ya es un error.

**Ver también:** [Claridad](#claridad), [Plantilla](#plantilla), [Contexto](#contexto)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 4: redactar borrador](../bloque-2/b2-m5-redactar-borrador.md)
- Bloque 3 — [Ficheros de contexto: glosario, tono, plantillas, casuística](../bloque-3/b3-m3-ficheros-de-contexto.md)
- Bloque 3 — [Ejercicios de sabotaje](../bloque-3/b3-m4-sabotaje.md)
- Bloque 3 — [Los cinco modos de fallo típicos](../bloque-3/b3-m5-modos-de-fallo.md)
- Bloque 3 — [Tu primer fichero de contexto de trabajo](../bloque-3/b3-m9-contexto-trabajo.md)
- Bloque 4 — [Responder bajo carga emocional](../bloque-4/b4-m6-respuesta-bajo-carga-emocional.md)

---

<a id="trabajo-invisible"></a>

### Trabajo invisible

Lo que ocupa tu jornada y no aparece en ninguna lista de tareas: interrupciones, reconstruir dónde estabas, coordinar, esperar, absorber el enfado de alguien. No se registra y decide el día.

**Ejemplo.** Tu diario dice "atención telefónica: 2 h". No dice que entre llamada y llamada has buscado tres albaranes, has preguntado a reparto y has vuelto a empezar el informe cuatro veces.

**Ver también:** [Interrupción](#interrupcion), [Coste de coordinación](#coste-de-coordinacion), [Granularidad](#granularidad)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Por qué nadie sabe explicar su propio trabajo](../bloque-1/b1-m1-nadie-sabe-explicar-su-trabajo.md)
- Bloque 1 — [El diario de tareas: cinco días, quince minutos](../bloque-1/b1-m2-diario-de-tareas.md)
- Bloque 1 — [Trabajo visible y trabajo invisible](../bloque-1/b1-m6-trabajo-visible-invisible.md)
- Bloque 1 — [Por qué casi todos los diarios de tiempo mienten](../bloque-1/profundizacion/b1-p1-por-que-fallan-los-diarios.md) *(profundización)*
- Bloque 1 — [Lo que cuesta volver a donde estabas](../bloque-1/profundizacion/b1-p3-coste-de-cambio-de-contexto.md) *(profundización)*

---

<a id="transferencia"></a>

### Transferencia

Que un método aprendido en un sitio te sirva en otro que no se le parece. Es la prueba de que has aprendido el método y no el caso.

**Ejemplo.** Descompones la compra semanal de tu casa con las mismas cuatro casillas que una reclamación de un cliente. Si funciona ahí, es que el esquema no dependía del trabajo.

**Ver también:** [Patrón](#patron), [Descomposición](#descomposicion), [Imaginación informada](#imaginacion-informada)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Caso cruzado: la misma lente en tu casa](../bloque-1/b1-m7-caso-cruzado-domestico.md)

---

<a id="transformar"></a>

### Transformar

Cambiar algo de formato conservando el contenido. Parece el verbo tonto y es el que más información pierde en silencio.

**Ejemplo.** Un hilo de cuatro correos convertido en un parte de incidencia de cinco líneas, declarando antes qué se puede perder: los saludos sí, el historial de reclamaciones no.

**Ver también:** [Formato](#formato), [Pérdida de información](#perdida-de-informacion), [Verbo](#verbo)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [Verbo 3: transformar](../bloque-2/b2-m4-transformar.md)

---

<a id="tutor"></a>

### Tutor

El acompañante de este curso, que está para darte tracción y no respuestas. No te da la solución de un ejercicio antes de que lo intentes y no se inventa contenido que el curso no tenga.

**Ejemplo.** Le preguntas dónde está el fallo del sabotaje de nivel 3 y te devuelve una pregunta: "¿de dónde sale el plazo de 14 días que dice ese texto?".

**Ver también:** [Artefacto](#artefacto), [Bitácora](#bitacora), [Diagnóstico](#diagnostico)

**Aparece en** (bloque de origen: 0):

- Bloque 0 — [Cómo se usa este repositorio](../bloque-0/b0-m2-como-usar-esto.md)

---

<a id="variabilidad"></a>

### Variabilidad

Cuánto cambia una tarea de una vez a otra. Se mira en el rango y no en la media, y hay tres tipos que se confunden: cambia la entrada, cambia el criterio o cambia el contexto.

**Ejemplo.** Contestar una reclamación te lleva entre 4 y 45 minutos. Esa horquilla dice mucho más sobre si se puede delegar que la media de 18.

**Ver también:** [Estabilidad del criterio](#estabilidad-del-criterio), [Excepción](#excepcion), [Frecuencia](#frecuencia)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Mapa de la semana: frecuencia, duración, variabilidad](../bloque-1/b1-m3-mapa-de-la-semana.md)
- Bloque 1 — [La variabilidad es la que mata automatizaciones](../bloque-1/profundizacion/b1-p2-variabilidad-mata-automatizaciones.md) *(profundización)*

---

<a id="verbo"></a>

### Verbo

Cada una de las seis operaciones básicas que se le pueden encargar a una máquina: clasificar, extraer, transformar, redactar borrador, comparar contra criterio y detectar anomalías. Casi todo el trabajo de oficina es una combinación de ellas.

**Ejemplo.** "Preparar el informe mensual de incidencias" no es una tarea suelta: es extraer, más clasificar, más detectar anomalías, más transformar a un formato de una página.

**Ver también:** [Patrón](#patron), [Cadena](#cadena), [Catálogo de patrones](#catalogo)

**Aparece en** (bloque de origen: 2):

- Bloque 2 — [El mapa de lo posible](../bloque-2/b2-m1-mapa-de-lo-posible.md)
- Bloque 2 — [Tu catálogo de patrones](../bloque-2/b2-m10-catalogo-de-patrones.md)
- Bloque 2 — [Verbo 1: clasificar](../bloque-2/b2-m2-clasificar.md)
- Bloque 2 — [Verbo 2: extraer](../bloque-2/b2-m3-extraer.md)
- Bloque 2 — [Verbo 3: transformar](../bloque-2/b2-m4-transformar.md)
- Bloque 2 — [Verbo 4: redactar borrador](../bloque-2/b2-m5-redactar-borrador.md)
- Bloque 2 — [Verbo 5: comparar contra criterio](../bloque-2/b2-m6-comparar-contra-criterio.md)
- Bloque 2 — [Verbo 6: detectar anomalías](../bloque-2/b2-m7-detectar-anomalias.md)
- Bloque 2 — [Verbos compuestos: encadenar sin perder el hilo](../bloque-2/b2-m8-verbos-compuestos.md)

---

<a id="verificacion"></a>

### Verificación

Comprobar si lo producido sirve, con un método y no con una lectura por encima. Es la asignatura troncal del curso porque producir es fácil y saber si vale es lo escaso.

**Ejemplo.** Antes de mandar la tabla de incidencias coges tres filas al azar, las contrastas con el correo original y compruebas que las categorías suman 800.

**Ver también:** [Checklist](#checklist), [Cuadre](#cuadre), [Omisión silenciosa](#omision)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [Anticipo: una victoria pequeña, medida](../bloque-1/b1-m9-primera-victoria.md)
- Bloque 2 — [Verbo 2: extraer](../bloque-2/b2-m3-extraer.md)
- Bloque 2 — [Verbo 4: redactar borrador](../bloque-2/b2-m5-redactar-borrador.md)
- Bloque 2 — [Verbos compuestos: encadenar sin perder el hilo](../bloque-2/b2-m8-verbos-compuestos.md)
- Bloque 2 — [Dónde se rompe la extracción](../bloque-2/profundizacion/b2-p2-limites-de-la-extraccion.md) *(profundización)*
- Bloque 2 — [Por qué el valor está en el borrador cero](../bloque-2/profundizacion/b2-p3-el-borrador-cero.md) *(profundización)*
- Bloque 3 — [Ejercicios de sabotaje](../bloque-3/b3-m4-sabotaje.md)
- Bloque 3 — [Verificación proporcional al riesgo](../bloque-3/b3-m6-verificacion-proporcional.md)
- Bloque 3 — [Tu plantilla de verificación](../bloque-3/b3-m8-plantilla-de-verificacion.md)
- Bloque 3 — [Por qué los modelos inventan datos](../bloque-3/profundizacion/b3-p1-por-que-alucinan.md) *(profundización)*
- Bloque 3 — [Técnicas de verificación numérica rápida](../bloque-3/profundizacion/b3-p2-verificacion-numerica.md) *(profundización)*
- Bloque 5 — [Encadenar pasos y poner los controles humanos](../bloque-5/b5-m4-encadenar-y-controles.md)
- Bloque 5 — [Qué se rompe con el tiempo y cómo enterarte](../bloque-5/b5-m5-mantenimiento.md)

---

<a id="volumen"></a>

### Volumen

Los minutos al mes que se lleva una tarea, calculados como frecuencia por duración. Es la primera pregunta del filtro y el umbral práctico son unas dos horas al mes.

**Ejemplo.** Una tarea de 3 minutos que haces cuatro veces al día son 240 minutos al mes: entra. Una de 40 minutos que haces una vez al trimestre, no.

**Ver también:** [Frecuencia](#frecuencia), [Línea base](#linea-base), [Coste de oportunidad](#coste-de-oportunidad)

**Aparece en** (bloque de origen: 1):

- Bloque 1 — [El filtro de automatizabilidad: cuatro preguntas](../bloque-1/b1-m5-filtro-automatizabilidad.md)

---

<a id="voz-del-cliente"></a>

### Voz del cliente

Lo que los clientes dicen con sus propias palabras, convertido en algo sobre lo que se pueda decidir. El trabajo no es leerlo: es agrupar, contar y quedarse con lo que cambia una decisión.

**Ejemplo.** 200 correos con quejas escritas de mil maneras. Agrupados, el 40% dicen lo mismo con palabras distintas: la factura no cuadra con el albarán.

**Ver también:** [Extraer](#extraer), [Clasificar](#clasificar), [Coste de la insatisfacción](#insatisfaccion)

**Aparece en** (bloque de origen: 4):

- Bloque 4 — [Voz del cliente: de texto libre a decisión](../bloque-4/b4-m9-voz-del-cliente.md)
