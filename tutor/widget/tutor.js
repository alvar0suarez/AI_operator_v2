/**
 * Widget del tutor. ESPECIFICACION.md §7.
 *
 * Todo lo que hace aquí el navegador es interfaz y estado local. La llamada a la
 * API va SIEMPRE por la función serverless: la clave no puede estar en el cliente
 * (§7.5). Este fichero no conoce ninguna clave y no habla con nadie más que con
 * el endpoint propio.
 *
 * El estado de progreso vive en el almacenamiento del navegador (§8). Es un
 * registro de trabajo, no una puntuación: aquí no hay insignias, ni rachas, ni
 * niveles superados (§2.7).
 */
(() => {
  'use strict';

  const ENDPOINT = '/api/tutor';
  const CLAVE_ESTADO = 'cxia.estado.v1';
  const CLAVE_PREGUNTAS = 'cxia.preguntas.v1';

  const MODOS = [
    { id: 'socratico', etiqueta: 'Sácame del atasco',
      ayuda: 'Preguntas que te acercan. No te da la solución, y es a propósito.' },
    { id: 'explicar-de-otra-forma', etiqueta: 'Explícamelo de otra forma',
      ayuda: 'Reformula este mismo nodo. No avanza materia.' },
    { id: 'revisar-artefacto', etiqueta: 'Revisa mi artefacto',
      ayuda: 'Feedback contra la rúbrica. Señala, no te lo reescribe.' },
    { id: 'mas-practica', etiqueta: 'Ponme más práctica',
      ayuda: 'Ejercicios nuevos del mismo tipo, con la solución escondida.' },
    { id: 'aplicar-a-mi-caso', etiqueta: 'Aplícalo a mi caso',
      ayuda: 'Tú describes la situación con tus palabras. Sin pegar datos.' },
  ];

  // ── Estado local ───────────────────────────────────────────────────────────

  function leer(clave, porDefecto) {
    try {
      const crudo = localStorage.getItem(clave);
      return crudo ? JSON.parse(crudo) : porDefecto;
    } catch {
      return porDefecto;   // navegación privada, almacenamiento bloqueado, etc.
    }
  }

  function escribir(clave, valor) {
    try { localStorage.setItem(clave, JSON.stringify(valor)); } catch { /* se sigue igual */ }
  }

  const estado = () => leer(CLAVE_ESTADO, { completados: {}, intentado: {}, artefactos: {}, bitacora: '' });
  const guardarEstado = (e) => escribir(CLAVE_ESTADO, e);

  // ── Utilidades ─────────────────────────────────────────────────────────────

  function nodoActual() {
    // El id del nodo es el nombre del fichero: /bloque-3/b3-m4-sabotaje/
    const m = location.pathname.match(/\/(b[0-6]-[mp]\d{1,2}-[a-z0-9-]+)\/?$/);
    return m ? m[1] : null;
  }

  const el = (etiqueta, props = {}, hijos = []) => {
    const n = document.createElement(etiqueta);
    for (const [k, v] of Object.entries(props)) {
      if (k === 'clase') n.className = v;
      else if (k === 'texto') n.textContent = v;
      else n.setAttribute(k, v);
    }
    for (const h of [].concat(hijos)) n.append(h);
    return n;
  };

  // ── Interfaz ───────────────────────────────────────────────────────────────

  function montar() {
    const nodoId = nodoActual();
    if (!nodoId) return;
    if (document.querySelector('.tutor')) return;

    const contenedor = document.querySelector('.md-content__inner') || document.body;

    const panel = el('section', { clase: 'tutor', 'aria-label': 'Tutor del curso' });
    const cabecera = el('button', { clase: 'tutor__abrir', type: 'button',
      'aria-expanded': 'false', texto: 'Preguntar al tutor' });
    const cuerpo = el('div', { clase: 'tutor__cuerpo', hidden: 'hidden' });

    cabecera.addEventListener('click', () => {
      const abierto = cuerpo.hasAttribute('hidden');
      if (abierto) cuerpo.removeAttribute('hidden'); else cuerpo.setAttribute('hidden', 'hidden');
      cabecera.setAttribute('aria-expanded', String(abierto));
      cabecera.textContent = abierto ? 'Cerrar el tutor' : 'Preguntar al tutor';
    });

    // Selector de modo. El socrático va primero y seleccionado: §9 lo marca como
    // mitigación de que el tutor se convierta en muleta.
    const modos = el('div', { clase: 'tutor__modos', role: 'radiogroup',
      'aria-label': 'Qué quieres del tutor' });
    let modoActivo = MODOS[0].id;
    const ayuda = el('p', { clase: 'tutor__ayuda', texto: MODOS[0].ayuda });

    for (const modo of MODOS) {
      const b = el('button', { clase: 'tutor__modo', type: 'button', role: 'radio',
        'data-modo': modo.id, texto: modo.etiqueta,
        'aria-checked': String(modo.id === modoActivo) });
      b.addEventListener('click', () => {
        modoActivo = modo.id;
        ayuda.textContent = modo.ayuda;
        modos.querySelectorAll('.tutor__modo').forEach((x) =>
          x.setAttribute('aria-checked', String(x.dataset.modo === modoActivo)));
      });
      modos.append(b);
    }

    const conversacion = el('div', { clase: 'tutor__conversacion', 'aria-live': 'polite' });
    const entrada = el('textarea', { clase: 'tutor__entrada', rows: '3',
      placeholder: 'Cuenta qué has intentado y dónde te has quedado. Sin datos de clientes.' });
    const enviar = el('button', { clase: 'tutor__enviar', type: 'button', texto: 'Preguntar' });

    const pie = el('p', { clase: 'tutor__nota', texto:
      'El tutor no te va a dar la solución de un ejercicio. Si lo hiciera, te quitaría ' +
      'justo lo que has venido a aprender.' });

    cuerpo.append(modos, ayuda, conversacion, entrada, enviar, pie, cajaProgreso(nodoId), historial(nodoId));
    panel.append(cabecera, cuerpo);
    contenedor.append(panel);

    const conversar = () => preguntar({ nodoId, entrada, enviar, conversacion, modo: () => modoActivo });
    enviar.addEventListener('click', conversar);
    entrada.addEventListener('keydown', (ev) => {
      if (ev.key === 'Enter' && (ev.metaKey || ev.ctrlKey)) conversar();
    });
  }

  /** Marcar el nodo como completado y el ejercicio como intentado. Sin puntos. */
  function cajaProgreso(nodoId) {
    const caja = el('div', { clase: 'tutor__progreso' });
    const e = estado();

    const casilla = (clave, etiqueta, ayuda) => {
      const id = `tutor-${clave}-${nodoId}`;
      const input = el('input', { type: 'checkbox', id });
      input.checked = Boolean(e[clave]?.[nodoId]);
      input.addEventListener('change', () => {
        const actual = estado();
        actual[clave] = actual[clave] || {};
        actual[clave][nodoId] = input.checked;
        guardarEstado(actual);
      });
      const label = el('label', { for: id, texto: etiqueta });
      const nota = el('span', { clase: 'tutor__ayuda', texto: ayuda });
      return el('div', { clase: 'tutor__casilla' }, [input, label, nota]);
    };

    caja.append(
      casilla('intentado', 'Ya lo he intentado',
        'Hasta que no marques esto, el tutor no comenta la solución de este ejercicio.'),
      casilla('completados', 'Nodo terminado',
        'Sirve para que el tutor sepa qué has cubierto y no te adelante materia.'),
    );
    return caja;
  }

  /** Su propio histórico de dudas en este nodo (§7.4, uso 1). */
  function historial(nodoId) {
    const previas = leer(CLAVE_PREGUNTAS, {})[nodoId] || [];
    const caja = el('details', { clase: 'tutor__historial' });
    caja.append(el('summary', { texto: `Lo que has preguntado aquí (${previas.length})` }));
    if (previas.length === 0) {
      caja.append(el('p', { clase: 'tutor__ayuda', texto: 'Todavía nada.' }));
    } else {
      const lista = el('ul');
      for (const p of previas.slice(-20).reverse()) {
        lista.append(el('li', { texto: `${p.fecha.slice(0, 10)} · ${p.pregunta}` }));
      }
      caja.append(lista);
    }
    return caja;
  }

  function anotarPregunta(nodoId, pregunta, modo) {
    const todas = leer(CLAVE_PREGUNTAS, {});
    todas[nodoId] = todas[nodoId] || [];
    todas[nodoId].push({ pregunta, modo, fecha: new Date().toISOString() });
    escribir(CLAVE_PREGUNTAS, todas);
  }

  // ── Conversación ───────────────────────────────────────────────────────────

  const historialTurnos = [];

  async function preguntar({ nodoId, entrada, enviar, conversacion, modo }) {
    const mensaje = entrada.value.trim();
    if (!mensaje) return;

    const modoActivo = modo();
    entrada.value = '';
    enviar.disabled = true;
    enviar.textContent = 'Pensando…';

    conversacion.append(el('div', { clase: 'tutor__turno tutor__turno--tuyo', texto: mensaje }));
    const respuesta = el('div', { clase: 'tutor__turno tutor__turno--tutor' });
    conversacion.append(respuesta);

    anotarPregunta(nodoId, mensaje, modoActivo);

    try {
      const r = await fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({
          modo: modoActivo, nodo_id: nodoId, mensaje,
          historial: historialTurnos.slice(-12), estado: estado(),
        }),
      });

      if (!r.ok || !r.body) {
        // Si el sitio está publicado en un hosting sin funciones (GitHub Pages, por
        // ejemplo), aquí no hay endpoint y llega el 404 del propio sitio. Decirlo,
        // en vez de fingir un fallo pasajero que la haga reintentar sin sentido.
        if (r.status === 404 || r.status === 405) {
          respuesta.textContent = 'El tutor no está activo en esta instalación del curso. '
            + 'Todo lo demás funciona igual: los nodos, los ejercicios y los sabotajes no '
            + 'lo necesitan.';
          return;
        }
        const err = await r.json().catch(() => ({}));
        respuesta.textContent = err.error || 'El tutor no ha podido responder. Vuelve a intentarlo.';
        return;
      }

      const completo = await leerFlujo(r.body, respuesta);
      historialTurnos.push({ role: 'user', content: mensaje },
                           { role: 'assistant', content: completo });
    } catch {
      respuesta.textContent = 'No se ha podido conectar con el tutor.';
    } finally {
      enviar.disabled = false;
      enviar.textContent = 'Preguntar';
    }
  }

  /** Lee el SSE de la función y va pintando. */
  async function leerFlujo(cuerpo, destino) {
    const lector = cuerpo.getReader();
    const decodificador = new TextDecoder();
    let resto = '';
    let completo = '';

    while (true) {
      const { done, value } = await lector.read();
      if (done) break;
      resto += decodificador.decode(value, { stream: true });

      const bloques = resto.split('\n\n');
      resto = bloques.pop() || '';

      for (const bloque of bloques) {
        const tipo = /^event: (.+)$/m.exec(bloque)?.[1];
        const datosCrudos = /^data: (.+)$/m.exec(bloque)?.[1];
        if (!tipo || !datosCrudos) continue;
        let datos;
        try { datos = JSON.parse(datosCrudos); } catch { continue; }

        if (tipo === 'aviso-datos') {
          // Aviso, nunca bloqueo silencioso (§7.3).
          destino.before(el('div', { clase: 'tutor__aviso', texto: datos.texto }));
        } else if (tipo === 'texto') {
          completo += datos.texto;
          destino.textContent = completo;
        } else if (tipo === 'nodos-inventados') {
          destino.textContent = datos.texto_corregido;
          completo = datos.texto_corregido;
        } else if (tipo === 'fin') {
          destino.textContent = datos.completo;
          completo = datos.completo;
        } else if (tipo === 'error') {
          destino.textContent = datos.texto;
        }
      }
    }
    return completo;
  }

  // MkDocs Material con navegación instantánea reemplaza el contenido sin recargar.
  if (window.document$ && typeof window.document$.subscribe === 'function') {
    window.document$.subscribe(montar);
  } else {
    document.addEventListener('DOMContentLoaded', montar);
  }
})();
