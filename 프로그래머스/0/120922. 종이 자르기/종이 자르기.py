def solution(M, N):
    M, N = max(M, N), min(M, N)
    answer = (M-1) + (M * (N-1))
    return answer