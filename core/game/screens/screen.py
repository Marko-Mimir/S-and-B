from core.classes.button import button
import pygame


class Screen:
    def __init__(self, render, delta, game):
        self.render = render
        self.game = game
        self.delta = delta
        self.texts = []
        self.obj = []
        self.up = []
        self.start()
    #basic init

    def start(self):
        pass
    #new screens must have start() defined, or it will not work

    def clean(self):
        for x in self.obj:
            self.render.obj = self.render.obj.remove(x)
            if self.render.obj is None:
                self.render.obj = []
        for x in self.texts:
            self.render.texts = self.render.texts.remove((x, x.last[0], x.last[1]))
            if self.render.texts is None:
                self.render.texts = []
        for x in self.up:
            self.delta.run_on_tick = self.delta.run_on_tick.remove(x)
            if self.delta.run_on_tick is None:
                self.delta.run_on_tick = []
        self.up = []
        self.texts = []
        self.obj = []
    #before delete make sure to clean.

    def update(self):
        for x in self.obj:
            if type(x) is button:
                if x.isHover:
                    if x.isClicked:
                        x.color = pygame.Color(150, 150, 150, 255)
                    else:
                        x.color = pygame.Color(20, 20, 20, 255)
                elif x.color != pygame.Color(0, 0, 0, 255) and not x.isHover:
                    x.color = pygame.Color(0, 0, 0, 255)
    #update loop for delta