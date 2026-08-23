// Adaptador para Cloudflare Pages Functions.
// Ruta pública: /api/tutor  (fichero: functions/api/tutor.js en el despliegue)
//
// La clave vive en las variables de entorno del proveedor y NUNCA en el cliente
// (ESPECIFICACION.md §7.5). REGISTRO_PREGUNTAS es un KV namespace opcional para
// el registro de §7.4.
import { atender } from '../handler.js';

export const onRequest = (contexto) => atender(contexto.request, contexto.env);
