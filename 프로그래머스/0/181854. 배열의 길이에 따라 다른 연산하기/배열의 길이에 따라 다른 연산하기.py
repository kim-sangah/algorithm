def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        for i, v in enumerate(arr):
            if i % 2 == 1:
                a = int(v) + int(n)
                answer.append(a)
            else: 
                answer.append(v)
    else:
        for i, v in enumerate(arr):
            if i % 2 == 0:
                a = int(v) + int(n)
                answer.append(a)
            else: 
                answer.append(v)
    return answer