# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 08:06:03 2021

@author: annes
"""

class Brick(): 

    #attribut de classe un dictionnaire de couleurs
    COLORS = {1: "#e9e0ec", 2: "#bb0606", 3: "#1b5021", 4: "#88bccb"}

    def __init__(self, x, y, hits):# le constructeur
        self.w = 75 # attribut longueur
        self.h = 20 # attribut largeur
        self.pos = PVector(x, y) # attribut position
        self.hits = hits #attribut clé pour la couleur
        self.col = Brick.COLORS[hits] # la couleur
     
    # méthode pour afficher la brique
    def display(self):
        fill(self.col)
        stroke("#ffffff") # couleur du bord
        strokeWeight(2)# épaisseur des bords
        rect(self.pos.x, self.pos.y, self.w, self.h)
        
