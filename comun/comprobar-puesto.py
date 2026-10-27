#!/usr/bin/env python3
"""Verificación de prerrequisitos, sin instalar ni modificar el equipo."""
import argparse,platform,shutil,subprocess,sys
p=argparse.ArgumentParser(description=__doc__);p.add_argument('perfil',choices=['base','web','osint','python']);a=p.parse_args()
needed={'base':['python3','git'],'web':['python3','git','curl','docker'],'osint':['python3','git'],'python':['python3','git']}[a.perfil]
bad=0
print('Sistema:',platform.system(),platform.machine())
for tool in needed:
 path=shutil.which(tool);print(('OK' if path else 'FALTA'),tool,path or '');bad+=not bool(path)
if a.perfil=='web' and shutil.which('docker'):
 for cmd in [['docker','compose','version'],['docker','info','--format','{{.OSType}} {{.Architecture}}']]:
  try:
   r=subprocess.run(cmd,capture_output=True,text=True,timeout=20);good=r.returncode==0
   print('OK' if good else 'FALLO',' '.join(cmd),r.stdout.strip() if good else 'Comprueba servicio/permisos');bad+=not good
  except subprocess.TimeoutExpired:bad+=1;print('FALLO: Docker no responde en 20 s')
print('Prerrequisitos:', 'comprobados; falta ejecutar la práctica' if not bad else f'{bad} incidencias')
sys.exit(1 if bad else 0)
