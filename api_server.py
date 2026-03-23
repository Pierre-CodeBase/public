# API REST python/Flask pour exposer les données du capteur sur demande du client
# À démarrer depuis une fenêtre de terminal.
# Port 5000

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__) # création d'un objet Flask
# CORS(app) # Permet les requêtes cross-origin si nécessaire (pas ici !)
JSON_FILE = "sensorData.json" # nom du fichier de données JSON où se trouvent les mesures

def read_data():
    """Lit les données depuis le fichier JSON : renvoie un JSON """

    if not os.path.exists(JSON_FILE):
        return None
    
    try:
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)
            return data
        
    except Exception as e:
        print(f"Erreur de lecture: {e}")
        return None
    
@app.route('/')
def home():
    """Page d'accueil de l'API"""
    return jsonify({
    "message": "API Capteur de Distance",
    "endpoints": {
    "/distance": "GET - Récupère la dernière distance mesurée"
    }
    })

@app.route('/distance', methods=['GET'])
def get_distance():
    """
    Endpoint principal: retourne la distance sous forme de json
    (après lecture du... json créé par l'app de génération de données)
    """

    data = read_data()

    if data is None:
        return jsonify({
        "error": "Aucune donnée disponible",
        "message": "Le capteur n'a pas encore produit de données"
        }), 404
    return jsonify(data), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint non trouvé"}), 404

if __name__ == '__main__':
    print("Démarrage de l'API REST...")
    print("Endpoint disponible : http://localhost:5000/distance")
    app.run(host='0.0.0.0', port=5000, debug=True)