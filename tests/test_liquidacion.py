"""HU-05: envio, total a pagar, ejemplo de integracion de reglas."""
from unittest.mock import Mock
import pytest
from mercado_sabanero.carrito import Carrito, Producto
from mercado_sabanero.liquidacion import liquidar


def crear_carrito(*items):
    inventario = Mock()
    inventario.stock_disponible.return_value = 100
    carrito = Carrito(inventario)
    for producto, cantidad in items:
        carrito.agregar(producto, cantidad)
    return carrito


def test_envio_a_sincelejo_cuesta_ocho_mil():
    carrito = crear_carrito((Producto('A', 'Arroz', 10000, 0), 1))
    resultado = liquidar(carrito, 'Sincelejo')
    assert resultado.envio == 8000


def test_envio_a_otro_municipio_cuesta_quince_mil():
    carrito = crear_carrito((Producto('A', 'Arroz', 10000, 0), 1))
    resultado = liquidar(carrito, 'Sampues')
    assert resultado.envio == 15000


def test_envio_gratis_si_productos_gravados_suman_ciento_cincuenta_mil():
    carrito = crear_carrito((Producto('L', 'Licuadora', 150000, 19), 1))
    resultado = liquidar(carrito, 'Sincelejo')
    assert resultado.envio == 0


def test_producto_exento_no_cuenta_para_envio_gratis():
    carrito = crear_carrito((Producto('A', 'Arroz', 180000, 0), 1))
    resultado = liquidar(carrito, 'Sincelejo')
    assert resultado.envio == 8000


def test_cupon_envio_gratis_evade_costo_de_envio():
    carrito = crear_carrito((Producto('A', 'Arroz', 10000, 0), 1))
    resultado = liquidar(carrito, 'Sampues', cupon='ENVIOGRATIS')
    assert resultado.envio == 0


def test_total_es_subtotal_menos_descuento_mas_iva_mas_envio():
    carrito = crear_carrito((Producto('C', 'Cafe', 100000, 5), 1))
    resultado = liquidar(carrito, 'Sincelejo')
    assert resultado.total == resultado.subtotal - resultado.descuento + resultado.iva + resultado.envio
    assert resultado.total == 113000


def test_ejemplo_completo_de_la_guia_coincide_en_subtotal_iva_y_total():
    # Preparar: licuadora, cafe y arroz del enunciado
    carrito = crear_carrito(
        (Producto('L', 'Licuadora', 180000, 19), 1),
        (Producto('C', 'Cafe', 15000, 5), 2),
        (Producto('A', 'Arroz', 4500, 0), 4),
    )
    # Ejecutar
    resultado = liquidar(carrito, 'Sincelejo', categoria='ESTANDAR')
    # Verificar
    assert (resultado.subtotal, resultado.descuento, resultado.iva, resultado.envio, resultado.total) == (
        228000, 11400, 33915, 0, 250515
    )


def test_iva_por_producto_esta_desglosado():
    carrito = crear_carrito((Producto('C', 'Cafe', 30000, 5), 1))
    resultado = liquidar(carrito, 'Sincelejo')
    assert resultado.iva_por_producto['C'] == 1500


def test_envio_gratis_no_depende_del_municipio():
    carrito = crear_carrito((Producto('L', 'Licuadora', 200000, 19), 1))
    resultado = liquidar(carrito, 'Corozal')
    assert resultado.envio == 0


def test_envio_gratis_se_calcula_sobre_base_gravada_con_descuento():
    # El producto gravado cuesta 150.000, pero con un 10% de cupon queda en 135.000
    carrito = crear_carrito((Producto('G', 'Gravado', 150000, 19), 1))
    resultado = liquidar(carrito, 'Sincelejo', cupon='SABANERO10')
    assert resultado.envio == 8000


def test_carrito_vacio_tiene_total_de_envio():
    carrito = crear_carrito()
    resultado = liquidar(carrito, 'Sincelejo')
    assert resultado.total == 8000
