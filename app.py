# -*- coding: utf-8 -*-
import streamlit as st
from pathlib import Path
from utils.loaders import load_index, list_temas
from utils.ui import tema_card

st.set_page_config(
    page_title="Química Orgánica – UTN FRN",
    page_icon="🧪",
    layout="wide",
)

idx = load_index()

# Encabezado institucional
col1, col2 = st.columns([1,3])
with col1:
    st.image(str(Path("assets/logos/utn.png")), use_container_width=True)
with col2:
    st.title(idx.get("catedra", "Química Orgánica"))
    st.subheader("Repositorio académico de la materia")
    st.write(f"**Profesor/a**: {idx.get('profesor','')}")
    autores = idx.get("autores", [])
    if autores:
        st.write("**Autores**: " + ", ".join(autores))

# Introducción
with st.container(border=True):
    st.markdown(idx.get("introduccion",""))

st.divider()

# Navegación rápida por tema (selectbox)
temas = list_temas()
tema_labels = {t["id"]: f"{t['id'][3:]} — {t['titulo']}" for t in temas}
seleccion = st.selectbox("Ir a un tema:", options=["(Elegir)"] + [t["id"] for t in temas],
                         format_func=lambda x: tema_labels.get(x, x))

colA, colB = st.columns([1,4])
with colA:
    if st.button("Abrir tema seleccionado"):
        if seleccion != "(Elegir)":
            st.session_state["tema_id"] = seleccion
            try:
                st.switch_page("pages/01_Temas.py")
            except Exception:
                st.success("Tema seleccionado. Abrí la página **Temas** en la barra lateral.")

with colB:
    st.info("También podés usar las tarjetas de abajo o la página **Temas** en el menú.")

st.markdown("### Temas destacados")
for t in temas:
    tema_card(t)

st.divider()
st.markdown("#### Accesos rápidos")
st.page_link("pages/01_Temas.py", label="Temas (Explorador)", icon="📚")
st.page_link("pages/02_Apuntes.py", label="Apuntes", icon="📝")
st.page_link("pages/03_Clases.py", label="Clases", icon="🎥")
st.page_link("pages/05_Bibliografia.py", label="Bibliografía", icon="📖")
st.page_link("pages/06_Novedades.py", label="Novedades", icon="🗞️")

st.caption("v0.1 – Este sitio es un prototipo académico sin credenciales ni base de datos.")