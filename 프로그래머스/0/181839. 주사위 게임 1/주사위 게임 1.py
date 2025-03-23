def solution(a, b):
    answer = 0
    odd_set = {1, 3, 5}
    check = int(a in odd_set) + int (b in odd_set)
    if check == 2:
        answer = a**2 + b**2
    elif check == 1:
        answer = 2*(a+b)
    else:
        answer = abs(a - b)
    return answer