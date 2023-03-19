import pygame
from core.classes.font import Font

class test:
    def __init__(self, parent, delta):
        self.delta = delta
        self.parent = parent
        my_font = Font("./sprites/font/stock-font-large.png", 5)
        font2 = Font("./sprites/font/stock-font-main.png", 1)
        parent.texts = [(font2, "\"testing\"", (20, 20)), (my_font, "\"The quick brown for jumps\"", (20, 80)), (my_font, "over the lazy dog", (20, 138))]

    def testUpdateLoop(self):
        print('tick!')

    def __del__(self):
        self.parent.texts = []
        print('deleted')
