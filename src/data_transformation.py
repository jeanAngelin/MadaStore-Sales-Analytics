import pandas as pd
from pathlib import Path
from sales_metrics import add_metrics
ROOT=Path(__file__).resolve().parents[1]
def transform():
 d=pd.read_csv(ROOT/'data/processed/sales_clean.csv',parse_dates=['order_date']); m=add_metrics(d)
 m.to_csv(ROOT/'data/processed/sales_analysis.csv',index=False,encoding='utf-8-sig'); return m
