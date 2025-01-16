Projet : Web Scraping des Champions de League of Legends
Ce projet est une application web qui permet de collecter et d’afficher des informations sur les champions du jeu League of Legends, récupérées depuis le site Fandom.

Fonctionnalités
Scraping des données : Extraction d'informations détaillées sur les champions (nom, rôle, statistiques, image, etc.) depuis la plateforme Fandom.
https://leagueoflegends.fandom.com/wiki/List_of_champions

Traitement des données :
Nettoyage des données récupérées (suppression des doublons, formatage des rôles).
Téléchargement des images des champions et stockage local pour éviter des problèmes de chargement.
Conversion des statistiques comme le mana manquant en "Energy" pour un affichage correct.
Interface utilisateur : Affichage des champions sous forme de cartes interactives dans une interface simple et esthétique

Prérequis

Avant de commencer, assurez-vous que les éléments suivants sont installés sur votre machine :
Python : Version 3.7 ou supérieure.
Pip : Gestionnaire de paquets Python.
Les frameworks Python nécessaires :
Scrapy : Pour effectuer le scraping.
Flask : Pour construire l'interface web.

Installation
Clonez ce dépôt :

git clone https://github.com/YanisRili/WebScraping_Fandom/tree/master
  
Installez les dépendances nécessaires :

pip install scrapy
pip install flask
pip install requests

Utilisation

Étape 1 : Scraper les données
Configurez le spider Scrapy dans le dossier spiders.
Exécutez la commande suivante pour lancer le scraping et enregistrer les données :

scrapy crawl champions -o champions.json  

Étape 2 : Télécharger les images
Exécutez le script pour télécharger les images des champions dans le dossier static/images :

python download_images.py  

Étape 3 : Lancer l’application Flask
Exécutez le serveur Flask :

python app.py  

Accédez à l’interface utilisateur à l’adresse : http://127.0.0.1:5000.
