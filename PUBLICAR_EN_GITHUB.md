# Publicar el trabajo en GitHub (Windows)

Este ZIP contiene una carpeta `.git` con el historial TDD real. Para que la profesora vea los commits, publica el repositorio **conservando esa carpeta**.

1. Descomprime `Mercado_Sabanero_Codigo_TDD.zip` y abre una terminal dentro de la carpeta `mercado-sabanero`.
2. En GitHub, crea un repositorio nuevo y vacio llamado `mercado-sabanero-tdd`. No marques inicializar con README, licencia ni `.gitignore`, porque el trabajo ya los incluye.
3. Sustituye `TU_USUARIO` por tu usuario de GitHub y ejecuta:

```bash
git remote add origin https://github.com/TU_USUARIO/mercado-sabanero-tdd.git
git push -u origin main
```

4. Abre la pestaña **Commits** y verifica los ciclos `test:`, `feat:` y `refactor:`.
5. Agrega a la profesora como colaboradora en **Settings > Collaborators**, si te lo pidio.
6. Escribe tu nombre y el enlace del repositorio en la portada del informe PDF antes de entregarlo. La entrega individual necesita autorizacion de la docente.

Si Git indica que `origin` ya existe, ejecuta `git remote set-url origin https://github.com/TU_USUARIO/mercado-sabanero-tdd.git` y vuelve a hacer `git push -u origin main`.

## Verificar las pruebas

```bash
python -m pip install -r requirements.txt
python -m pytest --cov=mercado_sabanero --cov-fail-under=80 --cov-report=term-missing
```

No se necesita interfaz grafica ni base de datos.
