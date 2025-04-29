def solution(my_string):
    num = '0123456789'
    num_list = [int(n) for n in my_string if n in num]
    return sorted(num_list)