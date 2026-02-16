def show_all(board):
    for row in board:
        for block in row:
            block.clicked()

