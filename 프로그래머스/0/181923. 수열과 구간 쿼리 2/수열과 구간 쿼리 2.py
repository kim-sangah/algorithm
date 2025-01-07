def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        slicing_list = arr[s:e+1]
        k_list = [num for num in slicing_list if num > k]
        if k_list:
            answer.append(min(k_list))
        else:
            answer.append(-1)
    return answer