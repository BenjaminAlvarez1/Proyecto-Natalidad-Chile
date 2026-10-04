# Transición Demográfica y Natalidad en Chile

## Proyecto 2026-II | EIN092B Visualización
**Autor:** Benjamín Álvarez  
**Profesor:** Jesús A. Parra  

---

## 1. Problema y Motivación
Este proyecto analiza la disminución de los nacimientos y el envejecimiento de la población en Chile. Entender cómo está cambiando nuestra población es fundamental para planificar a futuro en temas como salud y educación. Además, los datos muestran que esta caída en la natalidad no ocurre de forma igual en todos los sectores, sino que varía dependiendo de factores como la educación, la situación laboral y la zona de residencia de las personas.

## 2. Pregunta y Alcance
**Pregunta Principal:**
¿Cómo influyen el nivel educacional, la situación laboral, la nacionalidad y la región de residencia (X) en la cantidad de nacimientos y el grupo etario de la madre (Y) entre los años 2001 y 2023 (T)?

**Alcance:**
* **Población:** Más de 5 millones de nacidos vivos registrados.
* **Periodo:** Años 2001 a 2023.
* **Variables:** El análisis de características se enfoca principalmente en el perfil de la madre debido a la alta integridad de esos datos.

## 3. Dataset
* **Fuente:** Departamento de Estadísticas e Información de Salud (DEIS) del Ministerio de Salud.
* **Procesamiento:** Debido al tamaño de los datos combinados (más de 5.2 millones de filas), el procesamiento incluye scripts de agregación para optimizar la carga en Streamlit. Los datos originales se mantienen en `data/raw` (CSV y XLSX) y las versiones agrupadas en `data/processed/agg`.

## 4. Estructura del Repositorio
```text
Proyecto-Natalidad-Chile/
├── data/
│   ├── raw/               # Dataset original CSV y diccionario Excel
│   └── processed/         # Dataset procesado y agregaciones (.csv/.parquet)
├── notebooks/             # Scripts de exploración inicial (.gitkeep)
├── src/                   # Funciones y scripts de preparación de datos
│   └── aggregate_data.py  # Script para agregar y procesar los >5M registros
├── figures/               # Gráficos estáticos exportados (.gitkeep)
├── app/                   # Aplicación interactiva
│   ├── app.py             # Portada y Contexto (Página 1)
│   └── pages/
│       ├── 1_Exploracion.py # EDA - Distribuciones y Tiempo (Página 2)
│       └── 2_Analisis.py    # Cruce de Variables y Hallazgos (Página 3)
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación principal
```

## 5. Instrucciones de Ejecución

1. Crear un entorno virtual e instalar dependencias:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # En Windows
   pip install -r requirements.txt
   ```

2. Generar las agregaciones iniciales (si no están generadas):
   ```bash
   cd src
   python aggregate_data.py
   cd ..
   ```

3. Ejecutar la aplicación:
   ```bash
   cd app
   streamlit run app.py
   ```
