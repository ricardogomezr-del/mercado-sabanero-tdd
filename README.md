# Mercado Sabanero - pruebas unitarias y TDD

Actividad de logica de negocio (sin interfaz ni base de datos), desarrollada de forma individual.

## Ejecutar

Se necesita Python 3.10 o superior.

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS / Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
python -m pytest --cov=mercado_sabanero --cov-report=term-missing --cov-report=html
```

La carpeta `htmlcov/` generada contiene el informe de cobertura. Las pruebas incluyen el ejemplo completo de la guia.

## Evidencia TDD

El historial incluye ciclos `test:` (falla), `feat:` (pasa) y `refactor:` (mejora conservando las pruebas) para las seis historias HU-01 a HU-06. Se puede revisar con:

```bash
git log --reverse --oneline
```

## Documentacion

Ver `docs/PLAN_PRUEBAS.md`, `docs/MATRIZ_CASOS.csv` y `docs/REGISTRO_DEFECTOS.md`.

## Decisiones tomadas

- Montos en pesos, sin decimales; redondeo comercial `ROUND_HALF_UP`.
- Se aplica el descuento por linea y luego se calcula el IVA correspondiente.
- Para envio gratis, `productos con IVA` significa suma neta (ya descontada) de productos con tarifa 5 % o 19 %.
- Si SABANERO10 no alcanza $50.000, no hay descuento de cupon.
- En una misma compra se usa a lo sumo un cupon.
- El limite de 50 unidades es por producto dentro del carrito, aun despues de agregarlo dos veces.

## Nota de entrega

Para completar la entrega pedida por la docente, publicar este repositorio en GitHub y anadir el nombre del estudiante y el enlace en el informe. La sustentacion TDD en vivo depende de la docente. La tarea se presenta individualmente y no registra revision entre companeros.
