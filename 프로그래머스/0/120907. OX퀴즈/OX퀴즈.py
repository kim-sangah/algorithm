def solution(quiz):
    answer = []
    for q in quiz:
        calc, res = q.split('=')
        if eval(calc) == int(res):
            answer.append("O")
        else:
            answer.append("X")
    return answer