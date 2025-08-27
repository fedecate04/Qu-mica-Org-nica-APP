import streamlit as st

def tag_badge(tag: str):
    st.markdown(f"<span style='background:#eef; padding:2px 8px; border-radius:12px; margin-right:6px;'>{tag}</span>", unsafe_allow_html=True)

def tema_card(tema: dict):
    cols = st.columns([0.8, 0.2])
    with cols[0]:
        st.subheader(tema.get("titulo", "Tema"))
        st.caption(tema.get("resumen", ""))
        tags = tema.get("tags", [])
        if tags:
            st.write("")
            for tg in tags:
                tag_badge(tg)
    with cols[1]:
        st.write("")
        st.write("")
        st.button("Abrir", key=f"open_{tema['id']}", on_click=_select_tema, args=(tema["id"],))

def _select_tema(tema_id: str):
    st.session_state["tema_id"] = tema_id
    # Nota: si tu Streamlit soporta st.switch_page, podés navegar directo:
    try:
        st.switch_page("pages/01_Temas.py")
    except Exception:
        pass