# Guide de prise en main (français)

## Lancer le projet

Dans PowerShell, ouvrez le dossier du projet, puis lancez `python -m venv .venv`, `.venv\Scripts\Activate.ps1`, `python -m pip install -r requirements.txt`, `python src/generate_data.py`, `python src/data_cleaning.py`, `python src/database.py`, `python src/export_excel.py`, enfin `streamlit run dashboard/app.py`.

## Portfolio et administration

Lancez `streamlit run portfolio/app.py --server.port 8502` pour le portfolio. L’admin est dans l’application dashboard, menu « Portfolio Admin ». Elle met à jour `portfolio/content.json`. Cette édition est faite pour un usage local; ne déployez pas une page d’administration exposée publiquement sans authentification et stockage adaptés. Remplacez les champs de profil par vos informations réelles avant publication.

## Mesures métier

Ventes brutes = quantité × prix unitaire. Remise = ventes brutes × taux de remise. Ventes nettes = ventes brutes − remise. Coût = quantité × coût unitaire. Bénéfice = ventes nettes − coût. Marge = bénéfice ÷ ventes nettes. La devise utilisée dans le jeu synthétique est l’Ariary malgache (MGA).

## Données et confidentialité

Les fichiers dans `data/raw/` contiennent des défauts volontaires. Ne les corrigez pas manuellement : relancez le nettoyage. Aucun fichier ne décrit de vraies transactions, personnes ou entreprises. Les anomalies exercées sont documentées dans `data/ANOMALIES.md`.
