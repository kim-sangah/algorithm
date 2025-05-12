def solution(my_string):
    my_list = my_string.split()
    answer = int(my_list[0])
    
    for i in range(1, len(my_list), 2):
        op = my_list[i]
        num = int(my_list[i+1])
        
        if op == "+":
            answer += num
        else:
            answer -= num
            
    return answer