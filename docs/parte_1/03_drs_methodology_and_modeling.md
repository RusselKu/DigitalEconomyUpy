# 03. Digital Readiness Score (DRS) Methodology & Modeling

**Team 3: Agriculture**
**Assigned Economies:** Mexico 🇲🇽, Netherlands 🇳🇱, Kenya 🇰🇪, Argentina 🇦🇷, New Zealand 🇳🇿

---

## 1. Mathematical Formulation of the Digital Readiness Score (DRS)

The **Digital Readiness Score (DRS)** is a composite synthetic indicator designed to quantify the overall readiness, infrastructure strength, and knowledge-based value capture of the 5 assigned economies.

### General Formula
$$\text{DRS} = \sum_{i=1}^{8} w_i \cdot I_{i,\text{norm}}$$

Subject to:
$$\sum_{i=1}^{8} w_i = 1.0, \quad \text{with equal weighting } w_i = \frac{1}{8} = 0.125 \quad (12.5\% \text{ each})$$

---

## 2. Min-Max Normalization Architecture

Because indicators possess drastically different units (percentages from $0$ to $100$, and server counts exceeding $190,000$), a uniform **Min-Max scaling to $[0, 100]$** is applied:

### A. Direct Impact Indicators (+)
For positive indicators (`IT_NET_BBND`, `IT_NET_SECR`, `IT_NET_USER`, `ICT_SERV_EXP`, `DIGIT_DELIV_EXP`, `RD_EXP_GDP`, `PATENT_RES_PM`):
$$I_{i,\text{norm}} = \frac{x_i - x_{\min}}{x_{\max} - x_{\min}} \times 100$$

* The economy with the minimum observed value receives $0.00$ points.
* The economy with the maximum observed value receives $100.00$ points.

### B. Inverted Impact Indicator (-) (`ITU_PRICE_BASKET`)
For the ICT price basket, where higher cost represents an economic barrier and lower affordability:
$$I_{\text{ITU\_PRICE\_BASKET},\text{norm}} = \frac{x_{\max} - x_i}{x_{\max} - x_{\min}} \times 100$$

* The Netherlands (lowest cost: 0.82% GNI) receives $100.00$ points for maximum affordability.
* Kenya (highest cost: 10.40% GNI) receives $0.00$ points.

---

## 3. Normalized Score Matrix & Final DRS Ranking (2023)

| Economy | Broadband | Servers | Users | Affordability | ICT Exp. | Digital Serv. | R&D | Patents | **Final DRS** | **Rank** |
|---|---|---|---|---|---|---|---|---|---|---|
| 🇳🇱 **Netherlands** | 100.00 | 100.00 | 100.00 | 100.00 | 51.74 | 85.39 | 100.00 | 100.00 | **92.14** | **#1** |
| 🇳🇿 **New Zealand** | 86.77 | 9.60 | 94.33 | 98.33 | 31.12 | 51.13 | 64.00 | 10.86 | **55.77** | **#2** |
| 🇦🇷 **Argentina** | 56.20 | 2.65 | 88.02 | 78.29 | 100.00 | 100.00 | 16.50 | 0.41 | **55.26** | **#3** |
| 🇲🇽 **Mexico** | 44.92 | 0.06 | 75.62 | 88.20 | 0.00 | 0.00 | 0.00 | 0.20 | **26.13** | **#4** |
| 🇰🇪 **Kenya** | 0.00 | 0.00 | 0.00 | 0.00 | 59.85 | 37.03 | 26.50 | 0.00 | **15.42** | **#5** |

---

## 4. Complementary Analysis: Pearson Correlations & K-Means Clustering

### A. Key Pearson Correlations
* **Secure Servers & Resident Patents ($r = 0.9996$):** The five-economy sample shows an extremely high positive descriptive correlation. Because $n=5$, this result is exploratory and should not be interpreted as evidence of causality or as a stable population estimate.
* **Internet Users & ICT Affordability ($r = 0.96$):** Low relative broadband basket cost is the primary empirical determinant of widespread societal internet adoption.

### B. Cluster Profiles (K-Means on 8 Normalized Features)
1. **Cluster 1: Frontier Innovation Ecosystem (Netherlands - DRS: 92.14)**
   Netherlands forms its own cluster because of its exceptional server density, R&D intensity, and patent indicator.
2. **Cluster 0: Mixed Intermediate Profiles (New Zealand - DRS: 55.77 | Argentina - DRS: 55.26 | Mexico - DRS: 26.13)**
   These economies share intermediate multidimensional profiles despite substantial differences in their individual strengths: New Zealand in R&D and adoption, Argentina in digital-service exports, and Mexico in access and affordability.
3. **Cluster 2: Connectivity-Constrained Profile (Kenya - DRS: 15.42)**
   Kenya forms a separate profile because of its comparatively low fixed-broadband, server, internet-use, and affordability scores.

**Interpretation caution:** With only five economies and $k=3$, K-Means is exploratory; the clusters should be treated as descriptive groupings rather than robust population segments.
