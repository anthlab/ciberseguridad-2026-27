#!/usr/bin/env python3
"""
Pruebas de regresión de la validación de compras (PPS · UT6 · cultura del módulo).

Regla del módulo: una vulnerabilidad no está cerrada hasta que existe una prueba de
regresión que fallaría si alguien la reintroduce.

Aquí probamos que:
  - El servidor VULNERABLE concede premium ante un flag falso del cliente (documenta el bug).
  - El servidor SEGURO RECHAZA ese mismo flag falso, acepta un recibo firmado legítimo,
    y NO permite reutilizar el recibo. Estas tres son las pruebas que fallarían si alguien
    volviera a confiar en el cliente.

Ejecución:
    python3 -m pytest -v            # desde la carpeta compras/
"""
import servidor_compras_vulnerable as vuln
import servidor_compras_seguro as seguro


def setup_function(_):
    # Estado limpio entre pruebas (los servidores guardan estado en memoria de módulo)
    vuln.PREMIUM_CONCEDIDO.clear()
    seguro.PREMIUM_CONCEDIDO.clear()
    seguro.RECIBOS_CONSUMIDOS.clear()


# --- Documenta el fallo del servidor vulnerable ---------------------------------

def test_vulnerable_concede_premium_con_flag_falso():
    """El servidor vulnerable se deja engañar por el cliente. Esto es el bug."""
    r = vuln.procesar_compra({"usuario": "atacante", "purchase_valid": True})
    assert r["premium"] is True


# --- Regresión: el servidor seguro NO debe caer en lo mismo ---------------------

def test_seguro_rechaza_flag_falso_del_cliente():
    """REGRESIÓN: si alguien vuelve a confiar en el flag del cliente, esto falla."""
    r = seguro.procesar_compra({"usuario": "atacante", "purchase_valid": True})
    assert r["premium"] is False


def test_seguro_acepta_recibo_firmado_legitimo():
    recibo = seguro.emitir_recibo("pedido-legit-1")
    r = seguro.procesar_compra({"usuario": "cliente", "recibo": recibo})
    assert r["premium"] is True


def test_seguro_rechaza_recibo_manipulado():
    """Un recibo con la firma alterada no cuela."""
    recibo = seguro.emitir_recibo("pedido-legit-2")
    manipulado = recibo[:-1] + ("0" if recibo[-1] != "0" else "1")
    r = seguro.procesar_compra({"usuario": "atacante", "recibo": manipulado})
    assert r["premium"] is False


def test_seguro_no_permite_reutilizar_recibo():
    recibo = seguro.emitir_recibo("pedido-unico")
    assert seguro.procesar_compra({"usuario": "a", "recibo": recibo})["premium"] is True
    # Segundo intento con el mismo recibo -> rechazado
    assert seguro.procesar_compra({"usuario": "a", "recibo": recibo})["premium"] is False
