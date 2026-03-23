import RPi.GPIO as GPIO
import time
import json

class USRanger():

    def __init__(self,pin):

        #setup
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def get_distance(self):

        #Configure le pin en sortie pour envoyer le signal
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

        #Envoie une impulsion
        GPIO.output(self.pin, GPIO.HIGH)
        GPIO.output(self.pin, GPIO.LOW)

        #Configure le pin en entrée pour recevoir l'écho
        GPIO.setup(self.pin, GPIO.IN)

        #Attend le début dde l'écho avec timeout de 100ms
        timeout = time.time() + 0.1
        while GPIO.input(self.pin) == GPIO.LOW:
            pulse_start = time.time()
            if pulse_start > timeout:
                return -1
            
        #Attend la fin de l'écho avec timeout de 100ms
        timeout = time.time() + 0.1
        while GPIO.input(self.pin) == GPIO.HIGH:
            pulse_end = time.time()
            if pulse_end > timeout:
                return -1
        
        #Calcule la durée de l'allé-retour de l'écho
        pulse_duration = pulse_end - pulse_start

        #Calcule la distance à partir de la durée et de la vitesse du son dans l'air en centimètres
        distance = (pulse_duration * 34300) / 2
        
        #Renvoyer la distance calculée avec une précision au centième de centimètre
        return round(distance, 2)
    
    #Méthode de réinitialisation du GPIO
    def cleanup(self):
       
        GPIO.cleanup()