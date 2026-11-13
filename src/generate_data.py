"""Generate reproducible synthetic MadaStore sales data (2024–2025)."""
from __future__ import annotations
import csv, random
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RNG = random.Random(20261113)
CATEGORIES = ["Ordinateurs", "Smartphones", "Impression", "Accessoires", "Réseau", "Stockage"]
PRODUCTS = [
 ("LAP-14", "Laptop Pro 14", "Ordinateurs", 3200000, 2350000), ("LAP-15", "Laptop Essentiel 15", "Ordinateurs", 2450000, 1800000),
 ("PHN-A1", "Smartphone A1", "Smartphones", 1150000, 790000), ("PHN-P2", "Smartphone P2", "Smartphones", 1850000, 1320000),
 ("PRN-E1", "Imprimante Eco E1", "Impression", 780000, 525000), ("PRN-L2", "Imprimante Laser L2", "Impression", 1450000, 1030000),
 ("ACC-M1", "Souris sans fil", "Accessoires", 95000, 42000), ("ACC-K2", "Clavier USB", "Accessoires", 125000, 58000),
 ("ACC-H3", "Casque audio", "Accessoires", 210000, 112000), ("NET-R1", "Routeur Wi-Fi", "Réseau", 390000, 245000),
 ("NET-S2", "Switch 8 ports", "Réseau", 520000, 348000), ("STO-1T", "Disque externe 1 To", "Stockage", 310000, 198000),
 ("STO-SSD", "SSD 512 Go", "Stockage", 360000, 222000), ("LAP-GM", "Laptop Graphique", "Ordinateurs", 4850000, 3650000)]
REGIONS = [("Analamanga", "Antananarivo"), ("Atsinanana", "Toamasina"), ("Boeny", "Mahajanga"), ("Diana", "Antsiranana"), ("Haute Matsiatra", "Fianarantsoa"), ("Vakinankaratra", "Antsirabe"), ("Atsimo-Andrefana", "Toliara"), ("Sava", "Sambava")]
PAYMENTS = ["Mobile Money", "Carte bancaire", "Espèces", "Virement"]
CHANNELS = ["Magasin", "En ligne", "Téléphone"]

def write_csv(path, rows, fields):
 path.parent.mkdir(parents=True, exist_ok=True)
 with path.open("w", newline="", encoding="utf-8-sig") as f:
  w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

def generate(n=6000, anomalies=True):
 out=ROOT/'data'/'synthetic'; clean=ROOT/'data'/'processed'; raw=ROOT/'data'/'raw'
 category_ids={name:f'CAT{i:02}' for i,name in enumerate(CATEGORIES,1)}
 products=[dict(product_id=x[0],product_name=x[1],category=x[2],category_id=category_ids[x[2]],unit_price=x[3],unit_cost=x[4]) for x in PRODUCTS]
 regions=[dict(region_id=f'R{i:02}',region=x[0],city=x[1]) for i,x in enumerate(REGIONS,1)]
 customers=[dict(customer_id=f'C{i:04}',customer_name=f'Client {i:04}',region_id=f'R{RNG.randint(1,len(REGIONS)):02}') for i in range(1,1001)]
 write_csv(out/'products.csv',products,list(products[0])); write_csv(out/'categories.csv',[dict(category_id=f'CAT{i:02}',category=x) for i,x in enumerate(CATEGORIES,1)],['category_id','category']); write_csv(out/'regions.csv',regions,list(regions[0])); write_csv(out/'customers.csv',customers,list(customers[0]))
 rows=[]; start=date(2024,1,1); days=730
 for i in range(1,n+1):
  prod=RNG.choice(PRODUCTS); cust=RNG.choice(customers); q=RNG.choices([1,2,3,4,5],[42,32,15,8,3])[0]
  when=start+timedelta(days=RNG.randrange(days)); discount=RNG.choices([0,.05,.10,.15,.20],[45,25,18,9,3])[0]
  rows.append(dict(order_id=f'ORD{i:06}',order_date=when.isoformat(),customer_id=cust['customer_id'],product_id=prod[0],region_id=cust['region_id'],quantity=q,unit_price=prod[3],unit_cost=prod[4],discount_rate=discount,payment_method=RNG.choice(PAYMENTS),sales_channel=RNG.choice(CHANNELS)))
 clean_rows=[r.copy() for r in rows]
 write_csv(out/'sales.csv',rows,list(rows[0])); write_csv(clean/'sales_clean.csv',clean_rows,list(rows[0])); write_csv(clean/'products.csv',products,list(products[0])); write_csv(clean/'customers.csv',customers,list(customers[0])); write_csv(clean/'regions.csv',regions,list(regions[0])); write_csv(clean/'categories.csv',[dict(category_id=f'CAT{i:02}',category=x) for i,x in enumerate(CATEGORIES,1)],['category_id','category'])
 if anomalies:
  dirty=[r.copy() for r in rows]
  for r in dirty[:5]: r['quantity']='' # missing values
  dirty[5]['order_date']='31/13/2024'; dirty[6]['discount_rate']='1.5'; dirty.extend([dirty[10].copy(),dirty[20].copy()])
  write_csv(raw/'sales.csv',dirty,list(rows[0]))
  for name,arr in [('products',products),('customers',customers),('regions',regions),('categories',[dict(category_id=f'CAT{i:02}',category=x) for i,x in enumerate(CATEGORIES,1)])]: write_csv(raw/f'{name}.csv',arr,list(arr[0]))
 else:
  for name,arr in [('sales',rows),('products',products),('customers',customers),('regions',regions)]: write_csv(raw/f'{name}.csv',arr,list(arr[0]))
 return {'orders':len(rows),'raw_rows':len(rows)+(2 if anomalies else 0),'products':len(products),'customers':len(customers)}

if __name__=='__main__': print(generate())
