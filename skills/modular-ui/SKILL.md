---
name: modular-ui
description: Crear y refactorizar modales, formularios y componentes UI compartidos con contratos claros y organización por funcionalidades. Aplicar al construir interfaces reutilizables o separar presentación, estado, lógica de negocio y acceso a datos; adaptar la arquitectura al proyecto existente.
---

# UI modular y código organizado

Trabajar con el stack y las convenciones reales del repositorio. Esta skill guía implementación y mantenibilidad; no autoriza despliegues, refactors globales ni cambios de producto no solicitados.

## Antes de editar

- Leer los AGENTS aplicables e inspeccionar componentes, tokens, rutas y dependencias existentes. Buscar la pieza que ya resuelve el problema antes de crear otra.
- Si existen `brand/DESIGN.md`, `brand/VOICE.md` o un sistema de diseño, leerlos y conservar la identidad en ambos temas.
- Elegir el límite del cambio: comportamiento común, funcionalidad concreta y dependencias. Explicar una decisión de arquitectura solo cuando importe para entender el resultado.
- Modales o diálogos: leer [modals.md](references/modals.md).
- Extraer componentes, reorganizar carpetas o separar lógica: leer [architecture.md](references/architecture.md).

## Componentes compartidos

- Las primitivas compartidas contienen interacción y estilo, no endpoints, roles empresariales ni reglas de una pantalla. Preferir composición por contenido/slots frente a un componente gigante lleno de flags.
- Promover un componente a `shared` cuando varios consumidores necesiten el mismo contrato, o cuando centralice una interacción delicada como foco, menús o diálogos. La coincidencia visual por sí sola no basta.
- Reutilizar una primitiva accesible existente o una dependencia ya instalada antes de reimplementar foco, portal y navegación. No introducir un framework nuevo para resolver un modal.
- Contratos pequeños: propiedades tipadas, eventos con intención y dueño explícito del estado. Evitar dos fuentes de verdad entre props y estado interno, `any`, uniones de props ambiguas y contexto global para estado local.
- Compartir tokens semánticos de fondo, texto, borde, acento y estado. Revisar contraste real de hover, foco, selección, error, deshabilitado y carga en claro y oscuro; no limitarse al estado inicial.
- Selectores, dropdowns y menús: componentes personalizados, reutilizables y tematizables, con etiquetas, selección, flechas, Escape y cierre exterior. No entregar la apariencia nativa ni un menú plano sin diseño.

## Reglas de interfaz de Lucas

- Sin focus outlines, focus rings ni sombras que imiten anillos. Se permite `outline: none`; conservar navegación por teclado y señalar el foco con fondo, color, subrayado o contraste integrados.
- Cerrar sesión únicamente dentro de la página de perfil/cuenta. La sidebar puede enlazar a Mi perfil; no puede contener logout, tampoco escondido en su menú.
- Mantener la marca y la utilidad en pantallas pequeñas. No usar medidas fijas que corten contenido, acciones o formularios.

## Código funcional y límites

- Usar funciones puras para cálculos, normalización y transiciones cuando mejore la claridad. Pasar entradas explícitas y devolver resultados tipados; no mezclar cálculo con red, almacenamiento o navegación.
- Aislar efectos en adaptadores, servicios o hooks según el stack. En React, usar componentes funcionales y hooks con una responsabilidad; no imponer programación funcional a frameworks con servicios por clases.
- Reducir estado derivado y efectos de sincronización innecesarios. No mutar datos del consumidor ni esconder dependencias en singletons/globales.
- Mantener invariantes, validación y permisos en el servidor. El estado visual de un botón no protege una operación. No filtrar secretos a paquetes compartidos o al cliente.
- Aplicar SOLID, DRY y KISS con criterio: abstraer reglas estables, no crear capas vacías, factories, repositorios o paquetes por anticipación. Una implementación pequeña y explícita puede ser mejor que una abstracción prematura.

## Comprobación proporcional al cambio

- Verificar el flujo real que usa el componente y, si ya tiene otros consumidores, comprobar que conservan su contrato. Revisar los imports y los límites entre cliente/servidor tras mover archivos.
- Ejecutar build/typecheck/lint disponibles y pertinentes. Escribir pruebas cuando protejan comportamiento relevante: transiciones, permisos, interacción compleja o regresiones. No crear pruebas que solo copien JSX o comparen cadenas CSS.
- Comprobar teclado, foco sin anillos, claro/oscuro y móvil para cambios UI relevantes. Una captura del estado inicial no prueba el guardado, el cierre ni la recuperación de errores.
- No reorganizar todo el repositorio para un arreglo pequeño. Informar qué cambió, qué se verificó y cualquier limitación concreta.
