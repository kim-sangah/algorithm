def solution(str_list):
    for i, lr in enumerate(str_list):
        if lr == "l":
            return str_list[:i]
        elif lr == "r":
            return str_list[i+1:]
    return []