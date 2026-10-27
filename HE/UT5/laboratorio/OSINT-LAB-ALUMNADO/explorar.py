from pathlib import Path
import sys,json,xml.etree.ElementTree as ET
p=Path(__file__).resolve().parent/'datos'
a=sys.argv[1:]
if a and a[0]=='buscar' and len(a)==2:
 for f in sorted(p.iterdir()):
  for n,line in enumerate(f.read_text().splitlines(),1):
   if a[1].casefold() in line.casefold(): print(f.name,str(n),line,sep=' | ')
elif a==['certificados']:
 names={n for row in json.loads((p/'certificados.json').read_text()) for n in row['name_value'].splitlines()}
 for n in sorted(names): print(n)
elif a==['metadatos']:
 root=ET.parse(p/'cartel.svg').getroot()
 for e in root.find('{http://www.w3.org/2000/svg}metadata'): print(e.tag.split('}')[-1]+': '+str(e.text))
else: print('Uso: python3 explorar.py buscar TEXTO | certificados | metadatos');sys.exit(2)
