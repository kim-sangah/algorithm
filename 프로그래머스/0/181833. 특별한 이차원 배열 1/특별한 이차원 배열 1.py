def solution(n):
    answer = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(1 if i == j else 0)
        answer.extend([row])
    return answer
