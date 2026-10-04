import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Natalidad Chile", page_icon="👶", layout="wide")

st.title("👶 Transición Demográfica y Natalidad en Chile")
st.subheader("Proyecto 2026-II | EIN092B Visualización")

st.markdown("""
### Contexto del Proyecto
Este proyecto analiza la disminución de los nacimientos y el envejecimiento de la población en Chile.

**Pregunta Principal:**
¿Cómo influyen el nivel educacional, la situación laboral, la nacionalidad y la región de residencia en la cantidad de nacimientos y el grupo etario de la madre a lo largo del tiempo?

**Variables Principales:**
* **X (Predictores):** Nivel educativo, ocupación, nacionalidad y región de la madre.
* **Y (Objetivo):** Cantidad de nacimientos y Grupo Etario de la madre.
* **T (Temporal):** Periodo histórico 2001 - 2023.

---
### Descripción y Preparación del Dataset
Los datos provienen del DEIS (Ministerio de Salud) y registran todos los nacidos vivos en Chile. Hemos procesado más de 5 millones de registros históricos.

**Decisiones de Limpieza y Preparación:**
1. **Volumen de Datos:** Al exceder el límite de 1 millón de filas de Excel, el dataset completo se procesó mediante scripts de Python y se exportó a formato CSV.
2. **Valores Faltantes:** Se observó que los registros más antiguos (2001-2010) contienen una mayor proporción de datos no declarados (nulos) en características de los padres, mientras que la información geográfica y del parto es muy sólida. Se optó por **no eliminar** estos nulos masivamente para no perder la representatividad histórica, sino que se excluyen de forma dinámica solo al cruzar variables específicas en el EDA.
3. **Optimización:** Para asegurar la fluidez de esta aplicación, los datos mostrados son pre-agregaciones estadísticas generadas a partir de los 5 millones de registros base.
""")

# Intentar mostrar algunas estadísticas si los datos agregados ya existen
if os.path.exists("../data/processed/agg/nacimientos_por_mes_ano.csv"):
    df_agg = pd.read_csv("../data/processed/agg/nacimientos_por_mes_ano.csv")
    total = df_agg['Nacimientos'].sum()
    
    st.markdown("### 📊 Resumen de Datos")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Registros Totales", f"{total:,}".replace(',', '.'))
    col2.metric("Periodo", "2001 - 2023")
    col3.metric("Variables", "25")
    col4.metric("Tamaño Datos", "+5 Millones de filas")
else:
    st.info("Los datos agregados se están calculando... Vuelve a cargar la página en unos minutos.")

st.markdown("""
---
*Navega a través de las páginas en el menú lateral para explorar los datos (EDA) y analizar la pregunta del proyecto.*
""")
