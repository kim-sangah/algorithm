def solution(arr):
    a_len = len(arr)
    power = 2**(a_len-1).bit_length()
    if a_len == power:
        return arr
    else:
        p = power - a_len
        return arr + [0]*p


# 이진수 n>0, (n & (n-1)) == 0 /  power = 2**(n-1).bit_length()