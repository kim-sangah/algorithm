def solution(arr):
    index_arr = []
    for i , num in enumerate(arr):
        if num == 2:
            index_arr.append(i)
            
    if len(index_arr) >= 1:
        s = index_arr[0]
        e = index_arr[-1]
        return arr[s:e+1]
    return [-1]