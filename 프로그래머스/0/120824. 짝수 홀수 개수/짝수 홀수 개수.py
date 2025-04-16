def solution(num_list):
    even = len([num for num in num_list if num%2==0])
    odd = len([num for num in num_list if num%2==1])
    return [even, odd]