def solution(array):
    answer = [0] * 1000
    
    for num in array:
        answer[num] += 1
        
    max_num = max(answer)
    if answer.count(max_num) > 1:
        return -1
    return answer.index(max_num)