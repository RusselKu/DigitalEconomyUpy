# 05. Guía de Reproducibilidad y Defensa para Integrantes del Equipo

**Equipo 3: Agricultura**  
**Proyecto:** Digital Economy Intelligence Lab  
**Entregable:** Actividad 2 · Parte I

---

## 1. Responsabilidad Individual y Defensa del Proyecto
> **Regla de la Actividad:** Aunque el proyecto se desarrolló en equipo, cada integrante debe poder explicar individualmente la procedencia de los datos, el significado de cada uno de los 8 indicadores, el método de normalización del DRS y las conclusiones cuantitativas obtenidas.

---

## 2. Estructura de Archivos del Repositorio

```text
DigitalEconomyUpy/
├── .github/
│   └── workflows/
│       └── pipeline_and_deploy.yml   # Automatización CI/CD y despliegue a GitHub Pages
├── data/
│   ├── raw/                          # Archivos JSON/CSV originales descargados de APIs
│   │   ├── world_bank_raw.json
│   │   ├── world_bank_raw.csv
│   │   ├── itu_datahub_raw.json
│   │   ├── unctad_raw.json
│   │   └── wipo_raw.json
│   └── processed/
│       ├── digital_economy_clean.csv # Dataset con 5 países x 8 indicadores (2023)
│       └── digital_readiness_score.csv # Dataset con normalización y ranking DRS
├── notebooks/
│   └── Digital_Economy_Analysis.ipynb# Notebook ejecutable con análisis paso a paso
├── dashboard/
│   ├── index.html                    # Dashboard interactivo single-page
│   ├── styles.css                    # Estilos CSS modernos
│   ├── app.js                        # Lógica y gráficos dinámicos con Chart.js
│   └── data.json                     # Datos en JSON para consumo directo
├── docs/                             # Documentación exhaustiva para el equipo
│   ├── 01_marco_conceptual.md
│   ├── 02_seleccion_e_indicadores.md
│   ├── 03_metodologia_drs_y_analisis.md
│   ├── 04_diagnostico_y_brechas_mexico.md
│   └── 05_guia_de_reproducibilidad_equipo.md
├── scripts/
│   ├── 01_fetch_data.py              # Descarga desde APIs oficiales
│   ├── 02_process_data.py            # Limpieza, normalización y cálculo del DRS
│   └── 04_generate_notebook.py       # Reconstrucción del notebook Jupyter
├── source_log.csv                    # Registro formal de fuentes oficiales y URLs
├── data_dictionary.csv               # Diccionario formal de datos
├── requirements.txt                  # Dependencias de Python
└── README.md                         # Portada e instrucciones generales
```

---

## 3. Instrucciones de Reproducción Paso a Paso

Para ejecutar y validar todo el proyecto desde una terminal local:

### Paso 1: Clonar el repositorio e instalar dependencias
```bash
git clone https://github.com/RusselKu/DigitalEconomyUpy.git
cd DigitalEconomyUpy
pip install -r requirements.txt
```

### Paso 2: Ejecutar el pipeline de datos completo
```bash
# 1. Descargar datos crudos oficiales de APIs (Banco Mundial, ITU, UNCTAD, WIPO)
python scripts/01_fetch_data.py

# 2. Procesar y calcular el Digital Readiness Score (DRS)
python scripts/02_process_data.py

# 3. Generar y ejecutar el notebook reproducible
python scripts/04_generate_notebook.py
python -m jupyter nbconvert --to notebook --execute --inplace notebooks/Digital_Economy_Analysis.ipynb
```

### Paso 3: Visualizar el Dashboard Interactivo
* **Opción Local:** Abre directamente el archivo `dashboard/index.html` con cualquier navegador web (Chrome, Edge, Firefox, Safari).
* **Opción GitHub Pages:** Accede al enlace público desplegado automáticamente por GitHub Actions.

---

## 4. Preguntas Típicas de Examen / Defensa y Respuestas Clave

1. **¿Por qué se invirtió la escala de la canasta de precios TIC?**  
   *Respuesta:* Porque un mayor porcentaje del INB per cápita implica que el servicio es más caro y menos asequible. Al invertir la escala, $100$ puntos representa máxima asequibilidad (menor costo relativo), alineándolo con el sentido positivo del DRS.

2. **¿Por qué Argentina tiene un DRS más alto que México a pesar de tener un PIB per cápita similar?**  
   *Respuesta:* Porque el DRS premia fuertemente la sofisticación de la economía del conocimiento. Argentina exporta el 64.2% de sus servicios en formato digital y 15.9% en servicios TIC (software y AgTech), mientras que México exporta principalmente manufactura física de hardware y turismo, con solo 24.5% y 2.9% respectivamente.

3. **¿Cuál es la diferencia entre sector TIC y economía digitalizada en el agro?**  
   *Respuesta:* El sector TIC provee los chips y antenas. La economía digitalizada es la adopción profunda de esos sensores, imágenes satelitales y algoritmos de IA en los tractores y parcelas de cultivo para optimizar la cosecha.
