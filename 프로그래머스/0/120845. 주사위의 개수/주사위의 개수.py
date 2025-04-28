def solution(box, n):
    n_list = [i//n for i in box]
    return n_list[0] * n_list[1] * n_list[2]