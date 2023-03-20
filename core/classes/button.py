import pygame


class button:
    def __init__(self, text, x, y, w, h, color, font):
        self.text = text
        self.x = x
        self.font = font
        self.y = y
        self.width = w
        self.height = h
        self.isHover = False
        self.isClicked = False
        self.when_clicked = (None, "", None)
        self.color = pygame.Color(color)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        self.font.render(win, self.text, (self.x + round(self.width/2) - round(self.font.get_width(text=self.text)/2), self.y + round(self.height/2) - round(self.font.get_height()/2)))

    def on_hover(self):
        pos = pygame.mouse.get_pos()
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            self.isHover = True
            if pygame.mouse.get_pressed()[0] and self.isClicked == False:
                self.isClicked = True
                self.on_click()
            elif not pygame.mouse.get_pressed()[0] and self.isClicked:
                self.isClicked = False
        else:
            self.isHover = False
            self.isClicked = False

    def on_click(self):
        if self.when_clicked[0] is None or self.when_clicked[1] == "":
            return
        try:
            func = getattr(self.when_clicked[0], self.when_clicked[1])
        except AttributeError as e:
            print(e)
            return
        if self.when_clicked[2] is None:
            func()
        else:
            func(self.when_clicked[2])