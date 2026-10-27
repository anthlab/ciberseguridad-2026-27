#!/usr/bin/env python3
"""Priorizador didáctico offline. Requiere snapshots explícitos; no consulta la red."""
import argparse
import csv
import json
from pathlib import Path
import re
import sys


def priorizar(lote, kev_file, epss_file):
    kev_data = json.loads(Path(kev_file).read_text(encoding='utf-8'))
    kev = {v['cveID'].upper() for v in kev_data['vulnerabilities']}
    with open(epss_file, encoding='utf-8') as f:
        epss = {row['cve'].upper(): float(row['epss']) for row in csv.DictReader(line for line in f if not line.lstrip().startswith('#'))}
    if any(not 0 <= value <= 1 for value in epss.values()):
        raise ValueError('EPSS debe estar entre 0 y 1')
    rows = []
    seen = set()
    for line in Path(lote).read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        parts = [s.strip() for s in line.split(',')]
        cve = parts[0].upper()
        if not re.fullmatch(r'CVE-\d{4}-\d{4,}', cve) or cve in seen:
            raise ValueError('CVE inválida o duplicada: ' + cve)
        seen.add(cve)
        cvss = float(parts[1]) if len(parts) > 1 and parts[1] else None
        if cvss is not None and not 0 <= cvss <= 10:
            raise ValueError('CVSS fuera de rango: ' + cve)
        if cve not in epss:
            raise ValueError('Falta EPSS para ' + cve + '; desconocido no equivale a cero')
        rows.append({'cve': cve, 'kev': 'SÍ' if cve in kev else 'no', 'epss': epss[cve], 'cvss': '' if cvss is None else cvss})
    if not rows:
        raise ValueError('Lote vacío')
    rows.sort(key=lambda r: (r['kev'] == 'SÍ', r['epss'], r['cvss'] if r['cvss'] != '' else -1), reverse=True)
    for n, row in enumerate(rows, 1):
        row['prioridad'] = n
    return rows


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cve-list', required=True)
    p.add_argument('--kev-file', required=True)
    p.add_argument('--epss-file', required=True)
    p.add_argument('--salida', required=True)
    a = p.parse_args()
    try:
        rows = priorizar(a.cve_list, a.kev_file, a.epss_file)
        with open(a.salida, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=['prioridad', 'cve', 'kev', 'epss', 'cvss'])
            w.writeheader(); w.writerows(rows)
    except (OSError, ValueError, KeyError) as exc:
        print('FALLO:', exc, file=sys.stderr)
        return 1
    print(f'OK: {len(rows)} CVE; fuentes locales; salida {a.salida}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
