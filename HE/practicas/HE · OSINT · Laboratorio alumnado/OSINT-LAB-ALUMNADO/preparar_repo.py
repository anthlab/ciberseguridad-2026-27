from pathlib import Path
import subprocess,os
p=Path(__file__).resolve().parent/'repo-demo'
if p.exists():
 print('repo-demo ya existe; se conserva sin cambios.'); raise SystemExit(0)
p.mkdir()
env=os.environ.copy()
env.update(GIT_AUTHOR_NAME='Persona sintetica HE',GIT_AUTHOR_EMAIL='ova.kestrel@mail.xest.example',GIT_COMMITTER_NAME='Persona sintetica HE',GIT_COMMITTER_EMAIL='ova.kestrel@mail.xest.example')
def git(*args):subprocess.run(['git','-C',str(p),*args],check=True,env=env)
git('init')
(p/'configuracion.txt').write_text('usuario=kestrel_ova\nmarcador=XEST_LAB_NO_VALIDO_123\n')
git('add','configuracion.txt')
env.update(GIT_AUTHOR_DATE='2026-09-20T10:00:00Z',GIT_COMMITTER_DATE='2026-09-20T10:00:00Z')
git('-c','commit.gpgsign=false','commit','-m','Ejemplo sintetico inicial')
(p/'configuracion.txt').write_text('usuario=kestrel_ova\nmarcador=ELIMINADO_DEL_ESTADO_ACTUAL\n')
git('add','configuracion.txt')
env.update(GIT_AUTHOR_DATE='2026-09-21T10:00:00Z',GIT_COMMITTER_DATE='2026-09-21T10:00:00Z')
git('-c','commit.gpgsign=false','commit','-m','Retirar marcador del estado actual')
print('Repositorio de dos commits creado. No contiene credenciales reales.')
