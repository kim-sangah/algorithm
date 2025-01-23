def solution(num_list):
    if len(num_list) > 10:
        answer = sum(num_list)
    else:
        num = 1
        for i in num_list:
            num *= i
        answer = num
    return answer