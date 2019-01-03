import pygame

blue = (0,0,255)
white = (255,255,255)

pygame.init()

surfaceW = 800
surfaceH = 500
ballonW = 50
ballonH = 66

surface = pygame.display.set_mode((surfaceW, surfaceH))
pygame.display.set_caption("Fly Balloon")

img = pygame.image.load('Ballon01.png')


def ballon (x,y,image):
    surface.blit(image, (x,y))


def principal():
    x = 150
    y = 200
  
    #create a variable to now if the game need to stop
    game_over = False
    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        surface.fill(blue)
        ballon(x,y,img)
        pygame.display.update()


     
principal()
    #os._exit()
pygame.quit()
    #print(quit)