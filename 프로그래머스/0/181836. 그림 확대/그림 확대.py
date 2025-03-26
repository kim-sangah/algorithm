def solution(picture, k):
    answer = []
    for i in picture:
        row = ''
        for j in i:
            row += j*k
        answer.extend([row]*k)
    return answer