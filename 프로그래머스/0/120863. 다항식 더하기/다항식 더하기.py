def solution(polynomial):
    terms = polynomial.split(' + ')
    
    x_sum = 0
    num_sum = 0
     
    for term in terms:
        if 'x' in term:
            if term == 'x':
                x_sum += 1
            else:
                x_sum += int(term.replace('x', ''))
        else:
            num_sum += int(term)
    
    answer = []
    if x_sum == 1:
        answer.append('x')
    elif x_sum > 1:
        answer.append(f'{x_sum}x')
    if num_sum > 0:
        answer.append(f'{num_sum}')
        
    return ' + '.join(answer)