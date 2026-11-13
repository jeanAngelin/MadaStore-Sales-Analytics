# Index des captures réelles

Les captures ci-dessous proviennent du dashboard Streamlit exécuté localement (`http://localhost:8501`) et ont été enregistrées avec Playwright le 13 novembre 2026. Toutes les données affichées sont synthétiques. Les PNG absents sont explicitement signalés comme à faire ; les graphiques de `reports/figures/` sont des graphiques exportés, pas des captures d’écran d’applications.

| Dossier / fichier | Description | État |
|---|---|---|
| `07_streamlit/streamlit_home.png` | Dashboard local, vue initiale | Capturé |
| `07_streamlit/streamlit_overview.png` | Vue exécutive et indicateurs | Capturé |
| `07_streamlit/streamlit_product_analysis.png` | Analyse produit | Capturé |
| `07_streamlit/streamlit_regional_analysis.png` | Analyse régionale | Capturé |
| `07_streamlit/streamlit_time_analysis.png` | Analyse temporelle | Capturé |
| `07_streamlit/streamlit_profit_analysis.png` | Analyse des bénéfices | Capturé |
| `07_streamlit/streamlit_data_quality.png` | Contrôles de qualité dans le dashboard | Capturé |
| `07_streamlit/streamlit_recommendations.png` | Recommandations calculées | Capturé |
| `07_streamlit/streamlit_mobile_overview.png` | Dashboard en viewport mobile 390 × 844 | Capturé |
| `01_environment/` | Environnement Windows, versions et dépendances | À capturer |
| `02_data_generation/` | Fichiers générés, aperçu brut et statistiques | À capturer |
| `03_python_analysis/` | Nettoyage, valeurs manquantes et analyse exploratoire | À capturer |
| `04_sql/` | Tables, requêtes et résultats SQL | À capturer |
| `05_excel/` | Synthèse, produits et régions dans Excel | À capturer dans Excel |
| `06_powerbi/` | Vues Power BI | En attente : Power BI Desktop n’est pas installé |
| `08_testing/` | Résultats des tests et validation | À capturer |
| `09_github/` | Dépôt et README GitHub | En attente : aucun dépôt n’a été publié |

## Refaire les captures Streamlit

Avec les dépendances principales installées, démarrez `streamlit run dashboard/app.py`, puis dans une autre fenêtre PowerShell exécutez `python -m pip install -r requirements-screenshots.txt`, `python -m playwright install chromium` et `python src/capture_screenshots.py`. Le script vérifie les pages rendues et remplace les images correspondantes.
