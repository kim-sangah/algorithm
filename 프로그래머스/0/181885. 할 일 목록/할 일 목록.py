def solution(todo_list, finished):
    answer = []
    for i, w in enumerate(todo_list):
        if not finished[i]:
            answer.append(w)
    return answer