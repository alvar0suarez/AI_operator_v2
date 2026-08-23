/**
 * Ensamblado del contexto del tutor. ESPECIFICACION.md §7.2.
 *
 * Se inyecta:
 *   - el nodo actual completo, y los requisitos que ella ya ha cubierto
 *   - el glosario del curso
 *   - los artefactos que ella haya guardado
 *   - su bitácora reciente
 *
 * NO se inyecta nunca:
 *   - las soluciones de los ejercicios del nodo activo
 *   - nada de dataset/SOLUCIONES/
 *   - nodos que todavía no ha desbloqueado (el tutor no adelanta materia)
 *
 * Las dos primeras exclusiones no dependen de este fichero: el paquete
 * `curso.json` que construye scripts/empaquetar-tutor.py no las contiene. Aquí se
 * garantiza la tercera y se le da forma al resto.
 */

import { notaDeIntento } from './guardarrailes.js';

const LIMITE_ARTEFACTO = 6000;   // caracteres por artefacto
const LIMITE_BITACORA = 4000;    // caracteres de bitácora reciente
const LIMITE_HISTORIAL = 12;     // turnos de conversación que se conservan

/** Nodos cubiertos: los que ella ha marcado como completados, y solo esos. */
function cubiertos(estado) {
  return new Set(Object.keys(estado?.completados || {}).filter((k) => estado.completados[k]));
}

/**
 * El índice completo del curso viaja siempre: es lo que impide que el tutor se
 * invente nodos (guardarraíl 3). Lleva título, bloque y estado, pero NO el
 * contenido de los nodos que ella no ha desbloqueado.
 */
function indiceDelCurso(paquete) {
  const porBloque = new Map();
  for (const n of paquete.indice) {
    if (!porBloque.has(n.bloque)) porBloque.set(n.bloque, []);
    porBloque.get(n.bloque).push(n);
  }
  const lineas = [];
  for (const [bloque, nodos] of [...porBloque.entries()].sort((a, b) => a[0] - b[0])) {
    const info = paquete.bloques[bloque] || {};
    lineas.push(`\n## Bloque ${bloque} — ${info.titulo || ''}`);
    for (const n of nodos) {
      const marca = n.estado === 'pendiente-piloto' ? '  [SIN ESCRIBIR TODAVÍA]' : '';
      lineas.push(`- \`${n.id}\` — ${n.titulo} (${n.tipo}, ${n.duracion_min} min)${marca}`);
    }
  }
  return lineas.join('\n');
}

function recortar(texto, limite) {
  if (!texto) return '';
  const t = String(texto);
  return t.length <= limite ? t : `${t.slice(0, limite)}\n[...recortado...]`;
}

/**
 * Construye el prompt de sistema completo para una petición.
 * Devuelve también qué se ha incluido, para poder auditarlo y probarlo.
 */
export function construirSistema(paquete, { modo, nodoId, estado }) {
  const nodo = paquete.indice.find((n) => n.id === nodoId) || null;
  const yaCubiertos = cubiertos(estado);

  const partes = [];
  const incluido = { nodo: null, requisitos: [], glosario: false, artefactos: [], bitacora: false };

  partes.push(paquete.prompts['sistema-base'] || '');
  partes.push(`\n\n# Modo activo: ${modo}\n\n${paquete.prompts[`modo-${modo}`] || ''}`);

  // ── El curso entero como índice, nunca como contenido ──
  partes.push(`\n\n# Índice del curso\n
Éste es el curso COMPLETO. No existe ningún nodo fuera de esta lista. Si te preguntan
por algo que no está aquí, di que el curso no lo trata y señala el nodo más cercano por
su título y su id. Los marcados [SIN ESCRIBIR TODAVÍA] existen y están previstos, pero no
tienen contenido: puedes decir en qué bloque están y cómo se titulan, y NO puedes
desarrollarlos. Se escriben después del piloto, con lo que se vea que cuesta.
${indiceDelCurso(paquete)}`);

  // ── El nodo actual, completo ──
  if (nodo) {
    incluido.nodo = nodo.id;
    const cuerpo = paquete.cuerpos[nodo.id];
    partes.push(`\n\n# Nodo actual: \`${nodo.id}\` — ${nodo.titulo}
Tipo: ${nodo.tipo} · ${nodo.duracion_min} min · caducidad ${nodo.caduca}
${cuerpo?.objetivos?.length ? `Objetivos: ${cuerpo.objetivos.join(' / ')}` : ''}

${cuerpo?.texto || '(Este nodo todavía no tiene contenido escrito.)'}`);

    // ── Requisitos que ella YA ha cubierto. Los que no, no viajan. ──
    for (const req of nodo.requisitos || []) {
      if (!yaCubiertos.has(req)) continue;
      const meta = paquete.indice.find((n) => n.id === req);
      const cuerpoReq = paquete.cuerpos[req];
      if (!meta || !cuerpoReq) continue;
      incluido.requisitos.push(req);
      partes.push(`\n\n# Ya cubierto: \`${req}\` — ${meta.titulo}\n\n${recortar(cuerpoReq.texto, 5000)}`);
    }

    const nota = notaDeIntento(nodo, estado);
    if (nota) partes.push(`\n\n# Estado del ejercicio\n\n${nota}`);
  }

  // ── Glosario ──
  if (paquete.glosario?.length) {
    incluido.glosario = true;
    const terminos = paquete.glosario.map((t) => `- **${t.termino}** (\`${t.slug}\`): ${t.definicion}`);
    partes.push(`\n\n# Glosario del curso\n\n${terminos.join('\n')}`);
  }

  // ── Sus artefactos, si los ha guardado ──
  for (const [nombre, texto] of Object.entries(estado?.artefactos || {})) {
    if (!texto) continue;
    incluido.artefactos.push(nombre);
    partes.push(`\n\n# Artefacto suyo: ${nombre}\n\n${recortar(texto, LIMITE_ARTEFACTO)}`);
  }

  // ── Bitácora reciente ──
  if (estado?.bitacora) {
    incluido.bitacora = true;
    partes.push(`\n\n# Su bitácora reciente\n
Úsala para no repetirle lo que ya sabe y para conectar con lo que le falló antes. No la
cites de forma que parezca vigilancia.\n\n${recortar(estado.bitacora, LIMITE_BITACORA)}`);
  }

  return { sistema: partes.join(''), incluido, nodo };
}

/** Recorta el historial y lo normaliza al formato de la API. */
export function prepararMensajes(historial, mensaje) {
  const previos = (historial || [])
    .filter((m) => m && (m.role === 'user' || m.role === 'assistant') && m.content)
    .slice(-LIMITE_HISTORIAL)
    .map((m) => ({ role: m.role, content: String(m.content) }));

  // La API exige que el primer mensaje sea de usuario.
  while (previos.length && previos[0].role !== 'user') previos.shift();

  return [...previos, { role: 'user', content: mensaje }];
}

export const _limites = { LIMITE_ARTEFACTO, LIMITE_BITACORA, LIMITE_HISTORIAL };
