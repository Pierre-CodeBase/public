"""
Code pour capteur ultrasonique Grove à 3 pins sur Raspberry Pi 3
Compatible avec Grove Ultrasonic Ranger
Alim Vcc : +5V ou +3.3V
"""

import RPi.GPIO as GPIO
import time

class GroveUltrasonicRanger:
    def __init__(self, pin):
        """
        Initialise le capteur ultrasonique Grove
        
        Argument:
            pin (int): Numéro du pin GPIO (mode BCM) connecté au signal
        """
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
    
    def get_distance(self):
        """
        Mesure la distance en centimètres
        
        Returns:
            float: Distance en cm, ou -1 en cas d'erreur
        """
        # Configure le pin en sortie pour envoyer le signal
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(0.00001)  # 10 microseconds
        
        # Envoie une impulsion de 10µs
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.pin, GPIO.LOW)
        
        # Configure le pin en entrée pour recevoir l'écho
        GPIO.setup(self.pin, GPIO.IN)
        
        # Attend le début de l'écho
        timeout = time.time() + 0.1  # Timeout de 100ms
        while GPIO.input(self.pin) == GPIO.LOW:
            pulse_start = time.time()
            if pulse_start > timeout:
                return -1
        
        # Attend la fin de l'écho
        timeout = time.time() + 0.1
        while GPIO.input(self.pin) == GPIO.HIGH:
            pulse_end = time.time()
            if pulse_end > timeout:
                return -1
        
        # Calcule la durée de l'impulsion
        pulse_duration = pulse_end - pulse_start
        
        # Calcule la distance (vitesse du son = 34300 cm/s)
        # Distance = (Temps × Vitesse) / 2
        distance = (pulse_duration * 34300) / 2
        
        return round(distance, 2)
    
    def cleanup(self):
        """Nettoie les configurations GPIO"""
        GPIO.cleanup()



if __name__ == "__main__":
    # Utilise le GPIO 17 (pin 11 physique) - à adapter !!!
    SIGNAL_PIN = 17
    
    sensor = GroveUltrasonicRanger(SIGNAL_PIN)
    
    try:
        print("Capteur ultrasonique Grove - Mesure de distance")
        print("Appuyez sur Ctrl+C pour arrêter\n")
        
        while True:
            distance = sensor.get_distance()
            
            if distance > 0:
                print(f"Distance: {distance} cm")
            else:
                print("Erreur de mesure")
            
            time.sleep(0.5)  # Mesure toutes les 500ms
            
    except KeyboardInterrupt:
        print("\nArrêt du programme")
    
    finally:
        sensor.cleanup()
        print("GPIO nettoyés")