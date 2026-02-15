from block import Number

def show_all(board):
    for row in board:
        for block in row:
            block.clicked()

def add_numbers_to_board(board, rows, cols):

    def is_bomb(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        return board[r][c].type == "Bomb"

    def count_bombs(r, c):
        bombs = 0
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr == 0 and dc == 0:
                    continue
                if is_bomb(r+dr, c+dc):
                    bombs += 1
        return bombs

    for r in range(rows):
        for c in range(cols):
            if board[r][c].type == "Empty":
                n = count_bombs(r, c)
                if n > 0:
                    board[r][c] = Number(board[r][c].screen, board[r][c].color, 
                                         board[r][c].x, board[r][c].y, 
                                         board[r][c].size, n)

    return board


def indexes_of_neighbour_blocks(row, col, board):

    indexes = []
    visited = set()

    def flood_fill(x, y):
        if x < 0 or x >= 9 or y < 0 or y >= 9: return
        if (x, y) in visited: return

        visited.add((x,y))
        if board[x][y].type != "Empty":
            if board[x][y].type == "Number":
                indexes.append([x, y])
            return

        indexes.append([x,y])

        flood_fill(x-1, y)
        flood_fill(x+1, y)
        flood_fill(x, y+1)
        flood_fill(x, y-1)
    
    flood_fill(row, col)

    return indexes