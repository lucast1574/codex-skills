---
name: imagen-a-vector
description: Convertir una imagen raster a vectores editables, especialmente logos, iconos e ilustraciones; entregar SVG con trazados reales.
---

# Imagen a vector

Inspeccionar la imagen original antes de convertirla. Preservar proporciones, huecos, transparencia y rasgos distintivos. Determinar si conviene trazado automático, reconstrucción geométrica manual o simplificación estilizada. Para fotografías, explicar el nivel de simplificación elegido; una vectorización no conserva necesariamente toda su textura.

Consultar [trazado.md](references/trazado.md) cuando se necesite un trazador o limpieza de paths. Usar herramientas vectoriales para esta conversión explícita; generar otro bitmap no satisface el pedido.

Entregar SVG con `viewBox` coherente, trazados o formas editables y sin el raster original incrustado mediante `<image>` o data URI. Si la entrega exige autonomía, no dejar fuentes ni recursos externos necesarios para renderizarla. Para texto de marca, conservar el lettering mediante trazado o fuente identificada; no reemplazarlo silenciosamente con una fuente parecida. Preservar una versión con texto editable si se solicita.

Comparar un render del SVG con la imagen original al tamaño de uso y ampliado: contorno, colores, huecos, alineación y detalles. Comprobar que el archivo es SVG válido y no un bitmap envuelto. Simplificar nodos solo si mejora la edición sin deformar el diseño. Informar diferencias relevantes y aproximaciones.

Mantener el original intacto. Entregar SVG y un preview cuando ayude; generar PDF vectorial, EPS u otros formatos solo si se piden y comprobar que la exportación conserva los vectores.
