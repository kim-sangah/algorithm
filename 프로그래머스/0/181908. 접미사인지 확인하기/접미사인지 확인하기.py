def solution(my_string, is_suffix):
    answer = 0
    my_list = []
    for i in range(len(my_string)):
        my_list.append(my_string[i:])
    if is_suffix in my_list:
        answer += 1
    return answer