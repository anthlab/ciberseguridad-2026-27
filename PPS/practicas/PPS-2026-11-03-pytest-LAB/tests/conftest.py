import pytest


@pytest.fixture
def inscripcion():
    return {
        "dni": "12345678Z",
        "nombre": "Ana García",
        "email": "ana@ejemplo.es",
        "edad": 30,
        "cuota": 60.0,
    }
