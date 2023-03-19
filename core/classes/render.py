import pygame

class Renderer:
    def __init__(self, surf, mon):
        self.texts = []
        self.monitorSize = mon
        self.obj = []
        self.surf = surf

    def draw(self):
        # render texts
        for x in self.texts:
            x[0].render(self.surf, x[1], x[2])
        #render obj
        for x in self.obj:
            x.draw(self.surf)
        pygame.display.update()