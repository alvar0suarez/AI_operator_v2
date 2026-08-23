// Adaptador para Vercel Edge Functions.
import { atender } from '../handler.js';

export const config = { runtime: 'edge' };

export default async function handler(peticion) {
  return atender(peticion, process.env);
}
