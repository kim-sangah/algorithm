def solution(price):
    discount = [
        (10, 99999, 1),
        (100000, 299999, 0.95),
        (300000, 499999, 0.9),
        (500000, 1000000, 0.8)
    ]
    for low, high, rate in discount:
        if low <= price <= high:
            return int(price*rate)