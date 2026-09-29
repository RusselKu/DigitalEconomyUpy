"""
Script de procesamiento, normalización y cálculo del Digital Readiness Score (DRS)
Equipo 3: Agricultura (México, Países Bajos, Kenia, Argentina, Nueva Zelanda)
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
        {'country_iso3': 'MEX', 'country_name': 'México', 'region': 'América Latina', 'income_group': 'Upper-middle income'},
        {'country_iso3': 'NLD', 'country_name': 'Países Bajos', 'region': 'Europa', 'income_group': 'High income'},
        {'country_iso3': 'KEN', 'country_name': 'Kenia', 'region': 'África Subsahariana', 'income_group': 'Lower-middle income'},
        {'country_iso3': 'ARG', 'country_name': 'Argentina', 'region': 'América Latina', 'income_group': 'Upper-middle income'},
        {'country_iso3': 'NZL', 'country_name': 'Nueva Zelanda', 'region': 'Asia-Pacífico', 'income_group': 'High income'}
    ]
    df_clean = pd.DataFrame(countries)

    # 2. Cargar World Bank data
    wb_df = pd.read_csv(os.path.join(raw_dir, 'world_bank_raw.csv'))
    
    # Extraer los 4 indicadores del Banco Mundial más recientes (2023)
    # Suscripciones banda ancha fija
    bbnd = wb_df[(wb_df['indicator_id'] == 'IT.NET.BBND.P2') & (wb_df['year'] == 2023)].set_index('country_iso3')['value']
    # Servidores seguros
    secr = wb_df[(wb_df['indicator_id'] == 'IT.NET.SECR.P6') & (wb_df['year'] == 2023)].set_index('country_iso3')['value']
    # Usuarios de internet
    user = wb_df[(wb_df['indicator_id'] == 'IT.NET.USER.ZS') & (wb_df['year'] == 2023)].set_index('country_iso3')['value']
    # Exportaciones de servicios TIC (% exportaciones de servicios)
    ict_serv = wb_df[(wb_df['indicator_id'] == 'BX.GSR.CCIS.ZS') & (wb_df['year'] == 2023)].set_index('country_iso3')['value']
    # Gasto en I+D (% PIB) - Para NZL/ARG se toma el valor consolidado más reciente verificado
    rd_exp = wb_df[(wb_df['indicator_id'] == 'GB.XPD.RSDV.GD.ZS') & (wb_df['year'] == 2023)].set_index('country_iso3')['value']
    
    # Completar I+D si faltaba en el año exacto 2023 con último reporte oficial
    rd_fallback = {'MEX': 0.267, 'NLD': 2.267, 'KEN': 0.804, 'ARG': 0.601, 'NZL': 1.548}
    for iso, val in rd_fallback.items():
        if iso not in rd_exp or pd.isna(rd_exp[iso]):
            rd_exp[iso] = val

    # 3. Cargar ITU, UNCTAD y WIPO
    itu_df = pd.read_csv(os.path.join(raw_dir, 'itu_datahub_raw.csv')).set_index('country_iso3')['value']
    unctad_df = pd.read_csv(os.path.join(raw_dir, 'unctad_raw.csv')).set_index('country_iso3')['value']
    wipo_df = pd.read_csv(os.path.join(raw_dir, 'wipo_raw.csv')).set_index('country_iso3')['value']

    # Mapear al dataframe consolidado
    df_clean['IT_NET_BBND'] = df_clean['country_iso3'].map(bbnd).round(2)
    df_clean['IT_NET_SECR'] = df_clean['country_iso3'].map(secr).round(2)
    df_clean['IT_NET_USER'] = df_clean['country_iso3'].map(user).round(2)
    df_clean['ITU_PRICE_BASKET'] = df_clean['country_iso3'].map(itu_df).round(2)
    df_clean['ICT_SERV_EXP'] = df_clean['country_iso3'].map(ict_serv).round(2)
    df_clean['DIGIT_DELIV_EXP'] = df_clean['country_iso3'].map(unctad_df).round(2)
    df_clean['RD_EXP_GDP'] = df_clean['country_iso3'].map(rd_exp).round(2)
    df_clean['PATENT_RES_PM'] = df_clean['country_iso3'].map(wipo_df).round(2)

    # Guardar dataset limpio sin normalizar
    clean_csv_path = os.path.join(proc_dir, 'digital_economy_clean.csv')
    df_clean.to_csv(clean_csv_path, index=False, encoding='utf-8')
    print(f"[OK] Dataset procesado guardado en: {clean_csv_path}")
    print(df_clean[['country_name', 'IT_NET_BBND', 'IT_NET_SECR', 'IT_NET_USER', 'ITU_PRICE_BASKET', 'ICT_SERV_EXP', 'DIGIT_DELIV_EXP', 'RD_EXP_GDP', 'PATENT_RES_PM']])

    # 4. Cálculo del Digital Readiness Score (DRS)
    # Min-Max Normalization a escala [0, 100]
    # Indicadores positivos: (x - min) / (max - min) * 100
    # Indicadores inversos (ITU_PRICE_BASKET): (max - x) / (max - min) * 100
    indicators = [
        ('IT_NET_BBND', 1),
        ('IT_NET_SECR', 1),
        ('IT_NET_USER', 1),
        ('ITU_PRICE_BASKET', -1), # Inverso: menor costo = mayor asequibilidad = mejor calificación
        ('ICT_SERV_EXP', 1),
        ('DIGIT_DELIV_EXP', 1),
        ('RD_EXP_GDP', 1),
        ('PATENT_RES_PM', 1)
    ]

    weight = 1.0 / len(indicators) # 0.125 cada uno, suma = 1.0

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
    print(f"\n[OK] DRS calculado y guardado en: {drs_csv_path}")
    print(df_drs[['country_name', 'DRS', 'DRS_RANK']].sort_values(by='DRS_RANK'))

    # Exportar también a JSON para el dashboard interactivo
    dashboard_data = {
        'countries': df_drs.to_dict(orient='records'),
        'metadata': {
            'indicators_count': 8,
            'year': 2023,
            'sector': 'Agricultura y Economía Digital Global',
            'team': 'Equipo 3'
        }
    }
    with open(os.path.join(base_dir, 'dashboard', 'data.json'), 'w', encoding='utf-8') as f:
        json.dump(dashboard_data, f, indent=2, ensure_ascii=False)
    print(f"[OK] data.json generado para el dashboard.")

if __name__ == '__main__':
    process_data()
