import pandas as pd
from pathlib import Path
from openpyxl import load_workbook
from openpyxl.styles import Font,PatternFill
from openpyxl.chart import BarChart,Reference
from sales_metrics import add_metrics
ROOT=Path(__file__).resolve().parents[1]
def export():
 d=add_metrics(pd.read_csv(ROOT/'data/processed/sales_clean.csv',parse_dates=['order_date']))
 products=pd.read_csv(ROOT/'data/processed/products.csv'); regions=pd.read_csv(ROOT/'data/processed/regions.csv')
 d=d.merge(products[['product_id','product_name','category']],on='product_id').merge(regions[['region_id','region']],on='region_id')
 monthly=d.assign(month=d.order_date.dt.to_period('M').astype(str)).groupby('month',as_index=False).agg(revenue=('net_revenue','sum'),profit=('profit','sum'))
 prod=d.groupby(['product_name','category'],as_index=False).agg(units=('quantity','sum'),revenue=('net_revenue','sum'),profit=('profit','sum'))
 reg=d.groupby('region',as_index=False).agg(revenue=('net_revenue','sum'),profit=('profit','sum'))
 kpi=pd.DataFrame([['Ventes nettes',d.net_revenue.sum()],['Bénéfice',d.profit.sum()],['Commandes',d.order_id.nunique()],['Marge (%)',d.profit.sum()/d.net_revenue.sum()*100]])
 path=ROOT/'reports/MadaStore_Sales_Analysis.xlsx'
 with pd.ExcelWriter(path,engine='openpyxl') as w:
  pd.DataFrame({'MadaStore Sales Analytics':['Dataset synthétique | Période 2024–2025','Tous les montants en Ariary (MGA)','Les données ne représentent aucune entreprise réelle']}).to_excel(w,sheet_name='README',index=False)
  pd.read_csv(ROOT/'data/raw/sales.csv').to_excel(w,sheet_name='Raw_Data',index=False); d.to_excel(w,sheet_name='Clean_Data',index=False); kpi.to_excel(w,sheet_name='Sales_Overview',index=False,header=False); prod.to_excel(w,sheet_name='Product_Analysis',index=False); reg.to_excel(w,sheet_name='Regional_Analysis',index=False); monthly.to_excel(w,sheet_name='Monthly_Analysis',index=False); d[['order_id','net_revenue','total_cost','profit','profit_margin']].to_excel(w,sheet_name='Profit_Analysis',index=False)
 wb=load_workbook(path)
 for ws in wb.worksheets:
  ws.freeze_panes='A2'; ws.auto_filter.ref=ws.dimensions
  for cell in ws[1]: cell.font=Font(color='FFFFFF',bold=True); cell.fill=PatternFill('solid',fgColor='15324B')
  for col in ws.columns:
   letter=col[0].column_letter; ws.column_dimensions[letter].width=min(max(max(len(str(c.value or '')) for c in col)+2,12),32)
 wb.save(path); return path
if __name__=='__main__': print(export())
