#!/usr/bin/env python3
"""Comprueba integridad de la distribución antes de editar las prácticas."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parents[1]
manifest=root/'MANIFIESTO.json'
if not manifest.is_file():
 print('FALLO: falta MANIFIESTO.json');sys.exit(2)
rows=json.loads(manifest.read_text(encoding='utf-8'));bad=[]
for rel,digest in rows.items():
 p=(root/rel).resolve()
 if root not in p.parents:
  bad.append(rel+': ruta inválida');continue
 if not p.is_file():bad.append(rel+': ausente')
 elif hashlib.sha256(p.read_bytes()).hexdigest()!=digest:bad.append(rel+': modificado')
for issue in bad:print('FALLO',issue)
print(f'{len(rows)} archivos comprobados; {len(bad)} incidencias')
sys.exit(1 if bad else 0)
