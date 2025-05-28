def solution(sides):
    max_num = max(sides)
    min_num = min(sides)
    case1 = [i for i in range(max_num+1) if i + min_num > max_num]
    case2 = [i for i in range(max_num+min_num) if i < sum(sides) and i > max_num]
    return len(case1) + len(case2)