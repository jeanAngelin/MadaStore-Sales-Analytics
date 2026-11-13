"""Capture authentic screenshots of the running MadaStore Streamlit app.

Run after starting the dashboard at http://localhost:8501:
  .venv\\Scripts\\python.exe -m playwright install chromium
  .venv\\Scripts\\python.exe src/capture_screenshots.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "screenshots" / "07_streamlit"
URL = "http://localhost:8501"
PAGES = {
    "streamlit_overview.png": "Vue générale",
    "streamlit_product_analysis.png": "Produits",
    "streamlit_regional_analysis.png": "Régions",
    "streamlit_time_analysis.png": "Temps",
    "streamlit_profit_analysis.png": "Rentabilité",
    "streamlit_data_quality.png": "Qualité",
    "streamlit_recommendations.png": "Recommandations",
}

def capture():
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        response = page.goto(URL, wait_until="networkidle", timeout=60000)
        if not response or response.status != 200:
            raise RuntimeError(f"Dashboard indisponible sur {URL}")
        page.get_by_text("MadaStore Sales Analytics", exact=True).first.wait_for(timeout=30000)
        page.screenshot(path=str(OUT / "streamlit_home.png"), full_page=True)
        for filename, label in PAGES.items():
            page.get_by_role("radio", name=label).check(force=True)
            page.get_by_role("heading", name={
                "Vue générale": "Vue exécutive",
                "Produits": "Analyse des produits",
                "Régions": "Analyse géographique",
                "Temps": "Analyse temporelle",
                "Rentabilité": "Analyse des bénéfices",
                "Qualité": "Qualité et préparation des données",
                "Recommandations": "Recommandations commerciales",
            }[label]).wait_for(timeout=30000)
            page.wait_for_timeout(1200)
            page.screenshot(path=str(OUT / filename), full_page=True)
        page.set_viewport_size({"width": 390, "height": 844})
        page.get_by_role("radio", name="Vue générale").check(force=True)
        page.get_by_role("heading", name="Vue exécutive").wait_for(timeout=30000)
        page.wait_for_timeout(1200)
        page.screenshot(path=str(OUT / "streamlit_mobile_overview.png"), full_page=True)
        browser.close()
    return sorted(p.name for p in OUT.glob("*.png"))

if __name__ == "__main__":
    for name in capture():
        print(name)
