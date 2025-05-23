def solution(array):
    a = str(array)
    return sum(1 for i in a if i == '7')