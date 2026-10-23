"""Liquidacion de la compra usando las reglas comprobadas con TDD."""
from dataclasses import dataclass
from .cupones import descuento_final, envio_gratis_por_cupon
from .iva import valor_con_descuento, iva_de_linea


@dataclass(frozen=True)
class ResultadoCompra:
    subtotal: int
    descuento: int
    iva: int
    envio: int
    total: int
    iva_por_producto: dict


def liquidar(carrito, municipio, categoria='ESTANDAR', cupon=None):
    subtotal = sum(linea.bruto for linea in carrito.lineas)
    porcentaje = descuento_final(subtotal, cupon)
    descuento = 0
    iva_total = 0
    bases_con_iva = 0
    iva_por_producto = {}
    for linea in carrito.lineas:
        base = valor_con_descuento(linea.bruto, porcentaje)
        descuento += linea.bruto - base
        iva_linea = iva_de_linea(linea.bruto, linea.producto.iva_porcentaje, porcentaje)
        iva_total += iva_linea
        iva_por_producto[linea.producto.codigo] = iva_linea
        if linea.producto.iva_porcentaje > 0:
            bases_con_iva += base
    if bases_con_iva >= 150000 or envio_gratis_por_cupon(cupon):
        envio = 0
    elif municipio.strip().casefold() == 'sincelejo':
        envio = 8000
    else:
        envio = 15000
    total = subtotal - descuento + iva_total + envio
    return ResultadoCompra(subtotal, descuento, iva_total, envio, total, iva_por_producto)
