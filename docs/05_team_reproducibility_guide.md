# 05. Team Reproducibility and Project Defense Guide

**Team 3: Agriculture**  
**Project:** Digital Economy Intelligence Lab  
**Deliverable:** Activity 2 · Part I

---

## 1. Individual Responsibility and Defense
> **Course Rule:** Although the project was developed as a team, every member must be capable of independently explaining data provenance, the definition of each of the 8 indicators, the mathematical normalization of the DRS, and the quantitative findings.

---

## 2. Directory and File Structure

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
│   └── Digital_Economy_Analysis.ipynb# Reproducible Jupyter notebook with all 12 sections
├── dashboard/
│   ├── index.html                    # Modern Single-Page Dashboard (English)
│   ├── styles.css                    # Glassmorphic AgTech CSS design system
│   ├── app.js                        # Dynamic Chart.js logic & DRS Simulator
│   └── data.json                     # JSON data for frontend consumption
├── docs/                             # In-depth guides for team study
│   ├── 01_conceptual_framework.md
│   ├── 02_indicator_selection_and_breakdown.md
│   ├── 03_drs_methodology_and_modeling.md
│   ├── 04_strategic_diagnosis_and_gaps.md
│   └── 05_team_reproducibility_guide.md
├── scripts/
│   ├── 01_fetch_data.py              # Automated API acquisition
│   ├── 02_process_data.py            # Data cleaning & DRS computation
│   └── 04_generate_notebook.py       # Notebook generator
├── source_log.csv                    # Official traceability register
├── data_dictionary.csv               # Formal data dictionary
├── requirements.txt                  # Python dependencies
└── README.md                         # Main repository cover
```

---

## 3. Step-by-Step Reproduction Instructions

To execute and validate the complete pipeline on any local machine:

### Step 1: Clone the repository and install dependencies
```bash
git clone https://github.com/RusselKu/DigitalEconomyUpy.git
cd DigitalEconomyUpy
pip install -r requirements.txt
```

### Step 2: Run the full data pipeline
```bash
# 1. Fetch raw data from official APIs (World Bank, ITU, UNCTAD, WIPO)
python scripts/01_fetch_data.py

# 2. Process data and calculate Digital Readiness Score (DRS)
python scripts/02_process_data.py

# 3. Regenerate and execute the reproducible Jupyter notebook
python scripts/04_generate_notebook.py
python -m jupyter nbconvert --to notebook --execute --inplace notebooks/Digital_Economy_Analysis.ipynb
```

### Step 3: Launch the Interactive Dashboard
* **Local Option:** Double-click on `dashboard/index.html` to open it in any modern browser.
* **GitHub Pages:** View the live deployed dashboard via GitHub Pages.

---

## 4. Key Exam & Defense Q&A for Team Members

1. **Why was the scale inverted for the ICT price basket indicator?**  
   *Answer:* Because a higher price relative to national income indicates that internet access is expensive and unaffordable. By inverting the scale ($100$ points for the lowest relative cost), higher scores represent greater affordability, aligning with the positive direction of the DRS.

2. **Why does Argentina achieve a higher DRS score than Mexico despite a similar GDP per capita?**  
   *Answer:* The DRS heavily rewards knowledge-based and software export specialization. Argentina exports 64.2% of its services in digitally deliverable format and 15.9% in ICT services, whereas Mexico specializes in physical hardware assembly and tourism, exporting only 24.5% and 2.9% respectively.

3. **What is the difference between the ICT sector and a digitalized economy in agriculture?**  
   *Answer:* The ICT sector produces the physical microchips and cellular towers. The digitalized economy represents the actual adoption of those sensors, satellite data, and machine learning models on agricultural plots to optimize crop yields and reduce resource use.
