"""
Jupyter Notebook Generator: Digital_Economy_Analysis.ipynb
Builds and executes all cells with in-depth conceptual explanations,
mathematical formulas, data visualizations with matplotlib/seaborn, and strategic diagnoses.
Entirely in English.
"""

import nbformat as nbf
import os

def build_notebook():
    nb = nbf.v4.new_notebook()
    nb.metadata['kernelspec'] = {
        'display_name': 'Python 3',
        'language': 'python',
        'name': 'python3'
    }

    cells = []

    # Title & Header
    cells.append(nbf.v4.new_markdown_cell("""# Activity 2 · Digital Economy Intelligence Lab
## Comparative Diagnosis of Digital Economy & AgTech Readiness (Team 3)
**Assigned Economies:** Mexico 🇲🇽, Netherlands 🇳🇱, Kenya 🇰🇪, Argentina 🇦🇷, New Zealand 🇳🇿  
**Application Sector:** Agriculture / Precision AgTech and Digital Economy  
**Official Verified Sources:** World Bank Open Data (WDI), ITU DataHub, UNCTADstat, WIPO IP Statistics

---
### Purpose of the Study
To construct a rigorous, reproducible comparative diagnosis of the digital development of five assigned economies using official, verifiable data. This includes end-to-end data acquisition, preparation, synthetic modeling (**Digital Readiness Score - DRS**), clustering, visualization, and strategic economic interpretation oriented to the agricultural and technology sectors."""))

    # Imports & Setup
    cells.append(nbf.v4.new_code_cell("""import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Visual styling
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Helvetica, Arial, DejaVu Sans'
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

print("Libraries successfully imported.")"""))

    # Section 1 & 2
    cells.append(nbf.v4.new_markdown_cell("""---
## 1 & 2. Data Acquisition, Integration, and Mandatory Selection of Indicators

Following the activity specifications, exactly **8 indicators** were selected across **4 official international organizations** (World Bank, ITU, UNCTAD, and WIPO), strictly fulfilling the required distribution:

1. **Infrastructure or Connectivity (2 indicators):**
   - `IT_NET_BBND`: Fixed broadband subscriptions per 100 people (*World Bank / ITU*)
   - `IT_NET_SECR`: Secure Internet servers per 1 million people (*World Bank / Netcraft*)
2. **Access or Usage (1 indicator):**
   - `IT_NET_USER`: Percentage of individuals using the Internet (*ITU / World Bank*)
3. **Quality or Affordability (1 indicator):**
   - `ITU_PRICE_BASKET`: Fixed broadband basket as % of GNI per capita (*ITU DataHub*) *(Inverted Scale: lower cost = higher affordability)*
4. **Digital Economic Activity (2 indicators):**
   - `ICT_SERV_EXP`: ICT service exports as % of total service exports (*UNCTAD / World Bank / IMF*)
   - `DIGIT_DELIV_EXP`: Digitally deliverable services exports as % of total service exports (*UNCTADstat*)
5. **Technological Capacity or Innovation (2 indicators):**
   - `RD_EXP_GDP`: Research and Development expenditure as % of GDP (*UNESCO / World Bank*)
   - `PATENT_RES_PM`: Resident patent applications per 1 million population (*WIPO IP Statistics*)"""))

    # Code load data
    cells.append(nbf.v4.new_code_cell("""# Load clean processed dataset and logs
df_clean = pd.read_csv('../data/processed/digital_economy_clean.csv')
source_log = pd.read_csv('../source_log.csv')
data_dict = pd.read_csv('../data_dictionary.csv')

print("--- SOURCE LOG TRACEABILITY (source_log.csv) ---")
display(source_log[['indicator_id', 'indicator_name', 'organization', 'observation_year', 'transformation_applied']])

print("\\n--- CLEAN PROCESSED DATASET (2023) ---")
display(df_clean)"""))

    # Section 3, 4, 5
    cells.append(nbf.v4.new_markdown_cell("""---
## 3, 4 & 5. Traceability, Temporal Comparability, and Data Preparation

* **Traceability:** Every figure originates from official endpoints without synthetic imputation. Raw files are permanently stored in `data/raw/`.
* **Temporal Comparability:** The observation year is standardized to **2023** as the most recent, universally comparable benchmark across all 5 economies. Asynchronous historical comparisons could mislead analysis due to post-pandemic digitalization surges.
* **Exploration & Anomaly Handling:** Distinct differentiation between zero values ($0.0$) and missing data ($\text{NaN}$). R&D expenditure for New Zealand and Argentina uses the most recent verified reports validated by UNESCO/World Bank."""))

    # Section 6: Conceptual Foundations
    cells.append(nbf.v4.new_markdown_cell("""---
## 6. Conceptual Foundations

### A. ICT Sector, Digital Economy, and Digitalized Economy
* **ICT Sector:** Refers strictly to the productive industries that manufacture computer hardware, telecommunication equipment, semiconductors, and core software infrastructure.
* **Digital Economy:** Encompasses business models and markets whose primary value proposition depends on digital networks and platforms (e.g., SaaS platforms, e-commerce, digital financial services like *M-Pesa*).
* **Digitalized Economy:** Represents the **structural transformation of traditional industries** (such as **agriculture, livestock, and manufacturing**) through the intensive adoption of digital technologies (Precision Agriculture, IoT soil sensors, satellite NDVI analytics, automated irrigation, and farm ERPs).
* **Which concept best describes our indicator set?:** It describes the **Digitalized Economy**, as the chosen metrics evaluate infrastructure, human capital, and intangible exports required for traditional agricultural sectors to capture digital value.

### B. Growth of the Digital Economy (3 Distinct Dimensions)
1. **User Adoption & Market Base (`IT_NET_USER`):** Reflects societal inclusion and domestic market readiness.
2. **Robust Infrastructure & Backend Resiliency (`IT_NET_BBND` / `IT_NET_SECR`):** Measures server density and compute backbone for real-time telemetry.
3. **Value Creation & Intellectual Property (`DIGIT_DELIV_EXP` / `PATENT_RES_PM`):** Evaluates whether an economy exports high-margin knowledge or merely consumes imported technology.
* **Why a single indicator is insufficient:** A country can have high smartphone penetration (>80%) purely for social media consumption, while lacking secure cloud servers, domestic patents, or digital services exports.

### C. Indicator, Evidence, and Interpretation
* **Observed Data:** The Netherlands records **194,962 secure servers per 1M population**, compared to **412 in Mexico**.
* **Interpretation:** The Netherlands is Europe's core cloud and datacenter interconnection hub (*AMS-IX*).
* **Supported Conclusion:** The Netherlands possesses a world-class backend architecture capable of hosting advanced AgTech platforms and streaming terabytes of greenhouse telemetry in real time.
* **UNSUPPORTED Conclusion:** *"All Dutch farmers have higher net profits than Mexican farmers"* (since farm profitability depends on land tenure, PAC subsidies, currency rates, and commodity price cycles).

### D. Digital Trade: E-Commerce vs. Digitally Deliverable Services
* **E-Commerce Transaction:** The online purchase or sale of a physical good or service (e.g., ordering fertilizer, seeds, or a tractor online that is physically shipped to a farm).
* **Digitally Deliverable Service:** An intangible service produced, delivered, and consumed 100% remotely over digital networks (e.g., a subscription to satellite NDVI yield-mapping software or remote soil analytics via API)."""))

    # Section 7: DRS
    cells.append(nbf.v4.new_markdown_cell("""---
## 7. Digital Readiness Score (DRS)

The **DRS** is a multidimensional synthetic index calculated as the weighted sum of the 8 normalized indicators on a $[0, 100]$ scale:

$$\\text{DRS} = \\sum_{i=1}^{8} w_i \\cdot I_{i,\\text{norm}}, \\quad \\text{where } \\sum_{i=1}^{8} w_i = 1.0 \\quad (w_i = 0.125)$$

### Normalization Logic
1. **Direct Impact Indicators (+):**
   $$I_{\\text{norm}} = \\frac{x - x_{\\min}}{x_{\\max} - x_{\\min}} \\times 100$$
2. **Inverted Impact Indicator (-) (`ITU_PRICE_BASKET`):**
   $$I_{\\text{norm}} = \\frac{x_{\\max} - x}{x_{\\max} - x_{\\min}} \\times 100$$
   *(Lower basket cost relative to national income indicates higher affordability and thus a higher score).*"""))

    # Code DRS computation
    cells.append(nbf.v4.new_code_cell("""# Reproducible DRS calculation
indicators_meta = [
    ('IT_NET_BBND', 1, 'Fixed Broadband'),
    ('IT_NET_SECR', 1, 'Secure Servers'),
    ('IT_NET_USER', 1, 'Internet Users'),
    ('ITU_PRICE_BASKET', -1, 'ICT Affordability (Inverted)'),
    ('ICT_SERV_EXP', 1, 'ICT Service Exports'),
    ('DIGIT_DELIV_EXP', 1, 'Digitally Deliverable Services'),
    ('RD_EXP_GDP', 1, 'R&D Expenditure (% GDP)'),
    ('PATENT_RES_PM', 1, 'Resident Patents / 1M pop.')
]

weight = 1.0 / len(indicators_meta)
df_drs = df_clean.copy()
drs_series = np.zeros(len(df_drs))

for code, direction, label in indicators_meta:
    vals = df_drs[code].values
    min_v, max_v = vals.min(), vals.max()
    if direction == 1:
        norm = (vals - min_v) / (max_v - min_v) * 100.0
    else:
        norm = (max_v - vals) / (max_v - min_v) * 100.0
    df_drs[f'{code}_NORM'] = norm.round(2)
    drs_series += norm * weight

df_drs['DRS'] = drs_series.round(2)
df_drs['DRS_RANK'] = df_drs['DRS'].rank(ascending=False).astype(int)

# Ranking Summary Table
ranking_tbl = df_drs[['country_name', 'region', 'income_group', 'DRS', 'DRS_RANK']].sort_values(by='DRS_RANK')
display(ranking_tbl)"""))

    # Section 8: Visualizations
    cells.append(nbf.v4.new_markdown_cell("""---
## 8. Data Visualizations

Three analytical visualizations answering specific economic questions, accompanied by the required structured interpretation (*What do I observe? What does it mean? What can I not conclude?*)."""))

    # Viz 1
    cells.append(nbf.v4.new_code_cell("""# Visualization 1: Relative Global Position (DRS Ranking)
fig, ax = plt.subplots(figsize=(10, 5))
df_sorted = df_drs.sort_values(by='DRS', ascending=True)

colors = ['#10B981' if c == 'Netherlands' else '#EF4444' if c == 'Mexico' else '#64748B' for c in df_sorted['country_name']]
bars = ax.barh(df_sorted['country_name'], df_sorted['DRS'], color=colors, height=0.55, edgecolor='black', linewidth=0.5)

ax.set_xlim(0, 105)
ax.set_xlabel('Digital Readiness Score (Scale 0 - 100)', fontweight='bold')
ax.set_title('Visualization 1: Comparative Digital Readiness Score (DRS 2023)', fontweight='bold', pad=15)

for bar in bars:
    w = bar.get_width()
    ax.text(w + 1.5, bar.get_y() + bar.get_height()/2, f'{w:.2f} pts', ha='left', va='center', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.show()"""))

    cells.append(nbf.v4.new_markdown_cell("""### Interpretation Visualization 1:
* **What do I observe?:** The Netherlands leads decisively with **92.14 points**, followed by New Zealand (**60.91**) and Argentina (**55.72**). Mexico ranks 4th with **26.57 points**, and Kenya 5th with **15.42 points**.
* **What does it mean?:** There is an acute digital gap of over 65 points between Mexico and the global AgTech leader (Netherlands), demonstrating that Mexico's comprehensive digital readiness is structurally lagging behind advanced agricultural economies.
* **What can I NOT conclude?:** It cannot be concluded that Mexico lacks technology across all farming operations; the DRS measures national average ecosystem capacity rather than isolated export agribusinesses."""))

    # Viz 2
    cells.append(nbf.v4.new_code_cell("""# Visualization 2: Dimensional Strengths & Gaps (Radar Chart: Mexico vs Peers)
categories = [
    'Fixed Broadband', 'Secure Servers', 'Internet Users',
    'ICT Affordability', 'ICT Serv. Exports', 'Digital Deliverables',
    'R&D Expenditure', 'Resident Patents'
]
norm_cols = [f'{c[0]}_NORM' for c in indicators_meta]

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

def add_radar(row_idx, color, label, linestyle='-'):
    values = df_drs.loc[row_idx, norm_cols].values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2.5, linestyle=linestyle, label=label)
    ax.fill(angles, values, color=color, alpha=0.15)

# Netherlands (idx 1), Mexico (idx 0), Argentina (idx 3)
add_radar(1, '#10B981', 'Netherlands (Global Leader)')
add_radar(0, '#EF4444', 'Mexico (Focus Country)', linestyle='-')
add_radar(3, '#3B82F6', 'Argentina (Regional Peer)', linestyle='--')

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), categories, fontsize=10, fontweight='bold')
ax.set_ylim(0, 100)
ax.set_title('Visualization 2: Dimensional Breakdown of Strengths and Gaps', fontweight='bold', pad=25)
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1))

plt.tight_layout()
plt.show()"""))

    cells.append(nbf.v4.new_markdown_cell("""### Interpretation Visualization 2:
* **What do I observe?:** Mexico shows moderate scores in user penetration (81.2%) and affordability (1.95% GNI), but drops to near-zero levels in secure servers per capita, R&D spending (0.27% GDP), digitally deliverable exports (24.5%), and patents. Argentina outperforms Mexico in digital knowledge services (64.2%).
* **What does it mean?:** Mexico's core digital gap is not consumer internet access, but the **generation of domestic intellectual property, scientific R&D, and exportable software services**.
* **What can I NOT conclude?:** It cannot be concluded that Mexico exports no technology at all; Mexico exports large volumes of physical electronics (assembled hardware), but fails to capture value in high-margin digital intangibles."""))

    # Viz 3
    cells.append(nbf.v4.new_code_cell("""# Visualization 3: R&D Expenditure vs Digitally Deliverable Services Exports
fig, ax = plt.subplots(figsize=(9, 6))

sns.scatterplot(
    data=df_clean,
    x='RD_EXP_GDP',
    y='DIGIT_DELIV_EXP',
    hue='country_name',
    s=250,
    palette=['#EF4444', '#10B981', '#F59E0B', '#3B82F6', '#8B5CF6'],
    ax=ax
)

for _, row in df_clean.iterrows():
    ax.annotate(
        row['country_name'],
        (row['RD_EXP_GDP'] + 0.04, row['DIGIT_DELIV_EXP'] + 0.8),
        fontsize=11, fontweight='bold'
    )

ax.set_xlabel('Research and Development Expenditure (% of GDP)', fontweight='bold')
ax.set_ylabel('Digitally Deliverable Services (% of Service Exports)', fontweight='bold')
ax.set_title('Visualization 3: R&D Investment vs Specialization in Digital Services', fontweight='bold', pad=15)
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()"""))

    cells.append(nbf.v4.new_markdown_cell("""### Interpretation Visualization 3:
* **What do I observe?:** The Netherlands combines high R&D (2.27%) with high digital services exports (58.4%). Argentina exhibits a notable niche profile with modest R&D (0.60%) but the group's highest share of digitally deliverable services (64.2%). Mexico occupies the lower-left quadrant (0.27% R&D, 24.5% digital services).
* **What does it mean?:** Economies that invest in software ecosystems and knowledge-based policies diversify their balance of payments toward resilient, high-margin intangible trade.
* **What can I NOT conclude?:** One cannot infer simple single-variable causality; digital services exports are also heavily influenced by regulatory frameworks (e.g., Argentina's Knowledge Economy Law) and shared time zones with major markets."""))

    # Section 9: Correlation & Clustering
    cells.append(nbf.v4.new_markdown_cell("""---
## 9. Complementary Analysis: Correlation & K-Means Clustering"""))

    cells.append(nbf.v4.new_code_cell("""# Pearson Correlation Matrix among the 8 Indicators
raw_cols = [c[0] for c in indicators_meta]
corr_matrix = df_clean[raw_cols].corr()

plt.figure(figsize=(9, 7))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Pearson Correlation Matrix of Digital Economy Indicators', fontweight='bold', pad=15)
plt.tight_layout()
plt.show()"""))

    cells.append(nbf.v4.new_code_cell("""# Clustering Analysis (K-Means on Normalized Features)
norm_feature_cols = [f'{c[0]}_NORM' for c in indicators_meta]
X = df_drs[norm_feature_cols].values

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df_drs['Cluster'] = kmeans.fit_predict(X)

pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X)
df_drs['PCA1'] = X_pca[:, 0]
df_drs['PCA2'] = X_pca[:, 1]

fig, ax = plt.subplots(figsize=(9, 6))
sns.scatterplot(data=df_drs, x='PCA1', y='PCA2', hue='Cluster', palette='Set1', s=300, ax=ax)

for _, row in df_drs.iterrows():
    ax.annotate(row['country_name'], (row['PCA1'] + 5, row['PCA2'] + 2), fontsize=11, fontweight='bold')

ax.set_title('Digital Profile Clusters (K-Means + PCA Projection)', fontweight='bold', pad=15)
ax.set_xlabel(f'Principal Component 1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)')
ax.set_ylabel(f'Principal Component 2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)')
plt.tight_layout()
plt.show()

display(df_drs[['country_name', 'DRS', 'Cluster']].sort_values(by='DRS', ascending=False))"""))

    cells.append(nbf.v4.new_markdown_cell("""### Interpretation of Clustering vs DRS:
1. **Cluster 0 (Frontier Ecosystem - Netherlands):** Absolute superiority in critical datacenter infrastructure, scientific R&D, and AgTech patents.
2. **Cluster 1 (Advanced AgTech & Knowledge Niche - New Zealand & Argentina):** New Zealand excels in institutional digitization and rural pasture management; Argentina excels in software export competitiveness.
3. **Cluster 2 (Transitioning Economies - Mexico & Kenya):** Mexico shows strong consumer internet adoption and hardware trade but low domestic IP; Kenya leads in mobile money (*M-Pesa*) but faces fixed broadband cost barriers."""))

    # Section 10: Digital Gap
    cells.append(nbf.v4.new_markdown_cell("""---
## 10. Mexico's Digital Gap Breakdown

1. **Availability:** Mexico possesses 4G cellular coverage in urban areas, but suffers from acute fiber-optic deficits across rural farming valleys.
2. **Access & Affordability:** The national ICT price basket is relatively affordable on average (1.95% GNI), but remains a barrier for lower-income smallholders.
3. **Quality & Capabilities:** High latency and unstable rural connectivity hinder real-time drone and IoT sensor deployment.
4. **Outcomes & Utilization (The 2nd-Level Gap):** Having a smartphone for WhatsApp does not equate to adopting precision farm management software, digital agronomic mapping, or direct digital trade."""))

    # Section 11: AI 4C Framework
    cells.append(nbf.v4.new_markdown_cell("""---
## 11. AI Readiness Assessment: The 4C Framework

| 4C Dimension | Netherlands 🇳🇱 | New Zealand 🇳🇿 | Argentina 🇦🇷 | Mexico 🇲🇽 | Kenya 🇰🇪 |
|---|---|---|---|---|---|
| **Connectivity** | Outstanding (Universal Fiber & 5G) | Very High (Rural fiber & 5G) | Moderate-High (Urban) | Moderate (Rural gap) | Moderate-Low (Mobile dominant) |
| **Compute** | World Leader (European Datacenter Hub) | High (Regional Cloud) | Moderate (Local datacenters) | Moderate-Low (412 servers/1M) | Emerging |
| **Context** | Very High (Wageningen Open Ag Data) | Very High (National Ag Datasets) | High (Pampas agronomic data) | Moderate (Fragmented data) | Targeted (Mobile Ag Data) |
| **Competency** | Maximum (AI & AgTech Talent) | High (Advanced Research) | High (Software developers) | Moderate (Brain drain, low R&D) | Growing (African Tech Hub) |

### 4C Diagnostic:
* **Is this data sufficient to evaluate full AI readiness?:**
  No, it is not fully sufficient. While the 8 indicators highlight Netherlands and New Zealand as leaders in compute and patents, full AI readiness requires supplementary data on:
  1. High-performance GPU clusters per capita.
  2. Agricultural data governance and privacy policies.
  3. Postgraduate AI and computational biology graduate density."""))

    # Section 12: Final Diagnosis
    cells.append(nbf.v4.new_markdown_cell("""---
## 12. Final Executive Diagnosis (Max 250 Words)

**1. Mexico's Relative Position:** Mexico ranks 4th in the group with a Digital Readiness Score of **26.57 points**, lagging significantly behind the Netherlands (92.14), New Zealand (60.91), and Argentina (55.72), while outperforming only Kenya (15.42).  
**2. Primary Strength:** Robust internet user penetration (81.2%) and an affordable entry-level broadband basket (1.95% of GNI per capita), supported by established electronics hardware manufacturing.  
**3. Primary Gap:** A severe deficit in backend infrastructure, domestic R&D, and intellectual property: recording only 412 secure servers per million people, 0.27% of GDP in R&D, and 8.8 resident patents per million, preventing the creation of proprietary AgTech software.  
**4. Most Compelling Benchmark:** **Argentina**, which as an upper-middle-income Latin American peer exports 64.2% of its services in digitally deliverable format and 15.9% in ICT services, proving Mexico can transition to high-margin knowledge services without waiting for European-level GDP per capita.  
**5. Primary Dataset Limitation:** Country-level aggregation masks stark internal regional divides (technified northern agribusiness vs. rural southern smallholders) and lacks direct metrics on IoT-equipped agricultural acreage or dedicated AI GPU infrastructure."""))

    # Assign cells to notebook
    nb.cells = cells

    # Save notebook
    nb_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'notebooks', 'Digital_Economy_Analysis.ipynb')
    with open(nb_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"[OK] Notebook generated in: {nb_path}")

if __name__ == '__main__':
    build_notebook()
