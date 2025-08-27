# Química Orgánica – UTN FRN (App en Streamlit)

Repositorio académico multipágina para organizar **temas**, **apuntes**, **clases** y **bibliografía**.

## Estructura
```
quimica-organica-app/
├─ app.py
├─ pages/
│  ├─ 01_Temas.py
│  ├─ 02_Apuntes.py
│  ├─ 03_Clases.py
│  ├─ 05_Bibliografia.py
│  └─ 06_Novedades.py
├─ content/
│  ├─ index.yml
│  └─ temas/
│     ├─ 01_alcanos/ (meta.yml, apuntes.md, ejercicios.md, videos.yml)
│     └─ 02_alquenos/ (meta.yml, apuntes.md, ejercicios.md, videos.yml)
├─ data/ (bibliografia.yml, novedades.yml)
├─ assets/logos/utn.png
├─ utils/ (loaders.py, ui.py)
└─ requirements.txt
```

## Uso local
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy en Streamlit Community Cloud
1. Subí este repo a GitHub (botón "New" → cargar archivos o `git push`).
2. Entra a https://streamlit.io/cloud → "New app" → seleccioná tu repo y `app.py`.
3. Deploy. Listo.

## Agregar/editar contenido
- **Temas**: editar `content/index.yml` y cada carpeta en `content/temas/<id_tema>/`.
- **Videos/Audios**: actualizar `videos.yml` por tema (YouTube/Drive/Zoom).
- **Bibliografía**: `data/bibliografia.yml` (formato libre/APA).
- **Novedades**: `data/novedades.yml`.

> Si tu versión de Streamlit no soporta `st.switch_page`, navega con el menú lateral.