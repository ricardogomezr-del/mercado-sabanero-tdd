"""Cupones disponibles y seleccion del mayor descuento."""
from .descuentos import porcentaje_volumen


class CuponInvalido(ValueError):
    pass


CUPON_DESCUENTO = 'SABANERO10'
CUPON_ENVIO = 'ENVIOGRATIS'
CUPONES = {CUPON_DESCUENTO: True, CUPON_ENVIO: True, 'VENCIDO10': False}


def validar_cupon(cupon):
    if cupon is not None and not CUPONES.get(cupon, False):
        raise CuponInvalido('Cupon invalido o vencido')


def descuento_cupon(subtotal, cupon):
    validar_cupon(cupon)
    if cupon == CUPON_DESCUENTO and subtotal >= 50000:
        return 10
    return 0


def envio_gratis_por_cupon(cupon):
    validar_cupon(cupon)
    return cupon == CUPON_ENVIO


def descuento_final(subtotal, cupon=None):
    return max(porcentaje_volumen(subtotal), descuento_cupon(subtotal, cupon))
