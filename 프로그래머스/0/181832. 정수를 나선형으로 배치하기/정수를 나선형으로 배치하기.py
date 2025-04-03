def solution(n):
    answer = [[0]*n for _ in range(n)]
    
    if n == 1:
        return [[1]]
    
    x, y = 0, 0
    dir = 'right'
    
    for i in range(n**2):
        answer[x][y] = i + 1
        
        if dir == 'right':
            y += 1
            if y == n-1 or answer[x][y+1] != 0:
                dir = 'down'
        elif dir == 'down':
            x += 1
            if x == n-1 or answer[x+1][y] != 0:
                dir = 'left'
        elif dir == 'left':
            y -= 1
            if y == 0 or answer[x][y-1] != 0:
                dir = 'up'
        elif dir == 'up':
            x -= 1
            if x == 0 or answer[x-1][y] != 0:
                dir = 'right'
    
    return answer