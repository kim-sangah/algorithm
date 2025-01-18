def solution(arr, query):
    for i, num in enumerate(query):
        if i%2==0:
            arr = arr[:num+1]
        else:
            arr = arr[num:]
    return arr