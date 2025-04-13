def solution(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return n//gcd(n, 6)