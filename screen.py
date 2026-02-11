import pygame

class Screen:
    screen = 0
    
    def setWindow(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("My Game")
        self.screen.fill((30, 30, 30))



        


