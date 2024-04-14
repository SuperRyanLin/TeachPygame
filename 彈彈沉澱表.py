import numpy as np
import math
import random

import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
W = 640 * 2
H = 480 * 2
DISPLAYSURF = pygame.display.set_mode((W, H), FULLSCREEN)
pygame.display.set_caption("彈彈沉澱表")
graph = pygame.image.load("沉澱表.jpg")
GW = 320 * 2
GH = 240 * 2
graph = pygame.transform.scale(graph, (GW, GH))

x = 200
y = 150
xdir = 1
ydir = 1
theta = random.random() * 2 * math.pi
v = 20

while True:
    DISPLAYSURF.fill((255, 255, 255))

    x += v * math.cos(theta) * xdir
    y += v * math.sin(theta) * ydir
    
    if x > W or x < 0: xdir *= -1
    if y > H or y < 0: ydir *= -1

    DISPLAYSURF.blit(graph, (x - GW / 2, y - GH / 2))
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)

    