import pygame

class Update:
    def __init__(self):
        self.run_on_tick = []

    def tick(self):
        for x in self.run_on_tick:
            func = getattr(x[0], x[1])
            func()