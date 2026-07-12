import streamlit as st
from servicios.servicio_noticias import obtener_noticias
from servicios.servicio_groc import analizar_evento


def noticias_app():
    st.title("📰 Noticias y su impacto en bolsa")

    news = obtener_noticias()

    if not news:
        st.warning("No se pudieron cargar noticias en este momento.")
        return

    for n in news[:5]:
        st.subheader(n.get("title", "Sin título"))
        st.write(n.get("description", "Sin descripción"))

        if st.button("📊 Analizar impacto", key=n.get("title")):
            with st.spinner("Analizando con Gemini..."):
                analisis = analizar_evento(n.get("title", ""))
                st.info(analisis)
