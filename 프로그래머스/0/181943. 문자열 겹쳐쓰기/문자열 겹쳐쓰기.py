def solution(my_string, overwrite_string, s):
    a = len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[s+a:]
    return answer