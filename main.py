import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame, sys
from core.game.game import game
from core.classes.render import Renderer
from core.classes.update import Update

# blue chip stock

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
mon_w, mon_h = pygame.display.Info().current_w, pygame.display.Info().current_h
pygame.display.set_caption("TESTING-DEBUG")
screen = pygame.display.set_mode((640, 480), 0, 32)

run = True

delta = Update()
renderer = Renderer(screen, (mon_w, mon_h))
game = game(renderer, delta)

while run:

    screen.fill((60, 60, 60))
    renderer.draw()
    delta.tick()
    mainClock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_u:
                game.clear_all_scenes()
            if event.key == K_i:
                game.main()

