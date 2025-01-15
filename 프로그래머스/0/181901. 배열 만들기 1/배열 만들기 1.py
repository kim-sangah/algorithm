def solution(n, k):
    answer = []
    m = n//k
    for i in range(1, m+1):
        answer.append(k*i)
    return answer