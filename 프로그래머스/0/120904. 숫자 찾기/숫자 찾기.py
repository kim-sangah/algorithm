def solution(num, k):
    for i, v in enumerate(str(num), 1):
        if v == str(k):
            return i
    
    return -1