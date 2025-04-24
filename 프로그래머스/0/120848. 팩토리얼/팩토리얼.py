def solution(n):
    c = 0
    a = 1
    while a <= n:
        c += 1
        a *= c
    return c-1
