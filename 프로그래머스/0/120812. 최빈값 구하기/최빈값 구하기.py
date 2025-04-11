def solution(array):
    answer = [0] * 1000
    for num in array:
        answer[num] += 1
    if answer.count(max(answer)) > 1:
        return -1
    return answer.index(max(answer))