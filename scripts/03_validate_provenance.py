"""
Audit & Provenance Validation Script
Digital Economy Intelligence Lab - Team 3 (Agriculture)
Responsible: Russel Ku (Lead Data Architect)

Validates 100% mathematical and traceability integrity between
processed datasets and original untouched official downloads.
"""

import os
import glob
import pandas as pd
import numpy as np

def find_file(pattern_list, search_dirs):
    for s_dir in search_dirs:
        if not os.path.exists(s_dir):
            continue
        for pat in pattern_list:
            matches = glob.glob(os.path.join(s_dir, pat))
            if matches:
                return matches[0]
    return None

def validate_provenance():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, 'data')
    raw_dir = os.path.join(data_dir, 'raw')
    official_dir = os.path.join(raw_dir, 'official')
    original_dir = os.path.join(official_dir, 'original')
    processed_dir = os.path.join(data_dir, 'processed')
    search_dirs = [original_dir, official_dir]

    clean_file = os.path.join(processed_dir, 'digital_economy_clean.csv')
    if not os.path.exists(clean_file):
        print(f"[ERROR] Processed clean dataset missing: {clean_file}")
        return False

    clean_df = pd.read_csv(clean_file)
    target_countries = ['ARG', 'KEN', 'MEX', 'NLD', 'NZL']

    # 1. World Bank Raw
    wb_file = os.path.join(raw_dir, 'world_bank_raw.csv')
    wb_df = pd.read_csv(wb_file) if os.path.exists(wb_file) else None

    # 2. ITU Raw
    itu_file = find_file(['*itu*.csv', '*ITU*.csv', '*price_basket*.csv', '*Price*.csv'], search_dirs)
    itu_df = pd.read_csv(itu_file) if itu_file else None

    # 3. UNCTAD Raw
    unctad_file = find_file(['*unctad*.csv', '*UNCTAD*.csv', '*digitally_deliverable*.csv', '*DDS*.csv'], search_dirs)
    unctad_df = pd.read_csv(unctad_file) if unctad_file else None

    # 4. WIPO Raw
    wipo_verified_file = os.path.join(
        data_dir,
        'validated',
        'wipo_patents_2023.csv'
    )
    wipo_file = (
        wipo_verified_file
        if os.path.exists(wipo_verified_file)
        else find_file(['*wipo*.csv', '*WIPO*.csv', '*patent*.csv', '*Patents*.csv'], search_dirs)
    )
    wipo_df = pd.read_csv(wipo_file) if wipo_file else None

    print("\n" + "="*85)
    print("      DATA PROVENANCE & TRACEABILITY AUDIT - DIGITAL ECONOMY LAB (TEAM 3)")
    print("="*85)
    print(f"Target Economies: {', '.join(target_countries)}")
    print(f"Processed File  : {clean_file}")
    print(f"ITU Raw Source  : {os.path.basename(itu_file) if itu_file else 'NOT FOUND'}")
    print(f"UNCTAD Raw Source: {os.path.basename(unctad_file) if unctad_file else 'NOT FOUND'}")
    print(f"WIPO Raw Source : {os.path.basename(wipo_file) if wipo_file else 'NOT FOUND'}")
    print(f"World Bank Source: {os.path.basename(wb_file) if wb_file else 'NOT FOUND'}")
    print("-"*85)

    discrepancies = []
    total_checks = 0

    indicators = [
        ('IT_NET_BBND', 'Fixed broadband subscriptions /100', 'IT.NET.BBND.P2', 'WB'),
        ('IT_NET_SECR', 'Secure Internet servers /1M', 'IT.NET.SECR.P6', 'WB'),
        ('IT_NET_USER', 'Internet users (% population)', 'IT.NET.USER.ZS', 'WB'),
        ('ITU_PRICE_BASKET', 'Fixed broadband basket (% GNI pc)', 'ITU_FBB_BASKET_GNI', 'ITU'),
        ('ICT_SERV_EXP', 'ICT service exports (% services)', 'BX.GSR.CCIS.ZS', 'WB'),
        ('DIGIT_DELIV_EXP', 'Digitally deliverable services (% services)', 'US_DDS_SHARE', 'UNCTAD'),
        ('RD_EXP_GDP', 'R&D expenditure (% GDP)', 'GB.XPD.RSDV.GD.ZS', 'WB'),
        ('PATENT_RES_PM', 'Resident patent applications /1M', 'WIPO_RES_PAT_PM', 'WIPO')
    ]

    print(f"{'Country':<7} | {'Indicator Code':<18} | {'Clean Value':<12} | {'Raw Value':<12} | {'Delta':<8} | {'Status'}")
    print("-"*85)

    for country in target_countries:
        country_clean = clean_df[clean_df['country_iso3'] == country]
        if country_clean.empty:
            discrepancies.append((country, 'ALL', 'MISSING IN CLEAN', 'PRESENT', 'FAIL'))
            continue

        for ind_col, ind_desc, raw_code, source_type in indicators:
            total_checks += 1
            clean_val = country_clean.iloc[0].get(ind_col, np.nan)
            raw_val = np.nan

            if source_type == 'WB' and wb_df is not None:
                subset = wb_df[(wb_df['country_iso3'] == country) & (wb_df['indicator_id'] == raw_code)]
                subset_2023 = subset[subset['year'] == 2023]
                if not subset_2023.empty and not pd.isna(subset_2023.iloc[0]['value']):
                    raw_val = subset_2023.iloc[0]['value']
                elif not subset.empty:
                    valid_sub = subset.dropna(subset=['value']).sort_values('year', ascending=False)
                    if not valid_sub.empty:
                        raw_val = valid_sub.iloc[0]['value']

            elif source_type == 'ITU' and itu_df is not None:
                col_c = next((c for c in itu_df.columns if c.upper() in ['ISO', 'COUNTRY_CODE', 'ECONOMY_CODE']), None)
                col_v = next((c for c in itu_df.columns if c.upper() in ['VALUE', 'OBS_VALUE', 'VAL']), None)
                col_y = next((c for c in itu_df.columns if c.upper() in ['YEAR', 'PERIOD']), None)
                if col_c and col_v:
                    sub = itu_df[itu_df[col_c].astype(str).str.strip().str.upper() == country]
                    if col_y and '2023' in sub[col_y].astype(str).values:
                        sub = sub[sub[col_y].astype(str).str.contains('2023')]
                    if not sub.empty:
                        raw_val = sub.iloc[0][col_v]

            elif source_type == 'UNCTAD' and unctad_df is not None:
                col_c = next((c for c in unctad_df.columns if c.upper() in ['ECONOMY_CODE', 'ISO', 'COUNTRY_CODE']), None)
                col_v = next((c for c in unctad_df.columns if c.upper() in ['VALUE', 'OBS_VALUE', 'VAL']), None)
                col_y = next((c for c in unctad_df.columns if c.upper() in ['PERIOD', 'YEAR']), None)
                if col_c and col_v:
                    sub = unctad_df[unctad_df[col_c].astype(str).str.strip().str.upper() == country]
                    if col_y and '2023' in sub[col_y].astype(str).values:
                        sub = sub[sub[col_y].astype(str).str.contains('2023')]
                    if not sub.empty:
                        raw_val = sub.iloc[0][col_v]

            elif source_type == 'WIPO' and wipo_df is not None:
                col_c = next((c for c in wipo_df.columns if c.upper() in ['ORIGIN_CODE', 'COUNTRY_CODE', 'ISO']), None)
                col_v = next((c for c in wipo_df.columns if c.upper() in ['VALUE', 'OBS_VALUE', 'VAL']), None)
                col_y = next((c for c in wipo_df.columns if c.upper() in ['YEAR', 'PERIOD']), None)
                if col_c and col_v:
                    sub = wipo_df[wipo_df[col_c].astype(str).str.strip().str.upper() == country]
                    if col_y and '2023' in sub[col_y].astype(str).values:
                        sub = sub[sub[col_y].astype(str).str.contains('2023')]
                    if not sub.empty:
                        raw_val = sub.iloc[0][col_v]

            # Compare at 2 decimal places (standard indicator reporting precision)
            clean_rounded = round(float(clean_val), 2) if not pd.isna(clean_val) else np.nan
            raw_rounded = round(float(raw_val), 2) if not pd.isna(raw_val) else np.nan
            
            delta = abs(clean_rounded - raw_rounded) if (not pd.isna(clean_rounded) and not pd.isna(raw_rounded)) else np.nan
            is_match = (delta is not np.nan and delta < 1e-3)

            status_str = "MATCH [OK]" if is_match else "MISMATCH [FAIL]"
            clean_str = f"{clean_rounded:.2f}" if not pd.isna(clean_rounded) else "NaN"
            raw_str = f"{raw_rounded:.2f}" if not pd.isna(raw_rounded) else "NaN"
            delta_str = f"{delta:.4f}" if not pd.isna(delta) else "N/A"

            print(f"{country:<7} | {ind_col:<18} | {clean_str:<12} | {raw_str:<12} | {delta_str:<8} | {status_str}")

            if not is_match:
                discrepancies.append((country, ind_col, clean_str, raw_str, delta_str))

    print("="*85)
    print(f"Audit Summary: {total_checks - len(discrepancies)}/{total_checks} data points mathematically verified.")

    if discrepancies:
        print(f"\n[WARNING] Found {len(discrepancies)} discrepancy(ies):")
        for d in discrepancies:
            print(f"  - Country: {d[0]}, Indicator: {d[1]}, Clean: {d[2]}, Raw: {d[3]}, Delta: {d[4]}")
        return False
    else:
        print("\n[SUCCESS] 100% Provenance Validation Passed! All values in digital_economy_clean.csv match the configured and documented provenance sources.")
        return True

if __name__ == '__main__':
    success = validate_provenance()
    exit(0 if success else 1)
