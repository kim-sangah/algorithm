def solution(sides):
    return int(max(sides) >= (sum(sides) - max(sides))) + 1