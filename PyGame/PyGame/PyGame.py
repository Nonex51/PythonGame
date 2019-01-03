import pygame
import time
from random import *
import sqlite3

#color of the background
blue = (113,177,227)
white = (255,255,255)

pygame.init()

Donnees = "/Users/Guillaume/Documents/PythonGame/PyGame/Donnees.sq3"
conn = sqlite3.connect(Donnees)
cur = conn.cursor()

"""
#This code it's to create the file to save the Score
#Donnees = "/Users/Guillaume/Documents/PythonGame/PyGame/Donnees.sq3"
#Donnees = "/Users/Guillaume/Desktop/Donnees.sq3"
conn = sqlite3.connect(Donnees)
cur = conn.cursor()
cur.execute("create table membres (score integer)")
cur.execute("insert into membres (score) values (0)")
conn.commit()
cur.execute("insert into membres (score) values (0)")
conn.commit()
"""

surfaceW = 800
surfaceH = 500
ballonW = 50
ballonH = 66
cloudW = 300
cloudH = 300

surface = pygame.display.set_mode((surfaceW, surfaceH))
pygame.display.set_caption("Fly Balloon")
clock = pygame.time.Clock()

img = pygame.image.load('Ballon01.png')
img_cloud_1 =pygame.image.load('NuageHaut.png')
img_cloud_2 =pygame.image.load('NuageBas.png')

def score(compte):
    police = pygame.font.Font('BradBunR.ttf',16)
    text = police.render("Score: " + str(compte), True, white)
    surface.blit(text, [10,0])             #position of score

def Hscore(compte):
    police = pygame.font.Font('BradBunR.ttf',16)
    text = police.render("High.Score: " + str(compte), True, white)
    surface.blit(text, [700,0])         

def clouds(x_cloud, y_cloud, espace):
    surface.blit(img_cloud_1,(x_cloud,y_cloud))
    surface.blit(img_cloud_2,(x_cloud,y_cloud + cloudW + espace))


def PlayAgain():
    for event in pygame.event.get ([pygame.KEYDOWN, pygame.KEYUP,pygame.QUIT]): #if detect an input up down or quit with the cross of the windows
        if event.type == pygame.QUIT :
            pygame.quit()
        elif event.type == pygame.KEYUP :
            continue
        return event.key
    return None

def creaTextObj(text, Police):                  
    textSurface = Police.render(text,True,white)            #define an object for the text 
    return textSurface, textSurface.get_rect()

def messageScreen (text):
    BText = pygame.font.Font('BradBunR.ttf', 150)
    SText = pygame.font.Font('BradBunR.ttf', 20)

    BTextSurf, BTextRect = creaTextObj(text, BText)             #create the big text in the object text
    BTextRect.center = surfaceW/2, ((surfaceH/2)-50)
    surface.blit(BTextSurf,BTextRect)
    
    STextSurf, STextRect = creaTextObj("Press a touch to continu",SText)        #create the small text in the object text
    STextRect.center = surfaceW/2, ((surfaceH/2)+50)
    surface.blit(STextSurf,STextRect)

    pygame.display.update()
    time.sleep(2)

    while PlayAgain () == None :          #stop  the game during the gameover screen
        clock.tick()

    principal()

def gameOver(score_actuel):
    #"""
    a = str(score_actuel)     #create a list with a char

    Donnees = "/Users/Guillaume/Documents/PythonGame/PyGame/Donnees.sq3"
    conn =sqlite3.connect(Donnees)
    cur = conn.cursor()
    cur.execute("select * from membres")
    dataliste = list(cur)
                                    #save the best score in the DB file
    hscore=[]
    for i in range(0,len(dataliste)):
        hscore += dataliste[i]

    if (int(hscore[-1]) < score_actuel):
        cur.execute("insert into membres(score) values (?)", (a,))
        conn.commit()
        cur.close()
        conn.close()
    #"""
    messageScreen("Boom")                       #display an object message


def ballon (x,y,image):
    surface.blit(image, (x,y))

def principal():                          #my principal function main()
    x = 150
    y = 200
    y_mouvement = 0
    ballon_speed = 1
    x_cloud = surfaceW
    y_cloud = randint(-300,20)                #random value
    espace = ballonH*3                        #height of the space between the clouds
    cloud_speed = 2
    score_actuel = 0

    game_over = False                        #create a variable to now if the game need to stop
    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                                               #detect if you press an input
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP :
                #if event.key == pygame.K_SPACE :
                     y_mouvement = - ballon_speed
            if event.type == pygame.KEYUP :
            #if event.type == pygame.K_SPACE :
                y_mouvement = ballon_speed

        y+= y_mouvement

        surface.fill(blue)
        ballon(x,y,img)
        clouds(x_cloud,y_cloud, espace)
        score(score_actuel)

        cur.execute("select * from membres")    #take all in the data list and put the result inside the cursor (cur)
        dataliste = list(cur)                       # make a list with the data
       # print(cur)
       # print(dataliste)

        hscore = []
        for i in range (0,len(dataliste)):
            hscore +=dataliste[i]                    # format the data in list from table
       # print(hscore)

        Hscore(hscore[-1])
        x_cloud -= cloud_speed              #position of the cloud at each loop/frame

        if y >surfaceH -40 or y < -10 :     #when you touch the border of the windows
            gameOver(score_actuel)

                                         #increase the difficulty in function of your score
        if 1 <= score_actuel < 100 :
            cloud_speed = 2 + 0.5  * score_actuel
            ballon_speed = 2 + 0.1 * score_actuel
            espace = ballonH * 2.8 - 0.1*score_actuel
   
                                         #define when you touch the cloud with the ballon, you can change the difficulty here
        if x + ballonW > x_cloud +40:
            if y < y_cloud + cloudH -80:               #Space tolerate inside the cloud up and down
                if x - ballonW < x_cloud + cloudW -20 :
                    gameOver(score_actuel)

        if x +ballonW > x_cloud +40:
            if y + ballonH > y_cloud + cloudH + espace + 80: #Space tolerate on the side of the cloud 
                if x + ballonW < x_cloud +cloudW -20 :
                    gameOver(score_actuel)


        if x_cloud < (-1*cloudW) :              #give a new position for a new cloud
            x_cloud = surfaceW
            y_cloud = randint(-300,20)

       # print(x_cloud)
       # print(cloudW)
       # print( cloud_speed)
       # print(x)

        if x_cloud - 1 < (x - cloudW) < x_cloud + cloud_speed:          #select just one frame to incremente the score one time by cloud
            score_actuel +=1

       # a = list(str(score_actuel)) 
       # print(a)

        pygame.display.update()
          
principal()
pygame.quit()

    #print(quit)
    #os._exit()


#C:\Users\Guillaume\AppData\Local\Programs\Python\Python37-32>
#C:\Users\Guillaume\Documents\PythonGame\PyGame>pyinstaller "PyGame.py"

#Code from alexandre ghelli to learn Python for RSG
#https://www.youtube.com/channel/UCSXLZu6tCzXlSARAJ9utgow/videos