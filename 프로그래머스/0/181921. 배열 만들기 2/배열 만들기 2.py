import re

def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if re.match(r'^[05]+$', str(i)):
            answer.append(i)
    if not answer:
        answer = [-1]
    return answer