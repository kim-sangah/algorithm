def solution(price):
    rate = [1, 0.95, 0.95, 0.9, 0.9, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]
    return int(price*rate[price//100000])