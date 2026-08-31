# Transición Demográfica y Natalidad en Chile

## Proyecto 2026-II | EIN092B Visualización
**Autor:** Benjamín Álvarez  
**Profesor:** Jesús A. Parra  

---

## 1. Problema y Motivación
Este proyecto analiza la disminución de los nacimientos y el envejecimiento de la población en Chile. 

**¿Por qué vale la pena estudiarlo?**
Entender cómo está cambiando nuestra población es fundamental para planificar a futuro en temas como salud y educación. Además, los datos muestran que esta caída en la natalidad no ocurre de forma igual en todos los sectores, sino que varía dependiendo de factores como la educación, la situación laboral y la zona de residencia de las personas.

## 2. Pregunta y Alcance
**Pregunta Principal:**
¿Cómo influyen el nivel educacional, la situación laboral, la nacionalidad y la región de residencia (X) en la cantidad de nacimientos y el grupo etario de la madre (Y) entre los años 2020 y 2023 (T)?

**Alcance:**
* **Población y Región:** 735.611 nacidos vivos registrados en las 16 regiones de Chile.
* **Periodo:** Años 2020 a 2023 (con granularidad mensual).
* **Límites:** El análisis geográfico se mantiene a nivel regional (no comunal). La edad se maneja en rangos de 5 años (ej. 25 a 29 años), y los datos del padre presentan alta cantidad de información no declarada, por lo que el análisis de características se enfoca principalmente en el perfil de la madre.

## 3. Estructura X, Y y T
* **X (Variables explicativas):** Características de los padres (Nivel de educación, Actividad laboral, Nacionalidad, Región).
* **Y (Objetivo/Fenómeno):** Cantidad de nacimientos (recuento) y Grupo Etario de la madre al momento del parto.
* **T (Contexto temporal):** Periodo 2020-2023, analizado por año y mes.

## 4. Dataset y Narrativa Inicial
* **Fuente:** Departamento de Estadísticas e Información de Salud (DEIS) del Ministerio de Salud.
* **Observaciones:** 735.611 registros. Cada fila corresponde a un niño o niña nacido vivo.
* **Variables Principales:** Grupo etario, nivel educacional, actividad laboral, nacionalidad y región.
* **Narrativa:** El dataset representa el panorama actual de los nacimientos en Chile. La historia que buscamos explorar es cómo los distintos perfiles influyen en cuándo y cuántos hijos se tienen. Por ejemplo, observaremos cómo las madres con estudios superiores tienden a tener hijos después de los 30 años, o cómo la población extranjera ayuda a estabilizar la cantidad de nacimientos en algunas zonas específicas.

## 5. Estructura del Repositorio
```text
Proyecto-Natalidad-Chile/
├── data/
│   ├── raw/               # Dataset original CSV y diccionario Excel (excluidos de git por tamaño)
│   └── processed/         # Dataset procesado y ordenado (.xlsx)
├── notebooks/             # Scripts de exploración y análisis inicial
├── src/                   # Funciones reutilizables
├── figures/               # Gráficos e imágenes
├── app/                   # Aplicación de visualización (futuro Avance)
├── README.md              # Documentación principal del proyecto
└── .gitignore             # Configuración de archivos ignorados
```
