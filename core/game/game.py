import pygame
from core.classes.button import button
from core.classes.font import Font

class game:
    def __init__(self, render, delta):
        self.render = render
        self.delta = delta
        self.texts = []
        self.obj = []
        self.up = []
        self.main()

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
    def main(self):
        mainFont = Font("./sprites/font/stock-font-large.png", 4, True)
        math_width = 640/2 - mainFont.get_width("Stocks and Bonds")/2
        self.texts.append(mainFont)
        self.render.texts.append((mainFont, "Stocks and Bonds", (0,10)))

        self.delta.run_on_tick.append((self, "update"))
        self.up.append((self, "update"))


    def update(self):
        pass

    def click(self, btn):
        print('Button with the text was pressed!: '+btn.text)