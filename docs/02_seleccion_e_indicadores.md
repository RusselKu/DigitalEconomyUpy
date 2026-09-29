# 02. Selección, Comprensión y Trazabilidad de los 8 Indicadores

**Equipo 3: Agricultura**  
**Economías:** México 🇲🇽, Países Bajos 🇳🇱, Kenia 🇰🇪, Argentina 🇦🇷, Nueva Zelanda 🇳🇿

---

## 1. Justificación y Distribución por Categoría

Para evaluar la economía digitalizada y su aplicación en la agricultura y tecnología, se seleccionaron exactamente **8 indicadores** provenientes de **4 organismos internacionales reconocidos**, respetando la distribución exigida:

```
Distribución Exigida:
├── 2 Indicadores de Infraestructura / Conectividad (IT_NET_BBND, IT_NET_SECR)
├── 1 Indicador de Acceso o Uso (IT_NET_USER)
├── 1 Indicador de Calidad o Asequibilidad (ITU_PRICE_BASKET) [Inverso]
├── 2 Indicadores de Actividad Económica Digital (ICT_SERV_EXP, DIGIT_DELIV_EXP)
└── 2 Indicadores de Capacidad Tecnológica o Innovación (RD_EXP_GDP, PATENT_RES_PM)
```

---

## 2. Ficha Técnica Detallada de los Indicadores

### 1. Suscripciones a Banda Ancha Fija (`IT_NET_BBND`)
* **Categoría:** Infraestructura o Conectividad (1/2)
* **Definición:** Número de suscripciones residenciales y comerciales a redes fijas de alta velocidad (ADSL, cable coaxial, fibra óptica FTTH) por cada 100 habitantes.
* **Organismo:** International Telecommunication Union (ITU) / Banco Mundial
* **Relevancia para la Agricultura:** Las granjas inteligentes y las cooperativas agrícolas requieren fibra óptica y banda ancha fija en sus instalaciones para descargar imágenes satelitales multiespectrales de alta resolución y sincronizar servidores de gestión agronómica sin depender de cuotas móviles limitadas.
* **Valores 2023:** Países Bajos (43.26), Nueva Zelanda (37.85), Argentina (25.36), México (20.75), Kenia (2.39).

### 2. Servidores Seguros de Internet (`IT_NET_SECR`)
* **Categoría:** Infraestructura o Conectividad (2/2)
* **Definición:** Número de servidores de internet con certificados criptográficos SSL/TLS válidos por cada millón de personas.
* **Organismo:** Netcraft / Banco Mundial
* **Relevancia para la Agricultura:** Representa la infraestructura de cómputo seguro, servidores cloud y datacenters necesarios para almacenar telemetría de sensores, bases de datos de suelos y ejecutar modelos de predicción de cosechas con altos estándares de ciberseguridad.
* **Valores 2023:** Países Bajos (194,962.9), Nueva Zelanda (18,993.7), Argentina (5,451.2), México (412.1), Kenia (297.1).

### 3. Población que utiliza Internet (`IT_NET_USER`)
* **Categoría:** Acceso o Uso (1/1)
* **Definición:** Porcentaje de individuos que han utilizado internet en los últimos 3 meses desde cualquier ubicación o dispositivo.
* **Organismo:** ITU / Banco Mundial
* **Relevancia para la Agricultura:** Mide la masa crítica de agricultores, agrónomos y consumidores rurales capaces de adoptar aplicaciones móviles de asesoría técnica, alertas climáticas y bancarización digital.
* **Valores 2023:** Países Bajos (97.01%), Nueva Zelanda (93.33%), Argentina (89.23%), México (81.18%), Kenia (32.07%).

### 4. Canasta de Precios de Banda Ancha Fija (`ITU_PRICE_BASKET`)
* **Categoría:** Calidad o Asequibilidad (1/1)
* **Definición:** Costo mensual de la canasta básica de internet fijo expresado como porcentaje del Ingreso Nacional Bruto (INB) per cápita mensual.
* **Organismo:** ITU DataHub (ICT Price Trends)
* **Tratamiento en DRS:** **Sentido Inverso (-)**. A menor porcentaje, más asequible es el servicio. La meta de la Comisión de Banda Ancha de la ONU es que este costo sea menor al 2.0% del INB per cápita.
* **Valores 2023:** Países Bajos (0.82%), Nueva Zelanda (0.98%), México (1.95%), Argentina (2.90%), Kenia (10.40%).

### 5. Exportaciones de Servicios TIC (`ICT_SERV_EXP`)
* **Categoría:** Actividad Económica Digital (1/2)
* **Definición:** Porcentaje de exportaciones de telecomunicaciones, informática e información sobre las exportaciones totales de servicios comerciales.
* **Organismo:** FMI / UNCTAD / Banco Mundial
* **Relevancia para la Agricultura:** Refleja la capacidad del país de exportar servicios de desarrollo de software AgTech, soporte de bases de datos y arquitectura de telecomunicaciones a otros países.
* **Valores 2023:** Argentina (15.87%), Kenia (10.67%), Países Bajos (9.62%), Nueva Zelanda (6.95%), México (2.92%).

### 6. Exportaciones de Servicios Digitalmente Entregables (`DIGIT_DELIV_EXP`)
* **Categoría:** Actividad Económica Digital (2/2)
* **Definición:** Porcentaje de exportaciones de servicios que se suministran de forma remota a través de internet (software, consultoría agronómica, finanzas, ingeniería).
* **Organismo:** UNCTADstat Data Centre
* **Relevancia para la Agricultura:** Permite monetizar el conocimiento agrícola intangible (análisis de datos agronómicos por suscripción transfronteriza).
* **Valores 2023:** Argentina (64.2%), Países Bajos (58.4%), Nueva Zelanda (44.8%), Kenia (39.2%), México (24.5%).

### 7. Gasto en Investigación y Desarrollo (`RD_EXP_GDP`)
* **Categoría:** Capacidad Tecnológica o Innovación (1/2)
* **Definición:** Gasto doméstico total en investigación y desarrollo experimental expresado como porcentaje del Producto Interno Bruto (PIB).
* **Organismo:** UNESCO Institute for Statistics / Banco Mundial
* **Relevancia para la Agricultura:** Es el motor del desarrollo de nuevas biotecnologías, semillas mejoradas tolerantes al cambio climático, robots agrícolas e inteligencia artificial aplicada al campo.
* **Valores 2023:** Países Bajos (2.27%), Nueva Zelanda (1.55%), Kenia (0.80%), Argentina (0.60%), México (0.27%).

### 8. Patentes de Residentes por Millón de Habitantes (`PATENT_RES_PM`)
* **Categoría:** Capacidad Tecnológica o Innovación (2/2)
* **Definición:** Solicitudes de patentes presentadas por inventores nacionales residentes ante la oficina de patentes por cada millón de habitantes.
* **Organismo:** WIPO IP Statistics Data Center
* **Relevancia para la Agricultura:** Mide la creación y protección legal de invenciones y patentes AgTech locales (sistemas de riego automatizado, maquinaria patentada, biotecnología).
* **Valores 2023:** Países Bajos (118.50), Nueva Zelanda (63.80), Argentina (9.20), México (8.80), Kenia (4.50).

---

## 3. Matriz de Datos Oficiales Estandarizada (Año 2023)

| País | ISO3 | IT_NET_BBND | IT_NET_SECR | IT_NET_USER | ITU_PRICE_BASKET | ICT_SERV_EXP | DIGIT_DELIV_EXP | RD_EXP_GDP | PATENT_RES_PM |
|---|---|---|---|---|---|---|---|---|---|
| **México** | `MEX` | 20.75 | 412.12 | 81.18 | 1.95% | 2.92% | 24.50% | 0.27% | 8.80 |
| **Países Bajos** | `NLD` | 43.26 | 194962.90 | 97.01 | 0.82% | 9.62% | 58.40% | 2.27% | 118.50 |
| **Kenia** | `KEN` | 2.39 | 297.13 | 32.07 | 10.40% | 10.67% | 39.20% | 0.80% | 4.50 |
| **Argentina** | `ARG` | 25.36 | 5451.20 | 89.23 | 2.90% | 15.87% | 64.20% | 0.60% | 9.20 |
| **Nueva Zelanda**| `NZL` | 37.85 | 18993.65 | 93.33 | 0.98% | 6.95% | 44.80% | 1.55% | 63.80 |
