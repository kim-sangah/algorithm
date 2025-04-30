def solution(sides):
    a, b, c = sorted(sides, reverse=True)
    return int(not a < (b+c)) + 1