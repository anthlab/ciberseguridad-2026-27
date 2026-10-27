#!/usr/bin/env python3
"""Genera una BD sqlite de alertas SINTÉTICAS del SOC de xest (sin datos reales).

Uso:  python3 seed_alertas.py [ruta_db] [num_alertas]
      python3 seed_alertas.py soc.db 500

Las IP de origen son de rangos no enrutables (RFC 5737 TEST-NET-1 y RFC 1918):
ningún dato es real ni personal. La semilla fija hace el dataset reproducible en clase.
"""
import datetime
import random
import sqlite3
import sys

DB = sys.argv[1] if len(sys.argv) > 1 else "soc.db"
N = int(sys.argv[2]) if len(sys.argv) > 2 else 500

random.seed(42)  # reproducible: el mismo dataset en todas las estaciones

reglas = ["ssh-bruteforce", "web-sqli", "port-scan", "malware-eicar",
          "dns-tunneling", "priv-esc", "c2-beacon", "phishing-click",
          "lateral-smb", "exfil-http"]
severidades = ["baja", "media", "alta", "critica"]
hosts = [f"wks-{i:03d}.xest.local" for i in range(1, 41)] + \
        ["portal-soc.xest.local", "dc01.xest.local"]

con = sqlite3.connect(DB)
con.execute("DROP TABLE IF EXISTS alertas")
con.execute("""CREATE TABLE alertas(
    id        INTEGER PRIMARY KEY,
    ts        TEXT NOT NULL,
    severidad TEXT NOT NULL,
    regla     TEXT NOT NULL,
    origen    TEXT NOT NULL,
    host      TEXT NOT NULL)""")

base = datetime.datetime(2026, 9, 1, 0, 0, 0)
for i in range(1, N + 1):
    ts = (base + datetime.timedelta(minutes=random.randint(0, 60 * 24 * 7))).isoformat()
    if random.random() < 0.6:
        ip = f"192.0.2.{random.randint(1, 254)}"    # TEST-NET-1 (RFC 5737), no enrutable
    else:
        ip = f"10.10.10.{random.randint(1, 254)}"    # VLAN de aula (RFC 1918)
    con.execute(
        "INSERT INTO alertas(id, ts, severidad, regla, origen, host) VALUES(?,?,?,?,?,?)",
        (i, ts, random.choice(severidades), random.choice(reglas), ip, random.choice(hosts)))

con.commit()
total = con.execute("SELECT COUNT(*) FROM alertas").fetchone()[0]
con.close()
print(f"OK: {total} alertas sintéticas -> {DB}")
