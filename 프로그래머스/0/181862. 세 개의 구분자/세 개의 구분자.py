def solution(myStr):
    for abc in 'abc':
        myStr = myStr.replace(abc,' ')
    answer = myStr.split()
    return answer if answer else ["EMPTY"]