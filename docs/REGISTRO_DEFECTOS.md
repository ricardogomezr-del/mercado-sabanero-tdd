# Registro de defectos

## DEF-001: validacion de stock acumulado

- **Historia:** HU-01 / CA3 y CA4.
- **Estado:** corregido y verificado.
- **Severidad:** alta, porque se podia agregar una cantidad mayor al stock disponible.
- **Descripcion:** al agregar el mismo producto dos veces, el primer intento de codigo validaba solo la nueva cantidad, en vez de sumar lo que ya estaba en el carrito.
- **Pasos para reproducir:** crear un mock de inventario con 6 unidades disponibles; agregar 4 unidades de arroz; volver a agregar 3.
- **Resultado esperado:** lanzar `StockInsuficiente` porque 4 + 3 es mayor que 6.
- **Resultado observado inicialmente:** no se lanzo el error; la prueba falló con `DID NOT RAISE`.
- **Correccion:** comparar el stock contra la nueva cantidad acumulada.
- **Verificacion:** ejecutar de nuevo `test_verifica_stock_de_la_cantidad_acumulada_con_mock` y la suite completa; todas pasaron.
- **Evidencia:** `evidencias/defecto01_fallo.txt`, el codigo en `mercado_sabanero/carrito.py` y el commit `feat: HU-01 agrega carrito y corrige control de stock acumulado`.


