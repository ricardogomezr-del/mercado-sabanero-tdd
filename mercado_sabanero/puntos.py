"""Programa de puntos del cliente."""


PESOS_POR_PUNTO = 1000
MULTIPLICADOR_ORO = 2


def calcular_puntos(total_sin_envio, categoria):
    if total_sin_envio < 0:
        raise ValueError('Total invalido')
    if categoria not in ('ESTANDAR', 'ORO'):
        raise ValueError('Categoria invalida')
    base = total_sin_envio // PESOS_POR_PUNTO
    return MULTIPLICADOR_ORO * base if categoria == 'ORO' else base
