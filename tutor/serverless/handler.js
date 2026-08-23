/**
 * El tutor. ESPECIFICACION.md §7.
 *
 * La llamada a la API va SIEMPRE por aquí, nunca desde el navegador: la clave no
 * puede estar en el cliente (§7.5). Este módulo es agnóstico del proveedor de
 * serverless; los adaptadores concretos viven en `funciones/`.
 *
 * Identificadores de modelo y parámetros: consultados en la documentación oficial
 * antes de implementar, como exige §7.5. No se asumen.
 *   https://docs.claude.com/en/api/overview
 */

import Anthropic from '@anthropic-ai/sdk';
import { construirSistema, prepararMensajes } from './contexto.js';
import { revisarDatos, revisarCitas } from './guardarrailes.js';
import paquete from './curso.json' with { type: 'json' };

const MODELO = 'claude-opus-5';
const MAX_TOKENS = 64000;

// El tutor conversa; no está resolviendo el ejercicio por ella. Esfuerzo medio da
// respuestas rápidas y suficientemente pensadas, que es lo que hace falta a las
// nueve de la noche.
const ESFUERZO = 'medium';

const IDS_VALIDOS = new Set(paquete.indice.map((n) => n.id));
const MODOS = new Set(paquete.modos);

class ErrorDePeticion extends Error {
  constructor(mensaje, estado = 400) {
    super(mensaje);
    this.estado = estado;
  }
}

function validar(cuerpo) {
  const mensaje = String(cuerpo?.mensaje || '').trim();
  if (!mensaje) throw new ErrorDePeticion('Falta el mensaje.');
  if (mensaje.length > 20000) throw new ErrorDePeticion('El mensaje es demasiado largo.');

  const modo = cuerpo?.modo || paquete.modo_por_defecto;
  if (!MODOS.has(modo)) throw new ErrorDePeticion(`Modo desconocido: ${modo}`);

  const nodoId = cuerpo?.nodo_id || null;
  if (nodoId && !IDS_VALIDOS.has(nodoId)) throw new ErrorDePeticion(`Nodo desconocido: ${nodoId}`);

  return { mensaje, modo, nodoId, historial: cuerpo?.historial || [], estado: cuerpo?.estado || {} };
}

/**
 * Registro de preguntas (§7.4): {nodo_id, pregunta, timestamp, modo}.
 * Se guarda la versión ENMASCARADA, nunca el mensaje original.
 *
 * Tres usos, y los tres importan: ella ve su histórico de dudas por nodo; nosotros
 * vemos dónde se atasca la gente, que es el input directo para escribir el bloque 4;
 * y lo que se repite mucho se promueve a nodo de profundización permanente.
 */
async function registrarPregunta(entorno, registro) {
  if (!entorno?.REGISTRO_PREGUNTAS) return;   // sin almacén configurado, no se registra
  try {
    await entorno.REGISTRO_PREGUNTAS.put(
      `${registro.timestamp}-${registro.nodo_id || 'sin-nodo'}`,
      JSON.stringify(registro),
    );
  } catch (e) {
    // El registro es para nosotros. Que falle nunca puede romperle la sesión a ella.
    console.error('No se pudo registrar la pregunta:', e?.message);
  }
}

/**
 * Atiende una petición del tutor. Devuelve una Response estándar.
 *
 * @param {Request} peticion
 * @param {object} entorno  variables del proveedor: ANTHROPIC_API_KEY, REGISTRO_PREGUNTAS
 */
export async function atender(peticion, entorno) {
  if (peticion.method === 'OPTIONS') return new Response(null, { status: 204, headers: cabeceras() });
  if (peticion.method !== 'POST') return json({ error: 'Método no permitido.' }, 405);

  let datos;
  try {
    datos = validar(await peticion.json());
  } catch (e) {
    return json({ error: e.message }, e.estado || 400);
  }

  const clave = entorno?.ANTHROPIC_API_KEY;
  if (!clave) {
    return json({ error: 'El tutor no está configurado: falta la clave de API en el servidor.' }, 503);
  }

  // ── Guardarraíl 2, antes de cualquier llamada a la API ──
  const revision = revisarDatos(datos.mensaje);

  await registrarPregunta(entorno, {
    nodo_id: datos.nodoId,
    pregunta: revision.texto,          // la enmascarada, siempre
    timestamp: new Date().toISOString(),
    modo: datos.modo,
    datos_detectados: revision.senales.map((s) => s.tipo),
  });

  const { sistema } = construirSistema(paquete, {
    modo: datos.modo,
    nodoId: datos.nodoId,
    estado: datos.estado,
  });

  const cliente = new Anthropic({ apiKey: clave });

  try {
    const flujo = await cliente.messages.stream({
      model: MODELO,
      max_tokens: MAX_TOKENS,
      system: [{ type: 'text', text: sistema, cache_control: { type: 'ephemeral' } }],
      thinking: { type: 'adaptive' },
      output_config: { effort: ESFUERZO },
      messages: prepararMensajes(datos.historial, revision.texto),
    });

    return new Response(construirSSE(flujo, revision), {
      headers: {
        ...cabeceras(),
        'content-type': 'text/event-stream; charset=utf-8',
        'cache-control': 'no-store',
      },
    });
  } catch (e) {
    console.error('Fallo llamando a la API:', e?.message);
    const estado = e?.status === 429 ? 429 : 502;
    return json({ error: 'El tutor no ha podido responder ahora mismo. Vuelve a intentarlo.' }, estado);
  }
}

/**
 * Convierte el flujo del SDK en SSE para el navegador.
 *
 * El aviso de RGPD va PRIMERO y como evento propio: §7.3 exige aviso, no bloqueo
 * silencioso, y ella tiene que verlo antes que la respuesta.
 */
function construirSSE(flujo, revision) {
  const codificador = new TextEncoder();

  return new ReadableStream({
    async start(controlador) {
      const enviar = (tipo, datos) => {
        controlador.enqueue(codificador.encode(`event: ${tipo}\ndata: ${JSON.stringify(datos)}\n\n`));
      };

      try {
        if (revision.salta) {
          enviar('aviso-datos', { texto: revision.aviso, senales: revision.senales });
        }

        let completo = '';
        for await (const evento of flujo) {
          if (evento.type === 'content_block_delta' && evento.delta?.type === 'text_delta') {
            completo += evento.delta.text;
            enviar('texto', { texto: evento.delta.text });
          }
        }

        // ── Guardarraíl 3: se revisa la respuesta entera antes de cerrar ──
        const citas = revisarCitas(completo, IDS_VALIDOS);
        if (citas.inventados.length) {
          enviar('nodos-inventados', { ids: citas.inventados, texto_corregido: citas.texto });
        }

        enviar('fin', { completo: citas.texto });
      } catch (e) {
        console.error('Fallo durante el flujo:', e?.message);
        enviar('error', { texto: 'Se ha cortado la respuesta. Vuelve a preguntar.' });
      } finally {
        controlador.close();
      }
    },
  });
}

function cabeceras() {
  return {
    'access-control-allow-origin': '*',
    'access-control-allow-methods': 'POST, OPTIONS',
    'access-control-allow-headers': 'content-type',
  };
}

function json(cuerpo, estado = 200) {
  return new Response(JSON.stringify(cuerpo), {
    status: estado,
    headers: { ...cabeceras(), 'content-type': 'application/json; charset=utf-8' },
  });
}

export const _paraPruebas = { validar, MODELO, ESFUERZO, IDS_VALIDOS, ErrorDePeticion };
