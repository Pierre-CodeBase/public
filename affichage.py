from PyQt6.QtWidgets import (QApplication,QWidget,QLabel,QPushButton)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer
import sys
from USRanger import USRanger

class MyMainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        """Initialisation de la fenetre"""
        self.setGeometry(0,0,200,160)
        self.setWindowTitle("")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        
        #Label de titre de l'affichage
        labelDistance = QLabel(self)
        labelDistance.setText("Distance:")
        labelDistance.setFont(QFont('Arial',20))
        labelDistance.move(50,40)

        #Label d'affichage de la distance
        self.afficheurDistance = QLabel(self)
        self.afficheurDistance.setText("---")
        self.afficheurDistance.setFont(QFont('Arial',40))
        self.afficheurDistance.move(30,80)
        self.afficheurDistance.resize(200,100)

        #Bouton de démarrage
        startButton = QPushButton("Démarrer", self)
        startButton.clicked.connect(self.timerStart)

    def timerStart(self): #méthode appelant la mesure de distance tout les secondes
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mesurerDistance)
        self.timer.start(1000)
        self.capteur = USRanger(17)

    def mesurerDistance(self): #réception de la distance et actualisation de l'affichage

        distance = self.capteur.get_distance()
        self.afficheurDistance.setText(str(distance))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    sys.exit(app.exec())