import pygame
import time
import random
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
orange = (200,128,64)
bright_orange = (255,128,64)

rocket_width = 74

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Trevor Forget v9.24.17')
clock = pygame.time.Clock()

milkImg = pygame.image.load( os.path.join(ROOT_DIR,'ms.png') )
rocketImg = pygame.image.load( os.path.join(ROOT_DIR,'trevor.png') )
#hgImg = pygame.image.load ('hg.png')

def things_dodged(count):
    font = pygame.font.SysFont("Fixedsys Regular", 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def rocket(x,y):
    gameDisplay.blit(rocketImg,(x,y))

def thing(thingx, thingy, thingw, thingh):
        #pygame.draw.rect (gameDisplay, color, [thingx, thingy, thingw, thingh])
        gameDisplay.blit(milkImg, (thingx, thingy, thingw, thingh))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont("Fixedsys Regular", 25)
    TextSurf, TextRect = text_objects (text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)

    game_loop()

def crash():
    message_display('#TREVORFORGET')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("Fixedsys Regular", 20)
    textSurf, textRect = text_objects(msg,smallText)
    textRect.center = ( (x+(w/2)), (y+h/2))
    gameDisplay.blit(textSurf, textRect)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("Fixedsys Regular", 115)
        TextSurf, TextRect = text_objects ("Trevor Forget", largeText)
        TextRect.center = ((display_width/2),(display_height/3.0))
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont("Arial", 20)
        TextSurf, TextRect = text_objects ("Gone But Not Forgotten", smallText)
        TextRect.center = ((display_width/2),(display_height/2.0))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start",150, 450, 100, 50,orange,bright_orange,"play")
        button("Quit",550, 450, 100, 50,orange,bright_orange,"quit")

        pygame.display.update()
        clock.tick(15)



def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 150

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        #thing(thingx, thingy, thingw, thingh, color):
        thing(thing_startx, thing_starty, thing_width, thing_height)
        thing_starty += thing_speed
        rocket(x,y)
        things_dodged(dodged)


        if x > display_width - rocket_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 0.5

        if y < thing_starty+thing_height:
            #print ('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+rocket_width > thing_startx and x + rocket_width < thing_startx+thing_width:
                #print ('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
