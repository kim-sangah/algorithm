def solution(keyinput, board):
    key_dict = {'up':[0,1], 'down':[0,-1], 'left':[-1,0], 'right':[1,0]}
    answer = [0,0]
    
    for k in keyinput:
        x, y = key_dict.get(k, [0,0])
        if -(board[0]//2) <= answer[0] + x <= board[0]//2:
            answer[0] += x
        if -(board[1]//2) <= answer[1] + y <= board[1]//2:
            answer[1] += y
        
    return answer