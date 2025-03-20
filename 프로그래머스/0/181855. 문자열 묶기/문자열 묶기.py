def solution(strArr):
    l_dict = {}
    for l in strArr:
        key = len(l)
        if key not in l_dict:
            l_dict[key] = []  
        l_dict[key].append(l)
    c_dict = {}
    for k, v in l_dict.items():
        c_dict[k] = len(v)
    return max(c_dict.values())