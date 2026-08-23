# Guía de estilo del contenido — contrato para quien escribe nodos

Fuente normativa: `ESPECIFICACION.md` §§1, 2, 10. Si algo aquí contradice la
especificación, gana la especificación.

## Para quién se escribe

Una profesional de atención al cliente en una PyME. Usa Excel para casi todo,
correo, quizá un CRM básico. Habla con un chatbot pero no conoce patrones ni
límites. **No tiene autoridad para rediseñar procesos** y no va a subir datos de
su empresa a ningún sitio. Estudia después de trabajar, en sesiones de 45–60 min.

No es tonta. Es competente en su trabajo y ajena a este. La distancia entre
"principiante" y "tonta" es el error de tono más caro de este curso.

## Voz

- **Tuteo**, femenino cuando haya que marcar género. Español de España.
- Frases cortas. Si una frase necesita una coma para respirar dos veces, párte la.
- **Nada de entusiasmo de folleto.** Ni "¡Vamos allá!", ni "¡Genial!", ni emojis,
  ni "en este apasionante módulo". El texto respeta su tiempo.
- Se admite y se busca el registro seco y concreto: "Esto va a ser aburrido y es
  el bloque más importante del curso" es mejor apertura que cualquier promesa.
- **Ejemplos antes que definiciones.** Concreto → patrón → generalización (§2.2).
- Números siempre que se pueda. "Ahorras tiempo" no dice nada; "12 minutos por
  correo × 40 correos al mes = 8 horas" sí.

## Prohibiciones duras

1. **No prometer transformación organizativa.** Se le enseña a *ganarse el derecho*
   a proponer un cambio, que es otra cosa (§1).
2. **No pedirle datos reales**, nunca, bajo ninguna forma. Todo ejercicio corre
   sobre `/dataset/ficheros` o sobre algo que ella describe con sus palabras.
3. **No gamificación.** Ni insignias, ni rachas, ni puntos, ni "¡nivel completado!"
   El progreso son minutos medidos y artefactos (§2.7).
4. **No nombres de productos en el tronco.** Se enseñan patrones, no herramientas
   (§3, bloque 2). Todo lo que caduque va etiquetado `caduca: alto` y **al final**
   del bloque, nunca al principio (§0).
5. **No terminar en "has leído".** Todo nodo produce algo que ella conserva (§2.1).
6. No usar "IA" como sujeto mágico. La frase "la IA analiza tus tickets" está mal
   escrita: quien analiza es ella, con un instrumento.

## Obligaciones de estructura

- **Tres instancias por patrón** (§2.3): su sector (CX), otro dominio profesional
  (gestoría, tienda de barrio, clínica dental, taller), y vida personal. Las tres,
  no dos. La de vida personal no es decorativa: es la que demuestra que el patrón
  transfiere.
- **"Cuándo esto falla"** en todo nodo de concepto. Un patrón sin sus límites es
  una superstición.
- **"Escribe tú la regla"**: el cierre donde ella redacta la generalización con sus
  palabras. El pensamiento sistemático no transfiere si se lo damos escrito (§2.2).
- **Regla de parada**: siempre que se pueda subir de nivel, decir explícitamente
  cuándo NO hacerlo (§2.6).
- **Capa transversal** (§3): en cada bloque debe aparecer, sin ser módulo suelto,
  al menos uno de: qué no delegar, lectura de riesgo, causa vs. síntoma, RGPD
  aplicado, coste de oportunidad de automatizar algo que no debería existir.

## Longitud

- Nodo `concepto`: 700–1.400 palabras. Un nodo que no cabe en su `duracion_min`
  está mal dimensionado.
- Nodo `ejercicio`: consigna corta (≤400 palabras) + material. La consigna se lee
  en 3 minutos o no se hace.
- Nodo `profundizacion`: 500–1.200 palabras. Responde a "esto me interesa, quiero
  más", así que puede ser más técnico y asumir el tronco.

## Formato markdown

- H1 nunca en el cuerpo: lo pone el frontmatter.
- Tablas para comparaciones, no para prosa.
- Bloques `> [!NOTE]`, `> [!WARNING]`, `> [!TIP]` (admoniciones de MkDocs Material
  vía `pymdownx`) para avisos. Máximo dos por nodo o dejan de verse.
- Las soluciones de ejercicio van SIEMPRE en fichero aparte, nunca en el nodo,
  ni siquiera colapsadas dentro del mismo fichero (§7.2: el tutor lee el nodo).
- Rutas al dataset relativas: `dataset/ficheros/tickets.xlsx`.

## Comprobación final antes de dar un nodo por escrito

- [ ] ¿Termina en algo que ella conserva?
- [ ] ¿Hay tres instancias, y una es de su vida personal?
- [ ] ¿Está dicho cuándo el patrón falla?
- [ ] ¿Redacta ella la regla, o se la he dado yo hecha?
- [ ] ¿He prometido algo que el curso no puede cumplir?
- [ ] ¿Se lee en el `duracion_min` declarado, a la velocidad de alguien cansado?
