def solution(sides):
    return int(not max(sides) < (sum(sides) - max(sides))) + 1