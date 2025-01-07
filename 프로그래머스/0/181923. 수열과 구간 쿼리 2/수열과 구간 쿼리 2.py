def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        s_list = arr[s:e+1]
        k_list = []
        for num in s_list:
            if num > k:
                k_list.append(num)
        if k_list:
            answer.append(min(k_list))
        else:
            answer.append(-1)
    return answer