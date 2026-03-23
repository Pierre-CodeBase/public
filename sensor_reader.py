"""
Lecture d'un capteur US Ranger simulée (marégraphe) et stockage en JSON
À executer depuis une fenêtre de terminal ou depuis un IDE.
"""

import time
import json
import random
from datetime import datetime
from mesure import USRanger

# Configuration
JSON_FILE = "sensorData.json"
READ_INTERVAL = 5 # intervalle entre deux mesures secondes
ranger = USRanger(17)
    
def save_to_json(distance, numero):
    """Sauvegarde la distance dans un fichier JSON
    avec le numéro de mesure et la date/heure."""
    data = {
    "numero": numero,
    "distance_cm": distance,
    "timestamp": datetime.now().isoformat(),
    }

    try:
        with open(JSON_FILE, 'w') as f:
            json.dump(data, f, indent=2)
            print(f"Distance sauvegardée: {distance} cm")
    except Exception as e:
        print(f"Erreur d'écriture: {e}")
        
# main
numero = 1 # numéro de mesure initialisé

for i in range(100):

    distance = ranger.get_distance()
    print(distance)
    save_to_json(distance, numero)
    numero += 1
    time.sleep(READ_INTERVAL)