from flask import Flask, render_template
from flask import Response

import json


app = Flask(__name__)

@app.route('/')
def home():
    # Charger les données des champions depuis le fichier JSON
    with open('champions.json', 'r') as file:
        champions = json.load(file)

    # Trier les champions par nom
    champions_sorted = sorted(champions, key=lambda x: x['name'])

    # Passer les champions triés au template
    return render_template('index.html', champions=champions_sorted)

@app.after_request
def apply_caching(response: Response):
    response.headers["Content-Security-Policy"] = "default-src 'self'; img-src 'self' https://static.wikia.nocookie.net"
    return response
def add_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response    

if __name__ == '__main__':
    app.run(debug=True)
