def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if mode==0:
            if i%2==0 and code[i]!='1':
                answer += code[i]
            elif code[i]=='1':
                mode = mode + 1
        elif mode==1:
            if i%2==1 and code[i]!='1':
                answer += code[i]
            elif code[i]=='1':
                mode = mode - 1
    if not answer:
        answer = "EMPTY"
    return answer