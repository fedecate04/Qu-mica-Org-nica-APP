# -*- coding: utf-8 -*-
import streamlit as st
from utils.loaders import load_bibliografia

st.set_page_config(page_title="Bibliografía", page_icon="📖", layout="wide")
st.title("Bibliografía")

bib = load_bibliografia()
for ref in bib.get("referencias", []):
    st.markdown(f"- {ref.get('autores','')} ({ref.get('año','')}). *{ref.get('titulo','')}*. {ref.get('editorial','')}.")