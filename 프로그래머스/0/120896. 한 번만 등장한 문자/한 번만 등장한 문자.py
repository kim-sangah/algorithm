def solution(s):
    d = {}
    for k in s:
        if k in d:
            d[k] += 1
        else:
            d[k] = 1
    return ''.join(sorted(k for k, v in d.items() if v==1))