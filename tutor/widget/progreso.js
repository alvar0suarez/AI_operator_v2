/**
 * Página «Dónde vas». ESPECIFICACION.md §8 (el estado de progreso vive en el
 * almacenamiento del navegador) y §7.4 uso 1 (ella ve su propio histórico de dudas
 * por nodo, que es una forma de progreso muy real).
 *
 * Lo que esta página NO hace, y es deliberado (§2.7): no hay porcentaje de
 * completitud como nota, ni insignias, ni rachas, ni «llevas 5 días seguidos».
 * Muestra tres cosas y para: qué has terminado, qué toca ahora, y cómo va tu
 * portfolio. El progreso de verdad son los minutos que has medido y los seis
 * artefactos, y eso vive en ficheros tuyos, no aquí.
 */
(() => {
  'use strict';

  const CLAVE_ESTADO = 'cxia.estado.v1';
  const CLAVE_PREGUNTAS = 'cxia.preguntas.v1';

  function leer(clave, porDefecto) {
    try {
      const crudo = localStorage.getItem(clave);
      return crudo ? JSON.parse(crudo) : porDefecto;
    } catch {
      return porDefecto;
    }
  }

  const el = (etiqueta, props = {}, hijos = []) => {
    const n = document.createElement(etiqueta);
    for (const [k, v] of Object.entries(props)) {
      if (k === 'clase') n.className = v;
      else if (k === 'texto') n.textContent = v;
      else if (k === 'html') n.innerHTML = v;
      else n.setAttribute(k, v);
    }
    for (const h of [].concat(hijos)) if (h) n.append(h);
    return n;
  };

  function montar() {
    const destino = document.getElementById('cxia-progreso');
    if (!destino) return;

    const indice = window.CXIA_INDICE;
    if (!indice) {
      destino.append(el('p', { texto: 'No se ha podido cargar el índice del curso.' }));
      return;
    }

    const estado = leer(CLAVE_ESTADO, {});
    const completados = estado.completados || {};
    const intentados = estado.intentado || {};
    const preguntas = leer(CLAVE_PREGUNTAS, {});

    destino.replaceChildren();

    // ── Aviso honesto sobre dónde vive esto ──
    destino.append(el('div', { clase: 'admonition warning' }, [
      el('p', { clase: 'admonition-title', texto: 'Esto vive en este navegador' }),
      el('p', {
        texto: 'Lo que marcas aquí se guarda solo en el navegador que estés usando. Si abres '
          + 'el curso en el móvil, empieza en blanco; si borras los datos de navegación, se va. '
          + 'Al final de la página tienes cómo llevártelo de un sitio a otro.',
      }),
    ]));

    // ── Qué toca ahora ──
    const hechos = new Set(Object.keys(completados).filter((k) => completados[k]));
    const escritos = indice.filter((n) => n.estado === 'escrito');
    const siguiente = escritos.find(
      (n) => !hechos.has(n.id) && (n.requisitos || []).every((r) => hechos.has(r)),
    );

    destino.append(el('h2', { texto: 'Qué toca ahora' }));
    if (!siguiente) {
      destino.append(el('p', {
        texto: hechos.size === 0
          ? 'Todavía no has marcado nada. Se empieza por «Qué es este curso y qué no es».'
          : 'Has terminado todo lo que hay escrito. Los bloques 4, 5 y 6 se escriben después del piloto.',
      }));
    } else {
      const bloqueada = (siguiente.requisitos || []).some((r) => {
        const req = indice.find((n) => n.id === r);
        return req && req.bloqueante && !hechos.has(r);
      });
      destino.append(el('p', {}, [
        el('strong', {}, [el('a', { href: enlaceA(siguiente), texto: siguiente.titulo })]),
        el('span', { texto: ` — ${tipoLegible(siguiente.tipo)}, ${siguiente.duracion_min} min` }),
      ]));
      if (bloqueada) {
        destino.append(el('p', { clase: 'progreso-nota', texto: 'Antes tienes un nodo bloqueante sin terminar.' }));
      }
    }

    // ── Los bloques ──
    destino.append(el('h2', { texto: 'Por dónde has pasado' }));

    const bloques = [...new Set(indice.map((n) => n.bloque))].sort((a, b) => a - b);
    for (const b of bloques) {
      const nodos = indice.filter((n) => n.bloque === b);
      // El recuento va solo sobre el tronco. Las ramas de profundización son
      // opcionales (§6) y meterlas en el total haría que el bloque pareciera más
      // largo de lo que es, que es justo lo contrario de lo que hace falta aquí.
      const troncoB = nodos.filter((n) => n.estado === 'escrito' && n.tipo !== 'profundizacion');
      const hechosB = troncoB.filter((n) => hechos.has(n.id)).length;

      const det = el('details', { clase: 'progreso-bloque' });
      if (troncoB.length && hechosB < troncoB.length && hechosB > 0) det.setAttribute('open', 'open');

      const resumen = troncoB.length
        ? `Bloque ${b} — ${hechosB} de ${troncoB.length} terminados`
        : `Bloque ${b} — se escribe después del piloto`;
      det.append(el('summary', { texto: resumen }));

      const lista = el('ul', { clase: 'progreso-lista' });
      for (const n of nodos) {
        if (n.estado !== 'escrito') {
          lista.append(el('li', { clase: 'progreso-pendiente', texto: `${n.titulo} — sin escribir todavía` }));
          continue;
        }
        const marca = hechos.has(n.id) ? '✓' : '·';
        const li = el('li', { clase: hechos.has(n.id) ? 'progreso-hecho' : '' }, [
          el('span', { clase: 'progreso-marca', texto: marca }),
          el('a', { href: enlaceA(n), texto: n.titulo }),
        ]);
        const notas = [];
        if (n.tipo === 'profundizacion') notas.push('opcional');
        if (n.tiene_solucion) notas.push(intentados[n.id] ? 'intentado' : 'sin intentar');
        const nPreg = (preguntas[n.id] || []).length;
        if (nPreg) notas.push(`${nPreg} ${nPreg === 1 ? 'pregunta' : 'preguntas'} al tutor`);
        if (notas.length) li.append(el('span', { clase: 'progreso-nota', texto: ` — ${notas.join(' · ')}` }));
        lista.append(li);
      }
      det.append(lista);
      destino.append(det);
    }

    // ── El portfolio, que es el progreso de verdad ──
    destino.append(el('h2', { texto: 'Tu portfolio' }));
    destino.append(el('p', {
      texto: 'Esto es lo que de verdad mide si el curso te ha servido: seis documentos tuyos '
        + 'y los minutos que has medido. No viven aquí, viven en tus ficheros. Esta tabla solo '
        + 'te dice si has pasado por el nodo que los produce.',
    }));

    const tabla = el('table');
    tabla.append(el('thead', {}, [el('tr', {}, [
      el('th', { texto: 'Artefacto' }), el('th', { texto: 'Nodo' }), el('th', { texto: '' }),
    ])]));
    const tbody = el('tbody');
    for (const n of indice.filter((x) => x.tipo === 'artefacto')) {
      tbody.append(el('tr', {}, [
        el('td', { texto: n.titulo }),
        el('td', {}, [n.estado === 'escrito' ? el('a', { href: enlaceA(n), texto: `bloque ${n.bloque}` })
                                             : el('span', { texto: `bloque ${n.bloque}` })]),
        el('td', { texto: n.estado !== 'escrito' ? 'después del piloto' : (hechos.has(n.id) ? 'nodo terminado' : '') }),
      ]));
    }
    tabla.append(tbody);
    destino.append(tabla);

    // ── Llevárselo a otro sitio ──
    destino.append(el('h2', { texto: 'Llevarte esto a otro dispositivo' }));
    destino.append(el('p', {
      texto: 'Copia el texto de abajo y pégalo en el mismo sitio del otro navegador. Es todo tu '
        + 'estado: lo que has marcado y lo que le has preguntado al tutor.',
    }));

    const caja = el('textarea', { clase: 'progreso-estado', rows: '4', spellcheck: 'false' });
    caja.value = JSON.stringify({ estado, preguntas });

    const importar = el('button', { clase: 'progreso-boton', type: 'button', texto: 'Cargar lo que haya pegado aquí' });
    const aviso = el('p', { clase: 'progreso-nota' });
    importar.addEventListener('click', () => {
      try {
        const d = JSON.parse(caja.value);
        if (!d || typeof d !== 'object') throw new Error('formato');
        localStorage.setItem(CLAVE_ESTADO, JSON.stringify(d.estado || {}));
        localStorage.setItem(CLAVE_PREGUNTAS, JSON.stringify(d.preguntas || {}));
        aviso.textContent = 'Cargado. Recargando…';
        setTimeout(() => location.reload(), 600);
      } catch {
        aviso.textContent = 'Eso no tiene la pinta de ser un estado del curso. Cópialo entero, desde la llave inicial.';
      }
    });
    destino.append(caja, importar, aviso);
  }

  function enlaceA(nodo) {
    const sub = nodo.tipo === 'profundizacion' ? 'profundizacion/' : '';
    return `bloque-${nodo.bloque}/${sub}${nodo.id}/`;
  }

  function tipoLegible(t) {
    return { concepto: 'concepto', ejercicio: 'ejercicio', caso: 'caso',
             artefacto: 'artefacto', profundizacion: 'profundización' }[t] || t;
  }

  if (window.document$ && typeof window.document$.subscribe === 'function') {
    window.document$.subscribe(montar);
  } else {
    document.addEventListener('DOMContentLoaded', montar);
  }
})();
