import sqlite3
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def build_database():
 db=ROOT/'database/madastore.db'; db.parent.mkdir(exist_ok=True)
 with sqlite3.connect(db) as con:
  con.executescript((ROOT/'sql/01_create_tables.sql').read_text(encoding='utf-8'))
  for table in ['regions','categories','products','customers','sales']:
   df=pd.read_csv(ROOT/f'data/processed/{"sales_clean" if table=="sales" else table}.csv'); df.to_sql(table,con,if_exists='append',index=False)
 return db
if __name__=='__main__': print(build_database())
