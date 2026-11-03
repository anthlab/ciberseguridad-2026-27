import pytest

from inscripciones.almacen import guardar_inscripcion, leer_inscripciones
from inscripciones.validacion import (
    calcular_cuota,
    normalizar_nombre,
    validar_dni,
    validar_email,
)
@pytest.mark.parametrize(
    "dni, esperado",
    [
        ("12345678Z", True),       # Letra correcta
        ("12345678A", False),      # Letra incorrecta
        ("12345678z", True),       # Minúscula admitida
        ("  12345678Z  ", True),   # Espacios exteriores admitidos
        ("0000001R", False),       # 7 cifras
        ("000000001R", False),     # 9 cifras
    ],
)
def test_r1_dni(dni, esperado):
    assert validar_dni(dni) is esperado

@pytest.mark.parametrize(
    "email, esperado",
    [
        ("ana@ejemplo.es", True),
        ("ana@@ejemplo.es", False),
        ("ana@ejemplo", False),
        ("ana garcia@ejemplo.es", False),
        (" ana@ejemplo.es ", False),
    ],
)
def test_r2_email(email, esperado):
    assert validar_email(email) is esperado

def test_r3_normaliza_nombre():
    assert normalizar_nombre("  ana   garcía  ") == "Ana García"


@pytest.mark.parametrize("nombre", ["", "   "])
def test_r3_rechaza_nombre_vacio(nombre):
    with pytest.raises(ValueError, match="vacío"):
        normalizar_nombre(nombre)

def test_r4_rechaza_menor_de_16():
    with pytest.raises(ValueError, match="edad mínima"):
        calcular_cuota(15)


@pytest.mark.parametrize(
    "edad, desempleado, esperado",
    [
        (16, False, 40.0),
        (16, True, 20.0),
        (25, False, 40.0),
        (25, True, 20.0),
        (26, False, 60.0),
        (26, True, 30.0),
    ],
)
def test_r4_cuota(edad, desempleado, esperado):
    assert calcular_cuota(edad, desempleado) == esperado
@pytest.mark.parametrize("nombre", ["=1+1", "+x", "-x", "@x", "\tx", "\rx"])
def test_r5_neutraliza_nombre_en_csv(tmp_path, inscripcion, nombre):
    ruta = tmp_path / "inscripciones.csv"
    inscripcion["nombre"] = nombre

    guardar_inscripcion(ruta, inscripcion)

    assert leer_inscripciones(ruta)[0]["nombre"] == "'" + nombre
