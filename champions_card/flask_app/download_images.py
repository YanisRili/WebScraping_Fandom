import os
import json
import requests
import re

# Charger les données depuis le fichier JSON
with open('champions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Créer un dossier 'images' si il n'existe pas
if not os.path.exists('images'):
    os.makedirs('images')

# Fonction pour nettoyer le nom du fichier (enlever les caractères invalides)
def sanitize_filename(filename):
    # Remplacer les caractères non autorisés par des tirets (-)
    return re.sub(r'[<>:"/\\|?*]', '-', filename)

# Fonction pour télécharger une image
def download_image(url, filename):
    try:
        # Effectuer une requête pour obtenir l'image
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Ouvrir un fichier en mode écriture binaire et écrire l'image dedans
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Image téléchargée: {filename}")
        else:
            print(f"Erreur de téléchargement pour {url}")
    except Exception as e:
        print(f"Erreur pour {url}: {e}")

# Télécharger les images
for champion in data:
    image_url = champion.get('image_url')  # Récupérer l'URL de l'image
    champion_name = champion.get('name')  # Récupérer le nom du champion
    if image_url and champion_name:
        # Nettoyer le nom du champion pour créer un nom de fichier valide
        filename = sanitize_filename(champion_name) + '.jpg'
        image_path = os.path.join('images', filename)
        
        # Télécharger l'image
        download_image(image_url, image_path)
