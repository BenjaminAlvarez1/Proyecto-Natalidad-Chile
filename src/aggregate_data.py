import pandas as pd
import os

print("Cargando datos 2001-2019...")
df_hist = pd.read_csv('../data/raw/Serie_Nacimientos_2001_2019.csv', sep=';')
print("Cargando datos 2020-2023...")
df_rec = pd.read_excel('../data/processed/Nacimientos_2020_2023_Procesado.xlsx')

print("Concatenando...")
df = pd.concat([df_hist, df_rec], ignore_index=True)

print("Generando agregaciones para Streamlit...")
os.makedirs('../data/processed/agg', exist_ok=True)

agg_time = df.groupby(['ANO_NAC', 'MES_NAC']).size().reset_index(name='Nacimientos')
agg_time.to_csv('../data/processed/agg/nacimientos_por_mes_ano.csv', index=False)

agg_region = df.groupby(['ANO_NAC', 'GLOSA_REGION_RESIDENCIA']).size().reset_index(name='Nacimientos')
agg_region.to_csv('../data/processed/agg/nacimientos_por_region_ano.csv', index=False)

agg_edad = df.groupby(['ANO_NAC', 'GRUPO_ETARIO_MADRE']).size().reset_index(name='Nacimientos')
agg_edad.to_csv('../data/processed/agg/nacimientos_por_edad_madre.csv', index=False)

agg_nac = df.groupby(['ANO_NAC', 'NACIONALIDAD_MADRE']).size().reset_index(name='Nacimientos')
agg_nac.to_csv('../data/processed/agg/nacimientos_por_nacionalidad.csv', index=False)

agg_educ = df.groupby(['ANO_NAC', 'NIVEL_MADRE', 'GRUPO_ETARIO_MADRE']).size().reset_index(name='Nacimientos')
agg_educ.to_csv('../data/processed/agg/nacimientos_educ_edad.csv', index=False)

df_sample = df.sample(frac=0.01, random_state=42)
df_sample.to_csv('../data/processed/agg/sample_nacimientos.csv', index=False)

print("Agregaciones listas en data/processed/agg/")
