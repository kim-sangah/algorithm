def solution(num_list):
    if len(num_list) < 11:
        num = 1
        for i in num_list:
            num *= i
        return num
    else:
        return sum(num_list)