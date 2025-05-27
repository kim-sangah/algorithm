def solution(keyinput, board):
    key_dict = {'up':[0,1], 'down':[0,-1], 'left':[-1,0], 'right':[1,0]}
    x_lim, y_lim = board[0]//2, board[1]//2
    answer = [0,0]
    
    for k in keyinput:
        x, y = key_dict.get(k, [0,0])
        if abs(answer[0] + x) <= x_lim:
            answer[0] += x
        if abs(answer[1] + y) <= y_lim:
            answer[1] += y
        
    return answer