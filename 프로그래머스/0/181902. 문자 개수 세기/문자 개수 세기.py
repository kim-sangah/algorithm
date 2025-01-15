def solution(my_string):
    answer = [0] * 52
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for string in my_string:
        answer[alphabet.index(string)] += 1
    return answer