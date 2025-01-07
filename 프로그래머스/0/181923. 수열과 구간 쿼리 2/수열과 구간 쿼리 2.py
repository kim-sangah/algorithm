def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        l = [num for num in arr[s:e+1] if num > k]
        if l:
            answer.append(min(l))
        else:
            answer.append(-1)
    return answer