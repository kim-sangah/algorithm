def solution(num_list):
    answer = [0, 0]
    for c in num_list:
        answer[c%2] += 1
    return answer