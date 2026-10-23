"""HU-01: agregar productos. Patron AAA en cada prueba."""
from unittest.mock import Mock
import pytest
from mercado_sabanero.carrito import Carrito, Producto, CantidadInvalida, StockInsuficiente


def inventario_con(stock=100):
    doble = Mock()
    doble.stock_disponible.return_value = stock
    return doble


@pytest.mark.parametrize('cantidad', [1, 50])
def test_agrega_entre_una_y_cincuenta_unidades(cantidad):
    # Preparar
    carrito = Carrito(inventario_con())
    arroz = Producto('ARZ', 'Arroz', 4500, 0)
    # Ejecutar
    carrito.agregar(arroz, cantidad)
    # Verificar
    assert carrito.lineas[0].cantidad == cantidad


@pytest.mark.parametrize('cantidad', [0, -1, 51])
def test_rechaza_cantidad_fuera_del_rango(cantidad):
    # Preparar
    carrito = Carrito(inventario_con())
    arroz = Producto('ARZ', 'Arroz', 4500, 0)
    # Ejecutar y verificar
    with pytest.raises(CantidadInvalida):
        carrito.agregar(arroz, cantidad)


def test_rechaza_cantidad_no_entera():
    carrito = Carrito(inventario_con())
    producto = Producto('A', 'Arroz', 4500, 0)
    with pytest.raises(CantidadInvalida):
        carrito.agregar(producto, 1.5)


def test_rechaza_stock_insuficiente():
    # Preparar
    carrito = Carrito(inventario_con(3))
    arroz = Producto('ARZ', 'Arroz', 4500, 0)
    # Ejecutar y verificar
    with pytest.raises(StockInsuficiente):
        carrito.agregar(arroz, 4)


def test_suma_cantidades_del_mismo_producto():
    # Preparar
    carrito = Carrito(inventario_con(15))
    arroz = Producto('ARZ', 'Arroz', 4500, 0)
    # Ejecutar
    carrito.agregar(arroz, 4)
    carrito.agregar(arroz, 5)
    # Verificar
    assert len(carrito.lineas) == 1
    assert carrito.lineas[0].cantidad == 9


def test_verifica_stock_de_la_cantidad_acumulada_con_mock():
    # Preparar
    inventario = inventario_con(6)
    carrito = Carrito(inventario)
    arroz = Producto('ARZ', 'Arroz', 4500, 0)
    carrito.agregar(arroz, 4)
    # Ejecutar y verificar
    with pytest.raises(StockInsuficiente):
        carrito.agregar(arroz, 3)
    assert inventario.stock_disponible.call_count == 2


def test_rechaza_si_cantidad_acumulada_supera_cincuenta():
    carrito = Carrito(inventario_con(100))
    arroz = Producto('ARZ', 'Arroz', 4500, 0)
    carrito.agregar(arroz, 48)
    with pytest.raises(CantidadInvalida):
        carrito.agregar(arroz, 3)


def test_agrega_productos_diferentes():
    carrito = Carrito(inventario_con())
    carrito.agregar(Producto('A', 'Arroz', 4500, 0), 2)
    carrito.agregar(Producto('C', 'Cafe', 15000, 5), 1)
    assert len(carrito.lineas) == 2


def test_consulta_servicio_inventario_mediante_mock():
    inventario = inventario_con(10)
    carrito = Carrito(inventario)
    carrito.agregar(Producto('LIC', 'Licuadora', 180000, 19), 2)
    inventario.stock_disponible.assert_called_once_with('LIC')


def test_carrito_vacio_no_tiene_lineas():
    assert Carrito(inventario_con()).lineas == ()
