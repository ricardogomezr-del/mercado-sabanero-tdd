"""Reglas de descuento por subtotal."""


UMBRAL_CINCO = 200000
UMBRAL_DIEZ = 500000


def porcentaje_volumen(subtotal):
    if subtotal < 0:
        raise ValueError('Subtotal negativo')
    if subtotal >= UMBRAL_DIEZ:
        return 10
    if subtotal >= UMBRAL_CINCO:
        return 5
    return 0
