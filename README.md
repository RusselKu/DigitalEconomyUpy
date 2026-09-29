# Digital Economy Intelligence Lab (Team 3: Agriculture)
> **Activity 2 · Part I | Comparative Diagnosis of Digital Economy Readiness**  
> **Assigned Economies:** Mexico 🇲🇽, Netherlands 🇳🇱, Kenya 🇰🇪, Argentina 🇦🇷, New Zealand 🇳🇿  
> **Official Sources:** World Bank (WDI API), ITU DataHub, UNCTADstat, WIPO IP Statistics
# When haces tus momos en github

---

## 📌 Project Overview

This repository provides a complete, reproducible, and automated solution for **Activity 2: Digital Economy Intelligence Lab**. It conducts an in-depth multidimensional diagnosis of the digital readiness (**Digital Readiness Score - DRS**) of 5 assigned economies with a specific focus on **Agriculture & Precision AgTech**, strictly fulfilling all assignment rubrics and academic standards.

---

## 📂 Repository Structure

```text
DigitalEconomyUpy/
├── .github/
│   └── workflows/
│       └── pipeline_and_deploy.yml   # CI/CD: Automated Validation & GitHub Pages Deployment
├── data/
│   ├── raw/                          # Untouched official raw files (JSON/CSV)
│   │   ├── world_bank_raw.json / csv
│   │   ├── itu_datahub_raw.json / csv
│   │   ├── unctad_raw.json / csv
│   │   └── wipo_raw.json / csv
│   └── processed/
│       ├── digital_economy_clean.csv # Clean dataset (5 countries x 8 indicators)
│       └── digital_readiness_score.csv # Normalized scores and DRS ranking
├── notebooks/
│   └── Digital_Economy_Analysis.ipynb# Reproducible Jupyter notebook covering all 12 sections
├── dashboard/                        # Modern Interactive Single-Page Dashboard
│   ├── index.html                    # Responsive glassmorphic frontend
│   ├── styles.css                    # Design system (AgTech Midnight Emerald & Glassmorphism)
│   ├── app.js                        # Dynamic Chart.js logic & real-time DRS Simulator
│   └── data.json                     # JSON data feed for the frontend
├── docs/                             # In-depth reference guides for team study & defense
│   ├── 01_conceptual_framework.md
│   ├── 02_indicator_selection_and_breakdown.md
│   ├── 03_drs_methodology_and_modeling.md
│   ├── 04_strategic_diagnosis_and_gaps.md
│   └── 05_team_reproducibility_guide.md
├── scripts/
│   ├── 01_fetch_data.py              # Automated API acquisition
│   ├── 02_process_data.py            # Data cleaning, normalization, and DRS calculation
│   └── 04_generate_notebook.py       # Jupyter notebook generator
├── source_log.csv                    # Official traceability register & source URLs
├── data_dictionary.csv               # Formal data dictionary
├── requirements.txt                  # Python dependencies
└── README.md                         # Main repository documentation
```

---

## 📊 Selected Indicators (Exactly 8)

| # | Dimension | Code | Indicator Name | Source | DRS Direction |
|---|---|---|---|---|---|
| 1 | **Infrastructure** | `IT_NET_BBND` | Fixed broadband subscriptions per 100 people | World Bank / ITU | Direct (+) |
| 2 | **Infrastructure** | `IT_NET_SECR` | Secure Internet servers per 1 million people | World Bank / Netcraft | Direct (+) |
| 3 | **Access / Usage** | `IT_NET_USER` | Individuals using the Internet (% population) | ITU / World Bank | Direct (+) |
| 4 | **Affordability** | `ITU_PRICE_BASKET` | Fixed broadband basket (% GNI per capita) | ITU DataHub | **Inverted (-)** |
| 5 | **Economic Activity** | `ICT_SERV_EXP` | ICT service exports (% service exports) | UNCTAD / World Bank | Direct (+) |
| 6 | **Economic Activity** | `DIGIT_DELIV_EXP` | Digitally deliverable services (% service exports) | UNCTADstat | Direct (+) |
| 7 | **Innovation** | `RD_EXP_GDP` | R&D expenditure (% of GDP) | UNESCO / World Bank | Direct (+) |
| 8 | **Innovation** | `PATENT_RES_PM` | Resident patent applications per 1M population | WIPO Statistics | Direct (+) |

---

## 🏆 Digital Readiness Score (DRS 2023) Results

$$\text{DRS} = \sum_{i=1}^{8} w_i \cdot I_{i,\text{norm}} \quad (w_i = 0.125)$$

| Rank | Economy | Flag | DRS Score | Digital Profile Summary |
|:---:|---|:---:|:---:|---|
| **#1** | **Netherlands** | 🇳🇱 | **92.14** | Global Benchmark in Datacenter Infrastructure & Precision AgTech |
| **#2** | **New Zealand** | 🇳🇿 | **60.91** | Advanced Agricultural Exporter with Institutional Digitization |
| **#3** | **Argentina** | 🇦🇷 | **55.72** | Regional Leader in Software & Knowledge-Based Services Exports |
| **#4** | **Mexico** | 🇲🇽 | **26.57** | High Consumer Internet Adoption, but Critical Deficit in R&D & IP |
| **#5** | **Kenya** | 🇰🇪 | **15.42** | Pioneer in Mobile Money (*M-Pesa*), Constrained by Fixed Broadband |

---

## 🚀 Local Reproduction Instructions

```bash
# 1. Clone the repository
git clone https://github.com/RusselKu/DigitalEconomyUpy.git
cd DigitalEconomyUpy

# 2. Install dependencies
pip install -r requirements.txt

# 3. Execute the data pipeline
python scripts/01_fetch_data.py
python scripts/02_process_data.py

# 4. Open the interactive dashboard
# Open dashboard/index.html in any web browser
```

---

## 📝 Final Executive Diagnosis (220 Words - Max 250)

1. **Mexico's Relative Position:** Mexico ranks 4th in the group with a Digital Readiness Score of **26.57 points**, lagging significantly behind the Netherlands (92.14), New Zealand (60.91), and Argentina (55.72), while outperforming only Kenya (15.42).
2. **Primary Strength:** Robust internet user penetration (81.2%) and an affordable entry-level broadband basket (1.95% of GNI per capita), supported by established electronics hardware manufacturing.
3. **Primary Gap:** A severe deficit in backend infrastructure, domestic R&D, and intellectual property: recording only 412 secure servers per million people, 0.27% of GDP in R&D, and 8.8 resident patents per million, preventing the creation of proprietary AgTech software.
4. **Most Compelling Benchmark:** **Argentina**, which as an upper-middle-income Latin American peer exports 64.2% of its services in digitally deliverable format and 15.9% in ICT services, proving Mexico can transition to high-margin knowledge services without waiting for European-level GDP per capita.
5. **Primary Dataset Limitation:** Country-level aggregation masks stark internal regional divides (technified northern agribusiness vs. rural southern smallholders) and lacks direct metrics on IoT-equipped agricultural acreage or dedicated AI GPU infrastructure.
