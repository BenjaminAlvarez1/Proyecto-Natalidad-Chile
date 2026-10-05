import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Análisis Pregunta", layout="wide")
st.title("Análisis de la Pregunta")
st.markdown("¿Qué hemos aprendido hasta ahora sobre nuestra pregunta?")

agg_dir = "../data/processed/agg/"
if not os.path.exists(agg_dir + "nacimientos_educ_edad.csv"):
    st.warning("Los datos están siendo procesados. Intenta en unos minutos.")
    st.stop()

@st.cache_data
def load_data():
    df_educ = pd.read_csv(agg_dir + "nacimientos_educ_edad.csv")
    df_nac = pd.read_csv(agg_dir + "nacimientos_por_nacionalidad.csv")
    df_edad = pd.read_csv(agg_dir + "nacimientos_por_edad_madre.csv")
    return df_educ, df_nac, df_edad

df_educ, df_nac, df_edad = load_data()

st.sidebar.header("Filtros")
min_year = int(df_educ['ANO_NAC'].min())
max_year = int(df_educ['ANO_NAC'].max())
selected_year = st.sidebar.slider("Año Específico", min_year, max_year, max_year)

# 4. Educación vs Edad (Barras agrupadas en lugar de Heatmap para mejor resolución)
st.subheader("4. Relación entre Nivel Educacional y Edad de la Madre")
df_educ_f = df_educ[df_educ['ANO_NAC'] == selected_year]
# Limpiar Nulos si es necesario
df_educ_f = df_educ_f.dropna(subset=['NIVEL_MADRE', 'GRUPO_ETARIO_MADRE'])

# Convertir Nivel Madre a string para que Plotly use colores categóricos en lugar de gradiente continuo
df_educ_f['NIVEL_MADRE'] = df_educ_f['NIVEL_MADRE'].astype(str)

fig4 = px.bar(df_educ_f, x="GRUPO_ETARIO_MADRE", y="Nacimientos", color="NIVEL_MADRE",
              barmode="group",
              title=f"Distribución Educacional vs Edad en {selected_year}",
              labels={"GRUPO_ETARIO_MADRE": "Grupo Etario", "NIVEL_MADRE": "Nivel Educacional"})

st.plotly_chart(fig4, use_container_width=True)
st.info("**Hallazgo:** Las mujeres con mayores niveles educativos (Educación Superior) tienden a concentrar los nacimientos en grupos etarios mayores (30-34 y 35-39 años).")

# 5. Evolución por Nacionalidad (Temporal X, Y)
st.subheader("5. Impacto de la Nacionalidad en el Tiempo")

# Mapear códigos de nacionalidad a nombres legibles
nacionalidad_map = {'C': 'Chilena', 'E': 'Extranjera', 'N': 'Nacionalizada'}
df_nac['NACIONALIDAD_MADRE'] = df_nac['NACIONALIDAD_MADRE'].map(nacionalidad_map).fillna(df_nac['NACIONALIDAD_MADRE'])

# Simplificar a Top 5
top_nac = df_nac.groupby('NACIONALIDAD_MADRE')['Nacimientos'].sum().nlargest(5).index
df_nac_top = df_nac[df_nac['NACIONALIDAD_MADRE'].isin(top_nac)]

fig5 = px.line(df_nac_top, x='ANO_NAC', y='Nacimientos', color='NACIONALIDAD_MADRE', markers=True,
               title="Evolución de Nacimientos por Nacionalidad",
               labels={'ANO_NAC':'Año', 'NACIONALIDAD_MADRE': 'Nacionalidad'})
st.plotly_chart(fig5, use_container_width=True)
st.info("**Hallazgo:** Se observa un crecimiento notorio de madres extranjeras a partir de 2015, amortiguando la caída general de la natalidad en Chile.")
