"""Export static presentation charts from the processed synthetic dataset."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from sales_metrics import add_metrics
ROOT=Path(__file__).resolve().parents[1]
def create():
 out=ROOT/'reports/figures'; out.mkdir(exist_ok=True)
 d=add_metrics(pd.read_csv(ROOT/'data/processed/sales_clean.csv',parse_dates=['order_date']))
 products=pd.read_csv(ROOT/'data/processed/products.csv'); regions=pd.read_csv(ROOT/'data/processed/regions.csv')
 d=d.merge(products[['product_id','product_name','category']],on='product_id').merge(regions[['region_id','region']],on='region_id')
 monthly=d.assign(month=d.order_date.dt.to_period('M').astype(str)).groupby('month').net_revenue.sum()
 annual=d.assign(year=d.order_date.dt.year).groupby('year').net_revenue.sum()
 charts=[(monthly,'Ventes mensuelles — données synthétiques','Mois','MGA','monthly_revenue.png'),(d.groupby('category').profit.sum().sort_values(), 'Bénéfices par catégorie — données synthétiques','Catégorie','MGA','category_profit.png'),(d.groupby('region').net_revenue.sum().sort_values(), 'Ventes par région — données synthétiques','Région','MGA','regional_revenue.png'),(d.groupby('product_name').quantity.sum().nlargest(10).sort_values(), 'Top 10 produits par unités — données synthétiques','Produit','Unités','top_products.png')]
 for series,title,xlabel,ylabel,name in charts:
  fig,ax=plt.subplots(figsize=(10,5)); series.plot(kind='bar' if len(series)<30 else 'line',ax=ax,color='#137c8b'); ax.set_title(title); ax.set_xlabel(xlabel); ax.set_ylabel(ylabel); ax.grid(axis='y',alpha=.2); fig.tight_layout(); fig.savefig(out/name,dpi=160); plt.close(fig)
 return out
if __name__=='__main__': print(create())
