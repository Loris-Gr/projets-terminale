# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 10:35:48 2021

@author: annes
"""
import time # bibliothèque pour attendre des secondes
class Ball():

    def __init__(self):# le constructeur
        self.r = 10 #attribut rayon
        self.vel = PVector(1, 1)*5 # attribut vitesse
        self.dir = PVector(1, 1) # attribut direction
        self.pos = PVector(width/2, height/2) # attribut position
        self.vie = 3  # initialisation des vies
        
    # méthode pour l'actualisation de la position
    def update(self):
        self.pos.x += self.vel.x*self.dir.x
        self.pos.y += self.vel.y*self.dir.y

    # méthode pour afficher la balle ellipse(x,y,diamètre horizontal, diamètre vertical)
    def display(self):
        fill("#ffff64")
        noStroke()
        ellipse(self.pos.x, self.pos.y, self.r*2, self.r*2)

    #méthode pour les collision avec les bords
    def checkEdges(self):
        # bord droit
        if (self.pos.x > width - self.r and self.dir.x > 0):
            self.dir.x *= -1 # on change le signe de la direction
        # bord gauche
        if (self.pos.x < self.r and self.dir.x < 0):
            self.dir.x *= -1
        # bord haut
        if (self.pos.y < self.r and self.dir.y < 0):
            self.dir.y *= -1
        # bord bas
        if (self.pos.y > height - self.r and self.dir.y > 0):
            self.vie-=1 
            time.sleep(2)
            self.pos = PVector(width/2, height/2)
            
            
            
                                                                   

    # méthode pour détecter la collision avec le paddle
    def meets_paddle(self, paddle):
        if (self.pos.y < paddle.pos.y and
            self.pos.y > paddle.pos.y - self.r and
            self.pos.x > paddle.pos.x - self.r and
            self.pos.x < paddle.pos.x + paddle.w + self.r):
            return True
        else:
            return False

    # Méthode pour casser les briques rencontrées
    def meets_brick(self,brick):
        if (self.pos.y < brick.pos.y + brick.h+self.r and
        self.pos.y > brick.pos.y -self.r and
        self.pos.x > brick.pos.x -self.r and
        self.pos.x < brick.pos.x + brick.w+self.r):
            if (self.pos.y <= brick.pos.y + brick.h and
            self.pos.y >= brick.pos.y and
            self.pos.x >= brick.pos.x -self.r and
            self.pos.x <= brick.pos.x + brick.w+self.r):
                self.dir.x *= -1
                return True
            else:
                self.dir.y *=-1
                return True
        return False
                
        
