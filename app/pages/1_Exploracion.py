import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="EDA - Natalidad", page_icon="📈", layout="wide")
st.title("📈 Análisis Exploratorio de Datos (EDA)")
st.markdown("¿Cómo se comportan nuestros datos a nivel macro?")

agg_dir = "../data/processed/agg/"
if not os.path.exists(agg_dir + "nacimientos_por_mes_ano.csv"):
    st.warning("Los datos están siendo procesados. Intenta en unos minutos.")
    st.stop()

# Funciones de carga
@st.cache_data
def load_data():
    df_time = pd.read_csv(agg_dir + "nacimientos_por_mes_ano.csv")
    df_region = pd.read_csv(agg_dir + "nacimientos_por_region_ano.csv")
    df_edad = pd.read_csv(agg_dir + "nacimientos_por_edad_madre.csv")
    return df_time, df_region, df_edad

df_time, df_region, df_edad = load_data()

st.sidebar.header("Filtros")
min_year, max_year = int(df_time['ANO_NAC'].min()), int(df_time['ANO_NAC'].max())
selected_years = st.sidebar.slider("Rango de Años", min_year, max_year, (min_year, max_year))

# Filtrar datos
df_time_f = df_time[(df_time['ANO_NAC'] >= selected_years[0]) & (df_time['ANO_NAC'] <= selected_years[1])]
df_region_f = df_region[(df_region['ANO_NAC'] >= selected_years[0]) & (df_region['ANO_NAC'] <= selected_years[1])]
df_edad_f = df_edad[(df_edad['ANO_NAC'] >= selected_years[0]) & (df_edad['ANO_NAC'] <= selected_years[1])]

# 1. Evolución Temporal (Línea)
st.subheader("1. Evolución Temporal de Nacimientos")
nac_por_ano = df_time_f.groupby('ANO_NAC')['Nacimientos'].sum().reset_index()
fig1 = px.line(nac_por_ano, x='ANO_NAC', y='Nacimientos', markers=True, 
               title="Nacimientos Totales por Año en Chile",
               labels={'ANO_NAC': 'Año', 'Nacimientos': 'Total Nacimientos'})
st.plotly_chart(fig1, use_container_width=True)
st.info("💡 **Interpretación:** Se observa una tendencia general a la baja en la natalidad, especialmente marcada en los últimos años.")

col1, col2 = st.columns(2)

# 2. Distribución Espacial (Barras)
with col1:
    st.subheader("2. Distribución por Región")
    nac_region = df_region_f.groupby('GLOSA_REGION_RESIDENCIA')['Nacimientos'].sum().reset_index().sort_values('Nacimientos')
    fig2 = px.bar(nac_region, y='GLOSA_REGION_RESIDENCIA', x='Nacimientos', orientation='h',
                  title="Nacimientos por Región", labels={'GLOSA_REGION_RESIDENCIA':'Región'})
    st.plotly_chart(fig2, use_container_width=True)

# 3. Distribución Etaria de la Madre (Barras o KDE aproximado)
with col2:
    st.subheader("3. Grupo Etario de la Madre")
    nac_edad = df_edad_f.groupby('GRUPO_ETARIO_MADRE')['Nacimientos'].sum().reset_index()
    fig3 = px.bar(nac_edad, x='GRUPO_ETARIO_MADRE', y='Nacimientos',
                  title="Distribución de Edad de la Madre", 
                  labels={'GRUPO_ETARIO_MADRE':'Grupo Etario'})
    st.plotly_chart(fig3, use_container_width=True)
