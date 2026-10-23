"""Cupones disponibles y seleccion del mayor descuento."""
from .descuentos import porcentaje_volumen


class CuponInvalido(ValueError):
    pass


CUPONES = {'SABANERO10': True, 'ENVIOGRATIS': True, 'VENCIDO10': False}


def validar_cupon(cupon):
    if cupon is not None and not CUPONES.get(cupon, False):
        raise CuponInvalido('Cupon invalido o vencido')


def descuento_cupon(subtotal, cupon):
    validar_cupon(cupon)
    if cupon == 'SABANERO10' and subtotal >= 50000:
        return 10
    return 0


def envio_gratis_por_cupon(cupon):
    validar_cupon(cupon)
    return cupon == 'ENVIOGRATIS'


def descuento_final(subtotal, cupon=None):
    return max(porcentaje_volumen(subtotal), descuento_cupon(subtotal, cupon))
