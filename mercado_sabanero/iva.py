"""Calculos en pesos colombianos sin centavos."""
from decimal import Decimal, ROUND_HALF_UP

CIEN = Decimal('100')


def _pesos(numero):
    return int(Decimal(numero).quantize(Decimal('1'), rounding=ROUND_HALF_UP))


def valor_con_descuento(bruto, porcentaje):
    if not 0 <= porcentaje <= 100:
        raise ValueError('Descuento invalido')
    return _pesos(Decimal(bruto) * Decimal(100 - porcentaje) / CIEN)


def iva_de_linea(bruto, tarifa, descuento_porcentaje=0):
    if tarifa not in (0, 5, 19):
        raise ValueError('Tarifa IVA invalida')
    base = valor_con_descuento(bruto, descuento_porcentaje)
    return _pesos(Decimal(base) * Decimal(tarifa) / CIEN)
