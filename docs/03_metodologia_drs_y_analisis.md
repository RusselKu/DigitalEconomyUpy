# 03. Metodología de Cálculo del Digital Readiness Score (DRS) y Modelado

**Equipo 3: Agricultura**  
**Economías:** México 🇲🇽, Países Bajos 🇳🇱, Kenia 🇰🇪, Argentina 🇦🇷, Nueva Zelanda 🇳🇿

---

## 1. Justificación Metodológica del Digital Readiness Score (DRS)

El **Digital Readiness Score (DRS)** es un índice sintético compuesto diseñado para resumir la preparación, adopción y capacidad de captura de valor digital de las economías asignadas.

### A. Ecuación General
$$\text{DRS} = \sum_{i=1}^{8} w_i \cdot I_{i,\text{norm}}$$

Donde:
* $I_{i,\text{norm}}$ es el valor normalizado del indicador $i$ en la escala uniforme $[0, 100]$.
* $w_i$ es el peso ponderador asignado a cada indicador, sujeto a la restricción obligatoria $\sum_{i=1}^{8} w_i = 1.0$.
* Con 8 indicadores seleccionados en proporciones balanceadas, se aplica un esquema de ponderación equitativa: $w_i = \frac{1}{8} = 0.125$ (12.5% cada uno).

---

## 2. Esquema de Normalización Min-Max

Dado que las variables presentan unidades y magnitudes radicalmente distintas (desde porcentajes de $0$ a $100$, hasta servidores por millón de más de $190,000$), se utiliza el método de **Escalamiento Min-Max**:

### 1. Variables de Impacto Positivo / Directo (+)
Para indicadores donde un mayor valor representa mayor desarrollo digital (`IT_NET_BBND`, `IT_NET_SECR`, `IT_NET_USER`, `ICT_SERV_EXP`, `DIGIT_DELIV_EXP`, `RD_EXP_GDP`, `PATENT_RES_PM`):
$$I_{i,\text{norm}} = \frac{x_i - x_{\min}}{x_{\max} - x_{\min}} \times 100$$

* El país con el valor mínimo del grupo obtiene $0.00$ puntos.
* El país con el valor máximo del grupo obtiene $100.00$ puntos.

### 2. Variables de Impacto Negativo / Inverso (-)
Para la variable de costo/canasta de precios TIC (`ITU_PRICE_BASKET`), donde un valor más alto representa mayor barrera de entrada y menor asequibilidad económica:
$$I_{\text{ITU\_PRICE\_BASKET},\text{norm}} = \frac{x_{\max} - x_i}{x_{\max} - x_{\min}} \times 100$$

* El país con la canasta más barata (Países Bajos con 0.82% INB) obtiene $100.00$ puntos en asequibilidad.
* El país con la canasta más costosa (Kenia con 10.40% INB) obtiene $0.00$ puntos en asequibilidad.

---

## 3. Matriz de Resultados Normalizados y Ranking DRS

| País | Banda Ancha | Servidores | Usuarios | Asequibilidad | Exp. Serv. TIC | Serv. Digitales | Gasto I+D | Patentes | **DRS Final** | **Posición** |
|---|---|---|---|---|---|---|---|---|---|---|
| 🇳🇱 **Países Bajos** | 100.00 | 100.00 | 100.00 | 100.00 | 51.74 | 85.39 | 100.00 | 100.00 | **92.14** | **1º** |
| 🇳🇿 **Nueva Zelanda** | 86.77 | 9.60 | 94.33 | 98.33 | 31.12 | 51.13 | 64.00 | 52.02 | **60.91** | **2º** |
| 🇦🇷 **Argentina** | 56.20 | 2.65 | 88.02 | 78.29 | 100.00 | 100.00 | 16.50 | 4.12 | **55.72** | **3º** |
| 🇲🇽 **México** | 44.92 | 0.06 | 75.62 | 88.20 | 0.00 | 0.00 | 0.00 | 3.77 | **26.57** | **4º** |
| 🇰🇪 **Kenia** | 0.00 | 0.00 | 0.00 | 0.00 | 59.85 | 37.03 | 26.50 | 0.00 | **15.42** | **5º** |

---

## 4. Análisis Complementario: Correlaciones y Clustering (K-Means)

### A. Correlaciones Clave
* **Infraestructura de Servidores y Patentes ($r = 0.94$):** Correlación casi perfecta. Los países con infraestructura de centros de datos de clase mundial concentran la mayor densidad de propiedad intelectual y desarrollo tecnológico.
* **Usuarios de Internet y Asequibilidad ($r = 0.96$):** La reducción en el costo relativo de la canasta TIC es el factor determinante para masificar el acceso de la población a internet.

### B. Segmentación por Clusters (Perfiles Digitales)
1. **Cluster 0: Ecosistema Maduro de Frontera (Países Bajos - DRS: 92.14)**  
   Infraestructura crítica insuperable, alta inversión en I+D y liderazgo en AgTech institucional.
2. **Cluster 1: Potencias de Adopción y Especialización de Nicho (Nueva Zelanda - DRS: 60.91 | Argentina - DRS: 55.72)**  
   Nueva Zelanda lidera en penetración institucional y productividad rural; Argentina lidera en exportación de software y servicios basados en el conocimiento a pesar de restricciones macroeconómicas.
3. **Cluster 2: Economías en Desarrollo con Brechas Estructurales (México - DRS: 26.57 | Kenia - DRS: 15.42)**  
   México cuenta con penetración de usuarios y asequibilidad pero carece de I+D y software exportable; Kenia lidera en innovación móvil pero enfrenta altos costos relativos y déficit de fibra óptica.
