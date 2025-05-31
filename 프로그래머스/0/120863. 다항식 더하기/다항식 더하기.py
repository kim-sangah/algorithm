def solution(polynomial):
    terms = polynomial.split(' + ')
    x_sum = 0
    num_sum = 0
    
    for term in terms:
        if term.isdigit():
            num_sum += int(term)
        else:
            x_sum += 1 if term == 'x' else int(term[:-1])
    
    answer = []
    if x_sum:
        answer.append('x' if x_sum == 1 else f'{x_sum}x')
    if num_sum:
        answer.append(f'{num_sum}')
        
    return ' + '.join(answer)