/**
 * Pruebas de los tres guardarraíles (ESPECIFICACION.md §7.3).
 *
 * La prueba crítica es la primera: que ninguna ruta de dataset/SOLUCIONES/ ni
 * ninguna solución de ejercicio pueda acabar dentro del prompt ensamblado, por
 * ninguna vía. Si esa prueba falla, el curso ha perdido su corrector objetivo.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

import { revisarDatos, revisarCitas, notaDeIntento } from '../guardarrailes.js';
import { construirSistema, prepararMensajes } from '../contexto.js';

const AQUI = dirname(fileURLToPath(import.meta.url));
const paquete = JSON.parse(readFileSync(join(AQUI, '..', 'curso.json'), 'utf8'));

// ─────────────────────────── LA PRUEBA CRÍTICA ───────────────────────────────

test('el paquete del tutor no contiene ninguna solución', () => {
  const crudo = JSON.stringify(paquete);
  for (const centinela of ['dataset/SOLUCIONES', 'verdades-escondidas', 'taxonomia-real',
                           'pedidos-fantasma', 'cuentas-v4', 'mapa-duplicados']) {
    assert.ok(!crudo.includes(centinela), `el paquete contiene «${centinela}»`);
  }
  // Los campos internos tampoco viajan.
  for (const nodo of paquete.indice) {
    assert.equal(nodo.solucion, undefined, `${nodo.id} lleva el campo solucion`);
    assert.equal(nodo.brief, undefined, `${nodo.id} lleva el campo brief`);
  }
});

test('el prompt ensamblado no filtra soluciones por ninguna vía', () => {
  // Se prueba con un estado hostil: artefactos y bitácora que intentan colar rutas.
  const { sistema } = construirSistema(paquete, {
    modo: 'socratico',
    nodoId: paquete.indice[0].id,
    estado: {
      completados: Object.fromEntries(paquete.indice.map((n) => [n.id, true])),
      artefactos: { 'inventario.md': 'contenido cualquiera' },
      bitacora: 'una entrada',
    },
  });
  for (const centinela of ['dataset/SOLUCIONES', 'verdades-escondidas', 'taxonomia-real']) {
    assert.ok(!sistema.includes(centinela), `el prompt contiene «${centinela}»`);
  }
});

// ─────────────────────── Guardarraíl 1: intento previo ───────────────────────

test('sin intento marcado, el tutor recibe la instrucción de no dar la solución', () => {
  const nodo = { id: 'x', tiene_solucion: true };
  const nota = notaDeIntento(nodo, { intentado: {} });
  assert.match(nota, /TODAVÍA NO/);
  assert.match(nota, /no la tienes/);
});

test('con intento marcado, sigue sin poder afirmar la respuesta', () => {
  const nodo = { id: 'x', tiene_solucion: true };
  const nota = notaDeIntento(nodo, { intentado: { x: true } });
  assert.match(nota, /no afirmes cuál era la respuesta/);
});

test('un nodo sin solución no genera nota de intento', () => {
  assert.equal(notaDeIntento({ id: 'x', tiene_solucion: false }, {}), null);
});

// ─────────────────── Guardarraíl 2: datos que parecen reales ─────────────────

test('un dato suelto no dispara el aviso', () => {
  assert.equal(revisarDatos('Escríbeme a marta@ejemplo.es cuando puedas').salta, false);
  assert.equal(revisarDatos('Tengo una duda sobre el verbo clasificar').salta, false);
});

test('dos tipos de señal en el mismo mensaje sí disparan', () => {
  const r = revisarDatos('Marta Ibáñez, 942 12 34 56, marta@bar.es');
  assert.equal(r.salta, true);
  assert.ok(r.texto.includes('[TELEFONO]'));
  assert.ok(r.texto.includes('[EMAIL]'));
  assert.ok(!r.texto.includes('942 12 34 56'));
});

test('una sola señal repetida tres veces dispara', () => {
  const r = revisarDatos('942123456 / 678901234 / 600112233');
  assert.equal(r.salta, true);
});

test('los identificadores del dataset sintético no disparan', () => {
  const r = revisarDatos('CLI-0042 se queja del pedido PED-00123 y del ticket TCK-0777');
  assert.equal(r.salta, false, 'el dataset del curso es sintético y no debe avisar');
});

test('el aviso explica y ofrece alternativa, no solo prohíbe', () => {
  const r = revisarDatos('Marta Ibáñez, 942 12 34 56, marta@bar.es');
  assert.match(r.aviso, /CLIENTE_A/, 'tiene que decirle cómo contarlo sin datos');
  assert.match(r.aviso, /b3-m7-datos-y-rgpd/, 'tiene que enlazar al nodo donde se aprende');
});

// ──────────────────── Guardarraíl 3: no inventar contenido ───────────────────

test('un id de nodo inventado se marca de forma visible', () => {
  const validos = new Set(['b3-m1-anatomia-encargo']);
  const r = revisarCitas('Mira b3-m1-anatomia-encargo y también b5-m9-inventado', validos);
  assert.deepEqual(r.inventados, ['b5-m9-inventado']);
  assert.match(r.texto, /b5-m9-inventado \*\*\[este nodo no existe/);
  assert.ok(!r.texto.includes('b3-m1-anatomia-encargo **['), 'no debe marcar los válidos');
});

test('todos los ids del registro se consideran válidos', () => {
  const validos = new Set(paquete.indice.map((n) => n.id));
  const texto = paquete.indice.slice(0, 20).map((n) => n.id).join(' y ');
  assert.deepEqual(revisarCitas(texto, validos).inventados, []);
});

// ──────────────────────── Contexto: §7.2 al detalle ──────────────────────────

test('no se inyecta el contenido de nodos que ella no ha desbloqueado', () => {
  const conCuerpo = paquete.indice.find((n) => paquete.cuerpos[n.id]?.texto);
  if (!conCuerpo) return; // aún no hay contenido escrito: nada que comprobar

  const hijo = paquete.indice.find((n) => (n.requisitos || []).includes(conCuerpo.id));
  if (!hijo) return;

  const { incluido } = construirSistema(paquete, {
    modo: 'socratico', nodoId: hijo.id, estado: { completados: {} },
  });
  assert.deepEqual(incluido.requisitos, [], 'sin completar nada, no debe viajar ningún requisito');

  const { incluido: conCubierto } = construirSistema(paquete, {
    modo: 'socratico', nodoId: hijo.id, estado: { completados: { [conCuerpo.id]: true } },
  });
  assert.deepEqual(conCubierto.requisitos, [conCuerpo.id]);
});

test('el índice completo del curso siempre viaja, para que no invente nodos', () => {
  const { sistema } = construirSistema(paquete, { modo: 'socratico', nodoId: null, estado: {} });
  for (const nodo of paquete.indice.slice(0, 10)) {
    assert.ok(sistema.includes(nodo.id), `falta ${nodo.id} en el índice inyectado`);
  }
  assert.match(sistema, /SIN ESCRIBIR TODAVÍA/, 'los nodos pendientes deben ir marcados');
});

test('los cinco modos tienen prompt y el socrático es el predeterminado', () => {
  assert.equal(paquete.modo_por_defecto, 'socratico');
  for (const modo of paquete.modos) {
    assert.ok(paquete.prompts[`modo-${modo}`], `falta el prompt del modo ${modo}`);
    assert.ok(paquete.prompts[`modo-${modo}`].length > 400, `el prompt de ${modo} es sospechosamente corto`);
  }
  assert.ok(paquete.prompts['sistema-base'], 'falta el prompt de sistema base');
});

test('el prompt de cada modo lleva su restricción dura dentro', () => {
  assert.match(paquete.prompts['modo-socratico'], /nunca da la solución|no la das/i);
  assert.match(paquete.prompts['modo-revisar-artefacto'], /no devuelves su artefacto reescrito/i);
  assert.match(paquete.prompts['modo-explicar-de-otra-forma'], /no avanza materia|no introduces material/i);
  assert.match(paquete.prompts['modo-mas-practica'], /solución va oculta|nunca en el mismo mensaje/i);
  assert.match(paquete.prompts['modo-aplicar-a-mi-caso'], /no le hagas el trabajo/i);
});

// ─────────────────────────── Historial de la conversación ────────────────────

test('el historial se recorta y empieza siempre por un mensaje de usuario', () => {
  const historial = Array.from({ length: 30 }, (_, i) => ({
    role: i % 2 === 0 ? 'user' : 'assistant', content: `turno ${i}`,
  }));
  const mensajes = prepararMensajes(historial, 'la pregunta nueva');
  assert.ok(mensajes.length <= 13);
  assert.equal(mensajes[0].role, 'user');
  assert.equal(mensajes.at(-1).content, 'la pregunta nueva');
});

test('un historial que empieza por assistant se corrige', () => {
  const mensajes = prepararMensajes(
    [{ role: 'assistant', content: 'hola' }, { role: 'user', content: 'qué tal' }],
    'nueva',
  );
  assert.equal(mensajes[0].role, 'user');
});
