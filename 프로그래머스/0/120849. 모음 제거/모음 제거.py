def solution(my_string):
    vowels = 'aeiou'
    return ''.join(s for s in my_string if s not in vowels)