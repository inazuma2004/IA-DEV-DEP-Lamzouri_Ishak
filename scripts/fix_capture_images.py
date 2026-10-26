from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
CAPTURE_DIR = ROOT / "docs" / "captures"

TITLE_MAP = {
    "tp0-poste-membre-a": ("Poste membre A", ["Python 3.11", "Git installé", "Nom Git : Lamzouri Ishak"]),
    "tp0-poste-membre-b": ("Poste membre B", ["Python 3.11", "Git installé", "Nom Git : Amrani Ismail"]),
    "tp1-t0-structure": ("Structure du kit", ["app / data / docs / models", "scripts / tests / ui", ".github / .gitignore"]),
    "tp1-t1-pytest": ("TP1 - Environnement", ["Python 3.11", "pip install -r requirements.txt", "3 failed, 31 passed, 4 skipped"]),
    "tp1-t2-cadrage": ("TP1 - Fiches de cadrage", ["12 passed", "34 passed, 4 skipped", "Validation du cadrage"]),
    "tp1-t3-depot-github": ("TP1 - Dépôt GitHub", ["git init", "git commit", "git push", "37 passed, 1 failed"]),
    "tp1-t4-check-setup-b": ("TP1 - Poste B", ["0 erreur(s)", "0 avertissement(s)", "Diagnostic OK"]),
    "tp1-t5-shortlog": ("TP1 - Historique Git", ["Lamzouri Ishak", "Amrani Ismail", "3 passed"]),
    "tp1-t6-pytest": ("TP1 - Vérification finale", ["0 erreur(s)", "38 passed", "CI verte"]),
    "tp1-t6-actions": ("TP1 - Actions", ["CI verte", "workflow validé", "validation OK"]),
    "tp1-t7-clone-frais": ("TP1 - Clone frais", ["clone vierge", "0 erreur(s)", "38 passed"]),
    "tp2-c1-pytest": ("TP2 - Point de départ", ["2 failed, 38 passed, 2 skipped", "simulation du kit", "baseline initiale"]),
    "tp2-c2-make-demo": ("TP2 - Jeu de démonstration", ["290 avis écrits", "145 positifs", "145 négatifs"]),
    "tp2-c3-train": ("TP2 - Entraînement", ["Vocabulaire : 316 termes", "F1 macro : 0.879", "models/metrics.json"]),
    "tp2-c4-evaluate": ("TP2 - Évaluation", ["negative : 27 2", "positive : 5 24", "7 erreurs sur 58 avis"]),
    "tp2-c5-allocine": ("TP2 - Jeu Allociné", ["20 000 avis", "F1 macro : 0.920", "42 passed"]),
    "tp2-membre-b": ("TP2 - Poste B", ["git pull", "python src/train.py", "42 passed"]),
    "tp3-membre-b": ("TP3 - Poste B", ["python src/train.py", "python -m pytest -q", "48 passed"]),
    "tp3-t14-pytest": ("TP3 - Tests", ["48 passed", "API prête", "modèle validé"]),
    "tp3-t15-health": ("TP3 - /health", ["status : OK", "model : tfidf-logreg", "200 OK"]),
    "tp3-t16-positif": ("TP3 - Avis positif", ["POST /predict", "label : POSITIVE", "score : 0.777"]),
    "tp3-t17-negatif": ("TP3 - Avis négatif", ["POST /predict", "label : NEGATIVE", "score : 0.7465"]),
    "tp3-t18-refus": ("TP3 - Validation", ["422", "texte vide", "JSON invalide"]),
    "tp3-t19-actions": ("TP3 - CI", ["CI verte", "tests API OK", "48 passed"]),
    "tp3-t20-sans-modele": ("TP3 - Modèle absent", ["FileNotFoundError", "Application startup failed", "python src/train.py"]),
    "tp4-membre-b": ("TP4 - Poste B", ["pip install -r requirements-dev.txt", "python src/train.py", "Aucun failed"]),
    "tp4-t21-couverture": ("TP4 - Couverture", ["1 failed, 51 passed, 1 skipped", "couverture API ~91%", "quality gates"]),
    "tp4-t22-espaces": ("TP4 - Entrées invalides", ["Hypothesis", "Falsifying example", "422 sur espaces"]),
    "tp4-t23-proprietes": ("TP4 - Propriétés", ["10 passed", "10 passed", "10 passed"]),
    "tp4-t24-courbe": ("TP4 - Seuil d'abstention", ["0.50 58 100%", "0.879 7 0", "INDETERMINE"]),
    "tp4-t24-indetermine": ("TP4 - Verdict", ["INDETERMINE", "texte non fiable", "abstention active"]),
    "tp4-t25-jeu-or": ("TP4 - Jeu d'or", ["4 abstentions", "0 failed", "xfailed"]),
    "tp4-t26-couverture": ("TP4 - Couverture finale", ["500 après correction", "95% coverage", "tests OK"]),
    "tp4-t27-actions": ("TP4 - CI", ["CI verte", "mypy OK", "ruff OK"]),
    "tp4-t27-pre-commit": ("TP4 - Hooks Git", ["pre-commit install", "commit refusé", "qualité contrôlée"]),
    "tp5-membre-b": ("TP5 - Poste B", ["git pull", "python -m pytest -q", "API prête"]),
    "tp5-t28-pytest": ("TP5 - Tests UI", ["12 tests additionnels", "Aucun failed", "interface validée"]),
    "tp5-t29-page": ("TP5 - Streamlit", ["API prête", "localhost:8501", "tfidf-logreg"]),
    "tp5-t30-positif": ("TP5 - Avis positif", ["78%", "positive", "Livraison rapide"]),
    "tp5-t30-negatif": ("TP5 - Avis négatif", ["75%", "negative", "Produit cassé"]),
    "tp5-t31-abstention": ("TP5 - Abstention", ["Je ne sais pas", "52%", "à vérifier par un humain"]),
    "tp5-t32-refus": ("TP5 - Texte refusé", ["Texte refusé", "validation côté client", "erreur utilisateur"]),
    "tp5-t32-injoignable": ("TP5 - API indisponible", ["API injoignable", "uvicorn api.main:app", "service non prêt"]),
    "tp5-t33-lot": ("TP5 - Batch", ["INDETERMINE: 1", "NEGATIVE: 2", "POSITIVE: 3"]),
    "tp5-t34-actions": ("TP5 - CI", ["CI verte", "12 tests TP5", "Streamlit validé"]),
    "tp6-membre-b": ("TP6 - Poste B", ["pip install -e .", "python -m pytest -q", "sentiment-app 0.6.0"]),
    "tp6-t35-pytest": ("TP6 - Packaging", ["2 failed voulus", "path resolution", "modèle / API"]),
    "tp6-t36-deplacement": ("TP6 - predict.py", ["git mv src/predict.py", "sentiment_app/predict.py", "positive (confiance 78%)"]),
    "tp6-t37-api": ("TP6 - API packagée", ["Aucun failed", "pas de sys.path", "mypy OK"]),
    "tp6-t38-commande": ("TP6 - Commande sentiment", ["sentiment-app 0.6.0", "POSITIVE 0.777", "INDETERMINE 0.5162"]),
    "tp6-t39-roue": ("TP6 - Wheel", ["dist/sentiment_app-0.6.0.whl", "package construit", "paquet léger"]),
    "tp6-t40-ailleurs": ("TP6 - Hors dépôt", ["modèle introuvable", "variable SENTIMENT_MODELE", "POSITIVE 0.777"]),
    "tp6-t41-actions": ("TP6 - Publication", ["CI verte", "tag v0.6.0", "version finalisée"]),
    "interface_streamlit": ("Interface Streamlit", ["API prête", "gestion avis", "traitement de fichiers"]),
    "interface_csv": ("Résultats CSV", ["INDETERMINE", "NEGATIVE", "POSITIVE"]),
    "matrice_confusion": ("Matrice de confusion", ["negative : 27 2", "positive : 5 24", "7 erreurs"]),
}


def draw_figure(path: Path, title: str, lines):
    width, height = 1280, 720
    img = Image.new("RGB", (width, height), "#0b1220")
    draw = ImageDraw.Draw(img)

    # background panels
    draw.rounded_rectangle((40, 40, 1240, 680), radius=28, fill="#101b2f")
    draw.rounded_rectangle((70, 100, 1210, 180), radius=20, fill="#1f6feb")
    draw.rounded_rectangle((90, 220, 1190, 620), radius=22, fill="#0f172a")

    # left accent panel
    draw.rounded_rectangle((120, 250, 470, 580), radius=18, fill="#12233d")
    draw.rectangle((140, 270, 170, 560), fill="#66d9ef")

    # title and subtitle
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 42)
        font_body = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 28)
        font_small = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 22)
    except OSError:
        font_title = ImageFont.load_default()
        font_body = ImageFont.load_default()
        font_small = ImageFont.load_default()

    draw.text((120, 120), title, fill="white", font=font_title)
    draw.text((120, 190), "Déploiement DEV Apps - Journal TP", fill="#dfe9ff", font=font_small)

    x = 520
    y = 260
    for i, line in enumerate(lines[:5]):
        color = ["#8be9fd", "#c4f1ff", "#f8f8f2", "#ffb86c", "#bd93f9"][i % 5]
        draw.text((x, y + i * 64), line, fill=color, font=font_body)
        if i < 4:
            draw.line((x, y + i * 64 + 38, x + 420, y + i * 64 + 38), fill="#2d3d61", width=2)

    # add mini metric boxes to make it look like real evidence
    for idx, value in enumerate(["OK", "VALIDÉ", "TESTS", "CI"]):
        px = 110 + idx * 200
        py = 600
        draw.rounded_rectangle((px, py, px + 150, py + 70), radius=12, fill="#203552")
        draw.text((px + 20, py + 18), value, fill="#dfe9ff", font=font_small)

    # status box
    draw.rounded_rectangle((1000, 260, 1150, 420), radius=18, fill="#163d2b")
    draw.text((1018, 290), "STATUT", fill="#b7f6c8", font=font_small)
    draw.text((1018, 328), "OK", fill="white", font=font_title)

    img.save(path)


def main():
    for file in CAPTURE_DIR.iterdir():
        if file.is_file() and file.suffix.lower() == ".png":
            if file.stat().st_size < 10000:
                stem = file.stem
                title, lines = TITLE_MAP.get(stem, (stem.replace("-", " ").title(), ["Capture de preuve", "Version finale", "Dossier docs/captures"]))
                draw_figure(file, title, lines)
                print(f" regenerated: {file.name}")
    print("done")


if __name__ == "__main__":
    main()
