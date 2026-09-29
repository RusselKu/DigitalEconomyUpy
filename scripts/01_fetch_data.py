"""
Programmatic data acquisition and traceability script for official data
Digital Economy Intelligence Lab - Team 3 (Agriculture)
Official Sources: World Bank (WDI), ITU DataHub, UNCTADstat, WIPO IP Statistics
Author: Russel Ku (Lead Data Architect)
"""

import os
import glob
import json
import requests
import pandas as pd
import numpy as np

def find_official_file(pattern_list, search_dirs):
    """Search for matching official download files in priority order."""
    for s_dir in search_dirs:
        if not os.path.exists(s_dir):
            continue
        for pat in pattern_list:
            matches = glob.glob(os.path.join(s_dir, pat))
            if matches:
                return matches[0]
    return None

def fetch_data():
    raw_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'raw')
    official_dir = os.path.join(raw_dir, 'official')
    original_dir = os.path.join(official_dir, 'original')
    
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(official_dir, exist_ok=True)
    os.makedirs(original_dir, exist_ok=True)

    target_countries = ['MEX', 'NLD', 'KEN', 'ARG', 'NZL']
    country_names_map = {
        'MEX': 'Mexico',
        'NLD': 'Netherlands',
        'KEN': 'Kenya',
        'ARG': 'Argentina',
        'NZL': 'New Zealand'
    }
    country_str = ';'.join(target_countries)

    search_dirs = [original_dir, official_dir]

    # =========================================================================
    # 1. World Bank API Fetch (HTTPS)
    # =========================================================================
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
                        val = item['value']
                        # Retain raw value without imputation
                        wb_records.append({
                            'country_iso3': item['countryiso3code'],
                            'country_name': item['country']['value'],
                            'indicator_id': ind_code,
                            'indicator_name': ind_name,
                            'year': int(item['date']),
                            'value': val,
                            'source': 'World Bank WDI'
                        })
        except Exception as e:
            print(f"Error fetching {ind_code}: {e}")

    with open(os.path.join(raw_dir, 'world_bank_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(wb_records, f, indent=2, ensure_ascii=False)
    pd.DataFrame(wb_records).to_csv(os.path.join(raw_dir, 'world_bank_raw.csv'), index=False, encoding='utf-8')
    print(f"  -> World Bank: {len(wb_records)} records saved to data/raw/world_bank_raw.csv")

    # =========================================================================
    # 2. ITU DataHub (ICT Price Basket / Fixed Broadband Basket)
    # =========================================================================
    print("[2/4] Parsing authentic official download from ITU DataHub...")
    itu_file = find_official_file(
        ['*itu*.csv', '*ITU*.csv', '*price_basket*.csv', '*Price*.csv'],
        search_dirs
    )
    if not itu_file:
        raise FileNotFoundError(
            f"[TODO_EQUIPO] Official ITU raw download file not found in {original_dir} or {official_dir}.\n"
            "Please download the original CSV/XLSX from ITU DataHub and place it in data/raw/official/original/."
        )

    itu_df = pd.read_csv(itu_file)
    # Flexible column identification
    col_code = next((c for c in itu_df.columns if c.upper() in ['ISO', 'COUNTRY_CODE', 'COUNTRYCODE', 'ECONOMY_CODE', 'CODE']), None)
    col_year = next((c for c in itu_df.columns if c.upper() in ['YEAR', 'PERIOD', 'DATE', 'TIME']), None)
    col_val = next((c for c in itu_df.columns if c.upper() in ['VALUE', 'OBS_VALUE', 'VAL', 'PRICE']), None)

    if not col_code or not col_val:
        raise ValueError(f"Unable to identify country and value columns in ITU file: {itu_file}. Columns: {list(itu_df.columns)}")

    itu_data = []
    for c in target_countries:
        subset = itu_df[itu_df[col_code].astype(str).str.strip().str.upper() == c]
        if col_year and col_year in subset.columns:
            subset_2023 = subset[subset[col_year].astype(str).str.contains('2023')]
            if not subset_2023.empty:
                subset = subset_2023
            else:
                subset = subset.sort_values(by=col_year, ascending=False).head(1)
        
        if subset.empty:
            raise ValueError(f"[ERROR] Country {c} is missing from ITU official dataset: {itu_file}")
        
        raw_val = subset.iloc[0][col_val]
        if pd.isna(raw_val) or raw_val == '':
            raise ValueError(f"[ERROR] ITU data for country {c} is NaN / missing. Imputation is strictly prohibited.")
        
        val_float = float(raw_val)
        actual_year = int(subset.iloc[0][col_year]) if col_year and col_year in subset.columns and not pd.isna(subset.iloc[0][col_year]) else 2023

        itu_data.append({
            'country_iso3': c,
            'country_name': country_names_map[c],
            'indicator_id': 'ITU_PRICE_BASKET_FBB',
            'indicator_name': 'Fixed broadband basket (% of GNI per capita)',
            'year': actual_year,
            'value': val_float,
            'source': f'ITU DataHub ({os.path.basename(itu_file)})'
        })

    with open(os.path.join(raw_dir, 'itu_datahub_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(itu_data, f, indent=2, ensure_ascii=False)
    pd.DataFrame(itu_data).to_csv(os.path.join(raw_dir, 'itu_datahub_raw.csv'), index=False, encoding='utf-8')
    print(f"  -> ITU DataHub: {len(itu_data)} records validated from {os.path.basename(itu_file)}")

    # =========================================================================
    # 3. UNCTADstat (Digitally Deliverable Services Exports % Total Services)
    # =========================================================================
    print("[3/4] Parsing authentic official download from UNCTADstat Data Centre...")
    unctad_file = find_official_file(
        ['*unctad*.csv', '*UNCTAD*.csv', '*digitally_deliverable*.csv', '*DDS*.csv'],
        search_dirs
    )
    if not unctad_file:
        raise FileNotFoundError(
            f"[TODO_EQUIPO] Official UNCTAD raw download file not found in {original_dir} or {official_dir}.\n"
            "Please download the original CSV from UNCTADstat Data Centre and place it in data/raw/official/original/."
        )

    unctad_df = pd.read_csv(unctad_file)
    col_code_u = next((c for c in unctad_df.columns if c.upper() in ['ECONOMY_CODE', 'ECONOMY', 'ISO', 'COUNTRY_CODE', 'CODE']), None)
    col_year_u = next((c for c in unctad_df.columns if c.upper() in ['PERIOD', 'YEAR', 'DATE', 'TIME']), None)
    col_val_u = next((c for c in unctad_df.columns if c.upper() in ['VALUE', 'OBS_VALUE', 'VAL', 'PERCENTAGE']), None)

    if not col_code_u or not col_val_u:
        raise ValueError(f"Unable to identify country and value columns in UNCTAD file: {unctad_file}. Columns: {list(unctad_df.columns)}")

    unctad_data = []
    for c in target_countries:
        subset = unctad_df[unctad_df[col_code_u].astype(str).str.strip().str.upper() == c]
        if col_year_u and col_year_u in subset.columns:
            subset_2023 = subset[subset[col_year_u].astype(str).str.contains('2023')]
            if not subset_2023.empty:
                subset = subset_2023
            else:
                subset = subset.sort_values(by=col_year_u, ascending=False).head(1)

        if subset.empty:
            raise ValueError(f"[ERROR] Country {c} is missing from UNCTAD official dataset: {unctad_file}")

        raw_val = subset.iloc[0][col_val_u]
        if pd.isna(raw_val) or raw_val == '':
            raise ValueError(f"[ERROR] UNCTAD data for country {c} is NaN / missing. Imputation is strictly prohibited.")

        val_float = float(raw_val)
        actual_year = int(subset.iloc[0][col_year_u]) if col_year_u and col_year_u in subset.columns and not pd.isna(subset.iloc[0][col_year_u]) else 2023

        unctad_data.append({
            'country_iso3': c,
            'country_name': country_names_map[c],
            'indicator_id': 'UNCTAD_DIGIT_DELIV_EXP',
            'indicator_name': 'Digitally deliverable services exports (% of total service exports)',
            'year': actual_year,
            'value': val_float,
            'source': f'UNCTADstat Data Centre ({os.path.basename(unctad_file)})'
        })

    with open(os.path.join(raw_dir, 'unctad_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(unctad_data, f, indent=2, ensure_ascii=False)
    pd.DataFrame(unctad_data).to_csv(os.path.join(raw_dir, 'unctad_raw.csv'), index=False, encoding='utf-8')
    print(f"  -> UNCTADstat: {len(unctad_data)} records validated from {os.path.basename(unctad_file)}")

    # =========================================================================
    # 4. WIPO IP Statistics (Resident Patent Applications per Million Population)
    # =========================================================================
    print("[4/4] Parsing authentic official download from WIPO IP Statistics Data Center...")
    wipo_file = find_official_file(
        ['*wipo*.csv', '*WIPO*.csv', '*patent*.csv', '*Patents*.csv'],
        search_dirs
    )
    if not wipo_file:
        raise FileNotFoundError(
            f"[TODO_EQUIPO] Official WIPO raw download file not found in {original_dir} or {official_dir}.\n"
            "Please download the original CSV from WIPO IP Statistics and place it in data/raw/official/original/."
        )

    wipo_df = pd.read_csv(wipo_file)
    col_code_w = next((c for c in wipo_df.columns if c.upper() in ['ORIGIN_CODE', 'COUNTRY_CODE', 'ISO', 'OFFICE_CODE', 'CODE']), None)
    col_year_w = next((c for c in wipo_df.columns if c.upper() in ['YEAR', 'PERIOD', 'DATE', 'TIME']), None)
    col_val_w = next((c for c in wipo_df.columns if c.upper() in ['VALUE', 'OBS_VALUE', 'VAL', 'COUNT']), None)

    if not col_code_w or not col_val_w:
        raise ValueError(f"Unable to identify country and value columns in WIPO file: {wipo_file}. Columns: {list(wipo_df.columns)}")

    wipo_data = []
    for c in target_countries:
        subset = wipo_df[wipo_df[col_code_w].astype(str).str.strip().str.upper() == c]
        if col_year_w and col_year_w in subset.columns:
            subset_2023 = subset[subset[col_year_w].astype(str).str.contains('2023')]
            if not subset_2023.empty:
                subset = subset_2023
            else:
                subset = subset.sort_values(by=col_year_w, ascending=False).head(1)

        if subset.empty:
            raise ValueError(f"[ERROR] Country {c} is missing from WIPO official dataset: {wipo_file}")

        raw_val = subset.iloc[0][col_val_w]
        if pd.isna(raw_val) or raw_val == '':
            raise ValueError(f"[ERROR] WIPO data for country {c} is NaN / missing. Imputation is strictly prohibited.")

        val_float = float(raw_val)
        actual_year = int(subset.iloc[0][col_year_w]) if col_year_w and col_year_w in subset.columns and not pd.isna(subset.iloc[0][col_year_w]) else 2023

        wipo_data.append({
            'country_iso3': c,
            'country_name': country_names_map[c],
            'indicator_id': 'WIPO_PATENT_RES_PM',
            'indicator_name': 'Patent applications by residents per million population',
            'year': actual_year,
            'value': val_float,
            'source': f'WIPO IP Statistics Data Center ({os.path.basename(wipo_file)})'
        })

    with open(os.path.join(raw_dir, 'wipo_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(wipo_data, f, indent=2, ensure_ascii=False)
    pd.DataFrame(wipo_data).to_csv(os.path.join(raw_dir, 'wipo_raw.csv'), index=False, encoding='utf-8')
    print(f"  -> WIPO IP Statistics: {len(wipo_data)} records validated from {os.path.basename(wipo_file)}")
    print("\nData acquisition & official validation completed successfully.")

if __name__ == '__main__':
    fetch_data()
