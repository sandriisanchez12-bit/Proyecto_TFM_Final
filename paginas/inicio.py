# inicio.py

import streamlit as st

def inicio_app():

    st.markdown("""
    <style>
    .hero {
        padding: 3rem;
        border-radius: 15px;
        background: linear-gradient(135deg, #0f172a, #1e3a8a);
        color: white;
        text-align: center;
    }

    .feature {
    padding: 25px;
    border-radius: 15px;
    background-color: #f8f9fa;
    text-align: center;
    min-height: 280px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.10);
    transition: 0.3s;
    }

    .feature:hover{
        transform: translateY(-5px);
    }
    </style>
    """, unsafe_allow_html=True)

    # Banner principal
    st.markdown("""
    <div class="hero">
        <h1>📈 Agente de Inversiones en Bolsa con IA</h1>
        <h3>Aprende, analiza e invierte con el poder de la Inteligencia Artificial</h3>
        <p>
            Descubre una nueva forma de entender los mercados financieros mediante
            análisis inteligentes, noticias en tiempo real y visualizaciones interactivas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # Tarjetas de funcionalidades
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="feature">
            <h2>🎓</h2>
            <h4>Aprende</h4>
            <p>
                Accede a contenido teórico sobre inversión, análisis técnico,
                análisis fundamental y gestión del riesgo.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature">
            <h2>📰</h2>
            <h4>Noticias</h4>
            <p>
                Mantente al día con las últimas noticias económicas
                y financieras que impactan en los mercados.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature">
            <h2>🤖</h2>
            <h4>Asistente IA</h4>
            <p>
                Obtén análisis y recomendaciones personalizadas
                mediante modelos avanzados de Inteligencia Artificial.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="feature">
            <h2>📊</h2>
            <h4>Power BI</h4>
            <p>
                Explora dashboards interactivos y visualiza tendencias
                del mercado de forma intuitiva.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.success(
        "🚀 Utiliza el menú lateral para navegar por las distintas funcionalidades de la plataforma."
    )