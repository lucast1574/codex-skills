# Organización modular

## Respetar el proyecto

Inspeccionar su árbol, imports, puntos de entrada, pruebas y límites antes de proponer carpetas. Conservar la arquitectura existente si funciona. No imponer este ejemplo ni mover archivos solo por estética.

Una opción para un frontend por funcionalidades, cuando encaje:

```text
src/
  app/                    # composición, rutas y providers
  features/
    leads/
      components/         # UI específica del flujo
      model/              # tipos, reglas y transiciones puras
      api/                # acceso a datos de esa funcionalidad
  shared/
    ui/                   # Dialog, Field, Select, Button
    lib/                  # utilidades sin conocimiento del negocio
    api/                  # transporte y errores comunes
    theme/                # tokens y temas
```

Si existen `components/ui`, `lib` y `features`, reutilizarlos: no crear un segundo `shared/ui` paralelo. Mantener código que cambia junto cerca; no separar cada función en un archivo ni acumular todo en `utils.ts`, `common` o `helpers`.

## Dirección de dependencias

`app` compone funcionalidades; las funcionalidades consumen primitivas compartidas. Una primitiva no importa una funcionalidad ni conoce su API. La lógica pura de negocio no depende de React/DOM ni de transporte. Cruzar funcionalidades por contratos explícitos o composición superior; evitar ciclos y un store global usado como bus de eventos.

Exportar una superficie pública pequeña cuando ayude a ocultar detalles. Evitar barrels indiscriminados que introduzcan ciclos, ejecuten código lateral o mezclen módulos de servidor y navegador.

## Backend

Agrupar por capacidades del negocio cuando lo permita el framework: interfaz HTTP/DTO, caso de uso o servicio y acceso a datos. El controlador traduce la petición y la respuesta; el servicio decide reglas y permisos; el adaptador conserva detalles de persistencia/proveedores.

No crear una interfaz y clase vacías por cada operación. Extraer un adaptador cuando exista una dependencia externa, una variante real o un límite comprobable que lo justifique. Mantener efectos y transacciones donde se puedan razonar; separar funciones no debe romper atomicidad.

Compartir contratos seguros entre frontend y backend cuando el proyecto lo admita; no importar configuración privada, ORM ni código de servidor en el paquete de UI. La validación del cliente ayuda al usuario, la del servidor sigue siendo la autoridad.

## Antes de extraer una abstracción

Preguntar qué responsabilidad comparten los consumidores, qué variaciones son reales y quién controla el estado. Si obliga a una larga lista de booleanos, callbacks cruzados o excepciones por pantalla, dividir responsabilidades o mantener la solución local.

Separar transformaciones puras de I/O: por ejemplo, `buildLeadPayload(draft)` produce datos y el adaptador los envía; no usar una función que calcula, hace fetch, cierra el modal y navega a la vez.

Inyectar reloj, generador de identificadores o transporte solo cuando facilite reproducir una regla o sustituir una dependencia real. No introducir DI ceremonial.

## Migración pequeña y verificable

Mover una responsabilidad a la vez conservando el comportamiento y el contrato público. Actualizar todos los consumidores y pruebas pertinentes; eliminar la implementación duplicada cuando la extracción esté completa. Mantener separados los cambios de estructura y los cambios de negocio cuando su combinación dificulte revisar el resultado.

Validar la composición real, no solo la función extraída. Ejemplos útiles: formulario dentro de un modal con Select en portal; mismo componente en dos funcionalidades; fallo del servidor que conserva el borrador; import que sigue siendo válido en SSR/cliente. No inventar una suite para probar solo nombres de carpetas.
