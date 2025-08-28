def solution(dots):
    a, b, c, d = dots
    
    case = [
        (a, b, c, d),
        (a, c, b, d),
        (a, d, b, c)
    ]
    
    for d1, d2, d3, d4 in case:
        dx1, dy1 = d1[0] - d2[0], d1[1] - d2[1]
        dx2, dy2 = d3[0] - d4[0], d3[1] - d4[1]
        if dy1*dx2 == dy2*dx1:
            return 1
    return 0