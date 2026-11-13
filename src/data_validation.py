from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def validate():
 df=pd.read_csv(ROOT/'data/processed/sales_clean.csv')
 p=pd.read_csv(ROOT/'data/processed/products.csv'); c=pd.read_csv(ROOT/'data/processed/customers.csv'); r=pd.read_csv(ROOT/'data/processed/regions.csv')
 return {'sales_rows':len(df),'unique_orders':df.order_id.nunique(),'nulls':int(df.isna().sum().sum()),'unknown_products':int((~df.product_id.isin(p.product_id)).sum()),'unknown_customers':int((~df.customer_id.isin(c.customer_id)).sum()),'unknown_regions':int((~df.region_id.isin(r.region_id)).sum()),'date_min':df.order_date.min(),'date_max':df.order_date.max()}
if __name__=='__main__': print(validate())
