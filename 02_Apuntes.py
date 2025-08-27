# -*- coding: utf-8 -*-
import streamlit as st
from utils.loaders import list_temas, load_tema

st.set_page_config(page_title="Apuntes", page_icon="📝", layout="wide")
st.title("Apuntes")

q = st.text_input("Buscar en títulos y contenido...", "")

for t in list_temas():
    data = load_tema(t["id"])
    cuerpo = (data["apuntes"] or "") + "\n" + (data["ejercicios"] or "")
    if q.strip() and (q.lower() not in t["titulo"].lower() and q.lower() not in cuerpo.lower()):
        continue
    with st.container(border=True):
        st.subheader(t["titulo"])
        st.caption(", ".join(data["meta"].get("tags", [])))
        st.markdown(data["apuntes"] or "_Sin apuntes_")