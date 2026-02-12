import pygame
from abc import ABC

class Block(ABC):
    def __init__(self, screen, color, x, y, size):
        self.screen = screen
        self.color = (50, 205, 50) if color == 1 else (0, 255, 0)
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(x, y, size, size)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

  
class Empty(Block):
    def __init__(self, screen, color, x, y, size):
        super().__init__(screen, color, x, y, size)
    def clicked(self):
        self.color = (128,128,128)
        self.draw()

class Flag(Block):
    def __init__(self, screen, color, x, y, size):
        super().__init__(screen, color, x, y, size)
        self.flag_image = pygame.image.load("assets/images/flag.png").convert_alpha()
        self.flag_image = pygame.transform.scale(self.flag_image, (50, 50))
        self.flag_rect = self.flag_image.get_rect(center=self.rect.center)
    
    def clicked(self):
        self.screen.blit(self.flag_image, self.flag_rect)


class Number(Block):
    def __init__(self, screen, color, x, y, size, number):
        super().__init__(screen, color, x, y, size)
        self.number = number
        self.font = pygame.font.Font(None, 60)
    
    def clicked(self):
        self.color = (128,128,128)
        self.draw()
        self.update_text()

    def update_text(self):
        self.text_surface = self.font.render(str(self.number), True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.screen.blit(self.text_surface, self.text_rect)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)



class Bomb(Block):
    def __init__(self, screen, color, x, y, size):
        super().__init__(screen, color, x, y, size)