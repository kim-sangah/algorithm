def solution(num, total):
    m = (((total * 2) / num) + num - 1) / 2
    return sorted([m-i for i in range(num)])