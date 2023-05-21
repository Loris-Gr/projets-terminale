# coding=utf-8


class Carte(object):
    "Définition d'une carte"

    def __init__(self,val='as',coul='carreau'): # le constructeur
        self.valeur = val
        self.couleur = coul
        
    def __repr__(self):
        return str(self.valeur) + str(self.couleur)

    def dessin_carte(self):
        "Renvoi du nom du fichier image de la carte c"
        # les cartes sont dans le répertoire "cartes", au même niveau que ce programme
        nom = "cartes/"+self.valeur+"_"+self.couleur+".gif"
        return loadImage(nom)
    
