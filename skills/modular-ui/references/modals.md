# Modales reutilizables

## Elegir la superficie

Usar un modal para una tarea acotada que necesita contexto de la pantalla. Una ficha larga, un flujo de varias etapas o contenido enlazable puede requerir una página o drawer; no encerrar todo en un popup. Preferir un único diálogo con cambio de contenido cuando un segundo modal solo añade complejidad.

## Separar estructura y tarea

La primitiva `Modal`/`Dialog` maneja apertura, portal, semántica, foco, fondo inerte, capas y bloqueo de scroll. Un componente de funcionalidad como `EditLeadDialog` posee el formulario, validación y la operación; el contenedor de página decide qué registro abrir y cómo refrescar datos.

Reutilizar la API existente. Si hace falta una nueva, ofrecer un contrato pequeño: apertura controlada, callback de cambio/cierre, título y contenido. Añadir descripción, tamaño o pie solo cuando tengan uso real. Los botones de negocio pertenecen al contenido o al pie compuesto, no a un catálogo de flags en la primitiva.

## Interacción

- El diálogo tiene nombre accesible vinculado al título visible. Usar la semántica de la primitiva adoptada; declarar modalidad solo si el fondo realmente está bloqueado.
- Al abrir, colocar el foco dentro según la tarea; para contenido largo, el encabezado puede ser mejor que un campo situado abajo. En una confirmación destructiva, favorecer la acción menos peligrosa.
- Tab y Shift+Tab permanecen dentro. Al cerrar, restaurar foco al activador si existe o a un destino lógico del flujo. Proporcionar un control visible para cerrar.
- Escape cierra el diálogo superior. Si hay un dropdown abierto dentro, el primer Escape cierra ese dropdown; no debe cerrar también el diálogo ni perder el borrador.
- Cerrar por clic exterior solo cuando corresponda. Si hay cambios sin guardar, pasar la petición por la misma guarda que Escape y el botón cerrar. No descartar un formulario silenciosamente.
- Distinguir clic real en backdrop de un gesto que empezó dentro y terminó fuera. Portales de menús y calendarios se consideran parte de la interacción del diálogo.
- El fondo no recibe foco ni clics. Liberar scroll y listeners al desmontar; restaurar correctamente si hay capas anidadas. No establecer `aria-hidden` sobre un ancestro del propio diálogo.
- Sin contornos ni anillos: foco visible mediante fondo, texto o subrayado, también en el botón cerrar.

## Formularios y solicitudes

Separar borrador y registro guardado. Cambiar de registro no debe conservar por accidente valores o errores del anterior. No ejecutar guardados desde efectos que observan campos.

Envío único con estado de carga; evitar dobles clics y respuestas atrasadas que actualizan otro registro. En un error, conservar datos, explicar qué pasó y permitir reintentar. Cerrar y mostrar éxito solo cuando el servidor confirma. Cancelar la UI no garantiza cancelar una escritura ya enviada: no prometerlo.

Usar un formulario HTML real y acciones con tipo explícito; evitar formularios anidados y envíos accidentales al cerrar o abrir un selector.

## Tamaño, scroll y móvil

Encabezado y pie permanecen disponibles; el cuerpo largo puede desplazarse dentro. Calcular altura con viewport dinámico y espacio seguro cuando aplique. Comprobar teclado móvil, errores multilínea y campos/menús junto al borde. No recortar el dropdown dentro de un contenedor con overflow.

## Verificación que sí aporta

Probar el ciclo abrir → editar → error/reintento → guardar → cerrar → reabrir. Probar Escape, tabulación, devolución de foco, cierre exterior y formulario sucio. Si hay capas, comprobar que cerrar el selector no cierra el modal y que la página recupera scroll/foco al terminar.

Referencia primaria para semántica y teclado: [W3C WAI-ARIA APG, Dialog Modal](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/). Los estilos de foco siguen las preferencias de Lucas; conservar el comportamiento accesible.
