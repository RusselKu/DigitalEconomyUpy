# Digital Economy Intelligence Lab (Equipo 3: Agricultura)
> **Actividad 2 · Parte I | Diagnóstico Comparativo de Economía Digital**  
> **Economías Asignadas:** México 🇲🇽, Países Bajos 🇳🇱, Kenia 🇰🇪, Argentina 🇦🇷, Nueva Zelanda 🇳🇿  
> **Fuentes Oficiales:** World Bank (WDI API), ITU DataHub, UNCTADstat, WIPO IP Statistics

---

## 📌 Resumen del Proyecto

Este repositorio contiene la solución completa, reproducible y automatizada de la **Actividad 2: Digital Economy Intelligence Lab**. Se realiza un diagnóstico multidimensional de preparación digital (*Digital Readiness*) de 5 economías con énfasis en el sector agroalimentario y tecnológico (*AgTech*), cumpliendo estrictamente todos los lineamientos y rúbricas del curso.

---

## 📂 Estructura del Repositorio

```text
DigitalEconomyUpy/
├── .github/
│   └── workflows/
│       └── pipeline_and_deploy.yml   # CI/CD: Validación y Despliegue en GitHub Pages
├── data/
│   ├── raw/                          # Datos originales intactos de fuentes oficiales
│   │   ├── world_bank_raw.json / csv
│   │   ├── itu_datahub_raw.json / csv
│   │   ├── unctad_raw.json / csv
│   │   └── wipo_raw.json / csv
│   └── processed/
│       ├── digital_economy_clean.csv # Dataset consolidado (5 países x 8 indicadores)
│       └── digital_readiness_score.csv # Dataset con métricas normalizadas y DRS
├── notebooks/
│   └── Digital_Economy_Analysis.ipynb# Jupyter Notebook reproducible con los 12 puntos
├── dashboard/                        # Dashboard Web Interactivo Single-Page
│   ├── index.html                    # Interfaz moderna con métricas y radar dinámico
│   ├── styles.css                    # Estilos CSS modernos (Glassmorphism)
│   ├── app.js                        # Lógica y visualizaciones interactivas (Chart.js)
│   └── data.json                     # JSON para alimentación del frontend
├── docs/                             # Guías completas para estudio y defensa del equipo
│   ├── 01_marco_conceptual.md        # Definiciones y fundamentación conceptual
│   ├── 02_seleccion_e_indicadores.md # Justificación de los 8 indicadores y datos
│   ├── 03_metodologia_drs_y_analisis.md # Fórmulas del DRS, normalización y clustering
│   ├── 04_diagnostico_y_brechas_mexico.md # Brechas de México y marco 4C de IA
│   └── 05_guia_de_reproducibilidad_equipo.md # Manual paso a paso para el equipo
├── scripts/
│   ├── 01_fetch_data.py              # Adquisición vía APIs oficiales
│   ├── 02_process_data.py            # Limpieza, normalización y cálculo del DRS
│   └── 04_generate_notebook.py       # Generador del notebook reproducible
├── source_log.csv                    # Registro oficial de procedencia y URLs
├── data_dictionary.csv               # Diccionario formal de datos
├── requirements.txt                  # Dependencias de Python
└── README.md                         # Portada principal
```

---

## 📊 Indicadores Seleccionados (Exactamente 8)

| # | Dimensión | Código | Nombre del Indicador | Fuente | Sentido en DRS |
|---|---|---|---|---|---|
| 1 | **Infraestructura** | `IT_NET_BBND` | Suscripciones a banda ancha fija por 100 hab. | World Bank / ITU | Directo (+) |
| 2 | **Infraestructura** | `IT_NET_SECR` | Servidores seguros por millón de hab. | World Bank / Netcraft | Directo (+) |
| 3 | **Acceso / Uso** | `IT_NET_USER` | Población que utiliza Internet (%) | ITU / World Bank | Directo (+) |
| 4 | **Asequibilidad** | `ITU_PRICE_BASKET` | Canasta banda ancha fija (% INB per cápita) | ITU DataHub | Inverso (-) |
| 5 | **Actividad Económica** | `ICT_SERV_EXP` | Exportaciones de servicios TIC (% serv.) | UNCTAD / World Bank | Directo (+) |
| 6 | **Actividad Económica** | `DIGIT_DELIV_EXP` | Servicios digitalmente entregables (% serv.) | UNCTADstat | Directo (+) |
| 7 | **Capacidad / Innovación** | `RD_EXP_GDP` | Gasto en I+D (% del PIB) | UNESCO / World Bank | Directo (+) |
| 8 | **Capacidad / Innovación** | `PATENT_RES_PM` | Patentes de residentes por millón de hab. | WIPO Statistics | Directo (+) |

---

## 🏆 Resultados del Digital Readiness Score (DRS 2023)

$$\text{DRS} = \sum_{i=1}^{8} w_i \cdot I_{i,\text{norm}} \quad (w_i = 0.125)$$

| Ranking | País | Bandera | DRS Score | Perfil Digital |
|:---:|---|:---:|:---:|---|
| **1º** | **Países Bajos** | 🇳🇱 | **92.14** | Líder Global en Infraestructura y AgTech |
| **2º** | **Nueva Zelanda** | 🇳🇿 | **60.91** | Potencia Agroexportadora Tecnificada |
| **3º** | **Argentina** | 🇦🇷 | **55.72** | Exportador Líder de Servicios Digitales |
| **4º** | **México** | 🇲🇽 | **26.57** | Alto Consumo de Usuario, Bajo I+D y Backend |
| **5º** | **Kenia** | 🇰🇪 | **15.42** | Líder en Dinero Móvil, Retos en Red Fija |

---

## 🚀 Instrucciones para Ejecución Local

```bash
# 1. Clonar el repositorio
git clone https://github.com/RusselKu/DigitalEconomyUpy.git
cd DigitalEconomyUpy

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar el pipeline de adquisición y procesamiento
python scripts/01_fetch_data.py
python scripts/02_process_data.py

# 4. Abrir el dashboard interactivo
# Simplemente haz doble clic en dashboard/index.html o usa un servidor local
```

---

## 📝 Diagnóstico Final (Síntesis Ejecutiva de 220 Palabras)

1. **Posición de México:** México se posiciona en el 4º lugar del grupo con un DRS de **26.57 puntos**, por detrás de Países Bajos (92.14), Nueva Zelanda (60.91) y Argentina (55.72), superando solo a Kenia (15.42).
2. **Principal Fortaleza:** Alta penetración de usuarios de internet (81.2%) y una canasta de acceso fija asequible (1.95% del INB per cápita), junto a su capacidad de manufactura electrónica.
3. **Principal Brecha:** Rezago crítico en infraestructura de backend, I+D y propiedad intelectual: 412 servidores seguros por millón de habitantes, 0.27% del PIB en I+D y 8.8 patentes por millón, lo que limita su capacidad para desarrollar software y soluciones AgTech propias.
4. **Punto de Comparación más Interesante:** **Argentina**, que siendo un par latinoamericano de ingreso medio, exporta 64.2% de sus servicios en modalidad digitalmente entregable y 15.9% en servicios TIC, demostrando que México puede transitar hacia servicios basados en conocimiento sin requerir el PIB per cápita europeo.
5. **Principal Limitación de los Datos:** La agregación a nivel nacional oculta la polarización regional interna (norte tecnificado vs. sur rural) y no cuantifica directamente hectáreas con sensores IoT o capacidad de cómputo en GPUs para IA.
