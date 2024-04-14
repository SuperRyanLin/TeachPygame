import random
import pygame
import sys
from pygame.locals import *

# global macros
FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels

# colors
#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

# color settings
# BGCOLOR = WHITE

# graph = pygame.image.load("圖.jpg") # load image to variable
# sound = pygame.mixer.Sound("音效.mp3") # load sound effect to variable

def main():
    # initial settings
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    # DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), HWSURFACE|DOUBLEBUF|RESIZABLE) # resizable window
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), FULLSCREEN) # fullscreen window
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16) # font settings

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption("title") # the title of the game window

    # DISPLAYSURF.fill(BGCOLOR) # fill the window with the chosen background color

    # main game loop
    while True:
        # DISPLAYSURF.fill(BGCOLOR) # fill the window with the chosen background color

        # local variables
        # ...
        
        # game loop body
        # ...
        
        
        # DISPLAYSURF.blit(graph, (0, 0)) # draw a graph at (x, y)

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