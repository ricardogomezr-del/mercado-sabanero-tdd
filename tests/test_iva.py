"""HU-02: calculo de IVA sobre precio descontado."""
import pytest
from mercado_sabanero.iva import valor_con_descuento, iva_de_linea


@pytest.mark.parametrize('tarifa,esperado', [(0, 0), (5, 5000), (19, 19000)])
def test_calcula_iva_para_tarifas_permitidas(tarifa, esperado):
    # Preparar: linea de 100.000 pesos, sin descuento
    bruto = 100000
    # Ejecutar
    iva = iva_de_linea(bruto, tarifa, 0)
    # Verificar
    assert iva == esperado


def test_calcula_iva_sobre_base_con_descuento():
    # Preparar
    bruto, iva_porcentaje, descuento = 180000, 19, 5
    # Ejecutar
    iva = iva_de_linea(bruto, iva_porcentaje, descuento)
    # Verificar
    assert iva == 32490


def test_cafe_con_iva_cinco_y_descuento_cinco():
    assert iva_de_linea(30000, 5, 5) == 1425


def test_redondea_al_peso_mas_cercano_y_mitad_hacia_arriba():
    assert iva_de_linea(10, 5, 0) == 1


def test_descuento_redondea_al_peso_mas_cercano():
    assert valor_con_descuento(15, 10) == 14


def test_sin_descuento_mantiene_precio():
    assert valor_con_descuento(4500, 0) == 4500


@pytest.mark.parametrize('tarifa', [-1, 8, 20])
def test_rechaza_tarifa_iva_invalida(tarifa):
    with pytest.raises(ValueError):
        iva_de_linea(100000, tarifa, 0)
