def solution(box, n):
    a, b, c = [i//n for i in box]
    return a * b * c