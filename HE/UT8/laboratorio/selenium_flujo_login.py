#!/usr/bin/env python3
"""
HE UT8 · Flujo de login autenticado automatizado con Selenium (RA5.e).

Objetivo docente: demostrar cómo se automatiza un flujo autenticado de una SPA moderna
(OWASP Juice Shop) para poder repetirlo N veces — por ejemplo, para probar un IDOR a escala
o hacer una prueba de regresión tras corregir un fallo.

NO es una caja negra: cada paso está comentado. Uso EXCLUSIVO en la VLAN aislada de aula.

Requisitos (ya presentes en la VM Kali de aula):
    pip install selenium        # o: sudo apt install python3-selenium
    geckodriver + firefox-esr   # sudo apt install firefox-esr  (geckodriver viene con Kali)
    # Alternativa Chromium: pasar --browser chrome (necesita chromium + chromedriver)

Preparación (una sola vez): registrar el usuario de prueba en Juice Shop, por UI o por API:
    curl -s http://juice.xest.local:3000/api/Users/ -H 'Content-Type: application/json' \
      -d '{"email":"selenium@xest.local","password":"Xest.2027","passwordRepeat":"Xest.2027",\
"securityQuestion":{"id":1},"securityAnswer":"lab"}'

Ejemplo:
    python3 selenium_flujo_login.py --url http://juice.xest.local:3000 \
        --email selenium@xest.local --password 'Xest.2027' --headless
"""
import argparse
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException


def construir_driver(browser: str, headless: bool):
    """Devuelve un WebDriver de Firefox (por defecto) o Chrome."""
    if browser == "firefox":
        opts = webdriver.FirefoxOptions()
        if headless:
            opts.add_argument("-headless")
        return webdriver.Firefox(options=opts)
    else:
        opts = webdriver.ChromeOptions()
        if headless:
            opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        return webdriver.Chrome(options=opts)


def cerrar_banners(driver, wait):
    """Juice Shop muestra un aviso de bienvenida y una barra de cookies: los cerramos."""
    for selector in (
        (By.XPATH, "//button[@aria-label='Close Welcome Banner']"),
        (By.XPATH, "//a[contains(text(),'Me want it!')]"),
        (By.XPATH, "//a[contains(@aria-label,'dismiss') or contains(text(),'Dismiss')]"),
    ):
        try:
            el = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(selector))
            el.click()
            time.sleep(0.3)
        except TimeoutException:
            pass  # si no aparece, seguimos: no es un error


def login(driver, wait, base_url, email, password):
    """Navega al formulario de login y envía las credenciales por la UI."""
    driver.get(f"{base_url}/#/login")
    cerrar_banners(driver, wait)
    print("[+] Página de login cargada")

    campo_email = wait.until(EC.presence_of_element_located((By.ID, "email")))
    campo_pass = driver.find_element(By.ID, "password")
    campo_email.clear()
    campo_email.send_keys(email)
    campo_pass.clear()
    campo_pass.send_keys(password)
    driver.find_element(By.ID, "loginButton").click()
    print(f"[+] Login enviado como {email}")


def obtener_token(driver, wait):
    """El JWT queda en localStorage['token'] tras un login correcto."""
    def _token(d):
        return d.execute_script("return window.localStorage.getItem('token');")

    try:
        wait.until(lambda d: _token(d))
    except TimeoutException:
        return None
    return _token(driver)


def peticion_autenticada(driver, base_url, token):
    """
    Ejemplo de uso del token: pedir la cesta del propio usuario con fetch dentro del
    navegador (misma sesión). Devuelve (status, num_productos).

    Reutilizar este patrón cambiando el id de la cesta es la base para probar un IDOR
    a escala — SIEMPRE dentro del alcance del ROE.
    """
    script = """
        const cb = arguments[arguments.length - 1];
        const token = arguments[0];
        // Descubrir el id de cesta del propio usuario desde el whoami:
        fetch('/rest/user/whoami', {headers: {'Authorization': 'Bearer ' + token}})
          .then(r => r.json())
          .then(who => {
              const bid = (who && who.user && who.user.bid) ? who.user.bid : 1;
              return fetch('/rest/basket/' + bid, {headers: {'Authorization': 'Bearer ' + token}})
                       .then(r => r.json().then(j => cb({status: r.status, data: j})));
          })
          .catch(e => cb({status: -1, error: String(e)}));
    """
    driver.set_script_timeout(15)
    res = driver.execute_async_script(script, token)
    status = res.get("status")
    n = 0
    try:
        n = len(res.get("data", {}).get("data", {}).get("Products", []))
    except (AttributeError, TypeError):
        n = 0
    return status, n


def main():
    p = argparse.ArgumentParser(description="Flujo de login autenticado (HE UT8).")
    p.add_argument("--url", default="http://juice.xest.local:3000",
                   help="URL base de Juice Shop en la VLAN de aula")
    p.add_argument("--email", required=True)
    p.add_argument("--password", required=True)
    p.add_argument("--browser", choices=["firefox", "chrome"], default="firefox")
    p.add_argument("--headless", action="store_true")
    p.add_argument("--timeout", type=int, default=20)
    args = p.parse_args()

    base_url = args.url.rstrip("/")

    try:
        driver = construir_driver(args.browser, args.headless)
    except WebDriverException as e:
        print(f"[!] No se pudo arrancar el navegador ({args.browser}): {e}", file=sys.stderr)
        print("    Prueba con --browser chrome, o instala geckodriver/firefox-esr.", file=sys.stderr)
        sys.exit(2)

    wait = WebDriverWait(driver, args.timeout)
    try:
        login(driver, wait, base_url, args.email, args.password)
        token = obtener_token(driver, wait)
        if not token:
            print("[!] No se obtuvo token: credenciales incorrectas o el usuario no existe.",
                  file=sys.stderr)
            print("    Registra el usuario de prueba antes (ver cabecera del script).",
                  file=sys.stderr)
            sys.exit(1)
        print(f"[+] Sesión iniciada. Token (localStorage): {token[:24]}...")

        status, n = peticion_autenticada(driver, base_url, token)
        print(f"[+] Petición autenticada /rest/basket/<id> -> {status} ({n} producto/s)")
        if status == 200:
            print("[OK] Flujo autenticado completado")
            sys.exit(0)
        else:
            print(f"[!] La petición autenticada devolvió {status}", file=sys.stderr)
            sys.exit(1)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
