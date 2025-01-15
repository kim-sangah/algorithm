def solution(my_string):
    answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ABC_list = [chr(i) for i in range(65, 91)]
    abc_list = [chr(i) for i in range(97, 123)]
    chr_list = ABC_list + abc_list
    for string in my_string:
        i = chr_list.index(string)
        answer[i] += 1
    return answer