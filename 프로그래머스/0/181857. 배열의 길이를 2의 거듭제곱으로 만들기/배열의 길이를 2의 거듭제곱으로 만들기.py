def solution(arr):
    a = len(arr)
    p = 2**(a-1).bit_length()
    return arr + [0] * (p-a)