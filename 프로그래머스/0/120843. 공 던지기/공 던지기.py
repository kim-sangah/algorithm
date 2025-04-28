def solution(numbers, k):
    i = (k-1)*2 % len(numbers)
    return numbers[i]