import streamlit as st
import pandas as pd


def predicciones_app():
    st.subheader("Modelo predictivo")

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

    st.divider()

    st.subheader("Resumen del desarrollo del modelo")

    st.markdown("""
    El modelo de Inteligencia Artificial se desarrolló siguiendo tres fases principales:
    **preprocesamiento de los datos**, **entrenamiento del modelo** y **evaluación sobre un conjunto de prueba independiente**.
    """)

    # ======================================================
    # PREPROCESAMIENTO
    # ======================================================
    with st.expander("1️⃣ Preprocesamiento de los datos"):

        st.markdown("""
        **Datos utilizados**

        - Periodo: **31/08/2000 – 31/12/2025**
        - Fuente: **Yahoo Finance (yfinance)**
        - Activos empleados:
            - S&P 500
            - Oro
            - Plata
            - Cobre
            - Petróleo WTI
            - Gas Natural
            - Índice del dólar (DXY)
            - Índice de volatilidad VIX

        Se utilizaron los retornos logarítmicos de todos los activos, además del nivel del VIX.
        """)

        st.markdown("""
        **Objetivo del modelo**

        El modelo intenta predecir si durante los **próximos 10 días** el mercado entrará en un régimen de:

        - Baja volatilidad
        - Alta volatilidad

        La clasificación de alta volatilidad se definió utilizando el percentil 70 de la volatilidad calculado únicamente sobre el conjunto de entrenamiento.
        """)

        st.markdown("""
        **Conjuntos de datos**

        | Conjunto | Muestras | Variables |
        |-----------|---------:|----------:|
        | Train | 4089 | 97 |
        | Validation | 502 | 97 |
        | Test | 1496 | 97 |
        """)

        st.markdown("""
        **Distribución de clases**

        - Train: 70 % baja volatilidad / 30 % alta volatilidad
        - Validation: 75.3 % / 24.7 %
        - Test: 66.2 % / 33.8 %
        """)

        st.info("""
        Se aplicó una **purga temporal de 10 días** entre Train, Validation y Test para evitar **data leakage**.
        Esta técnica es especialmente importante en series temporales financieras, ya que las etiquetas utilizan información futura.
        """)

    # ======================================================
    # ENTRENAMIENTO
    # ======================================================
    with st.expander("2️⃣ Entrenamiento del modelo"):

        st.markdown("""
        Se entrenó un modelo de **XGBoost** utilizando las **97 variables predictoras** generadas durante el preprocesamiento.

        Entre las variables utilizadas se incluyen:

        - retornos recientes del S&P 500
        - volatilidad histórica
        - medias móviles
        - indicadores del VIX
        - correlaciones entre activos
        - variables del dólar, oro, petróleo y otras materias primas.
        """)

        st.markdown("""
        Los hiperparámetros se optimizaron mediante **Optuna**, realizando **600 pruebas (trials)** para maximizar la métrica **ROC-AUC**.

        Algunos de los parámetros optimizados fueron:

        - profundidad de los árboles
        - learning rate
        - número de árboles
        - regularización
        - peso de las clases
        - número de muestras por árbol
        """)

        st.markdown("""
        **Mejor resultado de Optuna**

        - Mejor trial: **336**
        - ROC-AUC validación: **0.7784**
        """)

        st.markdown("""
        Como XGBoost devuelve probabilidades, también se buscó automáticamente el **threshold óptimo**, obteniendo un valor de **0.36**, superior al uso tradicional de 0.50 para este problema.

        Durante el entrenamiento se aplicó **early stopping** para evitar sobreajuste.
        """)

    # ======================================================
    # EVALUACIÓN
    # ======================================================
    with st.expander("3️⃣ Evaluación del modelo"):

        st.markdown("""
        El modelo entrenado se evaluó sobre un conjunto de prueba completamente independiente.

        **Resultados principales**

        - Accuracy (Directional Accuracy): **77.41 %**
        - ROC-AUC: **0.824**
        - F1-macro: **0.7509**
        - p-value < **0.0001**
        """)

        st.markdown("""
        El ROC-AUC de **0.824** indica una buena capacidad para distinguir entre periodos de alta y baja volatilidad, mientras que el p-valor confirma que el rendimiento es significativamente superior al azar.
        """)

        st.markdown("""
        El modelo obtiene un mejor rendimiento detectando periodos de **baja volatilidad** (F1 = 0.83) que episodios de **alta volatilidad** (F1 = 0.68), algo habitual debido a que estos últimos son menos frecuentes y presentan una mayor complejidad.
        """)

        st.success("""
        En conjunto, el modelo demuestra una buena capacidad para anticipar cambios de régimen de volatilidad a un horizonte de 10 días, lo que puede resultar de utilidad en tareas de gestión del riesgo, cobertura y ajuste dinámico del tamaño de las posiciones.
        """)

    st.write("""
    A continuación puede descargar la documentación técnica del modelo, donde se describe la metodología empleada,
    el proceso de entrenamiento, las variables utilizadas y las métricas obtenidas durante la evaluación.
    """)

    st.divider()

    pdf_path = "modeloIA/documentacion_tfm.pdf"

    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    st.write("### 📄 Descargar resumen del análisis del modelo de IA")

    st.download_button(
        label="📥 Descargar PDF del análisis",
        data=pdf_bytes,
        file_name="analisis_modelo_IA.pdf",
        mime="application/pdf",
    )
    
