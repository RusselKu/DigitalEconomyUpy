"""
Data processing, normalization, and Digital Readiness Score (DRS) calculation script
Team 3: Agriculture (Mexico, Netherlands, Kenya, Argentina, New Zealand)
"""

import os
import json
import pandas as pd
import numpy as np

def process_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    raw_dir = os.path.join(base_dir, 'data', 'raw')
    proc_dir = os.path.join(base_dir, 'data', 'processed')
    os.makedirs(proc_dir, exist_ok=True)

    # 1. Base Countries
    countries = [
        {'country_iso3': 'MEX', 'country_name': 'Mexico', 'region': 'Latin America', 'income_group': 'Upper-middle income'},
        {'country_iso3': 'NLD', 'country_name': 'Netherlands', 'region': 'Europe', 'income_group': 'High income'},
        {'country_iso3': 'KEN', 'country_name': 'Kenya', 'region': 'Sub-Saharan Africa', 'income_group': 'Lower-middle income'},
        {'country_iso3': 'ARG', 'country_name': 'Argentina', 'region': 'Latin America', 'income_group': 'Upper-middle income'},
        {'country_iso3': 'NZL', 'country_name': 'New Zealand', 'region': 'Asia-Pacific', 'income_group': 'High income'}
    ]
    df_clean = pd.DataFrame(countries)

    # 2. Load World Bank data
    wb_df = pd.read_csv(os.path.join(raw_dir, 'world_bank_raw.csv'))
    
    # Extract the 4 World Bank indicators for 2023
    bbnd = wb_df[(wb_df['indicator_id'] == 'IT.NET.BBND.P2') & (wb_df['year'] == 2023)].set_index('country_iso3')['value']
    secr = wb_df[(wb_df['indicator_id'] == 'IT.NET.SECR.P6') & (wb_df['year'] == 2023)].set_index('country_iso3')['value']
    user = wb_df[(wb_df['indicator_id'] == 'IT.NET.USER.ZS') & (wb_df['year'] == 2023)].set_index('country_iso3')['value']
    ict_serv = wb_df[(wb_df['indicator_id'] == 'BX.GSR.CCIS.ZS') & (wb_df['year'] == 2023)].set_index('country_iso3')['value']
    rd_exp = wb_df[(wb_df['indicator_id'] == 'GB.XPD.RSDV.GD.ZS') & (wb_df['year'] == 2023)].set_index('country_iso3')['value']
    
    # Verified fallbacks for R&D
    rd_fallback = {'MEX': 0.267, 'NLD': 2.267, 'KEN': 0.804, 'ARG': 0.601, 'NZL': 1.548}
    for iso, val in rd_fallback.items():
        if iso not in rd_exp or pd.isna(rd_exp[iso]):
            rd_exp[iso] = val

    # 3. Load ITU, UNCTAD, and WIPO data
    itu_df = pd.read_csv(os.path.join(raw_dir, 'itu_datahub_raw.csv')).set_index('country_iso3')['value']
    unctad_df = pd.read_csv(os.path.join(raw_dir, 'unctad_raw.csv')).set_index('country_iso3')['value']
    wipo_df = pd.read_csv(os.path.join(raw_dir, 'wipo_raw.csv')).set_index('country_iso3')['value']

    # Map to consolidated dataframe
    df_clean['IT_NET_BBND'] = df_clean['country_iso3'].map(bbnd).round(2)
    df_clean['IT_NET_SECR'] = df_clean['country_iso3'].map(secr).round(2)
    df_clean['IT_NET_USER'] = df_clean['country_iso3'].map(user).round(2)
    df_clean['ITU_PRICE_BASKET'] = df_clean['country_iso3'].map(itu_df).round(2)
    df_clean['ICT_SERV_EXP'] = df_clean['country_iso3'].map(ict_serv).round(2)
    df_clean['DIGIT_DELIV_EXP'] = df_clean['country_iso3'].map(unctad_df).round(2)
    df_clean['RD_EXP_GDP'] = df_clean['country_iso3'].map(rd_exp).round(2)
    df_clean['PATENT_RES_PM'] = df_clean['country_iso3'].map(wipo_df).round(2)

    # Save raw processed dataset
    clean_csv_path = os.path.join(proc_dir, 'digital_economy_clean.csv')
    df_clean.to_csv(clean_csv_path, index=False, encoding='utf-8')
    print(f"[OK] Clean processed dataset saved to: {clean_csv_path}")

    # 4. Compute Digital Readiness Score (DRS)
    # Min-Max Normalization to [0, 100]
    indicators = [
        ('IT_NET_BBND', 1),
        ('IT_NET_SECR', 1),
        ('IT_NET_USER', 1),
        ('ITU_PRICE_BASKET', -1), # Inverted: lower cost = higher affordability
        ('ICT_SERV_EXP', 1),
        ('DIGIT_DELIV_EXP', 1),
        ('RD_EXP_GDP', 1),
        ('PATENT_RES_PM', 1)
    ]

    weight = 1.0 / len(indicators) # 0.125 each, sum = 1.0

    drs_scores = np.zeros(len(df_clean))
    norm_data = {}

    for ind, direction in indicators:
        vals = df_clean[ind].values
        min_v, max_v = vals.min(), vals.max()
        
        if direction == 1:
            norm_vals = (vals - min_v) / (max_v - min_v) * 100.0 if max_v != min_v else np.zeros_like(vals)
        else:
            norm_vals = (max_v - vals) / (max_v - min_v) * 100.0 if max_v != min_v else np.zeros_like(vals)
        
        norm_data[f'{ind}_NORM'] = norm_vals.round(2)
        drs_scores += norm_vals * weight

    df_drs = df_clean.copy()
    for col, vals in norm_data.items():
        df_drs[col] = vals
    df_drs['DRS'] = drs_scores.round(2)
    df_drs['DRS_RANK'] = df_drs['DRS'].rank(ascending=False, method='min').astype(int)

    drs_csv_path = os.path.join(proc_dir, 'digital_readiness_score.csv')
    df_drs.to_csv(drs_csv_path, index=False, encoding='utf-8')
    print(f"[OK] DRS calculated and saved to: {drs_csv_path}")

    # Export to JSON for frontend
    dashboard_data = {
        'countries': df_drs.to_dict(orient='records'),
        'metadata': {
            'indicators_count': 8,
            'year': 2023,
            'sector': 'Agriculture & Global Digital Economy',
            'team': 'Team 3'
        }
    }
    with open(os.path.join(base_dir, 'dashboard', 'data.json'), 'w', encoding='utf-8') as f:
        json.dump(dashboard_data, f, indent=2, ensure_ascii=False)
    print(f"[OK] data.json generated for dashboard.")

if __name__ == '__main__':
    process_data()
