def solution(num_list):
    num_1 = num_list[-1]
    num_2 = num_list[-2]
    if num_1 > num_2:
        num_list.append(num_1-num_2)
    else:
        num_list.append(num_1*2)
    return num_list