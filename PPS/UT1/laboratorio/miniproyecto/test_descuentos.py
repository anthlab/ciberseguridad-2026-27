"""Suite de PPS-E2. Incluye un test TRIVIAL (mucha cobertura, poco valor) y el
TEST DE REGRESIÓN que se escribe en clase para blindar el fallo histórico."""
import pytest
from descuentos import aplicar_descuento, es_precio_valido


# --- Test "verde" pero pobre: ejecuta la función pero casi no verifica nada.
#     Sirve para enseñar que cobertura alta != calidad.
def test_ejecuta_sin_reventar():
    aplicar_descuento(100, 10)
    assert True            # <-- aserción trivial: no comprueba el resultado


# --- Tests con aserciones significativas.
def test_descuento_correcto():
    assert aplicar_descuento(100, 10) == 90.0
    assert aplicar_descuento(50, 0) == 50.0
    assert aplicar_descuento(80, 100) == 0.0


# --- TEST DE REGRESIÓN (se escribe en la sesión): el fallo histórico NO debe volver.
#     Antes, pct=150 devolvía un precio negativo. Ahora debe lanzar ValueError.
def test_regresion_pct_fuera_de_rango():
    with pytest.raises(ValueError):
        aplicar_descuento(100, 150)
    with pytest.raises(ValueError):
        aplicar_descuento(100, -5)


def test_precio_negativo_se_rechaza():
    with pytest.raises(ValueError):
        aplicar_descuento(-10, 10)
