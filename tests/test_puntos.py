"""HU-06: puntos de fidelizacion sin incluir el valor del envio."""
from unittest.mock import Mock
import pytest
from mercado_sabanero.puntos import calcular_puntos
from mercado_sabanero.carrito import Producto, Carrito
from mercado_sabanero.liquidacion import liquidar


@pytest.mark.parametrize('total,esperado', [(0, 0), (999, 0), (1000, 1), (1999, 1), (250515, 250)])
def test_un_punto_por_cada_mil_pesos_completos(total, esperado):
    # Preparar: total sin envio
    # Ejecutar
    puntos = calcular_puntos(total, 'ESTANDAR')
    # Verificar
    assert puntos == esperado


def test_cliente_oro_recibe_el_doble_de_puntos():
    assert calcular_puntos(250515, 'ORO') == 500


def test_rechaza_categoria_desconocida():
    with pytest.raises(ValueError):
        calcular_puntos(1000, 'PLATINO')


def test_ejemplo_oficial_genera_exactamente_250_puntos():
    inventario = Mock()
    inventario.stock_disponible.return_value = 99
    carrito = Carrito(inventario)
    carrito.agregar(Producto('L', 'Licuadora', 180000, 19), 1)
    carrito.agregar(Producto('C', 'Cafe', 15000, 5), 2)
    carrito.agregar(Producto('A', 'Arroz', 4500, 0), 4)
    resultado = liquidar(carrito, 'Sincelejo', 'ESTANDAR')
    assert resultado.total == 250515
    assert resultado.puntos == 250


def test_envio_no_suma_puntos():
    inventario = Mock()
    inventario.stock_disponible.return_value = 50
    carrito = Carrito(inventario)
    carrito.agregar(Producto('A', 'Arroz', 1000, 0), 1)
    resultado = liquidar(carrito, 'Sincelejo', 'ESTANDAR')
    assert resultado.total == 9000
    assert resultado.puntos == 1


def test_ejemplo_oficial_cliente_oro_recibe_500_puntos():
    inventario = Mock()
    inventario.stock_disponible.return_value = 99
    carrito = Carrito(inventario)
    carrito.agregar(Producto('L', 'Licuadora', 180000, 19), 1)
    carrito.agregar(Producto('C', 'Cafe', 15000, 5), 2)
    carrito.agregar(Producto('A', 'Arroz', 4500, 0), 4)
    assert liquidar(carrito, 'Sincelejo', 'ORO').puntos == 500
