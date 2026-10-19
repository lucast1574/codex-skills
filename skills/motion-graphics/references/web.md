# Animación web

Separar composición de tiempo: definir duración y estados para poder inspeccionar frames concretos. Para geometría y texto simples usar SVG/CSS; para escenas procedurales usar canvas. Usar las bibliotecas existentes cuando aporten algo necesario.

Animar transformaciones y opacidad cuando convenga; evitar cambios de layout repetidos. En interfaces web ofrecer un estado legible con `prefers-reduced-motion`, y evitar que la animación bloquee interacción. Para previews independientes añadir play/pause y replay cuando facilite revisión.

Conservar una fuente editable y assets locales. Si se requiere render determinista, esperar a fuentes/assets y fijar semilla de cualquier aleatoriedad antes de capturar.
