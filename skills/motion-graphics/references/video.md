# Exportación de video

Confirmar la especificación desde el pedido: formato, relación de aspecto, duración, fps y audio. Si no se especifican, elegir defaults razonables y declararlos; para una pieza social vertical pueden ser 1080×1920, 30 fps, 5 segundos y sin audio. Esos valores no son requisitos universales.

Comprobar herramientas y codecs disponibles antes de elegir pipeline. Para un proyecto existente usar su sistema de render; para uno nuevo elegir un pipeline que permita fuentes editables y tiempo determinista. No instalar dependencias globales ni prometer un codec sin comprobarlo.

Renderizar primero una muestra corta o frames representativos. En la exportación final verificar con metadata y reproducción cuando sea posible: dimensiones, fps, duración, frames inicial/final, clipping y sincronía de audio. Para un loop verificar también la unión final-inicio. MP4 es una entrega común; transparencia requiere un formato/codec que la preserve. No asumir que MP4 conserva alpha.

Conservar fuente, assets y comandos para reproducir la entrega. No subir ni publicar el resultado salvo que forme parte del pedido.
