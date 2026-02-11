import pygame
from abc import ABC

class Block(ABC):
    def __init__(self, screen, color, x, y, size):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(x, y, size, size)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
  
class Empty(Block):
    def __init__(self, screen, color, x, y, size):
        super().__init__(screen, color, x, y, size)
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bomb(Block):
    def __init__(self, screen, color, x, y, size):
        super().__init__(screen, color, x, y, size)

class Flag(Block):
    def __init__(self, screen, color, x, y, size):
        super().__init__(screen, color, x, y, size)

class Number(Block):
    def __init__(self, screen, color, x, y, size):
        super().__init__(screen, color, x, y, size)