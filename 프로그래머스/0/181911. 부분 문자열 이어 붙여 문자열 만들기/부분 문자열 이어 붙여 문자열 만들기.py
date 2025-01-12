def solution(my_strings, parts):
    answer = ''
    n = 0
    for s, e in parts:
        i = my_strings[n]
        answer += i[s:e+1]
        n += 1
    return answer