# -*- coding: utf-8 -*-
import streamlit as st
from utils.loaders import list_temas, load_tema

st.set_page_config(page_title="Temas", page_icon="📚", layout="wide")

st.title("Temas")
st.write("Explorá los contenidos y abrí un tema para ver apuntes, clases y ejercicios.")

temas = list_temas()
ids = [t["id"] for t in temas]
labels = {t["id"]: f"{t['id'][3:]} — {t['titulo']}" for t in temas}

# Sidebar: selector y filtros simples
with st.sidebar:
    st.header("Navegación")
    default_sel = st.session_state.get("tema_id", ids[0] if ids else None)
    sel = st.selectbox("Tema", options=ids, index=ids.index(default_sel) if default_sel in ids else 0, format_func=lambda x: labels.get(x, x))

if not sel:
    st.warning("No hay temas aún.")
    st.stop()

# Cargar contenido del tema seleccionado
data = load_tema(sel)
meta = data["meta"]

st.subheader(meta.get("titulo", "Tema"))
st.caption(", ".join(meta.get("tags", [])))

col1, col2 = st.columns([2,1])
with col1:
    st.markdown("##### Objetivos de aprendizaje")
    for obj in meta.get("objetivos", []):
        st.write("- " + obj)
with col2:
    img_path = meta.get("imagen", None)
    if img_path:
        st.image(img_path, use_container_width=True)

st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["Apuntes", "Clases (video/audio)", "Ejercicios", "Material complementario"])

with tab1:
    st.markdown(data["apuntes"] or "_Sin apuntes por ahora._")

with tab2:
    media = data["media"] or {}
    vids = media.get("videos", [])
    auds = media.get("audios", [])
    if vids:
        st.markdown("**Videos**")
        for v in vids:
            st.write(v.get("titulo",""))
            st.video(v.get("url",""))
    if auds:
        st.markdown("**Audios**")
        for a in auds:
            st.write(a.get("titulo",""))
            st.audio(a.get("url",""))
    if not vids and not auds:
        st.info("Sin material multimedia aún.")

with tab3:
    st.markdown(data["ejercicios"] or "_Sin ejercicios por ahora._")

with tab4:
    mats = media.get("material", [])
    if mats:
        for m in mats:
            st.markdown(f"- [{m.get('titulo','Enlace')}]({m.get('url','')})")
    else:
        st.info("Sin material complementario aún.")