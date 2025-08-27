# -*- coding: utf-8 -*-
import streamlit as st
from utils.loaders import list_temas, load_tema

st.set_page_config(page_title="Clases", page_icon="🎥", layout="wide")
st.title("Clases – Videos y Audios")

for t in list_temas():
    data = load_tema(t["id"])
    media = data["media"] or {}
    vids = media.get("videos", [])
    auds = media.get("audios", [])
    if not vids and not auds:
        continue
    with st.expander(f"{t['titulo']}"):
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