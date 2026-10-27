#!/usr/bin/env python3
"""
Simulador de la app móvil NotasXest (PPS · UT6) — solo VLAN de aula.

Reproduce, desde el ordenador del aula y SIN necesitar un dispositivo Android, exactamente
lo que la app haría por la red: login con contraseña sobre HTTP en claro, envío de la
X-Api-Key incrustada y sincronización de notas. Está pensado para que mitmproxy lo
intercepte y el alumnado VEA la contraseña y la clave viajando en claro.

Uso típico (con mitmproxy escuchando en 127.0.0.1:8080):
    python3 app_cliente.py --proxy http://127.0.0.1:8080

Sin proxy (para probar que el backend responde):
    python3 app_cliente.py

Requiere: pip install requests
"""
import argparse
import requests

# Estos valores están "incrustados" igual que en el APK. Son lo que el proxy verá.
BASE_URL = "http://api.xest.local:8090"
API_KEY = "xk_live_9f2c7b41ad554e0e8d3b6a1029f4c7de"
USUARIO = "demo"
PASSWORD = "SuperSecreto123!"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=BASE_URL, help="URL base del backend")
    ap.add_argument("--proxy", default=None, help="proxy HTTP, p.ej. http://127.0.0.1:8080")
    args = ap.parse_args()

    proxies = {"http": args.proxy, "https": args.proxy} if args.proxy else None
    s = requests.Session()

    print("[app] POST /login (contraseña en claro sobre HTTP)")
    r = s.post(
        f"{args.base}/login",
        headers={"X-Api-Key": API_KEY, "Content-Type": "application/json"},
        json={"usuario": USUARIO, "password": PASSWORD},
        proxies=proxies,
        timeout=10,
    )
    print("[app] login ->", r.status_code, r.text)
    token = r.json().get("token", "")

    print("[app] GET /sync (con X-Api-Key incrustada + Bearer)")
    r = s.get(
        f"{args.base}/sync",
        headers={"X-Api-Key": API_KEY, "Authorization": f"Bearer {token}"},
        proxies=proxies,
        timeout=10,
    )
    print("[app] sync  ->", r.status_code, r.text)


if __name__ == "__main__":
    main()
