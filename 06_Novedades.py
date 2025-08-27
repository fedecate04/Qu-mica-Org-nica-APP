# -*- coding: utf-8 -*-
import streamlit as st
from utils.loaders import load_novedades

st.set_page_config(page_title="Novedades", page_icon="🗞️", layout="wide")
st.title("Novedades")

nov = load_novedades()
for it in nov.get("items", []):
    st.markdown(f"**{it.get('fecha','')}** — {it.get('descripcion','')}")