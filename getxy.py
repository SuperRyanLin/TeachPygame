import random
import pygame
import sys
from pygame.locals import *

# global macros
FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 1120 # size of window's width in pixels
WINDOWHEIGHT = 840 # size of windows' height in pixels

bg = pygame.image.load("A-main.png") # CHOOSE BACKGROUND FILE HERE
ratio = bg.get_width() / WINDOWWIDTH
bg = pygame.transform.scale(bg, (WINDOWWIDTH, WINDOWHEIGHT))
g = pygame.image.load("沉澱表.jpg") # CHOOSE SPRITE FILE HERE
g = pygame.transform.scale(g, (g.get_width() / ratio, g.get_height() / ratio))

def main():
    # initial settings
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("getxy") # the title of the game window

    # main game loop
    move = False
    p = (0, 0)
    while True:
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if move == False:
                    move = True
                else:
                    p = pygame.mouse.get_pos()
                    print(p)
                    move = False
        
        pos = pygame.mouse.get_pos()
        DISPLAYSURF.blit(bg, (0, 0))
        if move == True:
            DISPLAYSURF.blit(g, (pos[0], pos[1]))
        else:
            DISPLAYSURF.blit(g, (p[0], p[1]))
        
        pos = pygame.mouse.get_pos()
        
        checkForQuit()
        
        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(FPS)

###### program exiting functions begin
def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event) # put the other KEYUP event objects back
###### program exiting functions end

if __name__ == '__main__': # start the program
    main()