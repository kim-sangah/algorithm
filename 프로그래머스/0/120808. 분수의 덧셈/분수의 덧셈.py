def solution(numer1, denom1, numer2, denom2):
    def gcd(a, b):
        while b != 0: 
            a, b = b, a % b
        return a
        
    denom = denom1 * denom2 // gcd(denom1, denom2)
    numer = numer1 * (denom // denom1) + numer2 * (denom // denom2)
    common = gcd(denom, numer)
    
    return [numer//common, denom//common]