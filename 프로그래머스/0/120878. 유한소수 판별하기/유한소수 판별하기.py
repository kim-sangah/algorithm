def solution(a, b):
    
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    common = gcd(a, b)
    b //= common
    
    for p in (2, 5):
        while b % p == 0:
            b //= p
    
    return 1 if b == 1 else 2

    