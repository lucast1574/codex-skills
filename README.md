# Skills de Lucas para Codex

Respaldo privado del 19 de octubre de 2026: **64 skills** con sus referencias, scripts y recursos (668 archivos de skills).

- **10 personales:** listas para instalar desde `skills/`.
- **22 de plugins:** snapshot en `snapshots/plugins/`.
- **27 plantillas en caché:** snapshot en `snapshots/templates/`; no necesariamente activas en el chat original.
- **5 de sistema:** snapshot en `snapshots/system/`; Codex normalmente ya incorpora sus propias versiones.

Ver [catálogo completo](CATALOG.md), [orígenes y dependencias](PLUGINS.md) y `manifest.json`. Se conserva la autoría y las licencias incluidas por los proveedores. Este respaldo privado no otorga derechos de redistribución de recursos de terceros.

## Instalar en otra PC

Requiere Git, Python 3 y acceso a este repositorio privado. Autentícate en GitHub con tu cuenta por el mecanismo habitual de esa PC.

```bash
git clone https://github.com/lucast1574/codex-skills.git
cd codex-skills
python3 install.py
```

En Windows, usar `py -3 install.py`. El instalador solo usa la biblioteca estándar de Python. Por defecto instala las 10 personales en `$CODEX_HOME/skills` o `~/.codex/skills`, conserva las existentes y verifica los hashes del snapshot antes de copiar. Abre un nuevo chat de Codex para comprobar su disponibilidad; si la aplicación no actualiza el catálogo, reiníciala.

Para copiar absolutamente todas las instrucciones y recursos del respaldo:

```bash
python3 install.py --all
```

Esto **no instala los servidores MCP, conectores, runtimes ni dependencias de los scripts**. Para las skills de plugins se recomienda instalar el plugin original en la otra PC; consultar [PLUGINS.md](PLUGINS.md). La copia de un `SKILL.md` por sí sola no habilita una herramienta.

Opciones:

```bash
python3 install.py --all --dry-run
python3 install.py --group personal --group plugins
python3 install.py --dest /ruta/a/skills
python3 install.py --replace
```

`--replace` guarda las versiones anteriores en `skill-backups/<fecha UTC>/`, junto a la carpeta `skills`. Sin esa opción no sobrescribe ninguna skill existente. Para actualizar este snapshot desde la otra PC: `git pull --ff-only` y ejecutar nuevamente el instalador; usar `--replace` si deseas actualizar skills previamente instaladas.

También puedes pedirle al Codex de la otra PC:

> Clona mi repositorio privado lucast1574/codex-skills, lee README.md y PLUGINS.md e instala las skills personales con install.py. Revisa el catálogo de plugins y ayúdame a habilitar sus equivalentes disponibles. Conserva mis skills existentes. Lee preferences/AGENTS.md e incorpora esas preferencias sin borrar mis instrucciones actuales.

Con `$skill-installer`, las carpetas `skills/<nombre>` son instalables individualmente desde este repositorio privado.

## Preferencias globales

`preferences/AGENTS.md` contiene las preferencias de interfaz que Lucas compartió junto con este pedido. Puedes incorporarlas a tus instrucciones globales de Codex en la otra PC, preservando las que ya existan. El instalador no modifica tus instrucciones globales automáticamente.

## Alcance del respaldo

Se recopilaron las carpetas de skills personales, sistema y caché de plugins presentes en esta máquina. No contiene sesiones, memorias, archivos de autenticación ni configuración de cuentas. Se excluyeron cachés de Python y se sustituyó una contraseña ficticia de ejemplo de Atlas por una indicación de creación interactiva; el resto del contenido de las skills se conserva.

`leasy-atlas-rules` aplica exclusivamente al repositorio `leasyauto/atlas`.

Formato y dependencias: [documentación oficial de OpenAI para skills](https://developers.openai.com/plugins/build/skills).
