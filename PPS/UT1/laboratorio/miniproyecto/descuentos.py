"""PPS UT1 · Mini-proyecto para la práctica de pruebas y cobertura (PPS-E2).

Contiene un fallo histórico ya conocido (un porcentaje negativo o >100 producía
un precio absurdo). En clase se escribe el TEST DE REGRESIÓN que lo blinda.
"""


def aplicar_descuento(precio: float, pct: float) -> float:
    """Aplica un descuento porcentual a un precio.

    Reglas:
      - precio >= 0
      - 0 <= pct <= 100
    Un porcentaje fuera de rango debe RECHAZARSE, no calcularse.
    """
    if precio < 0:
        raise ValueError("precio negativo")
    if not (0 <= pct <= 100):
        # Corrección del fallo histórico: antes esta comprobación NO estaba
        # y un pct=150 devolvía un precio negativo (se "regalaba" dinero).
        raise ValueError("porcentaje fuera de rango [0, 100]")
    return round(precio * (1 - pct / 100), 2)


def es_precio_valido(precio: float) -> bool:
    return precio >= 0
