#!/usr/bin/env python3
"""Instala el snapshot de skills; no instala herramientas ni credenciales."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--all', action='store_true', help='Incluir plugins, plantillas y sistema')
    parser.add_argument('--group', action='append', choices=['personal','plugins','templates','system'], help='Grupo a instalar; repetible. Predeterminado: personal')
    parser.add_argument('--dest', type=Path, default=Path(os.environ.get('CODEX_HOME', str(Path.home()/'.codex')))/'skills')
    parser.add_argument('--replace', action='store_true', help='Reemplazar skills existentes, guardando copia previa')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    groups = {'personal','plugins','templates','system'} if args.all else set(args.group or ['personal'])
    manifest = json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    # Comprobar integridad del snapshot completo antes de copiar archivos.
    for line in (ROOT/'SNAPSHOT.sha256').read_text().splitlines():
        digest, rel = line.split('  ', 1)
        if hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() != digest:
            raise SystemExit(f'Integridad incorrecta: {rel}')
    destination = args.dest.expanduser().resolve()
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    backup = destination.parent/'skill-backups'/stamp
    installed = skipped = 0
    for entry in manifest['skills']:
        if entry['group'] not in groups:
            continue
        source = ROOT/entry['path']
        target = destination/entry['name']
        if target.exists() or target.is_symlink():
            if not args.replace:
                print(f'OMITIDA (ya existe): {target.name}')
                skipped += 1
                continue
            if not args.dry_run:
                backup.mkdir(parents=True, exist_ok=True)
                shutil.move(str(target), str(backup/target.name))
        print(f'{"SIMULAR" if args.dry_run else "INSTALAR"}: {entry["name"]} [{entry["group"]}]')
        if not args.dry_run:
            destination.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, target)
        installed += 1
    print(f'{installed} seleccionadas; {skipped} omitidas. Destino: {destination}')
    if backup.exists():
        print(f'Copia previa: {backup}')
    if groups - {'personal'}:
        print('Los snapshots de plugins requieren sus herramientas/conexiones y runtimes originales. Ver PLUGINS.md.')

if __name__ == '__main__':
    main()
