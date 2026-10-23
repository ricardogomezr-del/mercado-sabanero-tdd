"""HU-04: cupones y reglas de no acumulacion."""
import pytest
from mercado_sabanero.cupones import CuponInvalido, descuento_cupon, envio_gratis_por_cupon, descuento_final


def test_sabanero10_aplica_diez_por_ciento_desde_cincuenta_mil():
    # Preparar
    subtotal, cupon = 50000, 'SABANERO10'
    # Ejecutar
    porcentaje = descuento_cupon(subtotal, cupon)
    # Verificar
    assert porcentaje == 10


def test_sabanero10_no_aplica_por_debajo_de_cincuenta_mil():
    assert descuento_cupon(49999, 'SABANERO10') == 0


def test_cupon_envio_gratis_activa_beneficio():
    assert envio_gratis_por_cupon('ENVIOGRATIS') is True


def test_sabanero10_no_cambia_costo_de_envio():
    assert envio_gratis_por_cupon('SABANERO10') is False


@pytest.mark.parametrize('cupon', ['FALSO', 'VENCIDO10'])
def test_rechaza_cupon_inexistente_o_vencido(cupon):
    with pytest.raises(CuponInvalido):
        descuento_cupon(70000, cupon)


def test_no_acumula_descuento_volumen_y_sabanero10():
    # Preparar: descuento de volumen de 5 %, cupon de 10 %
    # Ejecutar
    porcentaje = descuento_final(220000, 'SABANERO10')
    # Verificar
    assert porcentaje == 10


def test_con_descuento_volumen_diez_no_se_suma_otro_diez():
    assert descuento_final(500000, 'SABANERO10') == 10


def test_sin_cupon_aplica_descuento_de_volumen():
    assert descuento_final(220000, None) == 5


def test_envio_gratis_no_elimina_descuento_de_volumen():
    assert descuento_final(220000, 'ENVIOGRATIS') == 5
