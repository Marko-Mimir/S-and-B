from core.classes.font import Font
from core.classes.button import button
from core.game.screens.screen import Screen
import pygame
import sys
class mainMenu(Screen):

    def start(self):
        mainFont = Font("./sprites/font/stock-font-large.png", 4, True)
        bF = Font("./sprites/font/stock-font-large.png", 4)
        self.texts.append(mainFont)
        self.render.texts.append((mainFont, "Working Title =)", (0, 10)))

        #INIT-START BUTTON
        self.obj.append(
            button("  Start  ", 640 / 2 - bF.get_width("  Start  ") / 2, 480 * .6, bF.get_width("  Start  ") + 5,
                   bF.get_height() + 5, (0, 0, 0, 255), bF))
        self.obj[0].when_clicked = (self, "whenStartClicked", None)
        self.render.obj.append(self.obj[0])
        self.delta.run_on_tick.append((self.obj[0], "on_hover"))

        #INIT-OPTIONS-BUTTON
        self.obj.append(
            button("  Options  ", 640/2-bF.get_width("  Options  ")/2, 480*.72, bF.get_width("  Options  ")+5,
                   bF.get_height()+5, (0,0,0,255), bF))
        self.obj[1].when_clicked = (self, "whenOptionsClicked", None)
        self.render.obj.append(self.obj[1])
        self.delta.run_on_tick.append((self.obj[1], "on_hover"))

        #INIT-QUIT-BUTTON
        self.obj.append(
            button("   QUIT   ", 640/2-bF.get_width("   QUIT   ")/2, 480*.84, bF.get_width("   QUIT   ")+5,
                   bF.get_height()+5, (0,0,0,255), bF))
        self.obj[2].when_clicked = (self, "whenQuitClicked", self)
        self.render.obj.append(self.obj[2])
        self.delta.run_on_tick.append((self.obj[2], "on_hover"))

        self.delta.run_on_tick.append((self, "update"))
        self.up.append((self, "update"))

    @staticmethod
    def whenStartClicked():
        print('Start Pressed')
    @staticmethod
    def whenOptionsClicked():
        print('Options Pressed')
    @staticmethod
    def whenQuitClicked(self):
        pygame.quit()
        sys.exit()