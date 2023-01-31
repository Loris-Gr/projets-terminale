from paddle import Paddle # import de la classe Paddle
from ball import Ball # import de la classe Ball
from briques import Brick # import de la classe Brick
import time
import random
playingGame = False
bricks = [] # Création de la liste
new_game = False
score=0 # Initialisation du score
def setup():
    global paddle, ball # on déclare les variables paddle et ball comme globale
    size(805,600) # on défini la taille de la fenêtre
    paddle = Paddle() # on crée l'objet paddle
    ball = Ball() # on crée l'objet ball


    if new_game == True :
        randomizer = random.randint(110,200)
        randomizer2 = random.randint(4,8)
        randomizer3 = random.randint(20,40)
        randomizer4 = random.randint(150,245)
        ball.vel = PVector(1, 1)*randomizer2
        for x in range(5,width - 80,75):
            addBrick(x+37.5,50,3)
            addBrick(x+37.5,70,2)
            addBrick(x+37.5,90,1)
            addBrick(x+37.5,randomizer,4)
            addBrick(x+37.5,randomizer+randomizer3,4)

    else :
        for x in range(5,width - 80,75):
            addBrick(x+37.5,50,3)
            addBrick(x+37.5,70,2)
            addBrick(x+37.5,90,1)

# Fonctions créant et stockant les briques dans la liste
def addBrick(x,y,hits):
    brick = Brick(x,y,hits)
    bricks.append(brick)

def f_score(score) :
    """fonction permettant d'afficher le score"""
    fill("#FFFFFF") #couleur blanche
    textSize(25)
    text("score :",0,25)
    text(score,90,25)
    
def f_vie(vie) :
    """fonction permettant d'afficher le score"""
    fill("#FFFFFF") #couleur blanche
    textSize(25)
    text("vies :",700,25)
    text(ball.vie,775,25)

def draw():
    global playingGame, score
    background(0,0,0)
    #appel des méthodes pour le paddle
    paddle.display()
    f_score(score)
    f_vie(ball.vie)
    casser = True
    if ball.vie == 0 :  # permet de stopper le jeu quand les 3 vies sont utilisées         
            playingGame = False
            fill("#FFFFFF") # couleur blanche
            textSize(30) # taille du texte
            text("Plus de vie, partie terminee",200,250) # message à afficher + sa position
            textSize(40)
            text("cliquez pour rejouer",200,300)
            if mousePressed :
                ball.vie = 3
                setup() # permet de recréer l'environnement (les briques + replacer le paddle)
                playingGame = True
    if ball.vie>0 and len(bricks)==0 :
        playingGame= False
        fill("#FFFFFF") #couleur blanche
        textSize(30)
        text("Bravo, tu as gagne !",250,200)
        textSize(30)
        text("cliquez pour rejouer dans un nouveau niveau",60,300)
        if mousePressed :
                ball.vie = 3
                new_game = True
                setup() # permet de recréer l'environnement (les briques + replacer le paddle)             
                playingGame = True     
    
    if playingGame: 
        paddle.checkEdges()
        paddle.update()
    #appel des méthodes pour la balle

        ball.checkEdges()
        ball.update()  
    ball.display()

    if (ball.meets_paddle(paddle)):
        if ball.dir.y > 0 :
            ball.dir.y *= -1
    for i in range(len(bricks)):
        bricks[i].display()
        

    #for i in range(len(bricks)-1,-1,-1):
    i=0
    while i < len(bricks) and i !=-1 :
        if ball.meets_brick(bricks[i]):
            score+=5
            bricks.pop(i) # détruit une brique i
            i=-2
        i+=1
            
        
def mousePressed():
    global playingGame
    playingGame = True

# détection des mouvements touches q et d
def keyPressed():
    if key == "q" or key == "Q":
        paddle.isMovingLeft = True
    elif key == "d" or key == "D":
        paddle.isMovingRight = True

#annulation des mouvements quand on relâche la touche
def keyReleased():
    paddle.isMovingRight = False
    paddle.isMovingLeft = False
