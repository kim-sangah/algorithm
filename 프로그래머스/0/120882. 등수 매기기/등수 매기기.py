def solution(score):
    avgs = [(i+j)/2 for i, j in score]
    ranks = sorted(avgs, reverse = True)
    answer = [ranks.index(avg) + 1 for avg in avgs]
    return answer