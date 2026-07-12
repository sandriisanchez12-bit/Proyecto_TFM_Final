import streamlit as st
import pandas as pd


def predicciones_app():
    st.subheader('Modelo predictivo')

    st.write("""
    En esta sección se presenta el modelo de Inteligencia Artificial desarrollado durante el Trabajo Fin de Máster.
    Tras evaluar diferentes enfoques para la predicción de mercados financieros, el estudio concluyó que la
    predicción de la dirección futura del precio del S&P 500 no ofrecía una capacidad predictiva significativa.
    """)
    st.write("""
    Como alternativa, se desarrolló un modelo basado en **XGBoost** cuyo objetivo es **predecir los regímenes
    de volatilidad futura del índice S&P 500** utilizando información histórica procedente de diferentes activos
    financieros, como índices bursátiles, materias primas, el índice de volatilidad VIX y el índice del dólar (DXY).
    """)
    st.write("""
    A continuación puede descargar la documentación técnica del modelo, donde se describe la metodología
    empleada, el proceso de entrenamiento, las variables utilizadas y las métricas obtenidas durante la evaluación.
    """)
    st.divider()

    pdf_path = "modeloIA\documentacion_tfm.pdf"

    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    st.write("### 📄 Descargar resumen del análisis del modelo de IA")

    st.download_button(
        label="📥 Descargar PDF del análisis",
        data=pdf_bytes,
        file_name="analisis_modelo_IA.pdf",
        mime="application/pdf"
    )
    