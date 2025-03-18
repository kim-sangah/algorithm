def solution(arr, k):
    answer = []
    for i, v in enumerate(arr):
        if v not in answer:
            answer.append(v)
    if len(answer) < k:
        p = k - len(answer)
        answer += [-1]*p
    else:
        answer = answer[:k]
    return answer