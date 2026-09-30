# 02. Indicator Selection, Justification, and Traceability

**Team 3: Agriculture**  
**Assigned Economies:** Mexico 🇲🇽, Netherlands 🇳🇱, Kenya 🇰🇪, Argentina 🇦🇷, New Zealand 🇳🇿

---

## 1. Mandatory Category Distribution

To evaluate the digitalized economy within the agricultural and technology domains, exactly **8 indicators** were selected across **4 recognized official international organizations**, strictly adhering to the required category quotas:

```
Category Quota Distribution:
├── 2 Infrastructure / Connectivity Indicators (IT_NET_BBND, IT_NET_SECR)
├── 1 Access / Usage Indicator (IT_NET_USER)
├── 1 Quality / Affordability Indicator (ITU_PRICE_BASKET) [Inverted Scale]
├── 2 Digital Economic Activity Indicators (ICT_SERV_EXP, DIGIT_DELIV_EXP)
└── 2 Technological Capacity / Innovation Indicators (RD_EXP_GDP, PATENT_RES_PM)
```

---

## 2. Detailed Technical Breakdown of the 8 Indicators

### 1. Fixed Broadband Subscriptions (`IT_NET_BBND`)
* **Category:** Infrastructure or Connectivity (1/2)
* **Definition:** Number of fixed-broadband residential and commercial high-speed internet subscriptions (FTTH, cable, DSL) per 100 inhabitants.
* **Official Source:** International Telecommunication Union (ITU) / World Bank
* **Agricultural Relevance:** Smart farms, packing plants, and agricultural cooperatives require high-speed fixed broadband to process gigabytes of multispectral satellite imagery, upload telemetry, and synchronize local farm servers.
* **2023 Values:** Netherlands (43.26), New Zealand (37.85), Argentina (25.36), Mexico (20.75), Kenya (2.39).

### 2. Secure Internet Servers (`IT_NET_SECR`)
* **Category:** Infrastructure or Connectivity (2/2)
* **Definition:** Number of publicly accessible internet servers with valid SSL/TLS encryption certificates per 1 million people.
* **Official Source:** Netcraft / World Bank
* **Agricultural Relevance:** Measures cloud compute capacity, datacenter concentration, and backend security necessary for hosting precision AgTech platforms and IoT databases.
* **2023 Values:** Netherlands (194,962.9), New Zealand (18,993.7), Argentina (5,451.2), Mexico (412.1), Kenya (297.1).

### 3. Population Using the Internet (`IT_NET_USER`)
* **Category:** Access or Usage (1/1)
* **Definition:** Percentage of individuals (aged 3+ or 5+) who used the internet from any location via any device in the last 3 months.
* **Official Source:** ITU / World Bank
* **Agricultural Relevance:** Represents the baseline addressable population of farmers, agronomists, and rural stakeholders capable of adopting agricultural apps and digital extension advisory services.
* **2023 Values:** Netherlands (97.01%), New Zealand (93.33%), Argentina (89.23%), Mexico (81.18%), Kenya (32.07%).

### 4. Fixed Broadband Basket Cost (`ITU_PRICE_BASKET`)
* **Category:** Quality or Affordability (1/1)
* **Definition:** Price of an entry-level fixed broadband monthly basket (minimum 5GB) expressed as a percentage of monthly Gross National Income (GNI) per capita.
* **Official Source:** ITU DataHub (ICT Price Trends)
* **Treatment in DRS:** **Inverted Scale (-)**. Lower basket cost signifies higher affordability. The UN Broadband Commission target is <2.0% of GNI per capita.
* **2023 Values:** Netherlands (0.82%), New Zealand (0.98%), Mexico (1.95%), Argentina (2.90%), Kenya (10.40%).

### 5. ICT Service Exports (`ICT_SERV_EXP`)
* **Category:** Digital Economic Activity (1/2)
* **Definition:** Telecommunications, computer, and information services exports as a percentage of total commercial service exports (BPM6 Balance of Payments).
* **Official Source:** IMF / UNCTAD / World Bank
* **Agricultural Relevance:** Reflects the national software industry's capacity to build and export AgTech software platforms, database architecture, and digital farm management solutions to foreign markets.
* **2023 Values:** Argentina (15.87%), Kenya (10.67%), Netherlands (9.62%), New Zealand (6.95%), Mexico (2.92%).

### 6. Digitally Deliverable Services Exports (`DIGIT_DELIV_EXP`)
* **Category:** Digital Economic Activity (2/2)
* **Definition:** Share of service exports that can be delivered remotely over ICT networks (consulting, engineering, software, financial analytics) as % of total service exports.
* **Official Source:** UNCTADstat Data Centre
* **Agricultural Relevance:** Measures an economy's capacity to monetize intangible agricultural knowledge (e.g., cross-border agronomic consulting and satellite yield analytics subscriptions).
* **2023 Values:** Argentina (64.2%), Netherlands (58.4%), New Zealand (44.8%), Kenya (39.2%), Mexico (24.5%).

### 7. Research & Development Expenditure (`RD_EXP_GDP`)
* **Category:** Technological Capacity or Innovation (1/2)
* **Definition:** Gross domestic expenditure on scientific research and experimental development expressed as a percentage of GDP.
* **Official Source:** UNESCO Institute for Statistics / World Bank
* **Agricultural Relevance:** The fundamental engine for creating climate-resilient crop varieties, biological crop protection, automated agricultural robotics, and machine learning models for yield prediction.
* **2023 Values:** Netherlands (2.27%), New Zealand (1.55%), Kenya (0.80%), Argentina (0.60%), Mexico (0.27%).

### 8. Resident Patent Applications (`PATENT_RES_PM`)
* **Category:** Technological Capacity or Innovation (2/2)
* **Definition:** Total patent applications filed with national patent offices by resident inventors per 1 million population.
* **Official Source:** WIPO IP Statistics Data Center
* **Agricultural Relevance:** Quantifies domestic proprietary innovation in agricultural machinery, automated irrigation hardware, and biotechnology.
* **2023 Values:** Netherlands (495.00), New Zealand (60.00), Argentina (9.00), Mexico (8.00), Kenya (7.00).

---

## 3. Consolidated Official Matrix (Year 2023)

| Economy | ISO3 | IT_NET_BBND | IT_NET_SECR | IT_NET_USER | ITU_PRICE_BASKET | ICT_SERV_EXP | DIGIT_DELIV_EXP | RD_EXP_GDP | PATENT_RES_PM |
|---|---|---|---|---|---|---|---|---|---|
| **Mexico** | `MEX` | 20.75 | 412.12 | 81.18% | 1.95% | 2.92% | 24.50% | 0.27% | 8.00 |
| **Netherlands** | `NLD` | 43.26 | 194962.90 | 97.01% | 0.82% | 9.62% | 58.40% | 2.27% | 495.00 |
| **Kenya** | `KEN` | 2.39 | 297.13 | 32.07% | 10.40% | 10.67% | 39.20% | 0.80% | 7.00 |
| **Argentina** | `ARG` | 25.36 | 5451.20 | 89.23% | 2.90% | 15.87% | 64.20% | 0.60% | 9.00 |
| **New Zealand** | `NZL` | 37.85 | 18993.65 | 93.33% | 0.98% | 6.95% | 44.80% | 1.55% | 60.00 |
