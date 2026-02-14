from screen import Screen
from block import Empty, Bomb, Number
import sys
import pygame
import random
from game_logic import show_all, add_numbers_to_board

pygame.init()

# ====== CONFIG ======
MENU_HEIGHT = 100
GRID_SIZE = 9
BLOCK_SIZE = 60
WIDTH = GRID_SIZE * BLOCK_SIZE
HEIGHT = WIDTH + MENU_HEIGHT
BOMB_COUNT = 5

# ====== WINDOW ======
window = Screen()
window.setWindow(WIDTH, HEIGHT)

# ====== CREATE BOARD ======
board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

bomb_positions = random.sample(
    [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE)],
    BOMB_COUNT
)


for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        color = (row + col) % 2
        x = col * BLOCK_SIZE
        y = row * BLOCK_SIZE + MENU_HEIGHT

        if (row, col) in bomb_positions:
            block = Bomb(window.screen, color, x, y, BLOCK_SIZE)
        else:
            block = Empty(window.screen, color, x, y, BLOCK_SIZE)

        board[row][col] = block


board = add_numbers_to_board(board,9,9)

# ====== GAME LOOP ======
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            col = mouse_x // BLOCK_SIZE
            row = (mouse_y - MENU_HEIGHT) // BLOCK_SIZE

            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                block = board[row][col]

                if event.button == 1 and block.flag is None:
                    block.clicked()
                
                if event.button == 1 and block.flag is None and block.type == "Bomb":
                    show_all(board)

                if event.button == 3 and not block.revealed:
                    block.put_flag()


    window.screen.fill((0, 0, 0))
    for row in board:
        for block in row:
            block.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()