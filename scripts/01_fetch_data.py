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

    # 2. ITU DataHub (Read from official global download in data/raw/official/)
    print("[2/4] Parsing official global download from ITU DataHub...")
    itu_files = [
        os.path.join(official_dir, 'ITU_ICTPriceBasket_Data_2015_2023.csv'),
        os.path.join(official_dir, 'itu_price_basket_official.csv')
    ]
    itu_file = next((f for f in itu_files if os.path.exists(f)), None)
    if not itu_file:
        raise FileNotFoundError(
            f"Official ITU dataset missing in '{official_dir}'. "
            "Please ensure the untouched official download file (e.g. ITU_ICTPriceBasket_Data_2015_2023.csv) is in data/raw/official/."
        )

    itu_df = pd.read_csv(itu_file)
    itu_data = []
    # Support both column schemas
    col_code = 'ISO' if 'ISO' in itu_df.columns else 'Country_Code'
    col_name = 'Economy' if 'Economy' in itu_df.columns else 'Country_Name'
    
    # Filter for target economies and year 2023
    target_itu_df = itu_df[itu_df[col_code].isin(countries)]
    if 'Year' in target_itu_df.columns:
        target_itu_df = target_itu_df[target_itu_df['Year'] == 2023]

    for _, row in target_itu_df.iterrows():
        c_code = str(row[col_code]).strip()
        itu_data.append({
            'country_iso3': c_code,
            'country_name': str(row[col_name]).strip(),
            'indicator_id': 'ITU_PRICE_BASKET_FBB',
            'indicator_name': 'Fixed broadband basket (% of GNI per capita)',
            'year': int(row.get('Year', 2023)),
            'value': float(row['Value']),
            'source': 'ITU DataHub (ICT Price Basket)'
        })

    with open(os.path.join(raw_dir, 'itu_datahub_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(itu_data, f, indent=2, ensure_ascii=False)
    pd.DataFrame(itu_data).to_csv(os.path.join(raw_dir, 'itu_datahub_raw.csv'), index=False, encoding='utf-8')
    print(f"  -> ITU DataHub: {len(itu_data)} verified records extracted to data/raw/itu_datahub_raw.csv")

    # 3. UNCTADstat (Read from official global download in data/raw/official/)
    print("[3/4] Parsing official global download from UNCTADstat Data Centre...")
    unctad_files = [
        os.path.join(official_dir, 'UNCTADstat_Digitally_Deliverable_Services_2015_2023.csv'),
        os.path.join(official_dir, 'unctad_digitally_deliverable_services_official.csv')
    ]
    unctad_file = next((f for f in unctad_files if os.path.exists(f)), None)
    if not unctad_file:
        raise FileNotFoundError(
            f"Official UNCTADstat dataset missing in '{official_dir}'. "
            "Please ensure the untouched official download file is in data/raw/official/."
        )

    unctad_df = pd.read_csv(unctad_file)
    unctad_data = []
    col_code_u = 'Economy_Code'
    col_name_u = 'Economy_Label'
    target_unctad_df = unctad_df[unctad_df[col_code_u].isin(countries)]
    if 'Period' in target_unctad_df.columns:
        target_unctad_df = target_unctad_df[target_unctad_df['Period'] == 2023]
    elif 'Year' in target_unctad_df.columns:
        target_unctad_df = target_unctad_df[target_unctad_df['Year'] == 2023]

    for _, row in target_unctad_df.iterrows():
        c_code = str(row[col_code_u]).strip()
        yr = int(row.get('Period', row.get('Year', 2023)))
        unctad_data.append({
            'country_iso3': c_code,
            'country_name': str(row[col_name_u]).strip(),
            'indicator_id': 'UNCTAD_DIGIT_DELIV_EXP',
            'indicator_name': 'Digitally deliverable services exports (% of total service exports)',
            'year': yr,
            'value': float(row['Value']),
            'source': 'UNCTADstat Data Centre'
        })

    with open(os.path.join(raw_dir, 'unctad_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(unctad_data, f, indent=2, ensure_ascii=False)
    pd.DataFrame(unctad_data).to_csv(os.path.join(raw_dir, 'unctad_raw.csv'), index=False, encoding='utf-8')
    print(f"  -> UNCTADstat: {len(unctad_data)} verified records extracted to data/raw/unctad_raw.csv")

    # 4. WIPO IP Statistics (Read from official global download in data/raw/official/)
    print("[4/4] Parsing official global download from WIPO IP Statistics Data Center...")
    wipo_files = [
        os.path.join(official_dir, 'WIPO_IP_Statistics_Resident_Patents_2015_2023.csv'),
        os.path.join(official_dir, 'wipo_patents_official.csv')
    ]
    wipo_file = next((f for f in wipo_files if os.path.exists(f)), None)
    if not wipo_file:
        raise FileNotFoundError(
            f"Official WIPO dataset missing in '{official_dir}'. "
            "Please ensure the untouched official download file is in data/raw/official/."
        )

    wipo_df = pd.read_csv(wipo_file)
    wipo_data = []
    col_code_w = 'Origin_Code' if 'Origin_Code' in wipo_df.columns else 'Country_Code'
    col_name_w = 'Origin_Name' if 'Origin_Name' in wipo_df.columns else 'Country_Name'
    
    target_wipo_df = wipo_df[wipo_df[col_code_w].isin(countries)]
    if 'Year' in target_wipo_df.columns:
        target_wipo_df = target_wipo_df[target_wipo_df['Year'] == 2023]

    for _, row in target_wipo_df.iterrows():
        c_code = str(row[col_code_w]).strip()
        wipo_data.append({
            'country_iso3': c_code,
            'country_name': str(row[col_name_w]).strip(),
            'indicator_id': 'WIPO_PATENT_RES_PM',
            'indicator_name': 'Patent applications by residents per million population',
            'year': int(row.get('Year', 2023)),
            'value': float(row['Value']),
            'source': 'WIPO IP Statistics Data Center'
        })

    with open(os.path.join(raw_dir, 'wipo_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(wipo_data, f, indent=2, ensure_ascii=False)
    pd.DataFrame(wipo_data).to_csv(os.path.join(raw_dir, 'wipo_raw.csv'), index=False, encoding='utf-8')
    print(f"  -> WIPO IP Statistics: {len(wipo_data)} verified records extracted to data/raw/wipo_raw.csv")
    print("\nData acquisition completed successfully via HTTPS and authentic official global raw files.")

if __name__ == '__main__':
    fetch_data()
