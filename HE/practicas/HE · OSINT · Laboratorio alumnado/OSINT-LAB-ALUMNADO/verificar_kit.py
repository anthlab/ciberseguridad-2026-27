from pathlib import Path
import json,hashlib,sys
p=Path(__file__).resolve().parent
ok=True
for name,expected in json.loads((p/'manifest.json').read_text()).items():
 f=p/'datos'/name
 good=f.exists() and hashlib.sha256(f.read_bytes()).hexdigest()==expected
 print(('OK ' if good else 'ERROR ')+name);ok=ok and good
sys.exit(0 if ok else 1)
