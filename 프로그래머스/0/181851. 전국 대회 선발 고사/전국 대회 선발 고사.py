def solution(rank, attendance):
    rank_list = []
    for i in range(len(rank)):
        if attendance[i]:
            rank_list.append(rank[i])
    rank_list.sort()
    a = rank_list[0]
    b = rank_list[1]
    c = rank_list[2]
    return rank.index(a)*10000 + rank.index(b)*100 + rank.index(c)