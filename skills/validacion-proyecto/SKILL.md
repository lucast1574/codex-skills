---
name: validacion-proyecto
description: Seleccionar y ejecutar los checks de un proyecto para validar cambios de código o diagnosticar CI, con evidencia breve de resultados.
---

# Validación del proyecto

Determinar los checks desde las instrucciones aplicables, scripts existentes y configuración de CI. Leer solo los archivos necesarios para identificar comandos y alcance; no aplicar reglas de otro repositorio.

Relacionar el diff con los checks requeridos y los riesgos de comportamiento. Preferir los scripts oficiales del repo y las pruebas existentes. Para una corrección reversible de bajo impacto, no crear tests que solo reproduzcan la implementación. Completar los checks obligatorios aunque el cambio sea pequeño.

Ejecutar checks independientes en paralelo solo si no compiten por servicios, archivos o recursos compartidos. No ejecutar comandos de despliegue, publicación o cambios de datos como parte de una validación rutinaria. Reutilizar los helpers existentes; añadir un script nuevo solo si evita trabajo determinista repetido y entra en el alcance solicitado.

Guardar logs largos en el área de trabajo, mostrar únicamente fallos relevantes y su ubicación. Conservar códigos de salida. Distinguir fallo del cambio, fallo preexistente y bloqueo del entorno; no declarar éxito cuando un check fue omitido o no pudo ejecutarse.

Corregir fallos dentro del alcance y repetir los checks afectados. Ampliar pruebas solo cuando surjan cambios, fallos o dudas concretas. Entregar comandos, resultados y limitaciones materiales en un resumen breve.
