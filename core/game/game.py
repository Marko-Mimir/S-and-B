import pygame
from core.classes.button import button
from core.classes.font import Font

class game:
    def __init__(self, render, delta):
        self.render = render
        self.delta = delta
        self.obj = []
        self.main()

    def main(self):
        mainFont = Font("./sprites/font/stock-font-large.png", 4)
        self.render.texts.append((mainFont, "Stocks and Bonds", (20, 20)))

        self.delta.run_on_tick.append((self, "update"))

    def update(self):
        pass

    def click(self, btn):
        print('Button with the text was pressed!: '+btn.text)
