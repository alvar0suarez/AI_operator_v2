/**
 * Los tres guardarraíles de ESPECIFICACION.md §7.3.
 *
 * Se aplican ANTES de llamar a la API. Un prompt es una petición; un guardarraíl
 * es una garantía. Regla que ordena todo lo demás: si algo se puede garantizar no
 * enviándolo, no se envía.
 *
 * Los guardarraíles 1 (la solución no llega antes del intento) y 3 (no inventar
 * curso) están implementados sobre todo en `scripts/empaquetar-tutor.py`: el
 * paquete que consume esta función no contiene ninguna solución. Aquí queda la
 * parte que sí depende de la petición concreta.
 */

// ── Guardarraíl 2: datos que parecen reales ─────────────────────────────────

const SENALES = [
  { tipo: 'telefono', etiqueta: '[TELEFONO]', re: /(?:\+34[\s-]?)?[6789]\d{2}(?:[\s.-]?\d{2}){3}\b|(?:\+34[\s-]?)?[6789]\d{2}(?:[\s.-]?\d{3}){2}\b/g },
  { tipo: 'email', etiqueta: '[EMAIL]', re: /\b[\w.+-]+@[\w-]+\.[\w.-]{2,}\b/g },
  { tipo: 'dni', etiqueta: '[DNI]', re: /\b[XYZ]?\d{7,8}[-\s]?[A-HJ-NP-TV-Z]\b/g },
  { tipo: 'cif', etiqueta: '[CIF]', re: /\b[ABCDEFGHJNPQRSUVW]\d{7}[0-9A-J]\b/g },
  { tipo: 'iban', etiqueta: '[IBAN]', re: /\bES\d{2}\s?(?:\d{4}\s?){5}\b/g },
  { tipo: 'direccion', etiqueta: '[DIRECCION]', re: /\b(?:C\/|Calle|Avda\.?|Avenida|Pza\.?|Plaza|Ctra\.?|Carretera)\s+[A-ZÁÉÍÓÚÑ][\wáéíóúñ'.-]*(?:\s+[\wáéíóúñ'.-]+){0,4}[,\s]+\d{1,4}\b/gi },
];

// Lista blanca: el dataset del curso es sintético y no dispara nada.
const SINTETICO = [
  /\bCLI-\d{4}\b/g, /\bTCK-\d{4}\b/g, /\bPED-\d{5}\b/g,
  /@aguasdelnorte\.[a-z]+/gi, /aguas del norte/gi,
];

/**
 * Detecta y enmascara datos que parecen reales.
 *
 * Umbral: dos tipos distintos de señal en el mismo mensaje, o una sola señal
 * repetida tres veces o más. Un correo suelto en una frase no salta; una tabla de
 * cuatro filas con nombre, teléfono y correo, sí. Se prefiere un falso positivo a
 * un falso negativo, pero un guardarraíl que salta cada dos mensajes se acaba
 * ignorando, y entonces no protege nada.
 */
export function revisarDatos(texto) {
  // Se aparta lo sintético antes de mirar, para no contarlo como señal.
  let limpio = texto;
  for (const re of SINTETICO) limpio = limpio.replace(re, ' SINTETICO ');

  const encontradas = [];
  let enmascarado = texto;

  for (const senal of SENALES) {
    const coincidencias = limpio.match(senal.re) || [];
    if (coincidencias.length === 0) continue;
    encontradas.push({ tipo: senal.tipo, veces: coincidencias.length });
    enmascarado = enmascarado.replace(senal.re, senal.etiqueta);
  }

  const tipos = encontradas.length;
  const repeticionMaxima = encontradas.length ? Math.max(...encontradas.map((e) => e.veces)) : 0;
  const salta = tipos >= 2 || repeticionMaxima >= 3;

  return {
    salta,
    senales: encontradas,
    texto: salta ? enmascarado : texto,
    aviso: salta ? redactarAviso(encontradas) : null,
  };
}

function redactarAviso(senales) {
  const nombres = {
    telefono: 'teléfonos', email: 'correos', dni: 'DNI',
    cif: 'CIF', iban: 'cuentas bancarias', direccion: 'direcciones',
  };
  const lista = senales.map((s) => `${s.veces} ${nombres[s.tipo] || s.tipo}`).join(', ');
  return [
    `Ojo, que ahí hay ${lista} que parecen reales. Eso no se pega en una herramienta`,
    'externa: en una PyME el responsable del tratamiento es la empresa, y el marrón',
    'acaba en quien lo pegó.',
    '',
    'No hace falta: cuéntamelo con etiquetas. "CLIENTE_A, pedido de unos 300 €, se queja',
    'del descuento" me sirve exactamente igual. Te respondo con lo que me has contado,',
    'ya enmascarado.',
    '',
    'Esto se trabaja entero en `b3-m7-datos-y-rgpd`.',
  ].join('\n');
}

// ── Guardarraíl 1: la solución no llega antes del intento ───────────────────

/**
 * El paquete del tutor nunca contiene soluciones, así que no hay nada que filtrar.
 * Lo que sí hace falta es decirle al modelo en qué estado está ella, para que
 * responda bien cuando le pida la solución sin haberlo intentado.
 */
export function notaDeIntento(nodo, estado) {
  if (!nodo?.tiene_solucion) return null;
  const intentado = Boolean(estado?.intentado?.[nodo.id]);
  if (intentado) {
    return [
      'Ella ya ha marcado este ejercicio como intentado. Aun así, tú no tienes la',
      'solución en el contexto: no la tienes porque no se te manda. Puedes comentar lo',
      'que ella te cuente que ha encontrado, pero no afirmes cuál era la respuesta.',
    ].join('\n');
  }
  return [
    'Este nodo tiene ejercicio con solución y ella TODAVÍA NO lo ha marcado como',
    'intentado. Si te pide la solución: no la tienes, y aunque la dedujeras no se la',
    'darías. Dile una vez por qué (el texto malo parece bien, y eso solo se aprende',
    'cazándolo, no leyéndolo), invítala a marcarlo como intentado, y ofrécele la',
    'primera pasada del método.',
  ].join('\n');
}

// ── Guardarraíl 3: no inventar curso ────────────────────────────────────────

const RE_ID = /\bb[0-6]-[mp]\d{1,2}-[a-z0-9-]+\b/g;

const MARCA_INVENTADO = ' **[este nodo no existe: el tutor se lo ha inventado]**';

/**
 * Marca en la respuesta cualquier id de nodo que no exista. Que se vea: es un fallo
 * del tutor y ella tiene que poder detectarlo. Forma parte de lo que está aprendiendo,
 * y es la demostración práctica de `b3-p1-por-que-alucinan`.
 */
export function revisarCitas(respuesta, idsValidos) {
  const citados = [...new Set(respuesta.match(RE_ID) || [])];
  const inventados = citados.filter((id) => !idsValidos.has(id));
  if (inventados.length === 0) return { texto: respuesta, inventados: [] };

  let texto = respuesta;
  for (const id of inventados) {
    texto = texto.split(id).join(id + MARCA_INVENTADO);
  }
  return { texto, inventados };
}

export const _paraPruebas = { SENALES, SINTETICO, RE_ID, MARCA_INVENTADO };
