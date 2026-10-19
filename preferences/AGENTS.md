# Preferencias globales de Lucas para interfaces

- No usar focus outlines ni focus rings en ningún proyecto: landings, aplicaciones, paneles administrativos o componentes. Evitar también box-shadows que simulen un anillo de foco. Se permite `outline: none` para desactivar el estilo nativo.
- Conservar la navegación por teclado y comunicar el foco con cambios sutiles de fondo, color, subrayado o contraste integrados en el diseño, sin contornos ni anillos.
- Selectores, dropdowns y menús deben usar componentes personalizados, reutilizables y tematizables, coherentes con la marca. No entregar la apariencia nativa del navegador ni menús planos sin diseño. Mantener etiquetas, estados seleccionados, Escape, navegación por flechas y cierre al pulsar fuera.
- El botón «Cerrar sesión» debe estar únicamente dentro de la página de perfil o cuenta del usuario; nunca en la sidebar, en un menú de la sidebar ni como acción directa de navegación. La sidebar puede incluir un acceso a «Mi perfil».
- Nunca usar emojis como iconos o decoración en interfaces web, landings, aplicaciones o paneles, ni en móvil ni en escritorio. Usar siempre iconos SVG coherentes, reutilizables y del mismo sistema visual; tampoco sustituirlos por glifos Unicode que puedan renderizarse como emoji.
- Nunca añadir botones ni controles para pausar o activar animaciones en landings o interfaces. Respetar automáticamente `prefers-reduced-motion` del navegador, sin controles visibles de reproducción o pausa.
