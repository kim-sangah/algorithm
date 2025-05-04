def solution(s):
    s_list = s.split()
    answer = []
    for i in s_list:
        if i == 'Z':
            answer.pop()
        else:
            answer.append(int(i))
    return sum(answer)