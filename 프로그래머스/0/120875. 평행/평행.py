def solution(dots):
    case = [
        (0, 1, 2, 3),
        (0, 2, 1, 3),
        (0, 3, 1, 2)
    ]
    
    for d1, d2, d3, d4 in case:
        x1, y1 = dots[d1]
        x2, y2 = dots[d2]
        x3, y3 = dots[d3]
        x4, y4 = dots[d4]
        
        if (y1-y2)*(x3-x4) == (y3-y4)*(x1-x2):
            return 1
    return 0