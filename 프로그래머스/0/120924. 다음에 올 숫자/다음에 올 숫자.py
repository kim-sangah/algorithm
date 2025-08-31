def solution(common):
    is_arith = common[1] - common[0] == common[-1] - common[-2]
    
    if is_arith:
        a = common[1] - common[0]
        return common[-1] + a
    else:
        g = common[1] // common[0]
        return common[-1]*g