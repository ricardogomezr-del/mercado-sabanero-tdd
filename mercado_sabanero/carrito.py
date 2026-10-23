"""Carrito de compras con inventario externo (inyectado)."""
from dataclasses import dataclass


class CantidadInvalida(ValueError):
    pass


class StockInsuficiente(ValueError):
    pass


@dataclass(frozen=True)
class Producto:
    codigo: str
    nombre: str
    precio: int
    iva_porcentaje: int

    def __post_init__(self):
        if not isinstance(self.precio, int) or self.precio < 0:
            raise ValueError('Precio invalido')
        if self.iva_porcentaje not in (0, 5, 19):
            raise ValueError('Tarifa de IVA invalida')


@dataclass(frozen=True)
class Linea:
    producto: Producto
    cantidad: int

    @property
    def bruto(self):
        return self.producto.precio * self.cantidad


class Carrito:
    def __init__(self, inventario):
        self._inventario = inventario
        self._lineas = {}

    @property
    def lineas(self):
        return tuple(self._lineas.values())

    @staticmethod
    def _validar_cantidad(cantidad, acumulada):
        if type(cantidad) is not int or not 1 <= cantidad <= 50 or acumulada + cantidad > 50:
            raise CantidadInvalida('Cantidad entre 1 y 50 por producto')

    def agregar(self, producto, cantidad):
        actual = self._lineas.get(producto.codigo)
        acumulada = actual.cantidad if actual else 0
        self._validar_cantidad(cantidad, acumulada)
        nuevo_total = cantidad + acumulada
        if self._inventario.stock_disponible(producto.codigo) < nuevo_total:
            raise StockInsuficiente('Stock insuficiente')
        self._lineas[producto.codigo] = Linea(producto, nuevo_total)
