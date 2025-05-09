def solution(array, n):
    array.sort()
    ads_list = [abs(n-i) for i in array]
    min_idx = min(ads_list)
    i = ads_list.index(min_idx)
    return array[i]