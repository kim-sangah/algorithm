def solution(n):
    answer = []
    i = 2
    
    while i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in answer:
                answer.append(i)
    if n > 1:
        answer.append(n)
        
    return answer