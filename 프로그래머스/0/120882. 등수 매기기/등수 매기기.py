def solution(score):
    sums = [sum(s) for s in score]
    rank = sorted(sums, reverse=True)
    
    rank_dict = {}
    for i, v in enumerate(rank):
        if v not in rank_dict:
            rank_dict[v] = i + 1
    
    return [rank_dict[v] for v in sums]