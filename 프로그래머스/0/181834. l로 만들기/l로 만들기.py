def solution(myString):
    answer = ''
    front_l = {'a','b','c','d','e','f','g','h','i','j','k',}
    for i in myString:
        answer += i if i not in front_l else 'l'
    return answer