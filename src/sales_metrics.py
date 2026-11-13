"""Canonical sales measures shared across project outputs."""
import pandas as pd
def add_metrics(df):
 d=df.copy(); d['gross_revenue']=d.quantity*d.unit_price; d['discount_amount']=d.gross_revenue*d.discount_rate
 d['net_revenue']=d.gross_revenue-d.discount_amount; d['total_cost']=d.quantity*d.unit_cost; d['profit']=d.net_revenue-d.total_cost
 d['profit_margin']=d.profit.div(d.net_revenue.where(d.net_revenue.ne(0))).fillna(0)*100
 return d
def summarize(df):
 d=add_metrics(df); rev=d.net_revenue.sum(); profit=d.profit.sum()
 return {'orders':int(d.order_id.nunique()),'quantity':int(d.quantity.sum()),'revenue':round(float(rev),2),'profit':round(float(profit),2),'margin_pct':round(float(profit/rev*100 if rev else 0),2)}
