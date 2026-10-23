"""Programa de puntos del cliente."""


def calcular_puntos(total_sin_envio, categoria):
    if total_sin_envio < 0:
        raise ValueError('Total invalido')
    if categoria not in ('ESTANDAR', 'ORO'):
        raise ValueError('Categoria invalida')
    base = total_sin_envio // 1000
    return 2 * base if categoria == 'ORO' else base
