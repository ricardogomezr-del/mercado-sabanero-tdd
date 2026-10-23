# Plan de pruebas agil - Mercado Sabanero

**Fecha:** 23 de octubre de 2026  
**Modalidad preparada:** individual (sujeta a la autorizacion de la docente).  
**Proyecto:** modulo de liquidacion de compras.  
**Alcance:** solo logica de negocio en Python; sin interfaz de usuario ni base de datos.

## 1. Objetivo

Comprobar que el carrito, el IVA, los descuentos, los cupones, el envio y los puntos funcionen como lo pide el enunciado, incluso cuando los datos estan en los limites permitidos. La meta es detectar fallos antes de entregar el codigo.

## 2. Estrategia y herramientas

- **Python 3**, por su sintaxis clara para este ejercicio.
- **pytest**, para ejecutar pruebas pequeñas y automatizadas con nombres descriptivos.
- **unittest.mock**, para simular el inventario sin depender de otro servicio.
- **pytest-cov / coverage.py**, para medir cuantas lineas del modulo se ejecutan.
- **Git y GitHub Actions**, para guardar el historial TDD y repetir las pruebas con cada cambio publicado.
- **TDD:** primero una prueba que falla, despues la implementacion minima y finalmente una mejora manteniendo las pruebas exitosas.
- **AAA:** preparar los datos, ejecutar la operacion y verificar la respuesta.

## 3. Historias y criterios

- HU-01: agregar productos al carrito (4 criterios).
- HU-02: calcular IVA por tarifa sobre el producto con descuento (2 criterios).
- HU-03: aplicar descuento por volumen segun el subtotal (3 criterios).
- HU-04: validar cupones sin sumar descuentos (4 criterios).
- HU-05: determinar envio y total a pagar (3 criterios).
- HU-06: acumular puntos por total sin envio y duplicarlos para ORO (2 criterios).

La matriz anexa incluye **35 casos**, relacionados con los **18 criterios** anteriores. La suite automatizada ejecuta **63 pruebas** porque algunos casos se prueban con varios datos de entrada.

## 4. Como se ejecutan

1. Instalar las dependencias del archivo `requirements.txt`.
2. Ejecutar `python -m pytest -v` para ver cada prueba.
3. Ejecutar `python -m pytest --cov=mercado_sabanero --cov-report=term-missing --cov-report=html`.
4. Consultar `htmlcov/index.html` para revisar la cobertura por archivo.
5. Al publicar el repositorio, GitHub Actions repite el proceso con cada `push` o `pull_request`.

**Criterios de exito:** minimo 20 pruebas, todas aprobadas; minimo 80% de cobertura de lineas; ejemplo oficial correcto; casos de error, limites y simulacion de inventario incluidos.

## 5. Riesgos y decisiones

- **Stock cambiante:** se sustituye el inventario por un mock controlado para probar la regla sin necesitar un servidor.
- **Calculos de dinero:** todos los montos son pesos enteros; el redondeo es al peso mas cercano con mitades hacia arriba.
- **Descuento e IVA:** el descuento se calcula por linea; el IVA se calcula despues sobre la base descontada.
- **Umbral de envio gratis:** se considera la suma de los importes netos de productos gravados con 5% o 19% de IVA. Es una interpretacion del enunciado, que no precisa si el umbral va antes o despues del descuento.
- **Cupon SABANERO10 con menos de $50.000:** no ofrece descuento. El enunciado no indica que deba generar error.
- **Cupon vencido:** para probarlo sin una fuente externa, el catalogo de cupones incluye `VENCIDO10` como inactivo.
- **Envio para un carrito vacio:** se calcula la tarifa base del destino; el enunciado no define una regla especial para este caso.

## 6. Seguimiento y mantenimiento

Un cambio que haga fallar una prueba debe corregirse antes de continuar. Los defectos se anotan con su descripcion, pasos, impacto y estado. Cuando aparezca una regla nueva se agrega primero un caso y despues el codigo. El historial de Git conserva los ciclos `test:`, `feat:` y `refactor:` de cada historia.
