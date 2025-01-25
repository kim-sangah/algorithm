def solution(arr):
    for x in range(100):
        new_arr = []
        for i in arr:
            if i >= 50 and i%2 == 0:
                new_arr.append(i/2)
            elif i < 50 and i%2 == 1:
                new_arr.append(i*2+1)
            else:
                new_arr.append(i)
        if arr == new_arr:
            return x
        arr = new_arr
