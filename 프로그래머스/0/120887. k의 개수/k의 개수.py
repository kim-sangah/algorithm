def solution(i, j, k):
    k_string = ''.join(str(n) for n in range(i, j+1) if str(k) in str(n))
    return k_string.count(str(k))