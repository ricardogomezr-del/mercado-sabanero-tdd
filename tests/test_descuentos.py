"""HU-03: descuentos por volumen, incluyendo limites."""
import pytest
from mercado_sabanero.descuentos import porcentaje_volumen


@pytest.mark.parametrize('subtotal,esperado', [
    (0, 0), (199999, 0), (200000, 5), (299999, 5),
    (499999, 5), (500000, 10), (800000, 10)
])
def test_aplica_descuento_correcto_en_los_limites(subtotal, esperado):
    # Preparar: valores limite del requisito
    # Ejecutar
    porcentaje = porcentaje_volumen(subtotal)
    # Verificar
    assert porcentaje == esperado


def test_rechaza_subtotal_negativo():
    with pytest.raises(ValueError):
        porcentaje_volumen(-1)
