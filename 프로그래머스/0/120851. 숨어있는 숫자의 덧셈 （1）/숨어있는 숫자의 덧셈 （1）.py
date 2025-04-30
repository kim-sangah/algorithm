def solution(my_string):
    num_list = [int(n) for n in my_string if n.isdigit()]
    return sum(num_list)