from screen import Screen
from block import Empty, Bomb, Flag, Number
import sys
import pygame

pygame.init() 
menu_height = 100
width = 540
height = 540 + menu_height
lvl = 9

blocks = []
block_size = 60 

new_window = Screen()
new_window.setWindow(width, height)

blocks = []

for i in range(lvl):
    for j in range(lvl):
        if (i + j) % 2 == 0:
            color = (50,205,50)
        else:
            color = (0,255,0)
        x = j * block_size
        y = i * block_size + menu_height 
        block = Empty(new_window.screen, color, x, y, block_size)
        blocks.append(block)

for block in blocks:
    block.draw()


pygame.display.flip()      


running = True
clock = pygame.time.Clock()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for block in blocks:
                if block.rect.collidepoint(event.pos):
                    block.color = (128, 128, 128)
                    block.draw()

            pygame.display.flip()
            clock.tick(60)

pygame.quit()
sys.exit()

