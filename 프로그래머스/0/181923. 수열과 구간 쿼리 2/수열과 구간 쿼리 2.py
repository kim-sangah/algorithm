def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        l = [num for num in arr[s:e+1] if num > k]
        answer.append(min(l) if l else -1)
    return answer