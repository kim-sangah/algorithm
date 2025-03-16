def solution(myString):
    answer = []
    x_list = myString.split('x')
    for i in x_list:
        if i:
            answer.append(i)
    return sorted(answer)