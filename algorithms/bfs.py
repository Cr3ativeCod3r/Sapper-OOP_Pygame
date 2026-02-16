from collections import deque

def indexes_of_neighbour_empty_blocks_bfs(row, col, board):
    indexes = set()
    def flood_fill(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            cx, cy = queue.popleft()
            if (cx, cy) in indexes:
                continue
            indexes.add((cx, cy))

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = cx + dx, cy + dy

                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                        cell = board[nx][ny]
                        if cell.type == "Bomb":
                            continue
                        if cell.type == "Number":
                            indexes.add((nx, ny))  
                        else:
                            queue.append((nx, ny))
    flood_fill(row, col)  
    return list(indexes)  