// Adaptador para Netlify Functions (runtime de Deno/Node con Web API).
// Ruta pública: /api/tutor
import { atender } from '../handler.js';

export default async (peticion) => atender(peticion, process.env);

export const config = { path: '/api/tutor' };
