def solution(board):
    mines = [(x, y) for x, row in enumerate(board)
                         for y, value in enumerate(row)
                         if value == 1]
    for x, y in mines:
        around = [
            (x-1, y-1), (x-1, y), (x-1, y+1),
            (x, y-1),            (x, y+1),
            (x+1, y-1), (x+1, y), (x+1, y+1),
        ]
        for nx, ny in around:
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                board[nx][ny] = 2
                
    return sum(row.count(0) for row in board)