import pygame
import time
from random import *

blue = (113,177,227)
white = (255,255,255)

pygame.init()

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

def clouds(x_cloud, y_cloud, espace):
    surface.blit(img_cloud_1,(x_cloud,y_cloud))
    surface.blit(img_cloud_2,(x_cloud,y_cloud + cloudW + espace))


def PlayAgain():
    for event in pygame.event.get ([pygame.KEYDOWN, pygame.KEYUP,pygame.QUIT]): #if detect an input up down or quit with the cross of the windows
        if event.type == pygame.QUIT :
            pygame.QUIT()
            quit()
        elif event.type == pygame.KEYUP :
            continue
        return event.key
    return None

def creaTextObj(text, Police):                  
    textSurface = Police.render(text,True,white)            #define an object for the text 
    return textSurface, textSurface.get_rect()

def message (text):
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

def gameOver():
    message("Boom")                       #display an object message

def ballon (x,y,image):
    surface.blit(image, (x,y))

def principal():                          #my principal function main()
    x = 150
    y = 200
    y_mouvement = 0
    
    x_cloud = surfaceW
    y_cloud = randint(-300,20)                #random value
    espace = ballonH*3                        #height of the space betwwen the clouds
    cloud_speed = 2

    game_over = False                        #create a variable to now if the game need to stop
    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                                                #detect if you press an input
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP :
                     y_mouvement = -1
            if event.type == pygame.KEYUP :
                y_mouvement = 1

        y+= y_mouvement

        surface.fill(blue)
        ballon(x,y,img)

        clouds(x_cloud,y_cloud, espace)

        x_cloud -= cloud_speed              #position of the cloud at each loop/frame

        if y >surfaceH -40 or y < -10 :     #when you touch the border of the windows
            gameOver()

                                         #define when you touch the ballon, you can change the difficulty here
        if x + ballonW > x_cloud +40:
            if y < y_cloud + cloudH -50:
                if x - ballonW < x_cloud + cloudW -20 :
                    gameOver()

        if x +ballonW > x_cloud +40:
            if y + ballonH > y_cloud + cloudH + espace + 50:
                if x + ballonW < x_cloud +cloudW -20 :
                    gameOver()

        if x_cloud < (-1*cloudW) :
            x_cloud = surfaceW
            y_cloud = randint(-300,20)

        pygame.display.update()


     
principal()
    #os._exit()
pygame.quit()
    #print(quit)

#Code from alexandre ghelli
#https://www.youtube.com/channel/UCSXLZu6tCzXlSARAJ9utgow/videos