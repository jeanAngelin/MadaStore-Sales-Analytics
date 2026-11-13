"""Validate and clean raw CSV files while preserving them unchanged."""
import pandas as pd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def clean_sales(source=None, target=None):
 source=Path(source or ROOT/'data/raw/sales.csv'); target=Path(target or ROOT/'data/processed/sales_clean.csv')
 df=pd.read_csv(source)
 before=len(df); df=df.drop_duplicates(subset=['order_id']).copy(); removed_duplicates=before-len(df); df['order_date']=pd.to_datetime(df.order_date,errors='coerce',format='mixed')
 df['quantity']=pd.to_numeric(df.quantity,errors='coerce'); df['discount_rate']=pd.to_numeric(df.discount_rate,errors='coerce')
 df=df.dropna(subset=['order_date','quantity']); df=df[(df.quantity>0)&df.discount_rate.between(0,0.5)].copy()
 for c in ['unit_price','unit_cost']: df[c]=pd.to_numeric(df[c],errors='coerce')
 df=df.dropna(subset=['unit_price','unit_cost']); df['order_date']=df.order_date.dt.strftime('%Y-%m-%d')
 df.to_csv(target,index=False,encoding='utf-8-sig')
 return {'raw_rows':before,'clean_rows':len(df),'duplicates_removed':removed_duplicates,'rows_removed_total':before-len(df)}
if __name__=='__main__': print(clean_sales())
