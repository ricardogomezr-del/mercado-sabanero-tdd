# Informe breve individual - Mercado Sabanero

**Asignatura:** Electiva Profesional en Ingenieria de Software.  
**Docente:** Laudyt Maria Lambraño Perez.  
**Estudiante:** [Completar nombre].  
**Fecha:** 23 de octubre de 2026.  
**Repositorio GitHub:** [Pegar enlace despues de publicarlo].

## 1. Que hice

Desarrolle la parte logica de un carrito de compras para Mercado Sabanero. El modulo agrega productos, revisa las cantidades con ayuda de un inventario simulado y calcula descuentos, IVA, envio y puntos. No tiene pantallas ni conexion a base de datos porque el ejercicio solo pide las reglas de negocio.

## 2. Herramientas

Use Python por ser facil de leer; pytest para verificar los resultados; unittest.mock para fingir las respuestas del inventario; pytest-cov para comprobar la cobertura; y Git para separar pruebas, desarrollo y mejoras en commits. El repositorio tambien trae una configuracion de GitHub Actions para repetir las pruebas cuando se publique.

## 3. Como aplique TDD

Para cada una de las seis historias cree pruebas primero, las ejecute para verlas fallar, escribi lo necesario para que pasaran y despues mejore el codigo sin cambiar el resultado. El historial local tiene commits con los prefijos `test:`, `feat:` y `refactor:`. Esto se puede comprobar con `git log --reverse --oneline`.

Un caso importante fue el stock acumulado. Una prueba demostro que si habia 6 unidades disponibles no debia permitir agregar 4 y luego 3 del mismo producto. El primer intento no rechazo la segunda operacion; corregi la comparacion y volvi a ejecutar las pruebas.

## 4. Resultados

- **Casos de la matriz:** 35 planeados, 35 con resultado esperado cubierto y aprobado.
- **Pruebas automatizadas:** 63 ejecutadas; 63 exitosas; 0 fallidas; 0 bloqueadas.
- **Cobertura del codigo:** 97% de lineas (mayor al 80% solicitado).
- **Errores registrados:** 1, corregido y verificado.

El ejemplo de la guia dio subtotal $228.000, descuento $11.400, IVA $33.915, envio $0, total $250.515 y 250 puntos para cliente ESTANDAR. Los resultados coinciden con la actividad.

## 5. Dificultades y conclusiones

La parte mas delicada fue controlar cantidades repetidas y el orden del calculo del descuento y el IVA. Trabajar con pruebas pequeñas permitio comprobar cada regla sin tener que montar una tienda completa. Tambien aprendi a mirar los limites: 0 y 51 unidades, $199.999 y $200.000, y compras cercanas al envio gratis.

La principal conclusion es que una prueba escrita antes del codigo ayuda a aclarar el comportamiento esperado y evita dar por bueno un resultado solo porque a simple vista parece correcto.

## 6. Declaracion de apoyo de IA

Use una herramienta de inteligencia artificial como apoyo para estructurar el codigo, redactar documentacion y revisar casos de prueba. La ejecucion de las pruebas y el reporte de cobertura se realizaron sobre el codigo incluido en esta entrega. La explicacion y sustentacion del contenido corresponden al estudiante.

**Alcance individual:** se omiten la revision entre companeros y la coevaluacion grupal. La sustentacion en vivo y la autorizacion de la modalidad individual dependen de la docente.
