import pygame

def clip(surf, x, y, x_size, y_size):
    handle_surf = surf.copy()
    clipR = pygame.Rect(x,y,x_size,y_size)
    handle_surf.set_clip(clipR)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()

class Font:
    def __init__(self, path, spacing):
        self.spacing = spacing
        font_img = pygame.image.load(path)
        current_char_width = 0
        #literally every single possible character
        self.character_order = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-",".",",",":","+","'","!","?","0","1","2","3","4","5","6","7","8","9","(",")","/","_","=","\\","[","]","*","\"","<",">",";"]
        self.characters = {}
        self.character_count = 0
        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            if c[0] == 99:
                char_img = clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                try:
                    pygame.Surface.set_colorkey(char_img, (0, 0, 0))
                    self.characters[self.character_order[self.character_count]] = char_img.copy()
                except IndexError:
                    print("Error with setting font, make sure the image is referenced correctly?")
                self.character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1

    def render(self, surf, text, loc):
        x_offset = 0
        for char in text:
            if char != " " and char in self.character_order:
                surf.blit(self.characters[char], (loc[0]+x_offset, loc[1]))
                x_offset += self.characters[char].get_width() + self.spacing
            elif char == " ":
                x_offset += self.characters["A"].get_width() + self.spacing

    def get_width(self, text):
        width = 0
        for char in text:
            if char != " " and char in self.character_order:
                width += self.characters[char].get_width()+self.spacing
            elif char == " ":
                width += self.characters["A"].get_width()+self.spacing

        return width

    def get_height(self):
        return self.characters["A"].get_height()