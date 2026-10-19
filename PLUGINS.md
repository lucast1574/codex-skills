# Plugins y herramientas en la otra PC

Los archivos de una skill son instrucciones y recursos. Las herramientas MCP, las conexiones de cuenta, las bibliotecas de documentos y los servicios del host se obtienen por separado. No se copian credenciales entre PCs.

Instala/habilita los plugins equivalentes mediante el catálogo disponible en tu Codex y conecta tus cuentas allí. La disponibilidad puede variar por versión, cuenta y sistema operativo. Las versiones de `manifest.json` registran el origen del respaldo, no una exigencia de instalar una versión antigua.

| Proveedor / plugin | Skills y requisitos |
| --- | --- |
| nexode / nexode-mcp 0.1.19 | nexode-deploy; requiere el plugin Nexode y su autenticación MCP. |
| openai-bundled / visualize 1.0.49 | visualize; requiere el renderizador y herramientas de visualización del host. |
| openai-primary-runtime / documents, pdf, presentations, spreadsheets, template-creator 26.1015.12040 | Requieren las herramientas/librerías del runtime de Codex. Excel live control además requiere una sesión conectada de Excel. |
| openai-curated-remote / google-drive 0.1.22 | Google Drive, Docs, Sheets, Slides y comentarios; requiere conectar Google Drive. |
| openai-curated-remote / pages 0.1.23 | Pages / Spaces; requiere sus herramientas y acceso a las páginas. |
| openai-curated-remote / sites 1.0.0 | Sites; requiere herramientas Sites para construir/publicar. |
| openai-curated-remote / work-pets 0.1.6 | Crear, editar y gestionar mascotas en ChatGPT Work; requiere herramientas Pets y ese contexto. |
| openai-curated-remote / plugin-management 0.1.0 | Requiere herramientas de administración del catálogo de plugins. |
| openai-curated-remote / openai-templates 0.1.6 | 27 plantillas en caché con recursos; pueden requerir los runtimes de documentos/presentaciones/hojas. |
| Codex integrado | imagegen, openai-docs, skill-creator, skill-installer, review-agent; normalmente ya disponibles según la versión. |

No registres los snapshots como reemplazo de plugins que ya estén instalados: podrías duplicar instrucciones o perder actualizaciones del proveedor. `install.py --all` ofrece una copia explícita del respaldo, pero no garantiza la ejecución completa de esas skills en otro host. Algunos documentos de proveedor usan rutas o recursos específicos del runtime: conserva la versión integrada cuando esté disponible.

Las skills personales también pueden pedir herramientas externas según la tarea, como GitHub CLI, un navegador, herramientas de video o vectorización. Consulta cada `SKILL.md` antes de ejecutarla.
