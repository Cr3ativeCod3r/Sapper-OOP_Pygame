import pygame
from abc import ABC


class Block(ABC):
    def __init__(self, screen, color, x, y, size):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(x, y, size, size)
        self.flag = None
        self.revealed = False
        self.covered = True

        if color == 1:
            self.base_color = (169, 214, 79)
            self.reveal_color = (230, 194, 158)  
        else:
            self.base_color = (161, 209, 71)
            self.reveal_color = (214, 183, 152)  

        self.color = self.base_color

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        if self.covered:
            pygame.draw.rect(self.screen, (23, 153, 94), self.rect, 1)

        if self.flag:
            self.flag.draw()

    def put_flag(self):
        if self.flag:
            self.flag = None
        else:
            self.flag = Flag(self.screen, self.x, self.y, self.size)

    def clicked(self):
        self.revealed = True
        self.covered = False
        self.color = self.reveal_color


# ================= FLAG =================


class Flag:
    def __init__(self, screen, x, y, size):
        self.screen = screen
        self.image = pygame.image.load("assets/images/flag.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self):
        self.screen.blit(self.image, self.rect)


# ================= EMPTY TILE =================


class Empty(Block):
    type = "Empty"

    def __init__(self, screen, color, x, y, size):
        super().__init__(screen, color, x, y, size)


# ================= NUMBER TILE =================


class Number(Block):
    type = "Number"

    def __init__(self, screen, color, x, y, size, number):
        super().__init__(screen, color, x, y, size)
        self.number = number
        self.font = pygame.font.Font(None, size)

    def draw(self):
        super().draw()

        if self.revealed:
            text_surface = self.font.render(str(self.number), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)
            self.screen.blit(text_surface, text_rect)


# ================= BOMB TILE =================


class Bomb(Block):
    type = "Bomb"

    def __init__(self, screen, color, x, y, size):
        super().__init__(screen, color, x, y, size)
