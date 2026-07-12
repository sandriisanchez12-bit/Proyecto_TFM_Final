import streamlit as st
import pandas as pd
import numpy as np
from paginas.conceptos import conceptos_app
from paginas.noticias import noticias_app
from paginas.predicciones import predicciones_app
from paginas.visualizacion import visualizacion_app
from paginas.inicio import inicio_app



st.set_page_config('Agente de Inversiones con IA',
        layout = 'wide')

st.title('📊 Agente de Inversiones en Bolsa con IA 📊')

opcion = st.sidebar.selectbox(
    "Menú:",
    ['Inicio', 
    'Conceptos de Finanzas', 
    'Notícias de Última Hora',  
    'Predicciones',
    'Resultados en PowerBI']
)

if opcion == 'Inicio':
    inicio_app()
elif opcion == 'Conceptos de Finanzas':
    conceptos_app()
elif opcion == 'Notícias de Última Hora':
    noticias_app()
elif opcion == 'Predicciones':
    predicciones_app()
elif opcion == 'Resultados en PowerBI':
    visualizacion_app()