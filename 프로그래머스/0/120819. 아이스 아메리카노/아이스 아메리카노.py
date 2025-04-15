def solution(money):
    cup = money//5500
    balance = money - 5500*cup
    return [cup, balance]