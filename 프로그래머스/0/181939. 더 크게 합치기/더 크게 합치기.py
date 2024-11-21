def solution(a, b):
    if int(f"{a}{b}") > int(f"{b}{a}"):
        answer = int(f"{a}{b}")
    elif int(f"{a}{b}") == int(f"{b}{a}"):
        answer = int(f"{a}{b}")
    else:
        answer = int(f"{b}{a}") 
    return answer