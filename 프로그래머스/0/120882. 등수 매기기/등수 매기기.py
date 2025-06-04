def solution(score):
    ranks = sorted([sum(i) for i in score], reverse = True)
    answer = [ranks.index(sum(i)) + 1 for i in score]
    return answer