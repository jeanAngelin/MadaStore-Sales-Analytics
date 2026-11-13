# MadaStore Sales Analytics

An end-to-end, recruiter-ready data analytics portfolio project built around a fictional Malagasy electronics retailer. **All data are synthetic and for demonstration only; they do not represent actual customers, sales, or business performance.**

## Business question

How can management understand revenue, profit, product mix, geographic performance, seasonality, payment preferences, and sales channels to make better decisions?

## Project highlights

- 6,000 reproducible synthetic transactions across 2024–2025, plus intentionally imperfect raw data and clean analytical data.
- Reusable Python pipeline for generation, cleaning, validation, metrics, SQLite, and Excel export.
- Fifteen documented SQL analyses, including joins, grouping, CTEs, and window functions.
- Interactive Streamlit dashboard with executive, product, regional, time, profitability, data-quality, and recommendation views.
- Authentic screenshots of the running dashboard (desktop and mobile); regeneration instructions are in `screenshots/INDEX.md`.
- Power BI model, DAX measures, query template, and build instructions. Power BI Desktop is now installed and the cleaned Excel table has been imported; report layout and PBIX saving are still in progress.

## Quick start (Windows PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/generate_data.py
python src/data_cleaning.py
python src/data_validation.py
python src/database.py
python src/export_excel.py
streamlit run dashboard/app.py
```

Open `http://localhost:8501` to explore the interactive sales dashboard. The portfolio website is maintained separately from this analytics project.

## Data and definitions

The synthetic source includes 6,000 orders plus documented test anomalies. Clean files reside under `data/processed/`; source files under `data/raw/` are preserved. Monetary values are MGA.

Gross revenue = Quantity × Unit Price. Discount Amount = Gross Revenue × Discount Rate. Net Revenue = Gross Revenue − Discount Amount. Total Cost = Quantity × Unit Cost. Profit = Net Revenue − Total Cost. Profit Margin = Profit ÷ Net Revenue.

## Repository map

See `docs/guide_debutant.md` for the French learner guide, `data/ANOMALIES.md` for cleaning rules, and `powerbi/` for the Power BI build kit. Excel output is generated at `reports/MadaStore_Sales_Analysis.xlsx`; SQLite at `database/madastore.db`.

Optional screenshot tooling is isolated in `requirements-screenshots.txt`; it is not required to run the dashboard.

## Limitations

Synthetic records cannot establish real customer behavior or future performance. Results and recommendations are demonstrations of analytical methods, not claims about a real company. Power BI visuals require Desktop setup by the user. Screenshots are included only when captured from an actually run app; see `screenshots/INDEX.md`.

## GitHub

See [`docs/github_guide_fr.md`](docs/github_guide_fr.md) for the publication steps. This local Git repository is ready to publish from the candidate's GitHub account.

## License

MIT. See `LICENSE`.
