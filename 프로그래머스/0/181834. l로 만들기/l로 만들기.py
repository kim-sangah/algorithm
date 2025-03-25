def solution(myString):
    answer = ''
    for i in myString:
        answer += i if ord(i)>ord('l') else 'l'
    return answer