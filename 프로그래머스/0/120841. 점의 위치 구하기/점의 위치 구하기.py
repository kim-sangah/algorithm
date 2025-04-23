def solution(dot):
    quad = [
        (2, 1), 
        (3, 4)
    ]

    return quad[dot[1]<0][dot[0]>0]