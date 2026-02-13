from screen import Screen
from block import Empty, Bomb, Number
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
        color = (i+j)%2
        x = j * block_size
        y = i * block_size + menu_height 
        
        if color == 1 :
            block = Empty(new_window.screen, color, x, y, block_size)
        else: 
            block = Number(new_window.screen, color, x, y, block_size, 10)
        

        # block = Flag(new_window.screen, color, x, y, block_size)
        # block = Bomb(new_window.screen, color, x, y, block_size, 10)
        
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
            mouse_pos = pygame.mouse.get_pos()

            if event.button == 1:
                for block in blocks:
                    if block.rect.collidepoint(mouse_pos) and block.flag is None:
                        block.clicked()

            if event.button == 3:
                for block in blocks:
                    if block.rect.collidepoint(mouse_pos) and block.revealed == False:
                        block.put_flag()

    new_window.screen.fill((0,0,0))

    for block in blocks:
        block.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

