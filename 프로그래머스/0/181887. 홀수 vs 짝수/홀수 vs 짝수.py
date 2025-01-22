def solution(num_list):
    a, b = 0, 0
    for i, num in enumerate(num_list):
        if i%2==0:
            a += num
        else:
            b += num
    return max(a, b)