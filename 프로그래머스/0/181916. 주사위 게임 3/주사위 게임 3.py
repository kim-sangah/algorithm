def solution(a, b, c, d):
    numbers = [a, b, c, d]
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    if len(count_dict) == 1: #0
        answer = list(count_dict.keys())[0]*1111
    elif len(count_dict) == 4: #0
        answer = min(numbers)
    elif len(count_dict) == 2 and list(count_dict.values())[0] == 2: #0
        p = list(count_dict.keys())[0]
        q = list(count_dict.keys())[1]
        answer = (p + q) * abs(p - q)
    elif len(count_dict) == 3:
        p = max(count_dict, key=count_dict.get)
        count_dict.pop(p)
        q = list(count_dict.keys())[0]
        r = list(count_dict.keys())[1]
        answer = q*r
    else: #0
        p = max(count_dict, key=count_dict.get)
        q = min(count_dict, key=count_dict.get)
        answer = (10*p+q)**2 
    return answer