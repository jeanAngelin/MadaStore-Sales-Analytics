import sys
import sqlite3
from pathlib import Path
import pandas as pd
from openpyxl import load_workbook
from streamlit.testing.v1 import AppTest
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src'))
from sales_metrics import add_metrics, summarize
def test_financial_formulas():
 d=add_metrics(pd.DataFrame([{'order_id':'x','quantity':2,'unit_price':100,'unit_cost':60,'discount_rate':.1}]))
 assert d.iloc[0].gross_revenue==200 and d.iloc[0].discount_amount==20 and d.iloc[0].net_revenue==180 and d.iloc[0].profit==60 and abs(d.iloc[0].profit_margin-100/3)<1e-10
def test_zero_revenue_margin_is_safe():
 d=add_metrics(pd.DataFrame([{'order_id':'x','quantity':0,'unit_price':0,'unit_cost':0,'discount_rate':0}]))
 assert d.iloc[0].profit_margin==0
def test_sales_summary():
 d=pd.DataFrame([{'order_id':'a','quantity':2,'unit_price':100,'unit_cost':60,'discount_rate':.1}])
 assert summarize(d)=={'orders':1,'quantity':2,'revenue':180.0,'profit':60.0,'margin_pct':33.33}
def test_processed_data_and_sqlite_totals_match():
 csv=pd.read_csv(ROOT/'data/processed/sales_clean.csv'); expected=round(summarize(csv)['revenue'],2)
 with sqlite3.connect(ROOT/'database/madastore.db') as con:
  actual=con.execute('SELECT ROUND(SUM(quantity*unit_price*(1-discount_rate)),2) FROM sales').fetchone()[0]
  assert con.execute('PRAGMA foreign_key_check').fetchall()==[]
 assert actual==expected and len(csv)>=5000
def test_excel_workbook_has_expected_sheets():
 wb=load_workbook(ROOT/'reports/MadaStore_Sales_Analysis.xlsx',read_only=True)
 assert wb.sheetnames==['README','Raw_Data','Clean_Data','Sales_Overview','Product_Analysis','Regional_Analysis','Monthly_Analysis','Profit_Analysis']
def test_raw_and_clean_dataset_anomalies_are_handled():
 raw=pd.read_csv(ROOT/'data/raw/sales.csv',dtype=str,keep_default_na=False)
 clean=pd.read_csv(ROOT/'data/processed/sales_clean.csv')
 assert len(raw)==6002 and raw.order_id.duplicated().sum()==2
 assert (raw.quantity=='').sum()==5 and '31/13/2024' in set(raw.order_date)
 assert len(clean)==5993 and clean.isna().sum().sum()==0 and clean.order_id.is_unique
def test_streamlit_dashboard_loads_without_app_errors():
 app=AppTest.from_file(str(ROOT/'dashboard/app.py'),default_timeout=30).run()
 assert not app.exception
