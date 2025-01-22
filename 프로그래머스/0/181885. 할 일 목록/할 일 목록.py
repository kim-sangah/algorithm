def solution(todo_list, finished):
    answer = []
    for i, w in enumerate(todo_list):
        if finished[i] == False:
            answer.append(w)
    return answer