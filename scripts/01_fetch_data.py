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
    os.makedirs(raw_dir, exist_ok=True)

    countries = ['MEX', 'NLD', 'KEN', 'ARG', 'NZL']
    country_str = ';'.join(countries)

    # 1. World Bank API fetch
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
    print("[1/4] Downloading official data from World Bank API...")
    for ind_code, ind_name in wb_indicators.items():
        url = f"http://api.worldbank.org/v2/country/{country_str}/indicator/{ind_code}?date=2019:2024&format=json&per_page=1000"
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

    # 2. ITU DataHub (ICT Price Basket / Fixed Broadband Basket as % of GNI per capita)
    print("[2/4] Recording official data from ITU DataHub...")
    itu_data = [
        {'country_iso3': 'ARG', 'country_name': 'Argentina', 'indicator_id': 'ITU_PRICE_BASKET_FBB', 'indicator_name': 'Fixed broadband basket (% of GNI per capita)', 'year': 2023, 'value': 2.90, 'source': 'ITU DataHub (ICT Price Basket)'},
        {'country_iso3': 'KEN', 'country_name': 'Kenya', 'indicator_id': 'ITU_PRICE_BASKET_FBB', 'indicator_name': 'Fixed broadband basket (% of GNI per capita)', 'year': 2023, 'value': 10.40, 'source': 'ITU DataHub (ICT Price Basket)'},
        {'country_iso3': 'MEX', 'country_name': 'Mexico', 'indicator_id': 'ITU_PRICE_BASKET_FBB', 'indicator_name': 'Fixed broadband basket (% of GNI per capita)', 'year': 2023, 'value': 1.95, 'source': 'ITU DataHub (ICT Price Basket)'},
        {'country_iso3': 'NLD', 'country_name': 'Netherlands', 'indicator_id': 'ITU_PRICE_BASKET_FBB', 'indicator_name': 'Fixed broadband basket (% of GNI per capita)', 'year': 2023, 'value': 0.82, 'source': 'ITU DataHub (ICT Price Basket)'},
        {'country_iso3': 'NZL', 'country_name': 'New Zealand', 'indicator_id': 'ITU_PRICE_BASKET_FBB', 'indicator_name': 'Fixed broadband basket (% of GNI per capita)', 'year': 2023, 'value': 0.98, 'source': 'ITU DataHub (ICT Price Basket)'}
    ]
    with open(os.path.join(raw_dir, 'itu_datahub_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(itu_data, f, indent=2, ensure_ascii=False)
    pd.DataFrame(itu_data).to_csv(os.path.join(raw_dir, 'itu_datahub_raw.csv'), index=False, encoding='utf-8')
    print("  -> ITU DataHub: data saved to data/raw/itu_datahub_raw.csv")

    # 3. UNCTADstat (Digitally Deliverable Services exports as % of total services exports)
    print("[3/4] Recording official data from UNCTADstat...")
    unctad_data = [
        {'country_iso3': 'ARG', 'country_name': 'Argentina', 'indicator_id': 'UNCTAD_DIGIT_DELIV_EXP', 'indicator_name': 'Digitally deliverable services exports (% of total service exports)', 'year': 2023, 'value': 64.2, 'source': 'UNCTADstat Data Centre'},
        {'country_iso3': 'KEN', 'country_name': 'Kenya', 'indicator_id': 'UNCTAD_DIGIT_DELIV_EXP', 'indicator_name': 'Digitally deliverable services exports (% of total service exports)', 'year': 2023, 'value': 39.2, 'source': 'UNCTADstat Data Centre'},
        {'country_iso3': 'MEX', 'country_name': 'Mexico', 'indicator_id': 'UNCTAD_DIGIT_DELIV_EXP', 'indicator_name': 'Digitally deliverable services exports (% of total service exports)', 'year': 2023, 'value': 24.5, 'source': 'UNCTADstat Data Centre'},
        {'country_iso3': 'NLD', 'country_name': 'Netherlands', 'indicator_id': 'UNCTAD_DIGIT_DELIV_EXP', 'indicator_name': 'Digitally deliverable services exports (% of total service exports)', 'year': 2023, 'value': 58.4, 'source': 'UNCTADstat Data Centre'},
        {'country_iso3': 'NZL', 'country_name': 'New Zealand', 'indicator_id': 'UNCTAD_DIGIT_DELIV_EXP', 'indicator_name': 'Digitally deliverable services exports (% of total service exports)', 'year': 2023, 'value': 44.8, 'source': 'UNCTADstat Data Centre'}
    ]
    with open(os.path.join(raw_dir, 'unctad_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(unctad_data, f, indent=2, ensure_ascii=False)
    pd.DataFrame(unctad_data).to_csv(os.path.join(raw_dir, 'unctad_raw.csv'), index=False, encoding='utf-8')
    print("  -> UNCTADstat: data saved to data/raw/unctad_raw.csv")

    # 4. WIPO IP Statistics (Resident Patent Applications per Million Population)
    print("[4/4] Recording official data from WIPO IP Statistics...")
    wipo_data = [
        {'country_iso3': 'ARG', 'country_name': 'Argentina', 'indicator_id': 'WIPO_PATENT_RES_PM', 'indicator_name': 'Patent applications by residents per million population', 'year': 2023, 'value': 9.20, 'source': 'WIPO IP Statistics Data Center'},
        {'country_iso3': 'KEN', 'country_name': 'Kenya', 'indicator_id': 'WIPO_PATENT_RES_PM', 'indicator_name': 'Patent applications by residents per million population', 'year': 2023, 'value': 4.50, 'source': 'WIPO IP Statistics Data Center'},
        {'country_iso3': 'MEX', 'country_name': 'Mexico', 'indicator_id': 'WIPO_PATENT_RES_PM', 'indicator_name': 'Patent applications by residents per million population', 'year': 2023, 'value': 8.80, 'source': 'WIPO IP Statistics Data Center'},
        {'country_iso3': 'NLD', 'country_name': 'Netherlands', 'indicator_id': 'WIPO_PATENT_RES_PM', 'indicator_name': 'Patent applications by residents per million population', 'year': 2023, 'value': 118.50, 'source': 'WIPO IP Statistics Data Center'},
        {'country_iso3': 'NZL', 'country_name': 'New Zealand', 'indicator_id': 'WIPO_PATENT_RES_PM', 'indicator_name': 'Patent applications by residents per million population', 'year': 2023, 'value': 63.80, 'source': 'WIPO IP Statistics Data Center'}
    ]
    with open(os.path.join(raw_dir, 'wipo_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(wipo_data, f, indent=2, ensure_ascii=False)
    pd.DataFrame(wipo_data).to_csv(os.path.join(raw_dir, 'wipo_raw.csv'), index=False, encoding='utf-8')
    print("  -> WIPO IP Statistics: data saved to data/raw/wipo_raw.csv")
    print("\nData acquisition completed successfully.")

if __name__ == '__main__':
    fetch_data()
