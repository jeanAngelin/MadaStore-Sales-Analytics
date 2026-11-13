"""Interactive portfolio-ready MadaStore analytics dashboard."""
from pathlib import Path
import sys
import pandas as pd
import plotly.express as px
import streamlit as st
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src'))
from sales_metrics import add_metrics
st.set_page_config(page_title='MadaStore | Sales Analytics',page_icon='📊',layout='wide')
@st.cache_data
def load_data():
 d=pd.read_csv(ROOT/'data/processed/sales_clean.csv',parse_dates=['order_date']); d=add_metrics(d)
 p=pd.read_csv(ROOT/'data/processed/products.csv'); r=pd.read_csv(ROOT/'data/processed/regions.csv'); c=pd.read_csv(ROOT/'data/processed/customers.csv')
 return d.merge(p[['product_id','product_name','category']],on='product_id').merge(r[['region_id','region','city']],on='region_id').merge(c[['customer_id','customer_name']],on='customer_id')
try: data=load_data()
except Exception as e: st.error(f"Données manquantes : exécutez d'abord `python src/generate_data.py` puis `python src/data_cleaning.py`. ({e})"); st.stop()
st.sidebar.title('MadaStore Analytics'); page=st.sidebar.radio('Navigation',['Vue générale','Produits','Régions','Temps','Rentabilité','Qualité','Recommandations'])
st.sidebar.caption('Données entièrement synthétiques • Madagascar • 2024–2025')
years=sorted(data.order_date.dt.year.unique()); selected=st.sidebar.multiselect('Année',years,default=years); cats=sorted(data.category.unique()); selected_cat=st.sidebar.multiselect('Catégorie',cats,default=cats)
d=data[data.order_date.dt.year.isin(selected)&data.category.isin(selected_cat)]
st.title('MadaStore Sales Analytics'); st.caption('Tableau de bord de démonstration — données synthétiques, aucune donnée réelle.')
if page=='Vue générale':
 st.subheader('Vue exécutive')
 cols=st.columns(4); rev=d.net_revenue.sum(); profit=d.profit.sum()
 for col,label,value in zip(cols,['Ventes nettes (MGA)','Bénéfice (MGA)','Commandes','Marge'],[f'{rev:,.0f}',f'{profit:,.0f}',f'{d.order_id.nunique():,}',f'{profit/rev*100 if rev else 0:.1f}%']): col.metric(label,value)
 m=d.assign(Mois=d.order_date.dt.to_period('M').astype(str)).groupby('Mois',as_index=False).net_revenue.sum()
 st.plotly_chart(px.line(m,x='Mois',y='net_revenue',title='Évolution mensuelle des ventes',markers=True),width='stretch')
 a,b=st.columns(2); a.plotly_chart(px.bar(d.groupby('category',as_index=False).net_revenue.sum().sort_values('net_revenue',ascending=False),x='category',y='net_revenue',title='Ventes par catégorie'),width='stretch'); b.plotly_chart(px.bar(d.groupby('region',as_index=False).net_revenue.sum().sort_values('net_revenue',ascending=False),x='region',y='net_revenue',title='Ventes par région'),width='stretch')
elif page=='Produits':
 st.subheader('Analyse des produits'); g=d.groupby(['product_name','category'],as_index=False).agg(Quantité=('quantity','sum'),Ventes=('net_revenue','sum'),Bénéfice=('profit','sum')); st.plotly_chart(px.bar(g.nlargest(10,'Ventes'),x='Ventes',y='product_name',color='category',orientation='h',title='Top produits par ventes'),width='stretch'); st.dataframe(g.sort_values('Bénéfice',ascending=False),width='stretch')
elif page=='Régions':
 st.subheader('Analyse géographique'); g=d.groupby(['region','city'],as_index=False).agg(Commandes=('order_id','nunique'),Ventes=('net_revenue','sum'),Bénéfice=('profit','sum')); st.plotly_chart(px.bar(g.sort_values('Ventes',ascending=False),x='region',y='Ventes',color='Bénéfice'),width='stretch'); st.dataframe(g,width='stretch')
elif page=='Temps':
 st.subheader('Analyse temporelle'); g=d.assign(Mois=d.order_date.dt.to_period('M').astype(str)).groupby('Mois',as_index=False).agg(Ventes=('net_revenue','sum'),Bénéfice=('profit','sum')); st.plotly_chart(px.line(g,x='Mois',y=['Ventes','Bénéfice'],markers=True),width='stretch'); st.dataframe(d.groupby(d.order_date.dt.year).net_revenue.sum().rename('Ventes annuelles'))
elif page=='Rentabilité':
 st.subheader('Analyse des bénéfices'); g=d.groupby('category',as_index=False).agg(Ventes=('net_revenue','sum'),Bénéfice=('profit','sum')); g['Marge %']=g.Bénéfice.div(g.Ventes.replace(0,pd.NA)).fillna(0)*100; st.plotly_chart(px.bar(g,x='category',y='Bénéfice',color='Marge %'),width='stretch'); st.dataframe(g,width='stretch')
elif page=='Qualité':
 st.subheader('Qualité et préparation des données'); st.info('Les fichiers bruts conservent volontairement des anomalies. Les fichiers traités éliminent doublons, dates invalides, quantités manquantes ou non positives et remises hors plage.'); st.json({'lignes affichées':len(d),'valeurs manquantes':int(d.isna().sum().sum()),'commandes uniques':int(d.order_id.nunique()),'lignes dupliquées':int(d.order_id.duplicated().sum())})
else:
 st.subheader('Recommandations commerciales'); g=d.groupby(['product_name','category'],as_index=False).agg(Ventes=('net_revenue','sum'),Bénéfice=('profit','sum'),Unités=('quantity','sum')); reg=d.groupby('region').net_revenue.sum().sort_values(ascending=False); cat=d.groupby('category').net_revenue.sum().sort_values(ascending=False); st.markdown(f"- **Catégorie moteur :** {cat.index[0]} ({cat.iloc[0]:,.0f} MGA de ventes filtrées).\n- **Région en tête :** {reg.index[0]} ({reg.iloc[0]:,.0f} MGA).\n- **Produit le plus vendu :** {g.sort_values('Ventes',ascending=False).iloc[0].product_name}.\n- Confirmer la disponibilité des produits rentables avant les périodes de pointe observées."); st.caption('Les recommandations sont exploratoires et reposent uniquement sur un jeu synthétique.')
st.download_button('Télécharger les données filtrées (CSV)',d.to_csv(index=False).encode('utf-8-sig'),'madastore_filtered.csv','text/csv')
