def solution(num_list):
    a = []
    b = []
    for i in num_list:
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    a_int = int(''.join(map(str, a)))
    b_int = int(''.join(map(str, b)))
    answer = a_int + b_int
    return answer