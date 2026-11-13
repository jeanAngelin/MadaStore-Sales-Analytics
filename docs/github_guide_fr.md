# Mettre le projet sur GitHub (Windows)

1. Créez un dépôt public vide nommé `MadaStore-Sales-Analytics` sur GitHub. Ne cochez pas la création automatique d’un README si vous utilisez celui du projet.
2. Dans PowerShell, ouvrez le dossier `MadaStore_Sales_Analytics` placé dans `DATA_ANALYST_PROJECTS`. Vérifiez d’abord les fichiers à publier : `git status --short`.
3. Initialisez et préparez le dépôt :

```powershell
git init
git add .
git status --short
git commit -m "Build MadaStore sales analytics portfolio project"
git branch -M main
git remote add origin https://github.com/jeanAngelin/MadaStore-Sales-Analytics.git
git push -u origin main
```

GitHub vous demandera peut-être de vous connecter dans le navigateur. Ne mettez jamais de mot de passe ou de jeton dans une commande ou dans un fichier. Le fichier `.gitignore` exclut l’environnement Python, les secrets et l’ancien module de portfolio local. Les données du projet sont entièrement synthétiques. Le rapport Power BI est encore en cours de finalisation ; le dossier contient ses instructions et modèles, pas encore le fichier PBIX.
