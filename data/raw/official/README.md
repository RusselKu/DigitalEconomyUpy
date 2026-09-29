# Guía Oficial de Trazabilidad y Descarga de Fuentes Originales
**Equipo 3: Agricultura** | **Digital Economy Intelligence Lab**
**Responsable de Datos:** Russel Ku

Esta guía documenta la ruta paso a paso para descargar los archivos originales e inalterados directamente de los portales oficiales de la ITU, UNCTAD y WIPO, cumpliendo con la regla estricta de trazabilidad y reproducibilidad.

---

## 📥 Directorio de Destino de Archivos Originales
Todos los archivos descargados directamente de los portales web oficiales deben depositarse **SIN MODIFICAR, SIN EDITAR Y CON SU NOMBRE ORIGINAL** en:
`data/raw/official/original/`

---

## 1. International Telecommunication Union (ITU) · DataHub
* **Organismo:** International Telecommunication Union (ITU)
* **Indicador:** Canasta de precios de banda ancha fija como % del INB per cápita (`ITU_PRICE_BASKET_FBB`)
* **Portal:** [https://datahub.itu.int/](https://datahub.itu.int/) / [ITU ICT Prices](https://www.itu.int/en/ITU-D/Statistics/Pages/ICTprices/default.aspx)
* **Ruta de Descarga Paso a Paso:**
  1. Ingresar a [https://datahub.itu.int/data/](https://datahub.itu.int/data/)
  2. En el menú de categorías, seleccionar **"Affordability / ICT Prices"**.
  3. Seleccionar el indicador: **"Fixed-broadband basket as % of GNI per capita"**.
  4. En el panel lateral de filtros:
     - **Economies:** Seleccionar "All Economies" (o buscar Argentina, Kenya, Mexico, Netherlands, New Zealand).
     - **Years:** Seleccionar rango `2015-2023` o `2023`.
  5. Clic en **"Export" / "Download"** -> Formato **CSV**.
  6. Guardar el archivo en `data/raw/official/original/` (ej. `ITU_ICTPriceBasket_2023.csv`).

---

## 2. UNCTADstat · Data Centre
* **Organismo:** United Nations Conference on Trade and Development (UNCTAD)
* **Indicador:** Servicios digitalmente entregables como % del total de exportaciones de servicios (`UNCTAD_DIGIT_DELIV_EXP`)
* **Portal:** [https://unctadstat.unctad.org/datacentre/](https://unctadstat.unctad.org/datacentre/)
* **Ruta de Descarga Paso a Paso:**
  1. Ingresar a [https://unctadstat.unctad.org/datacentre/](https://unctadstat.unctad.org/datacentre/)
  2. Navegar a: **"International Trade in Services"** -> **"Trade in digitally deliverable services"** (o código de tabla `US.DDS`).
  3. En la barra de configuración de tabla:
     - **Flow:** Seleccionar `Exports`.
     - **Indicator / Measure:** Seleccionar `Percentage of total services` (o valores en millones de USD).
     - **Period:** Seleccionar `2023` (o `2015-2023`).
     - **Economy:** Seleccionar "All economies" (o los 5 países asignados).
  4. Clic en **"Download"** -> **"CSV format (data only)"** o **"CSV format (with labels)"**.
  5. Guardar el archivo en `data/raw/official/original/` (ej. `UNCTAD_DDS_Exports_2023.csv`).

---

## 3. WIPO IP Statistics Data Center
* **Organismo:** World Intellectual Property Organization (WIPO)
* **Indicador:** Solicitudes de patentes presentadas por residentes por millón de habitantes (`WIPO_PATENT_RES_PM`)
* **Portal:** [https://www3.wipo.int/ipstats/](https://www3.wipo.int/ipstats/)
* **Ruta de Descarga Paso a Paso:**
  1. Ingresar a [https://www3.wipo.int/ipstats/](https://www3.wipo.int/ipstats/)
  2. En el menú de propiedad intelectual, seleccionar **"Patents"**.
  3. Seleccionar la vista de reporte: **"Total patent applications (direct and PCT national phase entries) by origin"** o **"Patent applications per million population (resident)"**.
  4. En los filtros de búsqueda:
     - **Indicator:** Resident patent applications per million population.
     - **Type of applicant:** Resident.
     - **Year:** `2023` (o histórico `2015-2023`).
     - **Country / Office of Origin:** All / Selected economies.
  5. Clic en el botón **"Download Data"** / **"Export CSV"**.
  6. Guardar el archivo en `data/raw/official/original/` (ej. `WIPO_Resident_Patents_Per_Million_2023.csv`).

---

## 4. Trazabilidad y Scripts de Validación
* **Ingesta:** `scripts/01_fetch_data.py` detecta automáticamente los archivos colocados en `data/raw/official/original/` o `data/raw/official/`.
* **Auditoría de Procedencia:** `scripts/03_validate_provenance.py` verifica fila por fila que los valores en `data/processed/digital_economy_clean.csv` coincidan con exactitud matemática contra las fuentes originales.
