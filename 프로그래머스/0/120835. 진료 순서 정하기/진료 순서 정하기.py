def solution(emergency):
    emergency_rank = sorted(emergency, reverse=True)
    answer = [emergency_rank.index(n) + 1 for n in emergency]
    return answer