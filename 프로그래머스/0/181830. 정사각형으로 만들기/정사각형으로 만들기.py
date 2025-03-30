def solution(arr):
    m = max(len(arr), len(arr[0]))
    answer = [[0] * m for row in range(m)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            answer[i][j] = arr[i][j]    
    return answer