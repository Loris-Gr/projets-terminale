from Paquet_de_cartes import Paquet_de_cartes 
from random import randint
import time

# la fonction pour initialiser le programme
def setup():
    global c1,jeu,c2,carte_j1,carte_j2,j1_gagne,j2_gagne,dessin_carte_dos,jeu1,jeu2,cartes_suspends,t,message # déclarées comme globales
    jeu1=[]
    jeu2=[]
    cartes_suspends = []
    message = ""
    t = time.time()
    j2_gagne = loadImage("j2_gagne.gif")
    j1_gagne = loadImage("j1_gagne.gif")
    dessin_carte_dos = loadImage("dos_cartes.gif")
    fullScreen() # taille de la fenêtre
    jeu = Paquet_de_cartes() # création du jeu de cartes        
    jeu.battre()
    # distribution
    while len(jeu.cartes) > 0:
        jeu1.append(jeu.tirer())
        jeu2.append(jeu.tirer())
    carte_j1 = jeu1[0]
    carte_j2 = jeu2[0]
    c1=jeu1[0]
    c2=jeu2[0]
    carte_j1_cache=None
    carte_j2_cache=None
    carte_j1_2=None
    carte_j2_2=None
    carte_suspends=[]
    
dict_valeur = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8, 'valet':9, 'dame':10, 'roi':11,'as':12} 

def bataille(duo_carte) :
        global jeu1,jeu2,c1,jeu,c2,carte_j1,carte_j2,j1_gagne,j2_gagne,dessin_carte_dos,cartes_suspends
        if dict_valeur[str(duo_carte[0].valeur)]>dict_valeur[str(duo_carte[1].valeur)] :    #si la carte du joueur 1 est plus forte que la carte du joueur 2
            jeu1.append(carte_j1)
            jeu1.append(carte_j2) 
            if cartes_suspends != [] :
                for i in range(len(cartes_suspends)) :
                    jeu1.append(cartes_suspends[i])                                          #on ajoute au jeu du joueur 1 les cartes en suspends
                cartes_suspends = []                                                         #on vide la liste de cartes en suspends
            return 'j1-1'
            
        if dict_valeur[str(duo_carte[0].valeur)]<dict_valeur[str(duo_carte[1].valeur)] :    #si la carte du joueur 2 est plus forte que la carte du joueur 1
            jeu2.append(carte_j1)
            jeu2.append(carte_j2)
            if cartes_suspends != [] :
                for i in range(len(cartes_suspends)) :                                       
                    jeu2.append(cartes_suspends[i])                                          #on ajoute au jeu du joueur 1 les cartes en suspends
                cartes_suspends = []                                                         #on vide la liste de cartes en suspends
            return 'j2-2'          
        
        else :                                                                              #s'il y a bataille
            carte_j1_2 = carte_j1                      # sauvegarde de la 1ere carte
            carte_j2_2 = carte_j2                      # sauvegarde de la 2eme carte
            carte_j1_cache = jeu1[0]
            carte_j2_cache = jeu2[0]
            jeu1.pop(0)
            jeu2.pop(0)
            cartes_suspends.append(carte_j1_2)#faire une liste où j'ajoute les cartes cachées et nouvelles
            cartes_suspends.append(carte_j2_2)
            cartes_suspends.append(carte_j1_cache)  
            cartes_suspends.append(carte_j2_cache)
            return 'bataille' 
        
# la fonction draw qui boucle à l'infini
def draw():
    global jeu1,jeu2,c1,jeu,c2,carte_j1,carte_j2,j1_gagne,j2_gagne,dessin_carte_dos,carte_j1_cache,carte_j2_cache,carte_j1_2,carte_j2_2,cartes_suspends,t,message
    background(59,173,56) # couleur de fond
    image(carte_j1.dessin_carte(),525,400) # affichage d'une carte image(img,abscisse, ordonnée)
    image(carte_j2.dessin_carte(),950,400)
    # affichage de texte text(le texte, abscisse,ordonnée)
    textSize(20)
    text("carte du joueur1",525,600)
    text("carte du joueur2",950,600)
    carte_j1_cache=None
    carte_j2_cache=None
    carte_j1_2=None
    carte_j2_2=None
    
    if mousePressed and time.time()-t > 0.25:
        t = time.time()
        if jeu1 == [] :
            image(j1_gagne,0,0)
            return True
        if jeu2 == [] :
            image(j2_gagne,0,0)
            return True       
        carte_j1 = jeu1[0]
        carte_j2 = jeu2[0]
        jeu1.pop(0)
        jeu2.pop(0)
        duo_carte =[carte_j1,carte_j2]
        image(carte_j1.dessin_carte(),525,400) # affichage d'une carte image(img,abscisse, ordonnée)
        image(carte_j2.dessin_carte(),950,400)
        textSize(20)
        text("carte du joueur1",525,600)
        text("carte du joueur2",950,600)
        Bataille = bataille(duo_carte)
        if Bataille == 'j1-1' :
            message = "Joueur 1 remporte la manche"
        elif Bataille == 'j2-2' :
            message = "Joueur 2 remporte la manche"
        elif Bataille == 'bataille' and time.time()-t > 0.25: 
            t = time.time()
            image(dessin_carte_dos,525,400) # affichage du dos d'une carte image(img,abscisse, ordonnée)
            image(dessin_carte_dos,950,400)
            message = "Bataille !"
    textSize(20)
    text(message,735,800)
            
