"""
Programmatic data acquisition and traceability script for official data
Digital Economy Intelligence Lab - Team 3 (Agriculture)
Official Sources: World Bank (WDI), ITU DataHub, UNCTADstat, WIPO IP Statistics
"""

import os
import json
import requests
import pandas as pd

def fetch_data():
    raw_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'raw')
    official_dir = os.path.join(raw_dir, 'official')
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(official_dir, exist_ok=True)

    countries = ['MEX', 'NLD', 'KEN', 'ARG', 'NZL']
    country_str = ';'.join(countries)

    # 1. World Bank API fetch (HTTPS)
    wb_indicators = {
        'IT.NET.BBND.P2': 'Fixed broadband subscriptions (per 100 people)',
        'IT.NET.SECR.P6': 'Secure Internet servers (per 1 million people)',
        'IT.NET.USER.ZS': 'Individuals using the Internet (% of population)',
        'BX.GSR.CCIS.ZS': 'ICT service exports (% of service exports, BoP 6)',
        'GB.XPD.RSDV.GD.ZS': 'Research and development expenditure (% of GDP)',
        'NY.GDP.PCAP.CD': 'GDP per capita (current US$)',
        'SP.POP.TOTL': 'Population, total'
    }

    wb_records = []
    print("[1/4] Downloading official data from World Bank API (HTTPS)...")
    for ind_code, ind_name in wb_indicators.items():
        url = f"https://api.worldbank.org/v2/country/{country_str}/indicator/{ind_code}?date=2019:2024&format=json&per_page=1000"
        try:
            resp = requests.get(url, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                if len(data) > 1 and data[1]:
                    for item in data[1]:
                        wb_records.append({
                            'country_iso3': item['countryiso3code'],
                            'country_name': item['country']['value'],
                            'indicator_id': ind_code,
                            'indicator_name': ind_name,
                            'year': int(item['date']),
                            'value': item['value'],
                            'source': 'World Bank WDI'
                        })
        except Exception as e:
            print(f"Error fetching {ind_code}: {e}")

    with open(os.path.join(raw_dir, 'world_bank_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(wb_records, f, indent=2, ensure_ascii=False)
    pd.DataFrame(wb_records).to_csv(os.path.join(raw_dir, 'world_bank_raw.csv'), index=False, encoding='utf-8')
    print(f"  -> World Bank: {len(wb_records)} records saved to data/raw/world_bank_raw.csv")

    # 2. ITU DataHub (Read from official untouched download in data/raw/official/)
    print("[2/4] Parsing official download from ITU DataHub...")
    itu_official_file = os.path.join(official_dir, 'itu_price_basket_official.csv')
    if not os.path.exists(itu_official_file):
        raise FileNotFoundError(
            f"Official ITU dataset missing: '{itu_official_file}'. "
            "Please ensure the untouched official download file is placed in data/raw/official/ without manual imputation."
        )

    itu_df = pd.read_csv(itu_official_file)
    itu_data = []
    for _, row in itu_df.iterrows():
        c_code = str(row['Country_Code']).strip()
        if c_code in countries:
            itu_data.append({
                'country_iso3': c_code,
                'country_name': str(row['Country_Name']).strip(),
                'indicator_id': 'ITU_PRICE_BASKET_FBB',
                'indicator_name': 'Fixed broadband basket (% of GNI per capita)',
                'year': int(row['Year']),
                'value': float(row['Value']),
                'source': 'ITU DataHub (ICT Price Basket)'
            })

    with open(os.path.join(raw_dir, 'itu_datahub_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(itu_data, f, indent=2, ensure_ascii=False)
    pd.DataFrame(itu_data).to_csv(os.path.join(raw_dir, 'itu_datahub_raw.csv'), index=False, encoding='utf-8')
    print(f"  -> ITU DataHub: {len(itu_data)} verified records extracted to data/raw/itu_datahub_raw.csv")

    # 3. UNCTADstat (Read from official untouched download in data/raw/official/)
    print("[3/4] Parsing official download from UNCTADstat Data Centre...")
    unctad_official_file = os.path.join(official_dir, 'unctad_digitally_deliverable_services_official.csv')
    if not os.path.exists(unctad_official_file):
        raise FileNotFoundError(
            f"Official UNCTADstat dataset missing: '{unctad_official_file}'. "
            "Please ensure the untouched official download file is placed in data/raw/official/ without manual imputation."
        )

    unctad_df = pd.read_csv(unctad_official_file)
    unctad_data = []
    for _, row in unctad_df.iterrows():
        c_code = str(row['Economy_Code']).strip()
        if c_code in countries:
            unctad_data.append({
                'country_iso3': c_code,
                'country_name': str(row['Economy_Label']).strip(),
                'indicator_id': 'UNCTAD_DIGIT_DELIV_EXP',
                'indicator_name': 'Digitally deliverable services exports (% of total service exports)',
                'year': int(row['Year']),
                'value': float(row['Value']),
                'source': 'UNCTADstat Data Centre'
            })

    with open(os.path.join(raw_dir, 'unctad_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(unctad_data, f, indent=2, ensure_ascii=False)
    pd.DataFrame(unctad_data).to_csv(os.path.join(raw_dir, 'unctad_raw.csv'), index=False, encoding='utf-8')
    print(f"  -> UNCTADstat: {len(unctad_data)} verified records extracted to data/raw/unctad_raw.csv")

    # 4. WIPO IP Statistics (Read from official untouched download in data/raw/official/)
    print("[4/4] Parsing official download from WIPO IP Statistics Data Center...")
    wipo_official_file = os.path.join(official_dir, 'wipo_patents_official.csv')
    if not os.path.exists(wipo_official_file):
        raise FileNotFoundError(
            f"Official WIPO dataset missing: '{wipo_official_file}'. "
            "Please ensure the untouched official download file is placed in data/raw/official/ without manual imputation."
        )

    wipo_df = pd.read_csv(wipo_official_file)
    wipo_data = []
    for _, row in wipo_df.iterrows():
        c_code = str(row['Country_Code']).strip()
        if c_code in countries:
            wipo_data.append({
                'country_iso3': c_code,
                'country_name': str(row['Country_Name']).strip(),
                'indicator_id': 'WIPO_PATENT_RES_PM',
                'indicator_name': 'Patent applications by residents per million population',
                'year': int(row['Year']),
                'value': float(row['Value']),
                'source': 'WIPO IP Statistics Data Center'
            })

    with open(os.path.join(raw_dir, 'wipo_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(wipo_data, f, indent=2, ensure_ascii=False)
    pd.DataFrame(wipo_data).to_csv(os.path.join(raw_dir, 'wipo_raw.csv'), index=False, encoding='utf-8')
    print(f"  -> WIPO IP Statistics: {len(wipo_data)} verified records extracted to data/raw/wipo_raw.csv")
    print("\nData acquisition completed successfully via HTTPS and official raw source files.")

if __name__ == '__main__':
    fetch_data()
