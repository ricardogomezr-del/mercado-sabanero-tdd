"""Reglas de descuento por subtotal."""


def porcentaje_volumen(subtotal):
    if subtotal < 0:
        raise ValueError('Subtotal negativo')
    if subtotal >= 500000:
        return 10
    if subtotal >= 200000:
        return 5
    return 0
