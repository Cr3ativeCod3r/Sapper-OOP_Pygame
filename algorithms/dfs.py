def indexes_of_neighbour_empty_blocks_dfs(row, col, board):
    indexes = []
    visited = set()

    def flood_fill(x, y):
        if x < 0 or x >= 9 or y < 0 or y >= 9:
            return
        if (x, y) in visited:
            return

        visited.add((x, y))

        cell = board[x][y]
        if cell.type != "Empty":
            if cell.type == "Number":
                indexes.append([x, y])
            return 

        indexes.append([x, y])

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  
                flood_fill(x + dx, y + dy)

    flood_fill(row, col)
    return indexes
