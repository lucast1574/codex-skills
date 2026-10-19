# Trazado y limpieza

Primero comprobar herramientas disponibles y las convenciones del proyecto. Opciones: un trazador como Potrace para siluetas monocromas, VTracer para ilustración a color o herramientas vectoriales ya disponibles. Para formas simples suele dar mejor resultado reconstruir paths o primitivas manualmente. Si faltan herramientas, elegir una alternativa local o una dependencia aislada adecuada al alcance; no subir imágenes a un conversor externo por defecto.

Para siluetas, ajustar umbral y conservar huecos con reglas de relleno correctas. Para color, reducir la paleta solo si es compatible con el diseño; comparar bordes y evitar zonas duplicadas o solapes que cambien el resultado. Para líneas, decidir si se requieren trazos centrales editables o contornos cerrados: un trazado de contornos no produce automáticamente centerlines.

Evitar eliminar detalles de marca como ruido. Revisar a tamaño de uso para decidir cuánto simplificar. Usar curvas limpias y mantener transparencias deliberadas. Organizar paths por color o parte cuando facilite editar sin aumentar mucho el archivo.

Validar el XML y renderizar con una herramienta disponible. Buscar elementos raster, referencias externas y fuentes dependientes. Un `viewBox` correcto debe contener el dibujo sin recortarlo ni dejar márgenes accidentales. Si se exporta a otro formato, verificar de nuevo el archivo resultante.
