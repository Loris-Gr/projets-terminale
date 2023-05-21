# coding=utf-8
from random import shuffle
from Cartes import Carte
class Paquet_de_cartes(object):
    global valeur,couleur
    """Paquet de cartes"""
    couleur = ('pique', 'trefle', 'carreau', 'coeur')
    valeur = ('as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi')

    def __init__(self):
        "Construction de la liste des 52 cartes"
        self.cartes = []
        for coul in range(4):
            for val in range(13):
                nouvelle_carte = Carte(valeur[val], couleur[coul])   # la valeur commence à  0
                self.cartes.append(nouvelle_carte)

    def battre(self):
        "Mélanger les cartes"
        shuffle(self.cartes)

    def tirer(self):
        "Tirer la première carte de la pile"
        t = len(self.cartes)
        if t>0:
            carte = self.cartes[0]   # choisir la première carte du jeu
            del(self.cartes[0])      # et la supprimer du jeu
            return carte
        else:
            return None
    
paquet = Paquet_de_cartes()
