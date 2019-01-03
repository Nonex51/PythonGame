import pygame
import time

blue = (113,177,227)
white = (255,255,255)

pygame.init()

surfaceW = 800
surfaceH = 500
ballonW = 50
ballonH = 66

surface = pygame.display.set_mode((surfaceW, surfaceH))
pygame.display.set_caption("Fly Balloon")
clock = pygame.time.Clock()

img = pygame.image.load('Ballon01.png')

def PlayAgain():
    for event in pygame.event.get ([pygame.KEYDOWN, pygame.KEYUP,pygame.QUIT]):
        if event.type == pygame.QUIT :
            pygame.QUIT()
            quit()
        elif event.type == pygame.KEYUP :
            continue
        return event.key
    return None

def creaTextObj(text, Police):
    textSurface = Police.render(text,True,white)
    return textSurface, textSurface.get_rect()

def message (text):
    BText = pygame.font.Font('BradBunR.ttf', 150)
    SText = pygame.font.Font('BradBunR.ttf', 20)

    BTextSurf, BTextRect = creaTextObj(text, BText)
    BTextRect.center = surfaceW/2, ((surfaceH/2)-50)
    surface.blit(BTextSurf,BTextRect)
    
    STextSurf, STextRect = creaTextObj("Press a touch to continu",SText)
    STextRect.center = surfaceW/2, ((surfaceH/2)+50)
    surface.blit(STextSurf,STextRect)

    pygame.display.update()
    time.sleep(2)

    while PlayAgain () == None :
        clock.tick()

    principal()



def gameOver():
    message("Boom")

def ballon (x,y,image):
    surface.blit(image, (x,y))


def principal():
    x = 150
    y = 200
    y_mouvement = 0

    #create a variable to now if the game need to stop
    game_over = False
    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP :
                     y_mouvement = -1
            if event.type == pygame.KEYUP :
                y_mouvement = 1

        y+= y_mouvement

        surface.fill(blue)
        ballon(x,y,img)

        if y >surfaceH -40 or y < -10 :
            gameOver()

        pygame.display.update()


     
principal()
    #os._exit()
pygame.quit()
    #print(quit)