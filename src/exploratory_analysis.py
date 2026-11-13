import pandas as pd
from pathlib import Path
from sales_metrics import add_metrics
ROOT=Path(__file__).resolve().parents[1]
def analysis():
 d=add_metrics(pd.read_csv(ROOT/'data/processed/sales_clean.csv',parse_dates=['order_date']))
 d=d.merge(pd.read_csv(ROOT/'data/processed/products.csv')[['product_id','product_name','category']],on='product_id').merge(pd.read_csv(ROOT/'data/processed/regions.csv')[['region_id','region']],on='region_id')
 return {'monthly':d.groupby(d.order_date.dt.to_period('M')).net_revenue.sum(),'products':d.groupby('product_name').agg(revenue=('net_revenue','sum'),profit=('profit','sum'),units=('quantity','sum')).sort_values('revenue',ascending=False),'regions':d.groupby('region').net_revenue.sum().sort_values(ascending=False)}
