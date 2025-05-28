def solution(sides):
    sides.sort()
    case1 = [i for i in range(sides[1]) if i + sides[0] > sides[1]]
    case2 = [i for i in range(sides[1], sum(sides)) if i < sum(sides)]
    return len(case1) + len(case2)