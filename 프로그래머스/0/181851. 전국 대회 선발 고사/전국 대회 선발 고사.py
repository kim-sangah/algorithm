def solution(rank, attendance):
    rank_list = []
    for i in range(len(rank)):
        if attendance[i]:
            rank_list.append(rank[i])
    rank_list.sort()
    a, b, c = rank_list[:3]
    return rank.index(a)*10000 + rank.index(b)*100 + rank.index(c)