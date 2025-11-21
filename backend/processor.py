import pandas as pd
from pathlib import Path
import re
import numpy as np

IDX_DATE = 0
IDX_DAY  = 1
IDX_OCC  = 11
IDX_REV  = 13
IDX_PRICE= 14

def clean_numeric_series(s: pd.Series) -> pd.Series:
    s = s.astype(str).replace({'nan':'', 'None':''})
    s = s.str.replace(r'[^\d\-,\.]', '', regex=True)
    s = s.str.replace(r'\s+', '', regex=True)
    has_comma = s.str.contains(',', regex=False)
    has_dot = s.str.contains('.', regex=True)
    s = s.where(~(has_comma & ~has_dot), s.str.replace('.', '').str.replace(',', '.'))
    s = s.str.replace(',', '.', regex=False)
    return pd.to_numeric(s, errors='coerce')

def read_and_extract(path):
    path = Path(path)
    df = pd.read_excel(path, sheet_name=0)
    def col_or_none(df, idx):
        return df.iloc[:, idx] if idx < df.shape[1] else pd.Series([pd.NA]*len(df))
    date_col = col_or_none(df, IDX_DATE)
    day_col  = col_or_none(df, IDX_DAY)
    occ_col  = col_or_none(df, IDX_OCC)
    rev_col  = col_or_none(df, IDX_REV)
    price_col= col_or_none(df, IDX_PRICE)

    dates = pd.to_datetime(date_col, errors='coerce', dayfirst=True)
    weekday_en = dates.dt.day_name()
    map_en_pt = {
        'Monday':'segunda-feira','Tuesday':'terça-feira','Wednesday':'quarta-feira',
        'Thursday':'quinta-feira','Friday':'sexta-feira','Saturday':'sábado','Sunday':'domingo'
    }
    weekday_pt = weekday_en.map(map_en_pt)

    occ = clean_numeric_series(occ_col)
    price = clean_numeric_series(price_col)
    rev = clean_numeric_series(rev_col)

    proc = pd.DataFrame({
        'source_file': path.name,
        'date': dates,
        'day_from_colB': day_col.astype(str),
        'weekday': weekday_pt,
        'occupancy_pct': occ,
        'avg_price': price,
        'total_revenue': rev
    })

    proc['flag_invalid_price'] = proc['avg_price'].apply(lambda x: True if pd.isna(x) or x <= 0 else False)
    proc['flag_invalid_occupancy'] = proc['occupancy_pct'].apply(lambda x: True if pd.isna(x) or (x<0) or (x>150) else False)
    return proc

def aggregate_by_date_type(df_proc, type_name):
    df = df_proc.copy()
    df['type'] = type_name
    summary = df.groupby(['date','type'], dropna=True).agg(
        occupancy_mean=('occupancy_pct','mean'),
        avg_price_mean=('avg_price','mean'),
        revenue_sum=('total_revenue','sum'),
        n_obs=('date','count')
    ).reset_index().sort_values(['type','date'])
    return summary
