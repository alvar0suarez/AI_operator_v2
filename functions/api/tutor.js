// Punto de entrada de la función del tutor en Cloudflare Pages.
//
// Cloudflare publica automáticamente como /api/tutor todo lo que esté en
// functions/api/tutor.js, así que este fichero tiene que vivir en la raíz del
// repositorio aunque el código de verdad esté en tutor/serverless/.
//
// La clave de API se configura como variable de entorno del proyecto en el panel
// de Cloudflare. Nunca aquí, y nunca en el cliente (ESPECIFICACION.md §7.5).
export { onRequest } from '../../tutor/serverless/funciones/tutor.js';
