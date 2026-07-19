import streamlit as st
import base64

def visualizacion_app():

    st.header("Resultados del modelo de Inteligencia Artificial")
    st.write("""
    En esta sección se presentan los resultados obtenidos tras el entrenamiento y evaluación
    del modelo XGBoost. El informe, desarrollado en Microsoft Power BI, recoge las principales
    métricas de rendimiento y diferentes visualizaciones que facilitan la interpretación de los
    resultados obtenidos.
    """)
    st.image("powerbis/metricas_xgboost.png", use_container_width=True)
    
    st.divider()

    st.subheader("Visualizaciones del modelo")
    st.write("""
    A continuación se muestran algunas de las representaciones gráficas más relevantes obtenidas durante
    la evaluación del modelo XGBoost, las cuales permiten interpretar su capacidad predictiva y el
    comportamiento de las variables empleadas.
    """)
    st.markdown("### 📈 Curva ROC")
    st.image(
        "modeloIA/results_vol/roc.png",
        caption="Curva ROC obtenida sobre el conjunto de test.",
        use_container_width=True
    )
    st.markdown("### 🔲 Matriz de confusión")
    st.image(
        "modeloIA/results_vol/confusion_matrix.png",
        caption="Matriz de confusión del modelo XGBoost.",
        use_container_width=True
    )
    st.markdown("### ⭐ Importancia de las variables (Feature Importance)")
    st.image(
        "modeloIA/results_vol/feature_importance.png",
        caption="Importancia de las variables utilizadas por el modelo XGBoost para la predicción de los regímenes de volatilidad del S&P 500.",
        use_container_width=True
    )
