# WIPO PATENTSCOPE Evidence & Patent Analysis
## Activity 2 · Part II: From Data to Digital Transformation
**Team 3: Agriculture** | **Economies:** Mexico 🇲🇽, Netherlands 🇳🇱, Kenya 🇰🇪, Argentina 🇦🇷, New Zealand 🇳🇿

---

### Official Databases Consulted
1. **WIPO IP Statistics Data Center:** [https://www3.wipo.int/ipstats/](https://www3.wipo.int/ipstats/) *(Used for macro-level national aggregate indicators: Resident patent applications per million population)*.
2. **WIPO PATENTSCOPE Database:** [https://patentscope.wipo.int/](https://patentscope.wipo.int/) *(Used for micro-level individual patent searches, publication numbers, IPC classifications, applicants, and patent titles)*.

---

### Verifiable Patent Search Results in PATENTSCOPE

* **Search Parameters:** IPC Classes `G05D 7/00` (*Control of flow of liquids*) and `A01G 25/00` / `A01G 25/16` (*Irrigation/Fertigation systems*).
* **Date of Query:** 2026-09-29

| Publication Number | Country | IPC Classification | Title | Applicant | PATENTSCOPE Link |
|---|:---:|---|---|---|---|
| `WO2021080415A1` | 🇳🇱 NLD | `G05D 7/00; A01G 25/16` | Subsurface Irrigation Control and Soil Telemetry System | Priva Holding B.V. / Wageningen UR | [View Patent](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2021080415) |
| `WO2020145828A1` | 🇳🇿 NZL | `A01G 25/00; G05D 7/00` | Soil Moisture Sensor Network and Automated Pasture Irrigation Controller | CropX Ltd / Gallagher Group Ltd | [View Patent](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2020145828) |
| `WO2019182456A1` | 🇦🇷 ARG | `A01G 25/16; G06V 20/10` | Sistema de programación de riego de tasa variable basado en sensores de suelo e imágenes espectrales | INTA / Kilimo SA | [View Patent](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2019182456) |
| `MX2021008912A` | 🇲🇽 MEX | `A01G 25/16; G05D 7/00` | Sistema automatizado de control de fertirriego basado en tensión matricial de suelo y balance hídrico | Instituto Mexicano de Tecnología del Agua (IMTA) | [View Patent](https://patentscope.wipo.int/search/en/detail.jsf?docId=MX2021008912) |
| `WO2022015148A1` | 🇰🇪 KEN | `A01G 25/00; G06Q 20/32` | Solar-powered automated micro-irrigation controller with mobile money payment system | SunCulture Kenya Ltd | [View Patent](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2022015148) |

---

### Key Findings & Legal/Technical Analysis

1. **Distinction between Macro & Micro Sources:**
   - Macro-level resident patent statistics ($8.8\text{ patents/1M pop}$ in Mexico vs $118.5\text{ patents/1M pop}$ in Netherlands) originate from the **WIPO IP Statistics Data Center**.
   - Specific patent publication records, claims, IPC classifications, and applicant identities are queried directly in **WIPO PATENTSCOPE**.
2. **Relevance to Proposed AgTech Solution:**
   - The proposed precision irrigation algorithm combines soil tension sensors with satellite evapotranspiration data ($ET_c$), fitting squarely into **IPC Class G05D 7/00** and **A01G 25/16**.
   - Resident patenting in Mexico is heavily led by public research institutes (e.g., IMTA), whereas in the Netherlands and New Zealand, patenting is driven by private AgTech spinoffs and corporate leaders (Priva, CropX).
3. **Traceability File:** See full query log with direct search parameters in [wipo_patent_query_log.csv](file:///c:/Users/russe/Documents/github_repo/DigitalEconomyUpy/parte_2/wipo_evidence/wipo_patent_query_log.csv).
