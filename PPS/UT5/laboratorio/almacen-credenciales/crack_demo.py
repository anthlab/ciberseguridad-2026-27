"""Demo de COSTE: por qué SHA-256 sin sal es indefendible y Argon2id no.

Crackea por fuerza bruta un PIN de 4 cifras contra cada esquema y mide el tiempo.
La idea no es el PIN: es ver que el mismo ataque que contra SHA-256 termina en
milisegundos, contra Argon2id se vuelve inviable porque cada intento CUESTA.

Ejecutar:  python3 crack_demo.py
Requiere:  pip install argon2-cffi
"""
import hashlib
import itertools
import time

from argon2 import PasswordHasher, exceptions

PIN = "4271"  # el "secreto" a romper por fuerza bruta (0000-9999)


def sha256(clave: str) -> str:
    return hashlib.sha256(clave.encode()).hexdigest()


# --- Ataque contra SHA-256 (hash rápido, sin sal) --------------------------------
objetivo_sha = sha256(PIN)
t0 = time.perf_counter()
encontrado = None
for combo in itertools.product("0123456789", repeat=4):
    intento = "".join(combo)
    if sha256(intento) == objetivo_sha:
        encontrado = intento
        break
dt_sha = time.perf_counter() - t0
print(f"SHA-256 : PIN {encontrado} roto probando el espacio entero en {dt_sha:.4f} s")

# --- Mismo ataque contra Argon2id (hash con coste) -------------------------------
# Solo probamos 50 intentos y extrapolamos: agotar 10.000 en clase no acaba.
ph = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=4)
objetivo_arg = ph.hash(PIN)
t0 = time.perf_counter()
intentos = 0
for combo in itertools.product("0123456789", repeat=4):
    intentos += 1
    try:
        ph.verify(objetivo_arg, "".join(combo))
        break
    except exceptions.VerifyMismatchError:
        pass
    if intentos >= 50:
        break
dt_arg = time.perf_counter() - t0
por_intento = dt_arg / intentos
print(f"Argon2id: {intentos} intentos en {dt_arg:.2f} s  (~{por_intento * 1000:.0f} ms/intento)")
print(f"          agotar los 10.000 PIN de 4 cifras => ~{por_intento * 10000 / 60:.1f} min")
print(f"          una clave de 8 caracteres alfanum. => inviable ({por_intento:.3f} s x 62^8 intentos)")
print()
print(f"Factor de encarecimiento por intento: x{por_intento / (dt_sha / 10000):,.0f} aprox.")
