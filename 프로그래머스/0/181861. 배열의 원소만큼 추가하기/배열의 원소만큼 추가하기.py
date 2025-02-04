def solution(arr):
    answer = []
    for num in arr:
        for a in range(num):
            answer += [num]
    return answer