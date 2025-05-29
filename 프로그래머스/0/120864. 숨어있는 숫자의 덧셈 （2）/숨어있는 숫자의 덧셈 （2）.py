def solution(my_string):
    my_string = my_string.lower()
    
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        my_string = my_string.replace(ch, 'a')
    
    my_string = my_string.split('a')
    return sum(int(i) for i in my_string if i!="")